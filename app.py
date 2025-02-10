from flask import Flask
from flask import render_template

app = Flask(__name__)
templates = '/templates'

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# About Me
@app.route('/about')
def about():
    return render_template('about.html')

# Projects
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Articles
@app.route('/articles')
def articles():
    return render_template('articles.html')

# Contact Me
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run()