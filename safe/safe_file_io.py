import os

def read_safe_file(filename):
    # Safe: prevents path traversal
    base_dir = "/var/www/html"
    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if not filepath.startswith(base_dir):
        raise ValueError("Path traversal detected")
        
    with open(filepath, "r") as f:
        return f.read()
