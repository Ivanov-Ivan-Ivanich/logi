from flask import Flask, render_template
from pythonapp import get_python_news


app = Flask(__name__)

@app.route('/')
def index():
    
    news_list =  get_python_news()
    return render_template('index.html',news_list=news_list)


if __name__ == "__main__":
    app.run(debug=True)