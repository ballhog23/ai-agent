from functions.args import parse_args
from functions.generate_content import generate_content
from functions.env_or_throw import env_or_throw
from functions.get_files_info import get_files_info

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    args = parse_args()

    load_dotenv()
    GEMINI_API_KEY = env_or_throw("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    user_prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    verbose_check = args.verbose
    get_files_info("calculator")
    # call gemini api
    # generate_content(client, messages, verbose_check, user_prompt)


if __name__ == "__main__":
    main()
