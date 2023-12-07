import os
import shutil
import time

import config
import ocr
from translator import create_translator

from glob import glob
from PIL import Image

from capture import capture
from region import SelectRegion

cfg = config.load_config()
hotkey = cfg["hotkey"]
source_lang = cfg["source_lang"]
target_lang = cfg["target_lang"]
translator_name = cfg["translator"]
select_region = SelectRegion(hotkey)

Translator = create_translator(translator_name)
translator = Translator()

def main():
    region = select_region.select_region()
    print("Start translation")
    try:
        im = capture(region)
    except ValueError:
        print(f"Shape {region.get_points()} is not appropriate.")
        return False
    start = time.time()
    txt = ocr.ocr(im)
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
        ja = translator.translate(txt, source_lang, target_lang)
    except ValueError:
        print(f"Err: `{txt}` text must not be empty")
        return False
    time_translate = time.time() - start

    print(txt)
    print(ja)
    num = len(glob("results/result_*.yaml"))+1
    os.makedirs("results", exist_ok=True)
    result={
        "ocr": txt,
        "translation": ja,
        "time":{
            "ocr": time_ocr,
            "translation": time_translate
        },
        "num_text": len(txt),
        "num_translate": len(str(ja)),
        "cfg": cfg,
        "img": f"results/screenshot_{num}.jpg"
    }

    config.save_yaml(result, f"results/result_{num}.yaml")
    shutil.move("screenshot.jpg", f"results/screenshot_{num}.jpg")
    return True
    
    # print(f"ocr: {time_ocr}, translate: {time_translate}")

if __name__ == "__main__":
    while True:
        main()