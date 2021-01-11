from Tema4_Actividad5.Ventas import borrar, conexion, actualizarventas, inventas,\
    importarcsv, csvproductos

dic = [(1,1,100,'Huelva','Null',15),(2,1,100,'Sevilla','Null',15),(3,2,100,'Sevilla','Null',18),(4,2,100,'Sevilla','Null',18),(5,2,100,'Huelva','Null',18),(6,3,100,'Sevilla','Null',21),(7,3,100,'Cordoba','Null',21),(8,4,100,'Sevilla','Null',24),(9,4,100,'Huelva','Null',24),(10,4,100,'Cordoba','Null',24),(11,5,100,'Almeria','Null',15.5),(12,5,100,'Sevilla','Null',15.5),(13,6,100,'Cadiz','Null',12.5),(14,6,100,'Sevilla','Null',12.5),(15,6,100,'Huelva','Null',12.5),(16,7,100,'Sevilla','Null',21.5),(17,7,100,'Almeria','Null',21.5),(18,8,100,'Sevilla','Null',24.2),(19,8,100,'Huelva','Null',24.2),(20,8,100,'Cordoba','Null',24.2)]


archivo = "mi_erp.db"
con = conexion(archivo)
cur = con.cursor()
#borrar(con)



ventas = []
i=0
for ventas in dic:
    ventas=dic[i]
    i=i+1
    inventas(con,ventas)

 
actualizarventas(con)

importarcsv(con)

csvproductos(con)


con.close()
