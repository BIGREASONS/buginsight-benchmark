def get_api_client():
    # Vulnerable to hardcoded secrets
    api_key = "AKIAIOSFODNN7EXAMPLE"
    secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    return {"key": api_key, "secret": secret_key}
