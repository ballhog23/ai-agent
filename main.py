import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from args import parse_args

def main():
    args = parse_args()

    load_dotenv()
    GEMINI_API_KEY = env_or_throw("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    user_prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    verbose_check = args.verbose

    # call gemini api
    generate_content(client, messages, verbose_check, user_prompt)

    

def env_or_throw(env_var_string: str) -> str:
    env_var = os.environ.get(env_var_string)
    if env_var == None:
        raise RuntimeError(f"{env_var_string} NOT SET IN .env")
    return env_var

def generate_content(client: genai.Client, messages: list, verbose: bool, user_prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )
    content_metadata = response.usage_metadata

    if not content_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {content_metadata.prompt_token_count}")
        print(f"Response tokens: {content_metadata.candidates_token_count}")

    print(response.text)

if __name__ == "__main__":
    main()
