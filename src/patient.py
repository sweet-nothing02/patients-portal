"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import uuid
from datetime import datetime
from config import *
import requests

from config import GENDERS, WARD_NUMBERS, ROOM_NUMBERS
from patient_db_config import *

class Patient:
    def __init__(self, name, age, gender):
        self.patient_id = str(uuid.uuid4())
        self.patient_name = name
        self.patient_age = age
        self.patient_gender = gender
        self.patient_checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.patient_checkout = None
        self.patient_ward = None
        self.patient_room = None

    def get_id(self):
        return self.patient_id

    def get_name(self):
        return self.patient_name

    def get_room(self):
        return self.patient_room

    def get_ward(self):
        return self.patient_ward

    def set_room(self, room):
        list = []
        for x in WARD_NUMBERS:
            for y in range(10):
                list.append(x * 10 + y)
        if room in list:
            self.patient_room = room
        else:
            raise ValueError("Invalid room number")

    def set_ward(self, ward):
        if ward not in WARD_NUMBERS:
            raise ValueError("Invalid ward number")
        self.patient_ward = ward

    def commit(self):
        if self.patient_gender not in GENDERS:
            raise ValueError("Invalid gender")
        if not (0 < self.patient_age < 150):
            raise ValueError("Invalid age")

        patient_data = {
            PATIENT_NAME_COLUMN: self.patient_name,
            PATIENT_AGE_COLUMN: self.patient_age,
            PATIENT_GENDER_COLUMN: self.patient_gender,
            PATIENT_WARD_COLUMN: self.patient_ward,
            PATIENT_ROOM_COLUMN: self.patient_room,
        }

        response = requests.post(f"{API_CONTROLLER_URL}/patients", json=patient_data)
        if response.status_code == 200:
            response_data = response.json()
        else:
            print("An error occurred while committing patient data to the database.")