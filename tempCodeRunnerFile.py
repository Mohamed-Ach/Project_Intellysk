import pandas as pd


"""
? REFERENCES:
"""

filiere_mapping = {
    "GINF": 1,
    "GSTR": 2,
    "GSEA": 3,
    "G3EI": 4,
    "GIL": 5
}

matiere_mapping = {
    "C++": 1,
    "Reseaux": 2,
    "Electronique": 3,
    "Energie": 4,
    "Dessin": 5
}

famsize_mapping = {
    "LE3": 1,
    "GT3": 2
}

pstatus_mapping = {
    "T": 1,
    "A": 2
}

mjob_mapping = {
    "at_home": 0,
    "teacher": 1,
    "health": 2,
    "services": 3,
    "other": 4
}

fjob_mapping = {
    "at_home": 0,
    "teacher": 1,
    "health": 2,
    "services": 3,
    "other": 4
}

reason_mapping = {
    "home": 0,
    "course": 1,
    "reputation": 2,
    "other": 3
}

guardian_mapping = {
    "mother": 0,
    "father": 1,
    "other": 3
}

schoolsup_mapping = {
    "no": 0,
    "yes": 1
}

activities_mapping = {
    "no": 0,
    "yes": 1
}

internet_mapping = {
    "no": 0,
    "yes": 1
}

romantic_mapping = {
    "no": 0,
    "yes": 1
}

sex_mapping = {
    "M": 1,
    "F": 0
}


df = pd.read_excel('csv/training_data.xlsx')
students_list = df.to_dict('records')


for student in students_list:
    student['sex'] = sex_mapping.get(student.get('sex', '').strip(), -1)
    student["Filier"] = filiere_mapping.get(
        student.get('Filier', '').strip(), -1)
    student["internet"] = internet_mapping.get(
        student.get('internet', '').strip(), -1)
    student["schoolsup"] = schoolsup_mapping.get(
        student.get('schoolsup', '').strip(), -1)
    student["activities"] = activities_mapping.get(
        student.get('activities', '').strip(), -1)
    student["guardian"] = guardian_mapping.get(
        student.get('guardian', '').strip(), -1)
    student["reason"] = reason_mapping.get(
        student.get('reason', '').strip(), -1)
    student["Fjob"] = fjob_mapping.get(student.get('Fjob', '').strip(), -1)
    student["Mjob"] = mjob_mapping.get(student.get('Mjob', '').strip(), -1)
    student["Pstatus"] = pstatus_mapping.get(
        student.get('Pstatus', '').strip(), -1)
    student["famsize"] = famsize_mapping.get(
        student.get('famsize', '').strip(), -1)
    student["Matiere"] = matiere_mapping.get(
        student.get('Matiere', '').strip(), -1)
    student["romantic"] = romantic_mapping.get(
        student.get('romantic', '').strip(), -1)


def save_students():
    df = pd.DataFrame(students_list)
    df.to_csv('training_data.csv', index=False)


save_students()


print("Done!")
