# OpenAI-Transpiler
Translate code from one language to another using OpenAI's GPT AI. Accepts user input or can read from a file as source input.

# Setup
1. Create a .env file with your OpenAI api key under OPENAI_API_KEY and install dependencies 

# Usage
Code snippets
`python3 transpile.py --in <language> --out <language>`

Transpile entire file
`python3 transpile.py --in <language> --out <language> --file-in <input_file>`

I've added 'perly.pl' just as a test to try converting from a file as input.
