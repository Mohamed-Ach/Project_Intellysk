import pandas as pd


# ** - The Main Functions of the Program:


def read_csv(file_name: str) -> list[dict]:
    df = pd.read_csv(file_name)

    # ** Dropping The 3 marks columns :
    df = df.drop('CC1', axis=1)
    df = df.drop('CC2', axis=1)
    df = df.drop('Note_Final', axis=1)

    return df.to_dict('records')


def merge_data_model(students_list: list[dict], predictions_list: list[float]) -> list[dict]:
    for student, mark in zip(students_list, predictions_list):
        student.update({"Mark": mark})

    return students_list


def get_students_gender(students_list: list[dict]) -> dict:
    return {
        "Males": len([student for student in students_list if student.get("sex") == "M"]),
        "Females": len([student for student in students_list if student.get("sex") == "F"])
    }


def get_daily_cigarettes(students_list: list[dict]) -> dict:
    return {
        index: len([student for student in students_list if student.get("Dciga") == index]) for index in range(0, 10)
    }


def get_students_absence(students_list: list[dict]) -> dict:
    return {
        index*2: len([student for student in students_list if student.get("absences") == index*2]) for index in range(0, 10)
    }


def get_students_romantics(students_list: list[dict]) -> dict:
    return {
        answer: len([student for student in students_list if student.get("romantic") == answer]) for answer in ("yes", "no")
    }


def get_students_internet(students_list: list[dict]) -> dict:
    return {
        answer: len([student for student in students_list if student.get("internet") == answer]) for answer in ("yes", "no")
    }
