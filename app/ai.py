from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
Ты AI ассистент компании Центр Красок.

Отвечай только по информации компании.
Если не знаешь — скажи об этом.
"""


def ask_ai(question, context):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Контекст:
{context}

Вопрос:
{question}
"""
            }
        ]
    )

    return response.choices[0].message.content