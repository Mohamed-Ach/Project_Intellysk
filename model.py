from flask import Flask, render_template, request,jsonify
import json
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


app = Flask(__name__)

# Chargez les données
df = pd.read_excel('data.xlsx')
df['NOFINAL'] = (df['CC1']+df['CC2'])/2

#FEATURE ENGINEERING 

filiere = {
    "GINF":1,
    "GSTR":2,
    "GSEA":3,
    "G3EI":4,
    "GIL":5
}
df['Filier'] = df['Filier'].str.strip()  # Supprime les espaces avant et après
df['Filier'] = df['Filier'].map(filiere)


Sex = {
     "F":0,
    "M":1,
}
df['sex'] = df['sex'].str.strip()  # Supprime les espaces avant et après
df['sex'] = df['sex'].map(Sex)

matiere = {
    "C++":1,
    "Reseaux":2,
    "Electronique":3,
    "Energie":4,
    "Dessin":5
}
df['Matiere'] = df['Matiere'].str.strip()  # Supprime les espaces avant et après
df['Matiere'] = df['Matiere'].map(matiere)

famsize = {
    "LE3":1,
    "GT3":2
}
df['famsize'] = df['famsize'].str.strip()  # Supprime les espaces avant et après
df['famsize'] = df['famsize'].map(famsize)


Pstatus = {
    "T":1,
    "A":2
}
df['Pstatus'] = df['Pstatus'].str.strip()  # Supprime les espaces avant et après
df['Pstatus'] = df['Pstatus'].map(Pstatus)


Mjob = {
    "at_home" : 0,
    "teacher":1,
    "health":2,
    "services":3,
    "other":4
}
df['Mjob'] = df['Mjob'].str.strip()  # Supprime les espaces avant et après
df['Mjob'] = df['Mjob'].map(Mjob)

Fjob = {
    "at_home" : 0,
    "teacher":1,
    "health":2,
    "services":3,
    "other":4
}
df['Fjob'] = df['Fjob'].str.strip()  # Supprime les espaces avant et après
df['Fjob'] = df['Fjob'].map(Fjob)


reasoon = {
    "home" : 0,
    "course":1,
    "reputation":2,
    "other":3
}
df['reason'] = df['reason'].str.strip()  # Supprime les espaces avant et après
df['reason'] = df['reason'].map(reasoon)

guardian = {
    "mother" : 0,
    "father":1,
    "other":3
}
df['guardian'] = df['guardian'].str.strip()  # Supprime les espaces avant et après
df['guardian'] = df['guardian'].map(guardian)

schoolsup = {
    "no" : 0,
    "yes":1
}
df['schoolsup'] = df['schoolsup'].str.strip()  # Supprime les espaces avant et après
df['schoolsup'] = df['schoolsup'].map(schoolsup)


activities = {
    "no" : 0,
    "yes":1
}
df['activities'] = df['activities'].str.strip()  # Supprime les espaces avant et après
df['activities'] = df['activities'].map(activities)


internet = {
    "no" : 0,
    "yes":1
}
df['internet'] = df['internet'].str.strip()  # Supprime les espaces avant et après
df['internet'] = df['internet'].map(internet)


romantic = {
    "no" : 0,
    "yes":1
}
df['romantic'] = df['romantic'].str.strip()  # Supprime les espaces avant et après
df['romantic'] = df['romantic'].map(romantic)


dr = df.drop(['Last Name',"First Name","Numero appoge","City"],axis=1)
x = dr.drop(["NOFINAL"],axis=1)
y = dr["NOFINAL"]



#Model Engineering 


best = 0

for _ in range(10):
    # test size represents the fraction of data preserved as test data-set
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
    model = RandomForestRegressor()
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    #print(acc, end='\n\n')
    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(model, f)

            pickle_in = open("studentmodel.pickle", "rb")
model = pickle.load(pickle_in)
print("acc = "+str(acc), end='\n\n')


print(x_test.info())
pred = model.predict(x_test)
mse = mean_squared_error(y_test, pred)
print(f"Mean Squared Error on initial test set: {mse}")


# Sauvegarde du modèle initial
pickle.dump(model, open("df.pkl", 'wb'))


