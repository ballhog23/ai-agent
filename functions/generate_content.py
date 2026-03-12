from google.genai import types
from google import genai
from functions.call_function import available_functions, call_function

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
        print(f"User Prompt: {user_prompt}")
        print(f"Prompt tokens: {content_metadata.prompt_token_count}")
        print(f"Response tokens: {content_metadata.candidates_token_count}")
    
    if not response.function_calls:
        print("Response:")
        print(response.text)
        return
    
    function_responses = []
    for function_call in response.function_calls:
        result = call_function(function_call, verbose)
        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")

        function_responses.append(result.parts[0])