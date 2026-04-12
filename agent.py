from groq import Groq
import os
from rag import get_answer
from tools import mock_lead_capture

class Agent:
    def __init__(self):
        Groq(api_key=os.getenv("GROQ_API_KEY"))

        self.state = {
            "name": None,
            "email": None,
            "platform": None,
            "stage": None
        }

    def detect_intent_llm(self, user_input):
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an intent classifier.

                    Rules:
                    - greeting → casual hi/hello
                    - pricing → asking about plans, cost, features
                    - high_intent → user wants to buy, try, subscribe, or shows interest in using product

                    IMPORTANT:
                    If user expresses desire to try, buy, or start → ALWAYS return high_intent
                    """
                },
                {
                    "role": "user",
                    "content": f"Message: {user_input}\nAnswer:"
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip().lower()

    def handle_input(self, user_input):

        # Lead flow
        if self.state["stage"] == "collect_name":
            self.state["name"] = user_input
            self.state["stage"] = "collect_email"
            return "Great! Please enter your email."

        elif self.state["stage"] == "collect_email":
            self.state["email"] = user_input
            self.state["stage"] = "collect_platform"
            return "Awesome! Which platform do you create on?"

        elif self.state["stage"] == "collect_platform":
            self.state["platform"] = user_input

            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"]
            )

            self.state["stage"] = None
            return "🎉 You're all set! Our team will contact you soon."

        # REAL AI INTENT
        intent = self.detect_intent_llm(user_input)

        if "greeting" in intent:
            return "Hey 👋 Welcome to AutoStream! How can I help you?"

        elif "pricing" in intent:
            return get_answer(user_input)

        elif "high_intent" in intent:
            self.state["stage"] = "collect_name"
            return "🔥 Awesome! Let's get you started.\nWhat's your name?"

        else:
            return "Can you clarify your question?"