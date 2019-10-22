from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/calc_tax', methods = ["GET", "POST"])
def calc_salary():
    #get user input
    user_data = dict (request.form)
    #make sure user inputted a number and not a string
    try:
        salary = int(user_data["salary"])
    except ValueError:
        #if a non number was entered, return an error
        return render_template("display_tax.html", tax = "bad data input!")
    tax = model.get_tax(salary)
    #return user task
    return render_template("display_tax.html", tax = int(tax))
