from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    # Safe: escapes HTML characters
    safe_name = html.escape(name)
    response = make_response(f"<h1>Hello {safe_name}</h1>")
    return response