@app.route('/', methods=['GET'])
def Home():
    #mydata = df[['Numero appoge','First Name','Last Name','sex','Filier','Matiere']]
    #mydata['NOFINAL']= pred ; 
      # Convertir le ndarray en liste puis en format JSON
    output = pd.DataFrame({'actual_charges':y_test,'predicted_charges':pred})
    return output.to_json(orient='records')

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    if 'age' in data:
            age = int(data['age'])

            # Traitez les autres champs de la même manière
            annee = int(data.get('Annee', -1))
            Medu = int(data.get('Medu', -1))
            Fedu = int(data.get('Fedu', -1))
            traveltime = int(data.get('traveltime', -1))
            studytime = int(data.get('studytime', -1))
            failures = int(data.get('failures', -1))
            famrel = int(data.get('famrel', -1))
            freetime = int(data.get('freetime', -1))
            Dciga = int(data.get('Dciga', -1))
            Wciga = int(data.get('Wciga', -1))
            health = int(data.get('health', -1))
            absences = int(data.get('absences', -1))
            CC1 = int(data.get('CC1', -1))
            CC2 = int(data.get('CC2', -1))

            # Effectuez le mappage pour les champs spécifiques
            Sex = 1 if data.get('sex', '').upper() == 'M' else 0

            filiere_mapping = {
                "GINF": 1,
                "GSTR": 2,
                "GSEA": 3,
                "G3EI": 4,
                "GIL": 5
            }
            Filier = filiere_mapping.get(data.get('Filier', ''), -1)

            matiere_mapping = {
                "C++": 1,
                "Reseaux": 2,
                "Electronique": 3,
                "Energie": 4,
                "Dessin": 5
            }
            Matiere = matiere_mapping.get(data.get('Matiere', ''), -1)

            famsize_mapping = {
                "LE3": 1,
                "GT3": 2
            }
            famsize = famsize_mapping.get(data.get('famsize', ''), -1)

            pstatus_mapping = {
                "T": 1,
                "A": 2
            }
            Pstatus = pstatus_mapping.get(data.get('Pstatus', ''), -1)

            mjob_mapping = {
                "at_home": 0,
                "teacher": 1,
                "health": 2,
                "services": 3,
                "other": 4
            }
            Mjob = mjob_mapping.get(data.get('Mjob', ''), -1)

            fjob_mapping = {
                "at_home": 0,
                "teacher": 1,
                "health": 2,
                "services": 3,
                "other": 4
            }
            Fjob = fjob_mapping.get(data.get('Fjob', ''), -1)

            reason_mapping = {
                "home": 0,
                "course": 1,
                "reputation": 2,
                "other": 3
            }
            reason = reason_mapping.get(data.get('reason', ''), -1)

            guardian_mapping = {
                "mother": 0,
                "father": 1,
                "other": 3
            }
            guardian = guardian_mapping.get(data.get('guardian', ''), -1)

            schoolsup_mapping = {
                "no": 0,
                "yes": 1
            }
            schoolsup = schoolsup_mapping.get(data.get('schoolsup', ''), -1)

            activities_mapping = {
                "no": 0,
                "yes": 1
            }
            activities = activities_mapping.get(data.get('activities', ''), -1)

            internet_mapping = {
                "no": 0,
                "yes": 1
            }
            internet = internet_mapping.get(data.get('internet', ''), -1)

            romantic_mapping = {
                "no": 0,
                "yes": 1
            }
            romantic = romantic_mapping.get(data.get('romantic', ''), -1)

            # Exécutez votre modèle avec les données traitées
            predictions = model.predict(np.array([Sex, age, annee, Filier, Matiere, famsize, Pstatus, Medu, Fedu, Mjob, Fjob,
                                     reason, guardian, traveltime, studytime, failures, schoolsup, activities,
                                     internet, romantic, famrel, freetime, Dciga, Wciga, health, absences, CC1, CC2]).reshape(1, -1))

            predictions_list = predictions.tolist()

                # Retournez les prédictions en tant que réponse JSON
            return jsonify({"predictions": predictions_list})

        

    return {"error": "This endpoint only accepts POST requests."}


if __name__ == "__main__":
    app.run(debug=True, port=8000)














