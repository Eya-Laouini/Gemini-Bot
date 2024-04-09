import google.generativeai as genai
from api import Gemini_API_KEY as api

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
while True:
    user_input = input("\nYou: ")

    response = chat.send_message(user_input)
    print("AI:", response.text)
