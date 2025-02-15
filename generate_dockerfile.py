import openai
import os

# Load API Key securely from environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

def generate_dockerfile():
    prompt = """
Generate a Dockerfile for a Flask application that:
- Uses a lightweight Python base image.
- Installs dependencies from `requirements.txt`.
- Copies the application code to `/app` in the container.
- Exposes port 5000 and runs `flask_app.py`.

The application should be production-ready and handle errors properly.
"""

    client = openai.OpenAI(api_key=API_KEY)  

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}]
    )

    dockerfile_content = response.choices[0].message.content

    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

    print("Dockerfile generated successfully!")

if __name__ == "__main__":
    generate_dockerfile()
