from time import perf_counter
import pandas as pd
import numpy as np
import pickle


# ** The Program's main functionalities :


def load_model(file_name: str):
    with open(file_name, "rb") as file:
        model = pickle.load(file)
    return model


def read_students(filename: str) -> list[dict]:
    df = pd.read_csv(filename)
    return df.to_dict("records")


def predict_all_students() -> list[float]:

    students_list = read_students("csv/students-raw.csv")
    students_model = load_model("pickle/students_model.pickle")

    predictions_list = []
    for student in students_list:
        params = [
            student.get("sex", -1),
            student.get("age", -1),
            student.get("Annee", -1),
            student.get("Filier", -1),
            student.get("Matiere", -1),
            student.get("famsize", -1),
            student.get("Pstatus", -1),
            student.get("Medu", -1),
            student.get("Fedu", -1),
            student.get("Mjob", -1),
            student.get("Fjob", -1),
            student.get("reason", -1),
            student.get("guardian", -1),
            student.get("traveltime", -1),
            student.get("studytime", -1),
            student.get("failures", -1),
            student.get("schoolsup", -1),
            student.get("activities", -1),
            student.get("internet", -1),
            student.get("romantic", -1),
            student.get("famrel", -1),
            student.get("freetime", -1),
            student.get("Dciga", -1),
            student.get("Wciga", -1),
            student.get("health", -1),
            student.get("absences", -1),
            student.get("CC1", -1),
            student.get("CC2", -1),
        ]

        predictions = students_model.predict(np.array(params).reshape(1, -1))
        predictions_list.append(float(predictions[0]))

    return [round(mark * 4) / 4 for mark in predictions_list]


def predict_single_student(apogee: int, student_data: dict[str, int]) -> float:
    students_list = read_students("csv/students-raw.csv")
    students_model = load_model("pickle/students_model.pickle")
    student = next(
        filter(lambda x: x["Numero appoge"] == apogee, students_list), None)
    student.update(student_data)

    params = [
        student.get("sex", -1),
        student.get("age", -1),
        student.get("Annee", -1),
        student.get("Filier", -1),
        student.get("Matiere", -1),
        student.get("famsize", -1),
        student.get("Pstatus", -1),
        student.get("Medu", -1),
        student.get("Fedu", -1),
        student.get("Mjob", -1),
        student.get("Fjob", -1),
        student.get("reason", -1),
        student.get("guardian", -1),
        student.get("traveltime", -1),
        student.get("studytime", -1),
        student.get("failures", -1),
        student.get("schoolsup", -1),
        student.get("activities", -1),
        student.get("internet", -1),
        student.get("romantic", -1),
        student.get("famrel", -1),
        student.get("freetime", -1),
        student.get("Dciga", -1),
        student.get("Wciga", -1),
        student.get("health", -1),
        student.get("absences", -1),
        student.get("CC1", -1),
        student.get("CC2", -1)
    ]
    predictions = students_model.predict(np.array(params).reshape(1, -1))
    # return round(float(predictions[0]) * 4) / 4
    return float(predictions[0])
