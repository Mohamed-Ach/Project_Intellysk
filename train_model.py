from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle


# - The Main Functions of the Program:
def read_training_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df


def create_pickle_model(dataframe: pd.DataFrame) -> None:

    dataframe["NOFINAL"] = (dataframe["CC1"] + dataframe['CC2']) / 2
    dr = dataframe.drop(
        ["Last Name", "First Name", "Numero appoge", "City"], axis=1)

    x = dr.drop(["NOFINAL"], axis=1)
    y = dr["NOFINAL"]

    best_model = None
    best_accuracy = 0

    for _ in range(10):
        # test size represents the fraction of data preserved as test data-set
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.3)
        model = RandomForestRegressor()
        model.fit(x_train, y_train)
        acc = model.score(x_test, y_test)

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

    if best_model is not None:
        with open("pickle/students_model.pickle", "wb") as file:
            pickle.dump(best_model, file)


create_pickle_model(read_training_data("csv/training_data.csv"))
