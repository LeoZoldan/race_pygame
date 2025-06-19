import json
from datetime import datetime


def init_db():
    try:
        open("log.dat","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        open("log.dat","w")
    
    
def writeData(name, points):
    init_db()
    
    db = open("log.dat","r")
    data = db.read()
    db.close()
    
    if data != "":
        dataDict = json.loads(data)
    else:
        dataDict = {}
        
    data_br = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if name in dataDict:
        dataDict[name].append((points, data_br))
    else:
        dataDict[name] = [(points, data_br)]
    
    db = open("log.dat","w")
    db.write(json.dumps(dataDict))
    db.close()
    
    
def getData():
    init_db()
    
    with open("log.dat", "r") as db:
        data = json.load(db)
    
    all_players = []
    for name, plays in data.items():
        for points, date_str in plays:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
            all_players.append((name, points, date_obj))
    
    all_players.sort(key=lambda x: x[2], reverse=True)

    return [(name, points, date.strftime("%d/%m/%Y %H:%M:%S")) for name, points, date in all_players]