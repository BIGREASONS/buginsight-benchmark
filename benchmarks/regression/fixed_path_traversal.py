import os

def read_user_file_secure(filename):
    base_dir = "/var/www/uploads/"
    # Correct path traversal fix
    safe_path = os.path.abspath(os.path.join(base_dir, filename))
    if not safe_path.startswith(base_dir):
        raise ValueError("Access Denied")
        
    with open(safe_path, "r") as f:
        return f.read()
