import pandas as pd
import _model

def read_csv(file_name: str) -> list[dict]:
    df = pd.read_csv(file_name)

    # ** Droping The 3 marks colunms :
    df = df.drop('CC1', axis=1)
    df = df.drop('CC2', axis=1)
    df = df.drop('Note_Final', axis=1)

    return df.to_dict('records')

def merge_data_model(students_list: list[dict], predictions_list: list[float]) -> list[dict]:
    for student, mark in zip(students_list, predictions_list):
        student.update({"Mark": mark})

    return students_list



students_list = read_csv("students.csv")
students_list = merge_data_model(students_list, _model.prediction_list)


students_gender = {
    "Males": len([student for student in students_list if student.get("sex") == "M"]),
    "Females": len([student for student in students_list if student.get("sex") == "F"])
}


daily_cigarettes = {
    index: len([student for student in students_list if student.get("Dciga") == index]) for index in range(0, 10)
}


students_absence = {
    index*2: len([student for student in students_list if student.get("absences") == index*2]) for index in range(0, 10)
}

students_romantics = {
    answer: len([student for student in students_list if student.get("romantic") == answer]) for answer in ("yes", "no")
}

students_internet = {
    answer: len([student for student in students_list if student.get("internet") == answer]) for answer in ("yes", "no")
}


for k, v in students_list[0].items():
    print(k, ":", v)

