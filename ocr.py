import pyocr

def ocr(img):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tools found")
    
    tool = tools[0]
    
    txt = tool.image_to_string(
        img,
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    return txt

if __name__ == "__main__":
    from PIL import Image

    img = Image.open("sample.jpg")
    result = ocr(img)
    print(result)