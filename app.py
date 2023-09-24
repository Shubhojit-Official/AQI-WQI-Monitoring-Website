from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/aqi-monitor')
def render_aqi():
    return render_template("aqi.html")

@app.route('/submit', methods=['POST'])
def form_action():
    city = request.form['city']
    print(city)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)