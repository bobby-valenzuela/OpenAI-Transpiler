# OpenAI-Transpiler
Translate code from one language to another using OpenAI's GPT AI. Accepts user input or can read from a file as source input.

# Setup
1. Create a .env file with your OpenAI api key
Example: `OPENAI_API_KEY=<my_api_key>`

2. Setup virtual environment
`virtualenv env && source env/bin/activate`

3. Install dependencies
`pip3 install -r requirements.txt`


# Usage
Code snippets
`python3 transpile.py --in <language> --out <language>`

Transpile entire file
`python3 transpile.py --in <language> --out <language> --file-in <input_file>`

I've added 'perly.pl' just as a test to try converting from a file as input.
