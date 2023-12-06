import argostranslate.package
import argostranslate.translate
from time import time


class ArgosTranslator:
    def __init__(self):
        self.source_lang = None
        self.target_lang = None
    
    def _install(self):
        # Download and install Argos Translate package
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == self.source_lang and x.to_code == self.target_lang, available_packages
            )
        )
        try:
            argostranslate.package.install_from_path(package_to_install.download())
        except StopIteration as e:
            print("There is no match language package.")
            raise e
            
    def translate(self, text, source_lang, target_lang):
        source_lang = self._check_lang(source_lang)
        target_lang = self._check_lang(target_lang)

        if self.source_lang != source_lang or self.target_lang != target_lang:
            self.source_lang = source_lang
            self.target_lang = target_lang
            self._install()
        # Translate
        translatedText = argostranslate.translate.translate(text, source_lang, target_lang)
        return translatedText
    
    def _check_lang(self, lang):
        langs ={
            "JA": "ja",
            "EN": "en"
        }
        try:
            return langs[lang]
        except KeyError as e:
            raise e

if __name__ == "__main__":
    
    to_code = "JA"
    from_code = "EN"
    translator = ArgosTranslator()

    start = time()
    text = "Argos Translate also manages automatically pivoting through intermediate languages to translate between languages that don't have a direct translation between them installed. For example, if you have a es ~ en and en ~ fr translation installed you are able to translate from es — fr as if you had that translation installed. This allows for translating between a wide variety of languages at the cost of some loss of translation quality."
    result = translator.translate(text, from_code, to_code)
    print(result)
    print(time() - start)