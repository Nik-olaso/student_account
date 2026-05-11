import pandas as pd


klass = {
    'A':['Иванов','Смирнов','Кузнецов','Попов','Васильев','Петров','Соколов', 'Михайлов', 'Новиков', 'Федоров'],
    'B':['Морозов','Волков','Алексеев','Лебедев','Семенов','Егоров','Павлов','Козлов','Степанов','Николаев'],
    }


tabl = pd.DataFrame(klass)
tabl = tabl.melt()
tabl = tabl.rename(columns={"variable": "bukva", "value": "name"})
print(tabl)