# llm/llm_client.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def generate_patch(prompt):

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    result = generate_patch(
        "Fix SQL Injection in: query = 'SELECT * FROM users WHERE id=' + user_input"
    )

    print(result)