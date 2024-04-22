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
from config import GENDERS, WARD_NUMBERS, ROOM_NUMBERS
from patient_db_config import PATIENT_ID_COLUMN, PATIENT_NAME_COLUMN, PATIENT_AGE_COLUMN, PATIENT_GENDER_COLUMN, \
    PATIENT_ROOM_COLUMN, PATIENT_WARD_COLUMN
# from api_controller import PatientAPIController

class Patient:
    def __init__(self, name, age, gender):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.gender = gender
        self.checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.checkout = None
        self.ward = None
        self.room = None

    def update_room_and_ward(self, ward, room):
        if ward not in WARD_NUMBERS:
            raise ValueError("Invalid ward number")
        if room not in ROOM_NUMBERS.get(ward, []):
            raise ValueError("Invalid room number")
        self.ward = ward
        self.room = room

    def commit_to_database(self, patientAPIController):
        # Validate patient attributes
        if self.gender not in GENDERS:
            raise ValueError("Invalid gender")
        if not (0 < self.age < 150):
            raise ValueError("Invalid age")
        
        # Create a dictionary representing the patient data
        patient_data = {
            PATIENT_ID_COLUMN: self.id,
            PATIENT_NAME_COLUMN: self.name,
            PATIENT_AGE_COLUMN: self.age,
            PATIENT_GENDER_COLUMN: self.gender,
            PATIENT_WARD_COLUMN: self.ward,
            PATIENT_ROOM_COLUMN: self.room,
        }

        # Use the API controller to commit the patient data to the database

        patientAPIController.patient_db.insert_patient(patient_data)

