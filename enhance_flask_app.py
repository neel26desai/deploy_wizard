import openai
import os

# Load API Key securely from environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

def enhance_flask_app():
    with open("flask_app.py", "r") as file:
        original_code = file.read()

    prompt = f"""
Improve the following Flask application to be more Docker-friendly by:
- Adding proper logging.
- Handling startup errors.
- Ensuring it runs smoothly inside a container.

Here is the current code:
{original_code}
"""

    client = openai.OpenAI(api_key=API_KEY)  #Secure API key usage

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  #Use GPT-3.5 for availability
        messages=[{"role": "user", "content": prompt}]
    )

    enhanced_code = response.choices[0].message.content

    with open("flask_app.py", "w") as file:
        file.write(enhanced_code)

    print("`flask_app.py` has been enhanced for Docker compatibility!")

if __name__ == "__main__":
    enhance_flask_app()
