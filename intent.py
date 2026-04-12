def detect_intent(user_input):
    user_input = user_input.lower()

    # HIGH INTENT FIRST (IMPORTANT)
    if any(x in user_input for x in ["buy", "subscribe", "want", "try", "start"]):
        return "high_intent"

    elif any(x in user_input for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in user_input for x in ["price", "plan", "cost"]):
        return "pricing"

    return "other"