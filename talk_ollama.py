from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, AIMessage, SystemMessage

class Ollama:
    def __init__(self, model_name="gemma2:2b"):
        self.llm = ChatOllama(model=model_name, temperature=0)
        self.messages = [("system", 'You are an expert DevOps Engineer')]  # Setting the system prompt
    
    def invoke(self, message):
        """Invokes the Ollama model with a user message."""
        # Append the user's message to the conversation history
        self.messages.append(('human', message))
        
        # Get a response from Ollama
        response = self.llm.invoke(message)
        
        # Append the model's response to the conversation history
        self.messages.append(('ollama', response.content))
        
        return response.content
