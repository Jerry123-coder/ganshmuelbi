from flask import Flask,render_template


app = Flask('__main__',template_folder='templates')

@app.route("/")
def home():
    return "Welcome to the Gan Shmuel Weight"


if __name__ == '__main__':
    app.run(debug=True)