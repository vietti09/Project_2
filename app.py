# import necessary libraries
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# common variables needed across functions
#################################################
app = Flask(__name__)
ticker = ""

#################################################
# Database Setup 
#################################################
##RP-leaving code as such. need to change according to our setup##
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/pets.sqlite"

#db = SQLAlchemy(app)

##<Add class defs>##
# class Pet(db.Model):
#   __tablename__ = 'pets'

#   id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64))
#   type = db.Column(db.String)
#   age = db.Column(db.Integer)

#   def __repr__(self):
#        return '<Pet %r>' % (self.name)

#############################
# Initial setup if any
#############################

@app.before_first_request
def setup():
    # Recreate database each time for demo
    #db.drop_all()
    #db.create_all()
    ticker = ""


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/sendStock", methods=["GET", "POST"])
def sendStock():
    #find stock ticker matching what user has entered. For simplicity we will raise an error for now if it 
    #is not a stock we have data for
        ticker = request.form["stockTicker"]
        #sample code left for reference
        #pet = Pet(name=name, type=pet_type, age=age)
        #db.session.add(pet)
        #db.session.commit()
        #return redirect("http://localhost:5000/", code=302)

    #not sure what we should render here, since we decided tio split the dashboard. We either have to
    # have a navigation mechanism to go to the different pages, in which case here we just set the ticker value
    # Otherwise we just render the dashboard for the stock, which will show both
        return render_template("stock_dashboard.html")


#######################################
# Data API routes
#########################################
#### commneted out for now. Update later based on what we want to provide APIs to

@app.route("/api/fundamentals")
def fundamentals():
    #pull results from db for the ticker and return as json object

    #sample code left for reference
#    results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()
#    pet_type = [result[0] for result in results]
#    age = [result[1] for result in results]

    fundamentals_data = {
        "ticker": ticker,
        "p": 35,
        "pe": 0.65,
        "pc": 0.55,
        "pb": 0.45,

    }

    return jsonify(fundamentals_data)


@app.route("/api/tradingData")
def tradingData():
    #stock_results = <API call>
    #sp_results
    #nasdaq_results
    #print(results)
    #it will be lot more complex than this but just putting in something
    trading_data = {
        "ticker": "AAPL",
        "p": 35,
        "s&p": 0.65,
        "nsdq": 0.55
    }
    return jsonify(trading_data)


if __name__ == "__main__":
    app.run()
