from flask import Flask , render_template, request, redirect, session
import random

app=Flask(__name__)
app.secret_key='lkjhfdfsdfs'

@app.route('/')
def index():
    if 'someKey' not in session:
        temp = random.randrange(1,101)
        session['someKey'] = temp
    print session['someKey']
 
    return render_template('index.html')

@app.route('/guess', methods = ["POST"])
def guess():
    guess = request.form["guess"]
    guess = int(guess)
    if guess < session["someKey"]:
        session["wrong"] = "Too low mofo!"
    elif guess > session["someKey"]:
        session["wrong"] = "Too high mofo!"
    else:
        if "wrong" in session:
            session.pop("wrong")
        session["win"] = "You guessed a random number congratulate yourself on having won a skilless game!"
    return redirect('/')

@app.route('/restart', methods=["POST"])
def restart():
    session.clear()
    return redirect('/')
        
app.run(debug=True)