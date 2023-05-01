#!/usr/bin/env python3
import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]

def main():

    try:

        # Accept multiple lines of iniput
        print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
        contents = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)

        in_code = "".join(contents)

        messages = [
            {"role": "user", "content": f"""Calculate the time complexity of the following function: {in_code} """}
        ]

        res = openai.ChatCompletion.create(
            messages=messages,
            model="gpt-4"
        )

        print("\n\n" + res["choices"][0]["message"]["content"])

    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()





