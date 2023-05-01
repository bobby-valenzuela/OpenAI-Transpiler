#!/usr/bin/env python3
import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values('.env');
openai.api_key = config["OPENAI_API_KEY"]


def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def getLangName(lang):
    # Handle full lanaguage name or file extension

    try:
        lang = str(lang)
    except TypeError:
        print("Please used a string data type for the language you are converting to")

    lang = "JavaScript" if lang.lower() == "javascript" or lang.lower() == "js" else lang
    lang = "TypeScript" if lang.lower() == "typescript" or lang.lower() == "ts" else lang
    lang = "Bash" if lang.lower() == "bash" or lang.lower() == "sh" else lang
    lang = "Powershell" if lang.lower() == "powershell" or lang.lower() == "ps1" else lang
    lang = "Perl" if lang.lower() == "perl" or lang.lower() == "pl" else lang
    lang = "Python" if lang.lower() == "python" or lang.lower() == "py" else lang
    lang = "C++" if lang.lower() == "c++" or lang.lower() == "cpp" else lang
    lang = "C" if lang.lower() == "c" else lang

    return lang

def main():

    parser = argparse.ArgumentParser(description="Simple command line chabot with GPT-3.5")
    parser.add_argument("--incoming",type=str,default="JavaScript",help="(Incoming) The incoming programming language to be translated",required=True)
    parser.add_argument("--outgoing",type=str,default="Python",help="(Outgoing) The programming language to be translated",required=True)
    parser.add_argument("--file-in",type=str,help="(Incoming) Incoming file containing the code to be transpiled",required=False)

    args = parser.parse_args()
    in_lang = getLangName(args.incoming)
    out_lang = getLangName(args.outgoing)
    file_in = args.file_in # parser converts hyphens to underscores
    
    # converted_dict = vars(args)

    print(blue("Converting from ") + bold(in_lang) + blue(" to ") + bold(out_lang) + "\n")

    while True:

        in_code = ''

        if file_in :
            f = open(file_in, "r")
            in_code = f.read()

        else:
            in_code = input(str(f"You ({red(in_lang)}): "))

        try:

            message = [
                {"role": "user", "content": f"Translate the following {in_lang} to {out_lang}: {in_code}"}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message,
                max_tokens=200
            )

            reply = response.choices[0].message.content

            print(f"Transpiler ({red(out_lang)}): \n" + reply + "\n")

            if file_in :
                exit()

        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()





