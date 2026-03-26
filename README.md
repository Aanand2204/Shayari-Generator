# AI Shayari Maker

AI Shayari Maker is a web application that generates profoundly beautiful, heart-wrenching 2-4 line Shayaris using the Groq API (powered by Llama 3 models). Designed to evoke the legendary styles of Shayars like Jaun Elia and Mirza Ghalib, this application creates emotionally resonant poetry in multiple languages based on any situation you provide.

## Features
- **Authentic Poetry Generation:** Crafts authentic Shayaris with proper *Kaafiya* and *Radeef* (poetic rhyme scheme and meter), completely avoiding generic or clichéd AI responses.
- **Multilingual Support:** Generates poetry in a variety of languages including Urdu, Hindi, Marathi, English, and more.
- **Context Awareness:** Maintains conversation history within a single session to provide contextually relevant continuity in generations.
- **Robust API Key Management:** Features an automatic API key rotation and fallback mechanism using the Groq API to ensure high availability and seamlessly handle rate limits.
- **Lightweight Backend:** Built entirely on Flask for a fast and efficient web server experience.

## Prerequisites
- Python 3.7+
- A [Groq API Key](https://console.groq.com/keys)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Groq API key(s) along with a Flask secret key. You can add multiple comma-separated keys for rate limit rotation.
   ```env
   GROQ_API_KEY=your_groq_api_key_1,your_groq_api_key_2
   FLASK_SECRET_KEY=your_secure_flask_session_key
   FLASK_DEBUG=True
   ```
   *Note: If `FLASK_SECRET_KEY` is not provided, the app will use a default development key, which is unsafe for production.*

## Usage

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the web interface:**
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Generate Shayari:**
   Input your desired language and a prompt describing the situation or emotion (Dard, Tanhai, Ishq), then generate your poetry.

## Project Structure
- `app.py`: Main Flask application handling web routes, request parsing, and session management.
- `modules/dialogue_engine.py`: Core AI logic for interacting with Groq, crafting the system persona prompt, and managing API key rotation/fallbacks.
- `templates/`: Contains the frontend HTML files (`index.html`).
- `static/`: Contains static assets like CSS and JavaScript files for styling the UI.
- `requirements.txt`: List of Python library dependencies.
