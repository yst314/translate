import os
from glob import glob
import translate_deepl
import shutil
import ocr
from PIL import Image
import time
from capture import capture
from region import SelectRegion
import config
import keyboard

cfg = config.load_config()
hotkey = cfg["hotkey"]
source_lang = cfg["source_lang"]
target_lang = cfg["target_lang"]
select_region = SelectRegion(hotkey)
region = select_region.select_region()
translator = translate_deepl.DeeplTranslator()

def on_triggered():
    print("start translation")
    im = capture(region)

    start = time.time()
    try:
        txt = ocr.ocr(im)
    except ValueError:
        print(f"Shapre {region.get_points()} is not appropriate.")
        return False
    time_ocr = time.time() - start

    txt = txt.replace("\n", " ")
    # "1 AM", "1AM"って書くだろ普通
    txt = txt.replace("|", "I")
    txt = txt.replace("1am", "I am")
    txt = txt.replace("1 am", "I am")
    txt = txt.replace("1'm", "I'm")

    # print(len(txt))
    start = time.time()
    try:
        ja = translator.translate(txt, source_lang=source_lang, target_lang=target_lang)
    except ValueError:
        print(f"Err: `{txt}` text must not be empty")
        return False
    time_translate = time.time() - start

    print(txt)
    print(ja)
    # logger
    num = len(glob("results/trans_*.txt"))
    os.makedirs("results", exist_ok=True)
    with open(f"results/trans_{num}.txt", "w",encoding="UTF-8") as f:
        f.write(str(ja))
    with open(f"results/ocr_{num}.txt", "w", encoding="UTF-8") as f:
        f.write(str(txt))
    shutil.move("screenshot.jpg", f"results/screenshot_{num}.jpg")
    
    # print(f"ocr: {time_ocr}, translate: {time_translate}")
    
def run(hotkey):
    keyboard.add_hotkey(hotkey, on_triggered)

if __name__=="__main__":
    keyboard.remove_hotkey(hotkey)

    run(hotkey)
    while True:
        pass