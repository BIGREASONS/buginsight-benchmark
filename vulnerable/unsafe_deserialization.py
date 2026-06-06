import pickle
import base64

def load_data(serialized_data):
    # Vulnerable: unpickles untrusted data
    data = base64.b64decode(serialized_data)
    return pickle.loads(data)
