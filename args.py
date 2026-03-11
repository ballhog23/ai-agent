import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Chatbot")
    # args
    parser.add_argument("user_prompt", type=str, help="User prompt: expects a string prompt to pass to gemini")
    # flags
    parser.add_argument("--verbose", action="store_true", help="Enbable verbose output")
    
    return parser.parse_args()