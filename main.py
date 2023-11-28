import PySimpleGUI as sg

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
        sg.Text("Gender:"),
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

while True:
    event, values = window.read()
    if event == CANCEL or event == sg.WIN_CLOSED:
        exit()

window.close()