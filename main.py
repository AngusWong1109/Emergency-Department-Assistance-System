import PySimpleGUI as sg
import data_class  # Import data class module
import ai_model    # Import AI Model
from test import identify_tests

PROJECT_NAME = "Project 11"
ADD_PATIENT = "Add more patient"
SUBMIT = "Submit"
CANCEL = "Cancel"
age_column = [
    [
        sg.Text("Age:"),
        sg.InputText(key="-AGE_IN-")
    ]
]
gender_column = [
    [
        sg.Text("Gender:"),
        sg.Radio('Male', "RADIO1", default=True, key="-GENDER_IN_MALE-"),
        sg.Radio('Female', "RADIO1", default=False, key="-GENDER_IN_FEMALE-")
    ]
]
chest_pain_column = [
    [
        sg.Text("Chest Pain:"),
        sg.Radio('0', "RADIO2", default=True, key="-CHEST_PAIN_IN_0-"),
        sg.Radio('1', "RADIO2", default=False, key="-CHEST_PAIN_IN_1-"),
        sg.Radio('2', "RADIO2", default=False, key="-CHEST_PAIN_IN_2-"),
        sg.Radio('3', "RADIO2", default=False, key="-CHEST_PAIN_IN_3-"),
        sg.Radio('4', "RADIO2", default=False, key="-CHEST_PAIN_IN_4-")
    ]
]
blood_pressure_column = [
    [
        sg.Text("Blood Pressure:"),
        sg.InputText(key="-BLOOD_PRESSURE_IN-")    
    ]
]
cholesterol_column = [
    [
        sg.Text("Cholesterol:"),
        sg.InputText(key="-CHOLESTEROL_IN-")   
    ]
]
heart_rate_column = [
    [
        sg.Text("Max heart rate:"),
        sg.InputText(key="-MAX_HEART_RATE_IN-")    
    ]
]
exercise_angina_column = [
    [
        sg.Text("Exercise Angina:"),
        sg.Radio('True', "RADIO3", default=False, key="-ANGINA_IN_TRUE-"),
        sg.Radio('False', "RADIO3", default=True, key="-ANGINA_IN_FALSE-")
    ]
]
plasma_glucose_column = [
    [
        sg.Text("Plasma glucose:"),
        sg.InputText(key="-PLASMA_GLUCOSE_IN-")
    ]
]
skin_thickness_column = [
    [
        sg.Text("Skin thickness:"),
        sg.InputText(key="-SKIN_THICKNESS_IN-")
    ]
]
insulin_column = [
    [
        sg.Text("Insulin:"),
        sg.InputText(key="-INSULIN_IN-")
    ]
]
bmi_column = [
    [
        sg.Text("Bmi:"),
        sg.InputText(key="-BMI_IN-")
    ]
]
diabetes_pedigree_column = [
    [
        sg.Text("diabetes pedigree:"),
        sg.InputText(key="-DIABETES_IN-")
    ]
]
hypertension_column = [
    [
        sg.Text("Hypertension:"),
        sg.Radio('True', "RADIO4", default=False, key="-HYPERTENSION_IN_TRUE-"),
        sg.Radio('False', "RADIO4", default=True, key="-HYPERTENSION_IN_FALSE-")
    ]
]
heart_disease_column = [
    [
        sg.Text("Heart diease:"),
        sg.Radio('True', "RADIO5", default=False, key="-HEART_DISEASE_IN_TRUE-"),
        sg.Radio('False', "RADIO5", default=True, key="-HEART_DISEASE_IN_FALSE-")
    ]
]
residence_type_column = [
    [
        sg.Text("Residence:"),
        sg.Radio('Urban', "RADIO6", default=True, key="-RESIDENCE_IN_URBAN-"),
        sg.Radio('Rural', "RADIO6", default=False, key="-RESIDENCE_IN_RURAL-")
    ]
]
smoking_status_column = [
    [
        sg.Text("Smoking status:"),
        sg.Radio('Never smoked', "RADIO7", default=True, key="-SMOKING_IN_NEVER-"),
        sg.Radio('Unknown', "RADIO7", default=False, key="-SMOKING_IN_UNKNOWN-"),
        sg.Radio('Formely smoked', "RADIO7", default=False, key="-SMOKING_IN_FORMELY-"),
        sg.Radio('Smokes', "RADIO7", default=False, key="-SMOKING_IN_SMOKES-")
    ]
]

