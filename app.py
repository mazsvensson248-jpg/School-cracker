from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/proxy")
def proxy():
    query = request.args.get("q", "")
    if not query:
        return "Please provide a search query.", 400

    duck_url = f"https://html.duckduckgo.com/html/?q={query}"
    resp = requests.get(duck_url)
    return Response(resp.content, content_type="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
