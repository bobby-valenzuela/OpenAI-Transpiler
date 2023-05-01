# OpenAI-Transpiler
Translate code from one language to another using OpenAI's GPT AI. Accepts user input or can read from a file as source input.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd OpenAI-Transpiler
   ```

4. Create a new virtual environment:

   ```bash
   $ python3 -m venv env && . env/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip3 install -r requirements.txt
   ```

6. Create a .env file with your OpenAI api key

   ```bash
   $ echo "OPENAI_API_KEY={api_secret} > .env 
   ```


## Usage

### Transpiler
`python3 transpile.py --in <language> --out <language>`

Transpile entire file
`python3 transpile.py --in <language> --out <language> --file-in <input_file>`

I've added 'perly.pl' just as a test to try converting from a file as input.

### Time Complexity Calculator
`python3 time_complexity_calculator.py 
