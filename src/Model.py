import joblib
import numpy as np
import pandas as pd

def generate_features(district,
                      seller,
                      area,
                      rooms,
                      bathrooms,
                      parking,
                      garden,
                      balcony,
                      terrace,
                      floor,
                      new,
                      estate,
                      townhouse,
                      apartment,
                      land,
                      studio):
         
    """

    Get predictions from model.

    Parameters
    ----------
    district : str
        District of property.
    seller : str
        Who is selling the property ?
    area : int
        Area in meters squared.
    rooms : int
        Number of rooms.
    bathrooms : int
        Number of bathrooms.
    parking : str
        Type of parking.
    garden : bool
        Has garden ?
    balcony : bool
        Has balcony ?
    terrace :
        Has terrace ?
    floor : bool
        Is on ground level ?
    new : bool
        Is new ?
    estate : bool
        Is in estate ?
    townhouse : bool
        Is townhouse ?
    apartment : bool
        Is apartment ?
    land : bool
        Includes land ?
    studio : bool
        Is studio flat ?

    Notes
    -----
    Features are created the same
    way as during the model building
    process. See Jupyter Notebook 
    for more information.

    """

    columns = ['District',
               'Seller',
               'Area',
               'Rooms',
               'Bathrooms',
               'Parking',
               'Garden',
               'Balcony',
               'Terrace',
               'Floor',
               'New',
               'Estate',
               'Townhouse',
               'Apartment',
               'Land',
               'Studio',
               'Log Area',
               'Bool Sum',
               'Area to Bool Sum',
               'Rooms to Bool Sum',
               'Rooms to Bathrooms',
               'Total Rooms',
               'Area to Rooms',
               'Area to Bathrooms',
               'Area to Total Rooms']    

    # Log Area    
    log_area = np.log(area)

    all_bools = [garden,
                 balcony,
                 terrace,
                 floor,
                 new,
                 estate,
                 townhouse,
                 apartment,
                 land,
                 studio]
    
    # Bool Sum    
    bool_sum = sum(all_bools)

    # Area to Bool Sum    
    area_to_bool_sum = area / (bool_sum + 1)
    
    # Rooms to Bool Sum    
    rooms_to_bool_sum = rooms / (bool_sum + 1)
        
    # Rooms to Bathrooms
    rooms_to_bathrooms = rooms / bathrooms
        
    # Total Rooms
    total_rooms = rooms + bathrooms

    # Area to Rooms
    area_to_rooms = area / total_rooms

    # Area to Bathrooms
    area_to_bathrooms = area / bathrooms

    # Area Total Rooms    
    area_to_total_rooms = area / total_rooms
    
    x = [district,
         seller,
         area,
         rooms,
         bathrooms,
         parking,
         garden,
         balcony,
         terrace,
         floor,
         new,
         estate,
         townhouse,
         apartment,
         land,
         studio,
         log_area,
         bool_sum,
         area_to_bool_sum,
         rooms_to_bool_sum,
         rooms_to_bathrooms,
         total_rooms,
         area_to_rooms,
         area_to_bathrooms,
         area_to_total_rooms]    
    
    x = pd.DataFrame([x], columns=columns)    

    return x

class Model(object):

    def __init__(self, name):
        self.name = name
        self.mdl = None

    def load(self):
        self.mdl = joblib.load(f'models/{self.name}.joblib')
        return self

    def predict(self, x):
        y_pred = self.mdl.predict(x)
        y_pred = int(round(float(y_pred), -3))
        return y_pred
