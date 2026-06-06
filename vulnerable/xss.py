from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    # Vulnerable to XSS
    response = make_response(f"<h1>Hello {name}</h1>")
    return response
