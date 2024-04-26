from flask import Flask, render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    # Your name
    name = "SURU"
    # Your GitHub profile URL
    github_profile = "https://github.com/surajupadhaya"
    return render_template('index.html', name=name, github_profile=github_profile)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

