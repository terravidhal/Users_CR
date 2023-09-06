from flask import Flask, render_template,redirect, request #add request
# import the class from user.py
from user import Users 

app = Flask(__name__)


@app.route("/")
def home():
   return redirect('/users')


@app.route("/users")
def index():
    # call the get all classmethod to get all users
   users = Users.get_all()
   # print(users)
   return render_template("index.html",all_Users = users)


@app.route("/users/new")
def create_new_user():
   return render_template("show.html")



@app.route('/new', methods=["POST"])
def create():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    datass = {
        "fname": request.form["inputName4"],
        "lname": request.form["inputlast_name4"],
        "eml": request.form["inputEmail"]
    }
    # We pass the data dictionary into the save method from the Users class.
    Users.create_user(datass)
    # Don't forget to redirect after saving to the database.
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

