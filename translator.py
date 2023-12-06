class Translator:
    def translate(self, text):
        raise NotImplementedError

def create_translator(name) -> Translator:
    if name == "deepl":
        from translate_deepl import DeeplTranslator
        return DeeplTranslator
    
    elif name == "gpt":
        from translate_llm import GptTransaltor
        return GptTransaltor
    
    elif name == "argos":
        from translate_argos import ArgosTranslator
        return ArgosTranslator
    
    else:
        raise ValueError(f"{name} is not exists in model lists")
    
if __name__ == "__main__":
    print(create_translator("deepl"))
    try:
        create_translator("AJIJNV--")
    except Exception as e:
        print(e)