import os

def env_or_throw(env_var_string: str) -> str:
    env_var = os.environ.get(env_var_string)
    if env_var == None:
        raise RuntimeError(f"{env_var_string} NOT SET IN .env")
    return env_var