button_column = [
    [
        sg.Button(ADD_PATIENT),
        sg.Button(SUBMIT),
        sg.Button(CANCEL)
    ]
]
layout = [
    [age_column],
    [gender_column],
    [chest_pain_column],
    [blood_pressure_column],
    [cholesterol_column],
    [heart_rate_column],
    [exercise_angina_column],
    [plasma_glucose_column],
    [skin_thickness_column],
    [insulin_column],
    [bmi_column],
    [diabetes_pedigree_column],
    [hypertension_column],
    [heart_disease_column],
    [residence_type_column],
    [smoking_status_column],
    [button_column],
]

window = sg.Window(PROJECT_NAME, layout)

# List of input field keys to clear
input_field_keys_to_clear = ["-AGE_IN-", "-GENDER_IN_MALE-", "-GENDER_IN_FEMALE-",
                              "-CHEST_PAIN_IN_0-","-CHEST_PAIN_IN_1-", "-CHEST_PAIN_IN_2-","-CHEST_PAIN_IN_3-", "-CHEST_PAIN_IN_4-",
                              "-BLOOD_PRESSURE_IN-","-CHOLESTEROL_IN-", "-MAX_HEART_RATE_IN-",
                              "-ANGINA_IN_TRUE-", "-ANGINA_IN_FALSE-",
                              "-PLASMA_GLUCOSE_IN-", "-SKIN_THICKNESS_IN-",
                              "-INSULIN_IN-", "-BMI_IN-", "-DIABETES_IN-",
                              "-HYPERTENSION_IN_TRUE-", "-HYPERTENSION_IN_FALSE-",
                              "-HEART_DISEASE_IN_TRUE-", "-HEART_DISEASE_IN_FALSE-",
                              "-RESIDENCE_IN_URBAN-", "-RESIDENCE_IN_RURAL-",
                              "-SMOKING_IN_NEVER-", "-SMOKING_IN_UNKNOWN-", "-SMOKING_IN_FORMELY-", "-SMOKING_IN_SMOKES-"
                              ]


