#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    ''' defines Place class '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = ''
    number_bathrooms = ''
    max_guest = ''
    price_by_night = ''
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''
