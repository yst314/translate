import os
import requests
from dotenv import load_dotenv
import deepl
from translator import Translator

load_dotenv()
API_KEY = os.environ['DEEPL_API_KEY']

def translate(text, target_lang, source_lang):

    params = {
                'auth_key' : API_KEY,
                'text' : text,
                "source_lang": source_lang, # 翻訳対象の言語
                "target_lang": target_lang,  # 翻訳後の言語
            }

    request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()

    return result

class DeeplTranslator(Translator):
    def __init__(self):
        self.translator = deepl.Translator(API_KEY)

    def translate(self, text, source_lang, target_lang):
        result = self.translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
        return result

if __name__ == "__main__":
    translator  = DeeplTranslator()
    result = deepl.translate("Even if you try hard, it's gonna been luck. But that is not reason to be lazy.","EN", "JA")
    # result = translate("Even if you try hard, it's gonna been luck. But that is not reason to be lazy.", "JA")
    # Even if you try hard, it's gonna been luck. But that is not reason to be lazy.
    # result = translate(result['translations'][0]["text"], "EN")
    # Even if you work hard, it depends on luck. But that is no reason to be lazy.
    print(result)