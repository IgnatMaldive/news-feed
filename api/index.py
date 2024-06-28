from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query', 'Technology')  # Default query
    api_key = '15e592a655654890885142a17dd3f6c9'  # Use your NewsAPI key
    url = f'https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
