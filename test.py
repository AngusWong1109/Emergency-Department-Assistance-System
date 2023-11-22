import csv

def identify_tests (object):
    All_entry = []
    for i in range(len(object)):
        
        Test_list = [str(i)]

        # CHECK CHEST PAIN, HEART RATE AND ANGINA IN ONE CONDITION
        if object[i].chestpain > 2 | object[i].maxheartrate > (220-object[i].age) | object[i].angina == 1:
            Test_list.append(", electrocardiogram (ECG)")
        
        if object[i].cholesterol > 240:
            Test_list.append(", lipid profile (blood test)")
        
        if object[i].plasma_glucose > 2:
            Test_list.append(", oral glucose tolerance test (OGTT")
        
        if object[i].skin_thickness > 50:
            Test_list.append(", biopsy, blood test")
        
        if object[i].bmi > 30:
            Test_list.append(", liver function test, thyroid function test")
            if ", blood test" not in Test_list:
                Test_list.append(", blood test")
            if ", electrocardiogram (ECG)" not in Test_list:
                Test_list.append(", electrocardiogram (ECG)")
        
        if object[i].smoking_status != "never smoked":
            Test_list.append(", spirometry, chest X-ray,")
        
        if object[i].hypertension == 1:
            if ", blood test" not in Test_list:
                Test_list.append(", blood test")

        if object[i].heartdisease == 1:
            if ", electrocardiogram (ECG)" not in Test_list:
                Test_list.append(", electrocardiogram (ECG)")
    

    All_entry.append(Test_list)

    with open('Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(All_entry)
