import pyocr

def ocr(img, lang):
    def lang_check(lang):
        langs = {
            "EN": "eng",
            "JA": "jpn",
            "ZH": "chi_sim",
            "KR": "kor"
        }
        try:
            return langs[lang]
        except KeyError as e:
            raise e

    lang = lang_check(lang)
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tools found")
    
    tool = tools[0]
    print(pyocr.tesseract)
    txt = tool.image_to_string(
        img,
        lang=lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    return txt


if __name__ == "__main__":
    from PIL import Image
    lang = "JA"

    img = Image.open("sample.jpg")
    result = ocr(img, lang)
    print(result)