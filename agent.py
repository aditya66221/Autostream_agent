import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

from rag import get_answer
from tools import mock_lead_capture

class Agent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set. Please configure your Groq API key."
            )

        self.client = Groq(api_key=api_key)

        self.state = {
            "name": None,
            "email": None,
            "platform": None,
            "stage": None,
        }

    def detect_intent_llm(self, user_input):
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an intent classifier for AutoStream.

Classify the user's message into exactly one of these categories:

- greeting → casual greetings such as hi, hello, hey
- product_question → questions about AutoStream, its product, features, pricing, plans, policies, platforms, support, or how it works
- high_intent → user wants to buy, try, subscribe, start, or shows clear interest in using AutoStream
- other → unrelated questions

IMPORTANT:
If the user expresses a desire to buy, try, subscribe, or start using the product,
return high_intent.

Return only the category name.
""",
                },
                {
                    "role": "user",
                    "content": f"Message: {user_input}\nAnswer:",
                },
            ],
            temperature=0,
        )

        intent = response.choices[0].message.content.strip().lower()

        valid_intents = {"greeting", "product_question", "high_intent", "other"}

        # Handle occasional extra LLM text safely.
        for valid_intent in valid_intents:
            if valid_intent in intent:
                return valid_intent

        return "other"

    @staticmethod
    def _is_valid_email(email):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        return bool(re.match(pattern, email))

    def handle_input(self, user_input):
        user_input = user_input.strip()

        if not user_input:
            return "Please enter a message."

        # -------------------------
        # Lead collection state flow
        # -------------------------

        if self.state["stage"] == "collect_name":
            if len(user_input) < 2:
                return "Please enter a valid name."

            self.state["name"] = user_input
            self.state["stage"] = "collect_email"

            return "Great! Please enter your email."

        elif self.state["stage"] == "collect_email":
            if not self._is_valid_email(user_input):
                return "Please enter a valid email address."

            self.state["email"] = user_input
            self.state["stage"] = "collect_platform"

            return "Awesome! Which platform do you create on?"

        elif self.state["stage"] == "collect_platform":
            if len(user_input) < 2:
                return "Please enter the platform you create on."

            self.state["platform"] = user_input

            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"],
            )

            self.state["stage"] = None

            return "🎉 You're all set! Our team will contact you soon."

        # -------------------------
        # Normal intent-based flow
        # -------------------------

        try:
            intent = self.detect_intent_llm(user_input)

            if intent == "greeting":
                return "Hey 👋 Welcome to AutoStream! How can I help you?"

            elif intent == "product_question":
                return get_answer(user_input)

            elif intent == "high_intent":
                self.state["stage"] = "collect_name"

                return "🔥 Awesome! Let's get you started.\nWhat's your name?"

            else:
                return (
                    "I'm here to help with AutoStream. "
                    "You can ask me about our features, pricing, "
                    "supported platforms, or plans."
                )

        except Exception as error:
            print(f"Agent error: {type(error).__name__}: {error}")
            return f"DEBUG ERROR: {type(error).__name__}: {error}"