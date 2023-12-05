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

cfg = config.load_config()
hotkey = cfg["hotkey"]
select_region = SelectRegion(hotkey)


while True:
    region = select_region.select_region()
    im = capture(region)

    start = time.time()
    txt = ocr.ocr(im)
    time_ocr = time.time() - start

    txt = txt.replace("\n", " ")

    # print(len(txt))
    start = time.time()
    ja = translate_deepl.translate_client(txt, target_lang="JA")
    time_translate = time.time() - start

    print(txt)
    print(ja)
    num = len(glob("results/trans_*.txt"))
    with open(f"results/trans_{num}.txt", "w",encoding="UTF-8") as f:
        f.write(str(ja))
    with open(f"results/ocr_{num}.txt", "w", encoding="UTF-8") as f:
        f.write(str(txt))
    shutil.move("screenshot.jpg", f"results/screenshot_{num}.jpg")
    
    # print(f"ocr: {time_ocr}, translate: {time_translate}")
