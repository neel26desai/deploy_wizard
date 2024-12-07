from talk_to_any_llm import Talker
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os


class MyOpenAI(Talker):
    FILE_WITH_SECRET = '/Users/neel/Documents/Keys/OpenAIDeployWizardKey.txt'
    
    def __init__(self,model = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model,temperature=0)
        self.messages = []
        os.environ["OPENAI_API_KEY"] = self.read_openai_key()
    
    def read_openai_key(self):
        try:
            with open(self.FILE_WITH_SECRET, 'r') as file:
                return file.read().strip()
        except Exception as e:
            return str(e)
        
    def invoke(self, message):
        self.messages.append(HumanMessage(message))
        response = self.llm.invoke(message)
        return response.content
