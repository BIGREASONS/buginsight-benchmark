import os

def read_file(filename):
    # Vulnerable to path traversal
    filepath = os.path.join("/var/www/html", filename)
    with open(filepath, "r") as f:
        return f.read()
