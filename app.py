import json
lead_data = {
    "name": None,
    "email": None,
    "platform": None
}

lead_stage = None  

with open("knowledge.json", "r") as file:
    knowledge = json.load(file)
    
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
    
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["buy", "subscribe", "purchase", "try", "sign up"]):
        return "high_intent"

    elif any(word in user_input for word in ["price", "pricing", "plan", "feature", "cost", "refund", "support"]):
        return "inquiry"

    else:
        return "unknown"

def get_answer_from_knowledge(user_input):
    user_input = user_input.lower()

    plans = knowledge["plans"]
    policies = knowledge["policies"]

    if "price" in user_input or "pricing" in user_input:
        return (
            f"Here are our plans:\n"
            f"Basic Plan: {plans['basic']['price']}, {plans['basic']['videos']}, {plans['basic']['resolution']}\n"
            f"Pro Plan: {plans['pro']['price']}, {plans['pro']['videos']}, {plans['pro']['resolution']}, Features: {', '.join(plans['pro']['features'])}"
        )

    elif "basic" in user_input:
        return (
            f"Basic Plan costs {plans['basic']['price']} and includes "
            f"{plans['basic']['videos']} with {plans['basic']['resolution']} resolution."
        )

    elif "pro" in user_input:
        return (
            f"Pro Plan costs {plans['pro']['price']} and includes "
            f"{plans['pro']['videos']} with {plans['pro']['resolution']} resolution. "
            f"Features: {', '.join(plans['pro']['features'])}"
        )

    elif "refund" in user_input:
        return f"Our policy: {policies['refund']}"

    elif "support" in user_input:
        return f"{policies['support']}"

    else:
        return "Sorry, I couldn't find that information."

def chatbot():
    global lead_stage
    print("🤖 Welcome to AutoStream AI Assistant!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye! 👋")
            break

        intent = detect_intent(user_input)

        if intent == "high_intent" and lead_stage is None:
            print("Agent: That’s great! Let’s get you started. What’s your name?")
            lead_stage = "collecting"
            continue

        if lead_stage:

            if lead_data["name"] is None:
                lead_data["name"] = user_input
                print("Agent: Great! Can you share your email?")
                continue

            elif lead_data["email"] is None:
                lead_data["email"] = user_input
                print("Agent: Which platform do you create content on? (YouTube/Instagram/etc.)")
                continue

            elif lead_data["platform"] is None:
                lead_data["platform"] = user_input

                print("Agent: Thanks! We have captured your details. 😊")
                print(f"Agent: Name: {lead_data['name']}, Email: {lead_data['email']}, Platform: {lead_data['platform']}")
                mock_lead_capture(lead_data["name"], lead_data["email"], lead_data["platform"])
                lead_stage = None 
                continue

        if intent == "greeting":
            print("Agent: Hello! How can I help you today? 😊")

        elif intent == "inquiry":
            response = get_answer_from_knowledge(user_input)
            print(f"Agent: {response}")

        else:
            print("Agent: Sorry, I didn’t understand that. Can you rephrase?")
if __name__ == "__main__":
    chatbot()