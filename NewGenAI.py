# from dotenv import load_dotenv
# import os
# load_dotenv()
# from google import genai

# # client = genai.Client(api_key=AIzaSyDdnvrUJ9xPs2dT0m2MR_--o1i7oi96lus))
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)