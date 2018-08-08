from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#def home_page():
    #return("swimming")

def swimming():
    swimmers=["Michael Phelps", "Mark Spitz", "Matt Biondi", "Ryan Lochte"]
    return render_template("index.html", sentence="my favorite sport:",
    swimmers=swimmers,
    likes_same_sport=True)


if __name__ == '__main__':
   app.run(debug = True)