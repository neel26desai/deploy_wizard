# import os
# from langchain_openai import ChatOpenAI  # Updated import

# from langchain.schema import HumanMessage, AIMessage, SystemMessage

# class MyOpenAI:
#     FILE_WITH_SECRET = '/Users/mansivekariya/Documents/Keys'  # Optional, we will use the environment variable

#     def __init__(self, model="gpt-4o-mini"):
#         # Try to read the OpenAI API key from the environment variable
#         api_key = os.getenv("OPENAI_API_KEY")
#         if not api_key:
#             raise ValueError("API Key is missing from environment variables.")
        
#         # Initialize the OpenAI model with the API key set as an environment variable
#         self.llm = ChatOpenAI(model=model, temperature=0)
#         self.messages = []

#     def invoke(self, message):
#         """
#         Invokes the LLM with either a single message or a list of formatted messages.

#         - If `message` is a `str`, it is treated as a user message and added to the conversation.
#         - If `message` is a `list[dict]`, it is treated as a full message history and used directly.
#         """
        
#         if isinstance(message, str):  # Single user message
#             human_message = HumanMessage(content=message)
#             self.messages.append(human_message)
#             response = self.llm.invoke(self.messages)  # Maintain context
#         elif isinstance(message, list) and all(isinstance(m, dict) for m in message):  # List of messages
#             self.messages = self._convert_messages(message)  # Reset context
#             response = self.llm.invoke(self.messages)
#         else:
#             raise ValueError("Invalid message format. Must be a string or list of dicts.")

#         ai_message = AIMessage(content=response.content)
#         self.messages.append(ai_message)
        
#         return response.content

#     def _convert_messages(self, message_list):
#         """ Converts a list of dicts into LangChain message objects. """
#         converted_messages = []
#         for msg in message_list:
#             role = msg.get("role")
#             content = msg.get("content", "")
#             if role == "system":
#                 converted_messages.append(SystemMessage(content=content))
#             elif role == "user":
#                 converted_messages.append(HumanMessage(content=content))
#             elif role == "assistant":
#                 converted_messages.append(AIMessage(content=content))
#         return converted_messages


from langchain_openai import ChatOpenAI  # Use the updated package
from langchain.schema import HumanMessage, AIMessage, SystemMessage  # Add this line to import message classes

class MyOpenAI:
    def __init__(self, model="gpt-4o-mini", api_key=None):
        self.llm = ChatOpenAI(model=model, temperature=0, openai_api_key=api_key)
        self.messages = []
    
    def invoke(self, message):
        """Invokes the LLM with either a single message or a list of formatted messages."""
        if isinstance(message, str):  # Single user message
            human_message = HumanMessage(content=message)  # Using HumanMessage to format the message
            self.messages.append(human_message)
            response = self.llm.invoke(self.messages)  # Maintain context
        elif isinstance(message, list) and all(isinstance(m, dict) for m in message):  # List of messages
            self.messages = self._convert_messages(message)  # Reset context
            response = self.llm.invoke(self.messages)
        else:
            raise ValueError("Invalid message format. Must be a string or list of dicts.")
        
        ai_message = AIMessage(content=response.content)  # Format the response from AI
        self.messages.append(ai_message)
        
        return response.content

    def _convert_messages(self, message_list):
        """ Converts a list of dicts into LangChain message objects. """
        converted_messages = []
        for msg in message_list:
            role = msg.get("role")
            content = msg.get("content", "")
            if role == "system":
                converted_messages.append(SystemMessage(content=content))
            elif role == "user":
                converted_messages.append(HumanMessage(content=content))
            elif role == "assistant":
                converted_messages.append(AIMessage(content=content))
        return converted_messages
