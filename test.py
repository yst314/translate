import translate_deepl
import ocr
from PIL import Image
import time
from capture import capture
from region import select_region
while True:
    region = select_region()
    im = capture(region)

    start = time.time()
    txt = ocr.ocr(im)
    time_ocr = time.time() - start

    txt = txt.replace("\n", " ")

    print(len(txt))
    start = time.time()
    ja = translate_deepl.translate_client(txt, target_lang="JA")
    time_translate = time.time() - start

    print(txt)
    print(ja)
    print(f"ocr: {time_ocr}, translate: {time_translate}")
