from flask import Flask, render_template
import pyjokes 
import Joking
import random
  
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
    joke=Joking.animal_joke()
    return render_template("joke.html", joke=joke)

@app.route("/dad")
def dad_joke():
    joke=Joking.random_dad_joke()
    return render_template("joke.html", joke=joke)

@app.route("/pun")
def pun_joke():
    joke=Joking.Pun()
    return render_template("joke.html", joke=joke)

@app.route("/dark")
def dark_joke():
    joke=Joking.DarkJoke()
    return render_template("joke.html", joke=joke)

@app.route("/law")
def law_joke():
    joke=Joking.Law_Joke()
    return render_template("joke.html", joke=joke)
  
  
if __name__ == "__main__": 
    app.run(debug=True)