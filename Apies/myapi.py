from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

donnees_json = [
    {"Numero appoge":"19001211","Last Name": "ACHERNAN", "First Name": "MOHAMED", "CC1": 14},
    {"Numero appoge":"19001137","Last Name": "AFOUD", "First Name": "HIND", "CC1": 10},
    {"Numero appoge":"20007078","Last Name":"BENAMRI","First Name":"AYMANE","CC1":10},
    {"Numero appoge":"20000757","Last Name":"BENATTOU","First Name":"IMANE","CC1":8},
    {"Numero appoge":"20000758","Last Name":"BENATTOU","First Name":"IHSANE","CC1":10},
    {"Numero appoge":"20002424","Last Name":"BOUKTAIB","First Name":"SOUFIAN","CC1":11},
    {"Numero appoge":"20000771","Last Name":"BOULAID","First Name":"SARA","CC1":8},
    {"Numero appoge":"20002251","Last Name":"EL  AALOUCH","First Name":"MOHAMMED YASSINE","CC1":7},
    {"Numero appoge":"20002670","Last Name":"EL ASSIRI","First Name":"AHLAM","CC1":16},
    {"Numero appoge":"20000742","Last Name":"EL AZOUAN","First Name":"AYA","CC1":16},
    {"Numero appoge":"20000741","Last Name":"EL BAGHDADI","First Name":"NADA","CC1":14},
    {"Numero appoge":"20000780","Last Name":"EL HABTI","First Name":"NAJOUA","CC1":16},
    {"Numero appoge":"20003925","Last Name":"EL HADDAD","First Name":"MOHAMED","CC1":14},
    {"Numero appoge":"20000755","Last Name":"EL HARRACHY","First Name":"ABDERRAHMANE","CC1":7},
    {"Numero appoge":"20000716","Last Name":"EL MAFTOUHI","First Name":"BILAL","CC1":11},
    {"Numero appoge":"20006989","Last Name":"EL MOUMOUHI","First Name":"HOUDA","CC1":7},
    {"Numero appoge":"19001413","Last Name":"EL YAMLAHI","First Name":"AICHA","CC1":14},
    {"Numero appoge":"20000759","Last Name":"ENNAJARI","First Name":"OUMAIMA","CC1":10},
    {"Numero appoge":"20000777","Last Name":"GLIOUAL","First Name":"YASSINE","CC1":7},
    {"Numero appoge":"20000763","Last Name":"HAYAOUI","First Name":"MOUAD","CC1":13},
    {"Numero appoge":"120000740","Last Name":"HIMMI","First Name":"HAJAR","CC1":8},
    {"Numero appoge":"20002137","Last Name":"IDRISSI","First Name":"YASSINE","CC1":12},
    {"Numero appoge":"20002554","Last Name":"KACHAR","First Name":"NABIL","CC1":11},
    {"Numero appoge":"20009742","Last Name":"KDIDAR","First Name":"HAJAR","CC1":7},
    {"Numero appoge":"19002804","Last Name":"LAHOIENI","First Name":"ABDERRAHIM","CC1":7},
    {"Numero appoge":"20002123","Last Name":"ZAOUI","First Name":"OUSSAMA","CC1":12}
]

absent_data=[{
    0:15,
    2:14,
    3:10,
    4:12,
    5:12,
    6:11,
    8:7,
    10:9,
    12:6,
    14:5,
    16:5,
    18:3
}
]

cigarette_data=[{
    0:18,
    1:13,
    2:11,
    3:13,
    4:6,
    5:9,
    6:9,
    7:8,
    9:7
}
]


@app.get("/api/students", response_model=List[Dict[str, str]])
async def get_etudiants():
    return donnees_json

@app.get("/api/students/gender",response_model=Dict[str, int])
async def bar_gender():
    return {
        "M":20,
        "F":25
    }

@app.get("/api/students/use_internet",response_model=Dict[str, int])
async def using_internet():
    return {
        "no":15,
        "yes":12
    }

@app.get("/api/students/absence",response_model=List[Dict[int, int]])
async def effects_absence():
    return absent_data


@app.get("/api/students/use_cigarette",response_model=List[Dict[int, int]])
async def effects_cigarette():
    return cigarette_data


@app.get("/api/students/in_relation",response_model=Dict[str, int])
async def en_realtion():
    return {
        "no":17,
        "yes":9
    }