import csv

# Abrir o arquivo csv e atribuir á uma variável
arquivo=open("clientes.csv","r",encoding="utf8")
linhas=csv.reader(arquivo)


for i in linhas:
    lin=str(i).replace("['","").replace("']","").split(";")
    if(lin[0]=="78"):
        print(lin)
    

