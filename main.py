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
        sg.Radio('Male', "RADIO1", default=True, key="-GENDER_IN-"),
        sg.Radio('Female', "RADIO1", default=False, key="-GENDER_IN-")
    ]
]
chest_pain_column = [
    [
        sg.Text("Chest Pain:"),
        sg.Radio('0', "RADIO2", default=True, key="-CHEST_PAIN_IN-"),
        sg.Radio('1', "RADIO2", default=False, key="-CHEST_PAIN_IN-"),
        sg.Radio('2', "RADIO2", default=False, key="-CHEST_PAIN_IN-"),
        sg.Radio('3', "RADIO2", default=False, key="-CHEST_PAIN_IN-"),
        sg.Radio('4', "RADIO2", default=False, key="-CHEST_PAIN_IN-")
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
        sg.Radio('True', "RADIO3", default=False, key="-ANGINA_IN-"),
        sg.Radio('False', "RADIO3", default=True, key="-ANGINA_IN-")
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
        sg.Radio('True', "RADIO4", default=False, key="-HYPERTENSION_IN-"),
        sg.Radio('False', "RADIO4", default=True, key="-HYPERTENSION_IN-")
    ]
]
heart_disease_column = [
    [
        sg.Text("Heart diease:"),
        sg.Radio('True', "RADIO5", default=False, key="-HEART_DISEASE_IN-"),
        sg.Radio('False', "RADIO5", default=True, key="-HEART_DISEASE_IN-")
    ]
]
residence_type_column = [
    [
        sg.Text("Residence:"),
        sg.Radio('Urban', "RADIO6", default=True, key="-RESIDENCE_IN-"),
        sg.Radio('Rural', "RADIO6", default=False, key="-RESIDENCE_IN-")
    ]
]
smoking_status_column = [
    [
        sg.Text("Smoking status:"),
        sg.Radio('Never smoked', "RADIO7", default=True, key="-SMOKING_IN-"),
        sg.Radio('Unknown', "RADIO7", default=False, key="-SMOKING_IN-"),
        sg.Radio('Formely smoked', "RADIO7", default=False, key="-SMOKING_IN-"),
        sg.Radio('Smokes', "RADIO7", default=False, key="-SMOKING_IN-")
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
input_field_keys_to_clear = ["-AGE_IN-", "-GENDER_IN-0", "-GENDER_IN-1",
                              "-CHEST_PAIN_IN-", "-BLOOD_PRESSURE_IN-",
                              "-CHOLESTEROL_IN-", "-MAX_HEART_RATE_IN-",
                              "-ANGINA_IN-0", "-ANGINA_IN-1",
                              "-PLASMA_GLUCOSE_IN-", "-SKIN_THICKNESS_IN-",
                              "-INSULIN_IN-", "-BMI_IN-", "-DIABETES_IN-",
                              "-HYPERTENSION_IN-0", "-HYPERTENSION_IN-1",
                              "-HEART_DISEASE_IN-0", "-HEART_DISEASE_IN-1",
                              "-RESIDENCE_IN-0", "-RESIDENCE_IN-1",
                              "-SMOKING_IN-0", "-SMOKING_IN-1", "-SMOKING_IN-2", "-SMOKING_IN-3"
                              ]



while True:
    event, values = window.read()
    if event == CANCEL or event == sg.WIN_CLOSED:
        break
    elif event == SUBMIT:
        
        # Create an instance of data_class and populate its attributes
        patient = data_class.data_class(
            """"
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
            """
        )

        # Now you can use the 'patient' object as needed, for example, insert it into your list
        insertPatient(patient)
        
        # Optionally clear the input fields after submission
        for key in input_field_keys_to_clear:
            window[key].update("")

        

window.close()