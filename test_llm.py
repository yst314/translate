import ocr
import time

from PIL import Image

from translate_llm import GptTransaltor
from capture import capture
from region import select_region

gpt = GptTransaltor()
while True:
    region = select_region()
    im = capture(region)

    start = time.time()
    txt = ocr.ocr(im)
    time_ocr = time.time() - start

    # txt = txt.replace("\n", " ")

    start = time.time()
    ja = gpt.translate(txt)
    time_translate = time.time() - start

    print(f"ocr: {time_ocr}, translate: {time_translate}")
