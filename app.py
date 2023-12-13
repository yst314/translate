import flet as ft
import time
import os

from glob import glob
import yaml

import shutil
import config
from region import SelectRegion
from translator import create_translator
import ocr
from capture import capture

def main(page: ft.page):
    t_status = ft.Text()
    t_ocr = ft.Text()
    t_trans = ft.Text()
    page.add(t_status)
    page.add(t_ocr)
    page.add(t_trans)
    page.window_height = 500
    page.window_width = 300
    page.window_maximizable = False

    t_status.value = "Initializing..."

    page.update()

    cfg = config.load_config()
    hotkey = cfg["hotkey"]
    source_lang = cfg["source_lang"]
    target_lang = cfg["target_lang"]
    translator_name = cfg["translator"]
    select_region = SelectRegion(hotkey)

    Translator = create_translator(translator_name)
    translator = Translator()

    while True:
        t_status.value = "Wainting for input."
        page.update()

        region = select_region.select_region()
        t_status.value = "Translating..."
        page.update()

        print("Start translation")
        try:
            im = capture(region)
        except ValueError:
            print(f"Shape {region.get_points()} is not appropriate.")
            continue 
        start = time.time()
        txt = ocr.ocr(im, source_lang)
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
            continue
        time_translate = time.time() - start

        print(txt)
        print(ja)
        txt = txt.replace("'", "\'")    
        ja = ja.replace("'", "\'")

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
        
        # print(f"ocr: {time_ocr}, translate: {time_translate}")
        result_paths = glob("results/result*.yaml")
        # num_result = len(result_paths)
        t_ocr.value = result["ocr"]
        t_trans.value = result["translation"]
        page.update()
        # with open(result_paths[num_result-1], "r", encoding="UTF-8") as f:
        #     data = yaml.safe_load(f)
        # print(data["ocr"])
        # st.write(data["ocr"])
        # st.write(data["translation"])


ft.app(target=main)