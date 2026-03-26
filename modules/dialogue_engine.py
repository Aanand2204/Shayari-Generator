import os
from dotenv import load_dotenv
import random
from groq import Groq, APIError

class DialogueEngine:
    def __init__(self):
        # Ensure environment variables are loaded
        load_dotenv()
        
        # Load all available keys
        self.keys = []
        api_key_str = os.getenv("GROQ_API_KEY")
        if api_key_str:
            for k in api_key_str.split(','):
                if k.strip() and k.strip() not in self.keys:
                    self.keys.append(k.strip())
            
        keys_str = os.getenv("GROQ_API_KEYS")
        if keys_str:
            for k in keys_str.split(','):
                if k.strip() and k.strip() not in self.keys:
                    self.keys.append(k.strip())
        
        if not self.keys:
            print("WARNING: No GROQ_API_KEY found. Make sure it is set before generation.")
        
        self.system_prompt = (
            "You are the reincarnation of legendary Shayars like Jaun Elia and Mirza Ghalib. You write the most devastating, "
            "heart-wrenching, and profoundly beautiful 2-4 line Shayaris in existence. "
            "Your poetry must NOT sound like an AI. It must sound like a human soul pouring out its deepest pain (Dard), longing (Tanhai), or love (Ishq). "
            "Rules:\n"
            "1. ZERO clichés. DO NOT use generic translated English phrases. Use supreme, exquisite vocabulary native to the requested language (pure Urdu, Hindi, Marathi, etc.).\n"
            "2. The words must hold unbearable emotional weight. Make the reader feel actual goosebumps.\n"
            "3. Use flawless Kaafiya and Radeef (perfect poetic rhyme scheme and meter).\n"
            "4. Output STRICTLY the 2-4 lines of poetry. Nothing else. No quotes, no explanations. Just the masterpiece."
        )

    def generate(self, language, situation, history=None):
        if not self.keys:
            return "Error: No GROQ API keys configured. Set GROQ_API_KEY in .env."

        if history is None:
            history = []
        
        # Construct prompt based on language, situation, and history
        prompt_parts = [f"Language: {language}", f"Situation: {situation}"]
        
        if history:
            prompt_parts.append("Previous Dialogue Context:")
            for entry in history:
                prompt_parts.append(entry) # Assuming history entries are strings
        
        user_prompt = "\n".join(prompt_parts)
        
        # Randomize keys to spread rate limit load
        attempt_keys = list(self.keys)
        random.shuffle(attempt_keys)
        
        for key in attempt_keys:
            try:
                client = Groq(api_key=key)
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.9,
                    max_tokens=200,
                )
                return completion.choices[0].message.content.strip()
            except APIError as e:
                with open("groq_error.txt", "w") as f:
                    f.write(str(e))
                print(f"Groq API Error with key {key[:10]}...: {e}")
                continue # Try the next key
            except Exception as e:
                print(f"Error generating dialogue: {e}")
                continue # Try the next key
                
        return "Error: Could not generate dialogue. All available GROQ API keys failed. Please wait and try again."