
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAvIk3QMAk8DKce8hwXocrdsgPf8MXjZ54")

try:
    print("Listing models...")
    models = genai.list_models()
    with open("models_list.txt", "w") as f:
        for m in models:
            if "gemini" in m.name:
                f.write(f"{m.name}\n")
                print(m.name)
except Exception as e:
    print(f"Error: {e}")
