import numpy as np

class data_class:
    def __init__(self, age, gender, chest_pain, blood_pressure, cholesterol, max_heart_rate, exercise_angina, plasma_glucose, skin_thickness, insulin, bmi, diabetes_pedigree, hypertension, heart_disease, residence_type, smoking_status, triage):
        self.age = age
        self.gender = gender
        self.chest_pain = chest_pain
        self.blood_pressure = blood_pressure
        self.cholesterol = cholesterol
        self.max_heart_rate = max_heart_rate
        self.exercise_angina = exercise_angina
        self.plasma_glucose = plasma_glucose
        self.skin_thickness = skin_thickness
        self.insulin = insulin
        self.bmi = bmi
        self.diabetes_pedigree = diabetes_pedigree
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.residence_type = residence_type
        self.smoking_status = smoking_status
        self.triage = triage
    def to_np_arr(self):
        arr = []
        arr.append(self.age)
        arr.append(self.gender)
        arr.append(self.chest_pain)
        arr.append(self.blood_pressure)
        arr.append(self.cholesterol)
        arr.append(self.max_heart_rate)
        arr.append(self.exercise_angina)
        arr.append(self.plasma_glucose)
        arr.append(self.skin_thickness)
        arr.append(self.insulin)
        arr.append(self.bmi)
        arr.append(self.diabetes_pedigree)
        arr.append(self.hypertension)
        arr.append(self.heart_disease)
        arr.append(self.residence_type)
        arr.append(self.smoking_status)
        return np.array(arr)