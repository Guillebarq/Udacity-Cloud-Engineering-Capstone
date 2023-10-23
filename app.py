from flask import Flask, render_template
import Joking
import os
  
app=Flask(__name__) 
  
  
@app.route("/") 
def home(): 
    return render_template("joke.html")

@app.route("/joke")
def joke():
    joke=Joking.random_joke()
    return render_template("joke.html", joke=joke)

@app.route("/animal")
def animal_joke():
    animal_joke=Joking.animal_joke()
    return render_template("joke.html", joke=animal_joke)

@app.route("/dad")
def dad_joke():
    dad_joke=Joking.random_dad_joke()
    return render_template("joke.html", joke=dad_joke)

@app.route("/pun")
def pun_joke():
    pun_joke=Joking.Pun()
    return render_template("joke.html", joke=pun_joke)

@app.route("/knock-knock")
def knock_knock_joke():
    knock_knock_joke=Joking.Random_knock_knock_joke()
    return render_template("joke.html", joke=knock_knock_joke)

@app.route("/law")
def law_joke():
    law_joke=Joking.Law_Joke()
    return render_template("joke.html", joke=law_joke)
  
  
if __name__ == "__main__": 
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)