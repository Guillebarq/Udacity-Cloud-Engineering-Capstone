from flask import Flask, render_template
import pyjokes 
  
app=Flask(__name__) 
  
  
@app.route("/") 
def home(): 
    return render_template("joke.html")

@app.route("/joke")
def joke():
    joke=pyjokes.get_joke()  #It only returns one joke. We get random joke each time. 
    return render_template("joke.html", joke=joke)
  
  
if __name__ == "__main__": 
    app.run(debug=True)