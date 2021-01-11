#Actividad 4
from Tema4_Actividad4.Empleados import conexion, insertaremple, importarcsv,\
    importeencsv, borrar

dic = [(1,'Juan Jose Gutierrez',39100,'Financiero','Analista','15-02-1998'),(2,'Ainhoa Guerrero',15100,'Financiero','Ayudante','03-04-2008'),(3,'Luisa Perez',64100,'Gerencia','Gerente','15-02-1998'),(4,'Andres Perez',46100,'Comercial','Director Comercial','13-09-2001'),(5,'Manuel Gonzalez',28100,'Comercial','Comercial','15-02-2007'),(6,'Alejandro Garcia',15100,'Comercial','Administrativo','30-11-2014'),(7,'Jose Zubieta',21000,'Comercial','Comercial','04-10-2018'),(8,'Gerardo Posma',18100,'PostVenta','Reponedor','17-04-200'),(9,'Manuel Jose Gomez',32100,'Informatica','Analista','28-03-2006'),(10,'Maria Fernandez',23100,'Informatica','Programador','24-01-2006'),(11,'Fernando Vazquez',15100,'Informatica','Programador','15-07-2019'),(12,'Pedro Buenaventura',32100,'Comercial','Comercial','28-03-2020'),(13,'Antonio Diez',15100,'Informatica','Programador','28-03-2020'),(14,'Lucia Rodriguez',15100,'Informatica','Programador','28-03-2020')]

#abrir = open("empleados.txt", "r")

#for leer in abrir.readline():
#    dic.append(leer)
    
    
#abrir.close()

#print(dic)
# He intentado leer el archivo empleados.txt y pasarlo a un diccionario para poder asi manejarlo pero me daba problemas debido a que tambien cogia /n en cada salto de linea del documento y a la hora de realizar las consultas sql aunque intentaba hacerlas de una en una se cogia todo el diccionario a la vez y me intentaba introducri todos los datos en la misma consulta por ello lo he metido directamente en un diccionario

archivo = "prueba.db"
con = conexion(archivo)
cur = con.cursor()
#borrar(con)
empleados = []
i=0
for empleados in dic:
    empleados=dic[i]
    i=i+1
    insertaremple(con,empleados)
 

importarcsv(con)
importeencsv(con)



con.close()
