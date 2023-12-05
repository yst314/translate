from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

class GptTransaltor:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0, 
            model_name="gpt-3.5-turbo", 
            streaming=True,
            api_key=OPENAI_API_KEY,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
        template = """入力はOCRで認識した文章です、そのため文章には"I am"が"1 am"のような間違いがある可能性があります。文脈から適切な文章を推測し、日本語に翻訳してください.
        変換前:{input}
        変換後:"""
        self.prompt = PromptTemplate(template=template, input_variables=["input"])

    def translate(self, text):
        result = self.llm.invoke(
            [
                HumanMessage(content=self.prompt.format(input=text))
            ]
        )
        return result

if __name__ == "__main__":
    gpt = GptTransaltor()
    result = gpt.translate("Undistorted images from D2Net are not available anymore.For a temporal alternative, please use the undistorted images provided by the MegaDepth_v1 (should be downloaded along with the required depth files). ")
    print(result)