ai = ai_model.ai_model()
while True:
    event, values = window.read()
    if event == CANCEL or event == sg.WIN_CLOSED:
        break        
    elif event == SUBMIT:
        print("Submit pressed")
        # Create an instance of data_class and populate its attributes
        patient = data_class.data_class(
            age = int(values["-AGE_IN-"]),
            gender = 1 if values["-GENDER_IN_MALE-"] else 0,
            chest_pain = 1 if values["-CHEST_PAIN_IN_1-"] else 2 if values["-CHEST_PAIN_IN_2-"] else 3 if values["-CHEST_PAIN_IN_3-"] else 4 if values["-CHEST_PAIN_IN_4-"] else 0,
            blood_pressure = int(values["-BLOOD_PRESSURE_IN-"]),
            cholesterol = int(values["-CHOLESTEROL_IN-"]),
            max_heart_rate = int(values["-MAX_HEART_RATE_IN-"]),
            exercise_angina = 1 if values["-ANGINA_IN_TRUE-"] else 0 if values["-ANGINA_IN_FALSE-"] else 0,
            plasma_glucose = int(values["-PLASMA_GLUCOSE_IN-"]),
            skin_thickness = int(values["-SKIN_THICKNESS_IN-"]),
            insulin = int(values["-INSULIN_IN-"]),
            bmi = float(values["-BMI_IN-"]),
            diabetes_pedigree = float(values["-DIABETES_IN-"]),
            hypertension = 1 if values["-HYPERTENSION_IN_TRUE-"] else 0 if values["-HYPERTENSION_IN_FALSE-"] else 0,
            heart_disease= 1 if values["-HEART_DISEASE_IN_TRUE-"] else 0 if values["-HEART_DISEASE_IN_FALSE-"] else 0,
            residence_type= 0 if values["-RESIDENCE_IN_URBAN-"] else 1,
            smoking_status= 0 if values["-SMOKING_IN_NEVER-"] else 3 if values["-SMOKING_IN_UNKNOWN-"] else
            1 if values["-SMOKING_IN_FORMELY-"] else 2,
            triage = 0,
            id = 1
            )
        
        # Need to confiure tensorflow and keras
        # Insert the patient into the list in ai_model
        ai.insertPatient(patient)
        
        # Use the created model to predict on data
        predictions = ai.predict_on_data()

        # Print predicted triage values
        print("Predicted Triage Values:", predictions)
        # Need to confiure tensorflow and keras until here

        
        ai.sortList
        identify_tests(ai.listOfPatientObjects)
        
    elif event == ADD_PATIENT:
        print("Add more Patient pressed")


        # Create an instance of data_class and populate its attributes
        patient = data_class.data_class(
            age = int(values["-AGE_IN-"]),
            gender = 1 if values["-GENDER_IN_MALE-"] else 0,
            chest_pain = 1 if values["-CHEST_PAIN_IN_1-"] else 2 if values["-CHEST_PAIN_IN_2-"] else 3 if values["-CHEST_PAIN_IN_3-"] else 4 if values["-CHEST_PAIN_IN_4-"] else 0,
            blood_pressure = int(values["-BLOOD_PRESSURE_IN-"]),
            cholesterol = int(values["-CHOLESTEROL_IN-"]),
            max_heart_rate = int(values["-MAX_HEART_RATE_IN-"]),
            exercise_angina = 1 if values["-ANGINA_IN_TRUE-"] else 0 if values["-ANGINA_IN_FALSE-"] else 0,
            plasma_glucose = int(values["-PLASMA_GLUCOSE_IN-"]),
            skin_thickness = int(values["-SKIN_THICKNESS_IN-"]),
            insulin = int(values["-INSULIN_IN-"]),
            bmi = float(values["-BMI_IN-"]),
            diabetes_pedigree = float(values["-DIABETES_IN-"]),
            hypertension = 1 if values["-HYPERTENSION_IN_TRUE-"] else 0 if values["-HYPERTENSION_IN_FALSE-"] else 0,
            heart_disease= 1 if values["-HEART_DISEASE_IN_TRUE-"] else 0 if values["-HEART_DISEASE_IN_FALSE-"] else 0,
            residence_type= 0 if values["-RESIDENCE_IN_URBAN-"] else 1,
            smoking_status= 0 if values["-SMOKING_IN_NEVER-"] else 3 if values["-SMOKING_IN_UNKNOWN-"] else
            1 if values["-SMOKING_IN_FORMELY-"] else 2,
            triage = 0,
            id = 1
            )
        
        # Print all attributes of the patient instance
        print("Patient attributes:")
        print(f"Age: {patient.age}")
        print(f"Gender: {patient.gender}")
        print(f"Chest Pain: {patient.chest_pain}")
        print(f"Blood Pressure: {patient.blood_pressure}")
        print(f"Cholesterol: {patient.cholesterol}")
        print(f"Max Heart Rate: {patient.max_heart_rate}")
        print(f"Exercise Angina: {patient.exercise_angina}")
        print(f"Plasma Glucose: {patient.plasma_glucose}")
        print(f"Skin Thickness: {patient.skin_thickness}")
        print(f"Insulin: {patient.insulin}")
        print(f"BMI: {patient.bmi}")
        print(f"Diabetes Pedigree: {patient.diabetes_pedigree}")
        print(f"Hypertension: {patient.hypertension}")
        print(f"Heart Disease: {patient.heart_disease}")
        print(f"Residence Type: {patient.residence_type}")
        print(f"Smoking Status: {patient.smoking_status}")
        print(f"Triage: {patient.triage}")

        
        
        # Need to confiure tensorflow and keras
        # Now you can use the 'patient' object as needed, for example, insert it into your list
        ai.insertPatient(patient)
        # Need to confiure tensorflow and keras until here
        
        # Optionally clear the input fields after submission
        for key in input_field_keys_to_clear:
            window[key].update("")
        

window.close()