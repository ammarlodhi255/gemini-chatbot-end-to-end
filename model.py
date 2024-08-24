import os 
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a model to generate responses
model = genai.GenerativeModel("gemini-pro")

def get_model():
    return model
