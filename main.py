from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from config import MAX_AGENT_ITERATIONS
import sys
from functions.args import parse_args
from functions.generate_content import generate_content
from functions.env_or_throw import env_or_throw

def main():
    args = parse_args()

    load_dotenv()
    GEMINI_API_KEY = env_or_throw("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    user_prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    verbose_check = args.verbose

    if verbose_check:
        print(f"User Prompt: {user_prompt}")

    # allow agent to iterate on a task until task completion, limiting to MAX_AGENT_ITERATIONS, else exit with 1
    for _ in range(MAX_AGENT_ITERATIONS):
        response = generate_content(client, messages, verbose_check)

        # generate_content will return content.text whenever there are no longer any function_calls remaining
        if response:
            break
    else:
        print("MAX_AGENT_ITERATIONS reached... exiting")
        sys.exit(1)


if __name__ == "__main__":
    main()
