import os
from flask import Flask, render_template, request, jsonify, session
from modules.dialogue_engine import DialogueEngine

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "super_secret_dev_key_please_change") # Load from env, fallback for dev
if app.secret_key == "super_secret_dev_key_please_change":
    print("WARNING: FLASK_SECRET_KEY is not set in environment. Using a default development key. CHANGE THIS FOR PRODUCTION!")
engine = DialogueEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    language = data.get('language', 'English')
    situation = data.get('situation', '')
    
    # Get history from session
    history = session.get('dialogue_history', [])
    print(f"DEBUG: Session History Length: {len(history)}")
    
    dialogue = engine.generate(language, situation, history=history)
    print(f"DEBUG: Generated Dialogue: {dialogue[:50]}...")
    
    # Update history - Truncate dialogue for session storage
    MAX_DIALOGUE_HISTORY_LENGTH = 500
    truncated_dialogue = dialogue[:MAX_DIALOGUE_HISTORY_LENGTH]
    if len(dialogue) > MAX_DIALOGUE_HISTORY_LENGTH:
        truncated_dialogue += "..." # Indicate truncation
    
    history.append(truncated_dialogue)
    if len(history) > 5:
        history.pop(0)
    session['dialogue_history'] = history
    
    return jsonify({'dialogue': dialogue})

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)