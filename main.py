from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')

@app.route("/Resume")
def Resume():
    return render_template('Resume.html')

@app.route("/Certificates")
def Certificates():
    return render_template('Certificates.html')

if __name__ == '__main__':
    app.run(debug=True)