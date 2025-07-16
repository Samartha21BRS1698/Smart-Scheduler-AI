# code for scheduler_agent.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the API with proper error handling
try:
    genai.configure(api_key=API_KEY)
    
    # List available models to verify
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"Available model: {model.name}")
    
    # Use the correct model name
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
except Exception as e:
    print(f"❌ Configuration Error: {str(e)}")
    raise

def ask_agent(user_message: str) -> str:
    """Send a message to the Gemini model and return the response."""
    try:
        # Create a chat session for multi-turn conversation
        chat = model.start_chat(history=[])
        
        # Send the message with safety settings configured
        response = chat.send_message(
            user_message,
            safety_settings={
                'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
                'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE'
            },
            generation_config={
                "temperature": 0.7,
                "top_p": 1,
                "top_k": 32,
                "max_output_tokens": 1024,
            }
        )
        return response.text
    except Exception as e:
        return f"❌ Error generating response: {str(e)}"