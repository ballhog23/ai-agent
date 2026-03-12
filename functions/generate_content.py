from google import genai
from google.genai import types

def generate_content(client: genai.Client, messages: list, verbose: bool, user_prompt: str, system_prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0
        ),
    )
    content_metadata = response.usage_metadata

    if not content_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {content_metadata.prompt_token_count}")
        print(f"Response tokens: {content_metadata.candidates_token_count}")

    print(response.text)
