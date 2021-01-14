from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from datetime import datetime
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Kilometers_Driven=int(request.form['Kilometers_Driven'])
        Owner_Type=int(request.form['Owner_Type'])
        Mileage=float(request.form['Mileage'])
        Engine=float(request.form['Engine'])
        Power=float(request.form['Power'])
        Seats=float(request.form['Seats'])
        Year = int(request.form['Year'])
        No_of_Years=datetime.today().year-Year
        Location=request.form['Location']
        if(Location=='Bangalore'):
            Location_Bangalore=1
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Chennai'):
            Location_Bangalore=0
            Location_Chennai=1
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Coimbatore'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=1
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Delhi'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=1
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Hyderabad'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=1
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Jaipur'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=1
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Kochi'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=1
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Kolkata'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=1
            Location_Mumbai=0
            Location_Pune=0
        elif(Location=='Mumbai'):
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=1
            Location_Pune=0
        else:
            Location_Bangalore=0
            Location_Chennai=0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=1    
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
            Fuel_Type_Electric=0
            Fuel_Type_LPG=0
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
            Fuel_Type_Electric=0
            Fuel_Type_LPG=0
        elif(Fuel_Type=='Electric'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_Electric=1
            Fuel_Type_LPG=0
        elif(Fuel_Type=='LPG'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_Electric=0
            Fuel_Type_LPG=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            Fuel_Type_Electric=0
            Fuel_Type_LPG=0
        Transmission=request.form['Transmission']
        if(Transmission=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        prediction=model.predict([[Kilometers_Driven, Owner_Type, Mileage, Engine, Power,Seats, No_of_Years, Location_Bangalore, Location_Chennai,Location_Coimbatore, Location_Delhi, Location_Hyderabad,Location_Jaipur, Location_Kochi, Location_Kolkata,Location_Mumbai, Location_Pune, Fuel_Type_Diesel,Fuel_Type_Electric, Fuel_Type_LPG, Fuel_Type_Petrol,Transmission_Manual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {} lakhs.".format(output))

if __name__=="__main__":
    app.run(debug=True)
