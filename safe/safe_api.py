import os

def get_api_client():
    # Safe: loads from environment variables
    api_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    if not api_key or not secret_key:
        raise ValueError("Missing AWS credentials")
    return {"key": api_key, "secret": secret_key}
