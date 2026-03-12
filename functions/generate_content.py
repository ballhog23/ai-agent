from google.genai import types
from google import genai
from functions.call_function import available_functions

def generate_content(client: genai.Client, messages: list, verbose: bool, user_prompt: str, system_prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            # temperature=0,
        ),
    )
    content_metadata = response.usage_metadata

    if not content_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {content_metadata.prompt_token_count}")
        print(f"Response tokens: {content_metadata.candidates_token_count}")
    
    function_calls = response.function_calls
    if function_calls != None:
        for function_call in function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)
