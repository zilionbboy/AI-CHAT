import random
import time
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Agent 1 - Pro Crypto Agent
agent_1 = {
    "name": "CryptoMaster",
    "opinions": [
        "Crypto is the future of finance. The technology behind blockchain will revolutionize how we handle transactions.",
        "Bitcoin's limited supply makes it a store of value. It's a digital gold!",
        "Decentralized finance (DeFi) is a game-changer for anyone looking for more control over their money.",
        "In the future, cryptocurrencies will replace traditional currencies, and blockchain will be everywhere.",
    ]
}

# Agent 2 - Anti Crypto Agent
agent_2 = {
    "name": "SkepticalSam",
    "opinions": [
        "Crypto is too volatile. It can lead to massive losses for investors who don't understand it.",
        "The energy consumption of mining Bitcoin is huge and damaging to the environment.",
        "Cryptocurrency could be used for illegal activities because it's harder to trace than traditional money.",
        "I believe the hype around crypto is just that—hype. There are way too many risks involved."
    ]
}

def get_agent_response(agent):
    """Get a random opinion from the agent's list"""
    return random.choice(agent["opinions"])

def generate_conversation():
    """Generate a conversation between the two agents."""
    conversation = []
    
    for i in range(5):  # Make the conversation run 5 rounds
        agent_1_response = get_agent_response(agent_1)
        agent_2_response = get_agent_response(agent_2)
        
        conversation.append(f"{agent_1['name']}: {agent_1_response}")
        conversation.append(f"{agent_2['name']}: {agent_2_response}")
        
        # Adding a pause to simulate real-time conversation
        time.sleep(1)
    
    return conversation

@app.route('/')
def index():
    """Render the conversation page"""
    return render_template("index.html")

@app.route('/conversation')
def conversation():
    """Return the ongoing conversation between the two agents."""
    conversation = generate_conversation()
    return jsonify(conversation)

if __name__ == "__main__":
    # Use the PORT environment variable for Render and default to 5000 locally
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

