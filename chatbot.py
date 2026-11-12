from rapidfuzz import process, fuzz
import re
chatbot = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! What can I do for you?",
    "hey": "Hey there! How's it going?",
    "thanks": "You're welcome! If you have any more questions, feel free to ask.",
    "what is your name": "I'm a simple chatbot created to assist you. You can call me Chatbot.",
    "help": "Sure! How can I help?",
    "how are you": "I am doing great!"
}
blocked_requests = ["hack", "malware", "virus", "phishing", "illegal", "steal", "attack", "exploit", "bypass", "crack"]
safe_requests = ["prevent", "protect", "secure", "defend", "safeguard", "shield", "guard", "fortify", "strengthen", "enhance", "avoid"]
while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    is_blocked = any(word in user_input for word in blocked_requests)
    is_safe = any(word in user_input for word in safe_requests)
    if is_blocked and not is_safe:
        print("Chatbot: I'm sorry, I cannot assist with that request.")
        continue
    elif is_safe:
        print("Chatbot: I'm glad you're interested in safety measures!")
        continue
    cleaned_input = re.sub(r'[^\w\s]', '', user_input)
    best_match = process.extractOne(cleaned_input, chatbot.keys(), scorer=fuzz.ratio, score_cutoff=70)
    if best_match:
        matched_key = best_match[0]
        print("Chatbot: " + chatbot[matched_key])
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase or ask something else?")

