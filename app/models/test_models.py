import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("\nAVAILABLE MODELS:\n")

for model in genai.list_models():
    print(model.name)