from groq import Groq
import os
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def get_answer(query):
    with open("data/knowledge.json") as f:
        data = json.load(f)

    context = str(data)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Answer using ONLY the given context."
            },
            {
                "role": "user",
                "content": f"""
                Context: {context}

                Question: {query}
                """
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content