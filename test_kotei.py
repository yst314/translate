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
select_region = SelectRegion(hotkey)
region = select_region.select_region()

def on_triggered():
    print("start translation")
    im = capture(region)

    start = time.time()
    txt = ocr.ocr(im)
    time_ocr = time.time() - start

    txt = txt.replace("\n", " ")
    txt = txt.replace("|", "I")

    # print(len(txt))
    start = time.time()
    ja = translate_deepl.translate_client(txt, target_lang="JA")
    time_translate = time.time() - start

    print(txt)
    print(ja)
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