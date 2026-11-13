
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

print("Testing Groq connection...")

llm = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-20b",
    temperature=0
)

response = llm.invoke("Say Hello in one sentence.")

print("\nSUCCESS! Groq is connected.")
print(response.content)
