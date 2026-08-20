import json
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is not set. Please configure your Groq API key."
    )

client = Groq(api_key=api_key)


def load_knowledge_base():
    with open("data/knowledge.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_answer(query):
    try:
        data = load_knowledge_base()

        context = json.dumps(data, indent=2)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the AutoStream product assistant. "
                        "Answer the user's question using ONLY the provided context. "
                        "If the answer is not present in the context, clearly say "
                        "that the information is not available."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Context:\n{context}\n\n"
                        f"Question: {query}"
                    ),
                },
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except FileNotFoundError:
        return "Sorry, the product knowledge base could not be found."

    except Exception as error:
        print(f"RAG error: {error}")

        return (
            "Sorry, I couldn't retrieve that information right now. "
            "Please try again later."
        )