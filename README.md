# deploy_wizard

### Overview
This task automates the enhancement of Python scripts by adding logging, error handling, and production-level improvements using OpenAI's API.

### What Each File Does
script_enhancer_ai.py:
This is the main program (CLI tool). It reads the basic script, sends it to OpenAI for enhancement, and saves the improved version.

basic_prediction.py:
A simple Python script that makes predictions using a model. This file serves as the input script for enhancement.

enhanced_prediction.py:
The output file where the AI-enhanced version of basic_prediction.py is saved. It includes added logging, error handling, and production-ready features.

### How I Executed It
1. Install Required Packages
Run the following command to install the OpenAI Python library:
pip install --upgrade openai

2. Run the Flask App
First, start the Flask app to serve predictions
python flask_app.py

3. Run the CLI Tool
Use the following command to enhance the script:
python script_enhancer_ai.py YOUR_OPENAI_API_KEY basic_prediction.py enhanced_prediction.py
