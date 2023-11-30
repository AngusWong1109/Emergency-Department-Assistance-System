import PySimpleGUI as sg
import data_class  # Import your data_class module

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



while True:
    event, values = window.read()
    if event == CANCEL or event == sg.WIN_CLOSED:
        break
    elif event == ADD_PATIENT:
        print("Add more Patient pressed")
        """""
        # Create an instance of data_class and populate its attributes
        patient = data_class.data_class(
            
            age=int(values["-AGE_IN-"]),
            gender="Male" if values["-GENDER_IN-0"] else "Female",
            chest_pain=int(values["-CHEST_PAIN_IN-"]),
            blood_pressure=int(values["-BLOOD_PRESSURE_IN-"]),
            cholesterol=int(values["-CHOLESTEROL_IN-"]),
            max_heart_rate=int(values["-MAX_HEART_RATE_IN-"]),
            exercise_angina=bool(values["-ANGINA_IN-"]),
            plasma_glucose=int(values["-PLASMA_GLUCOSE_IN-"]),
            skin_thickness=int(values["-SKIN_THICKNESS_IN-"]),
            insulin=int(values["-INSULIN_IN-"]),
            bmi=float(values["-BMI_IN-"]),
            diabetes_pedigree=float(values["-DIABETES_IN-"]),
            hypertension=bool(values["-HYPERTENSION_IN-"]),
            heart_disease=bool(values["-HEART_DISEASE_IN-"]),
            residence_type="Urban" if values["-RESIDENCE_IN-"] else "Rural",
            smoking_status="Never smoked" if values["-SMOKING_IN"] else "Unknown" if values["-SMOKING_IN-1"] else
            "Formerly smoked" if values["-SMOKING_IN-2"] else "Smokes"
            
        )

        # Now you can use the 'patient' object as needed, for example, insert it into your list
        insertPatient(patient)
        """
        # Optionally clear the input fields after submission
        for key in input_field_keys_to_clear:
            window[key].update("")
    elif event == SUBMIT:
        print("Submit pressed")

        

window.close()