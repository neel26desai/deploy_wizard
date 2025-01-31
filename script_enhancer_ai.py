import argparse
import openai
import traceback

class ScriptEnhancerAI:
    """
    Uses AI to enhance a basic prediction script with logging and error handling.
    """
    def __init__(self, api_key, input_file, output_file):
        self.api_key = api_key
        self.input_file = input_file
        self.output_file = output_file
        openai.api_key = self.api_key

    def read_script(self):
        """
        Reads the input script file.
        """
        try:
            print(f"🔹 Attempting to read {self.input_file}...")  # Debugging print
            with open(self.input_file, 'r') as file:
                script_content = file.read()
            print(f"✅ Successfully read {self.input_file}")  # Debugging print
            return script_content
        except FileNotFoundError:
            raise ValueError(f"❌ Error: Input file {self.input_file} not found.")

    def enhance_script_with_ai(self, script_content):
        """
        Uses OpenAI's API to enhance the script with logging and error handling.
        """
        try:
            print("🔹 Sending request to OpenAI API...")  # Debugging print
            prompt = f"""
You are an experienced software engineer. Improve the following Python script by:
1. Adding logging (info, error) to track execution.
2. Adding try-except blocks for robust error handling.
3. Making it production-ready while keeping the functionality intact.

Here is the script:
{script_content}
"""

            # 🔹 UPDATED OpenAI API USAGE 🔹

            client = openai.OpenAI(api_key=self.api_key)  # Explicitly set API key

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0
            )

            enhanced_script = response.choices[0].message.content.strip()
            print("✅ AI Enhancement Successful! Output:\n", enhanced_script)  # Debugging print
            return enhanced_script
        except Exception as e:
            raise RuntimeError(f"❌ AI enhancement failed: {e}")

    def save_enhanced_script(self, enhanced_script):
        """
        Saves the enhanced script to the output file.
        """
        try:
            print(f"🔹 Saving the script to {self.output_file}...")  # Debugging print
            with open(self.output_file, 'w') as file:
                file.write(enhanced_script)
            print(f"✅ Enhanced script saved successfully as {self.output_file}")  # Debugging print
        except Exception as e:
            print(f"❌ Error saving file {self.output_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Enhance a basic prediction script with logging and error handling using AI.")
    parser.add_argument("api_key", type=str, help="Your OpenAI API key.")
    parser.add_argument("input_file", type=str, help="Path to the input script file.")
    parser.add_argument("output_file", type=str, help="Path to save the enhanced script.")

    args = parser.parse_args()
    enhancer = ScriptEnhancerAI(args.api_key, args.input_file, args.output_file)

    try:
        print("🔹 Starting enhancement process...")
        script_content = enhancer.read_script()
        enhanced_script = enhancer.enhance_script_with_ai(script_content)
        enhancer.save_enhanced_script(enhanced_script)
        print("✅ Enhancement process completed successfully!")
    except Exception as e:
        print("❌ An error occurred:")
        traceback.print_exc()  # Print full error details

if __name__ == "__main__":
    main()
