import os
import requests
from dotenv import load_dotenv
import deepl
load_dotenv()
API_KEY = os.environ['DEEPL_API_KEY']

def translate(text, target_lang, source_lang="Auto"):

    params = {
                'auth_key' : API_KEY,
                'text' : text,
                "target_lang": target_lang  # 翻訳後の言語
            }

    if source_lang != "Auto":
        params["source_lang"] = source_lang # 翻訳対象の言語

    request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()

    return result

def translate_client(text, target_lang):
    translator = deepl.Translator(API_KEY)
    result = translator.translate_text(text, target_lang=target_lang)
    return result

if __name__ == "__main__":
    result = translate_client("Even if you try hard, it's gonna been luck. But that is not reason to be lazy.", "JA")
    # result = translate("Even if you try hard, it's gonna been luck. But that is not reason to be lazy.", "JA")
    # Even if you try hard, it's gonna been luck. But that is not reason to be lazy.
    # result = translate(result['translations'][0]["text"], "EN")
    # Even if you work hard, it depends on luck. But that is no reason to be lazy.
    print(result)