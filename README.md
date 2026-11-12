Rule-Based AI Chatbot

Overview

This project is a simple Python-based Rule-Based AI Chatbot that interacts with users through predefined rules, keyword matching, and fuzzy matching.

The chatbot identifies user intents based on input patterns and provides appropriate responses. It also includes basic input preprocessing and rule-based guardrails to handle unsupported or inappropriate requests.

Features

* Rule-based conversational responses
* Multiple predefined intents
* Dictionary-based keyword matching
* Input normalization using strip() and lower()
* Text cleaning using Python’s re module
* Fuzzy matching using RapidFuzz
* Similarity threshold for approximate keyword matching
* Basic rule-based guardrails
* Fallback responses for unknown inputs
* Continuous conversation loop
* Exit functionality using commands such as bye and exit

Technologies Used

* Python 3.10+
* RapidFuzz
* Regular Expressions (re)
* Python Dictionaries and Lists

Project Structure

Rule_Based_AI_Chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
└── .gitignore

Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project directory

cd Rule_Based_AI_Chatbot

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

How to Run

Run the chatbot using:

python chatbot.py

Example Conversation

Chatbot: Hello! How can I help you?
You: hello
Chatbot: Hello! How can I help you?
You: helo
Chatbot: [Appropriate greeting response]
You: bye
Chatbot: Goodbye!

Actual responses depend on the rules and intents implemented in the chatbot.

Guardrails

The chatbot implements basic rule-based guardrails to identify and handle certain inappropriate or unsupported requests.

These guardrails use predefined keywords and contextual rules.

Note: These are basic educational guardrails, not a comprehensive security system or advanced semantic safety mechanism.

Limitations

* Responses are based on predefined rules.
* The chatbot does not understand language like a large language model.
* Its ability to recognize user intent depends on available keywords and fuzzy matching.
* Guardrails are limited to predefined conditions.
* It does not maintain advanced conversational memory.

Future Improvements

* Add more conversational intents.
* Improve context-aware responses.
* Implement more advanced guardrails.
* Add a graphical user interface.
* Integrate NLP-based intent classification.

Author

Hadia Rani

Project: Rule-Based AI Chatbot