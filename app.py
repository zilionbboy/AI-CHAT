from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

# Sample messages for each agent
crypto_fan_messages = [
    "Crypto is the future of finance!",
    "Have you seen the latest BTC rally?",
    "Blockchain solves real-world problems.",
    "Decentralized finance (DeFi) is the next big thing."
]

crypto_critic_messages = [
    "Crypto is too volatile to be reliable.",
    "Most blockchain projects fail.",
    "What about the energy consumption of Bitcoin?",
    "Traditional finance is much safer."
]

conversation = []

@app.route('/get_chat', methods=['GET'])
def get_chat():
    global conversation
    # Alternate between agents
    if len(conversation) == 0 or conversation[-1]["role"] == "critic":
        new_message = {"role": "fan", "content": random.choice(crypto_fan_messages)}
    else:
        new_message = {"role": "critic", "content": random.choice(crypto_critic_messages)}

    conversation.append(new_message)

    # Limit chat history to the last 20 messages
    conversation = conversation[-20:]
    return jsonify(conversation)

if __name__ == '__main__':
    app.run(debug=True)
