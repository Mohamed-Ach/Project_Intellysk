import pandas as pd


# def read_excel(file_name: str) -> pd.DataFrame:
#     df = pd.read_excel(file_name)
#     return df


if __name__ == '__main__':

    df = pd.read_excel("affichageElHaddad.xlsx")

    # Index The Dataframe by the column "APOGEE":
    df.set_index('APOGEE', inplace=True)

    # Get The APOGEE =  20000755
    desired_row = df.loc[20000755]

    print(desired_row)  # ? Xohtek weslat 7ta n3and Pandas
