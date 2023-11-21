import csv

def identify_tests (object):
    All_entry = []
    for i in range(len(object)):
        Test_list = [str(i)]
        if object[i].chestpain > 2:
            Test_list.append(", electrocardiogram (ECG)")
        if object[i].cholestrol > 240:
            Test_list.append(", lipid profile (blood test)")
        if object[i].maxheartrate > (220-object[i].age):
            Test_list.append(", electrocardiogram (ECG)")
        if object[i].plasma_glucose > 2:
            Test_list.append(", oral glucose tolerance test (OGTT")
    

    All_entry.append(Test_list)

    with open('Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(All_entry)
