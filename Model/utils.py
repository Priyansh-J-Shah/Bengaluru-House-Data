import pickle
import json
import numpy as np
import pandas as pd
import config

class BengaluruHouseData() :
    def __init__ (self,area_type,availability,location,size,total_sqft,bath,balcony) :
        
        self.area_type = "area_type_" + area_type
        self.availability = availability
        self.location = "location_" + location
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony


    def load_model (self) :
        with open (config.Bengaluru_MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open (config.Bengaluru_JSON_FILE_PATH) as f:
            self.json_data = json.load(f)

    def get_predicted_price (self) :
        self.load_model()

        area_type_index = self.json_data["columns"].index(self.area_type)
        location_index = self.json_data["columns"].index(self.location)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.json_data["availability"][self.availability]
        array[1] = self.json_data["size"][self.size]
        array[2] = self.total_sqft
        array[3] = self.bath
        array[4] = self.balcony
        array[area_type_index] = 1
        array[location_index] = 1

        print ("Test Array :\n",array)
        predicted_price = self.model.predict([array])[0]
        print ("Predicted Price :",predicted_price)
        return np.around(predicted_price,2)

if __name__ == "__main__" :
    area_type = "Plot  Area"
    availability = "18-May"
    location = "Kengeri"
    size = "3 BHK"
    total_sqft = 1140.0
    bath = 2
    balcony = 1

    Beng_house_data = BengaluruHouseData(area_type,availability,location,size,total_sqft,bath,balcony)
    price = Beng_house_data.get_predicted_price()
    print ()
    print (f"Price Prediction of House in Bengalore {price}")