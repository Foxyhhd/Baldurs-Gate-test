from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", mathods=["POST"])
def result():
    answers = request.form
    character = determine_character(answers)
    return render_template("result.html", character=character)

def datermine_character(answers):
    if answers.get("question1") == "brave":
        return "Minsc"
    elif answers.get("question1") == "wise":
        return "Jeheira"
    else:
        return "Imoem"
    
if __name__=="__main__":
    app.run(debug=True)