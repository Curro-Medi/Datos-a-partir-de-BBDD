import sqlite3
from sqlite3 import Error
import csv
def conexion(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conexion realizada a ", filename)
    except Error:
        print(Error)
        con = None 
    finally:
        return con
    
def borrar(con):

    cur = con.cursor()
        
    cur.execute("delete from ventas") 
    con.commit()
    
    
    
def actualizarventas(con):
    try:
        
        cur = con.cursor()

        cur.execute("update ventas set importe = cantidad * precio ")
        con.commit()
            
        
    except sqlite3.OperationalError:
        print("Algo fue mal")
  
  
  
def inventas(con, dic):
    try:
        cur = con.cursor()
            
        cur.execute("insert into ventas values (?,?,?,?,?,?)", dic)
        con.commit()
    
    except sqlite3.IntegrityError as err:
        print("Error --> ", err )
        print("No se aniadieron los registros")

  
  
def importarcsv(con):

    cur = con.cursor()
    
    cur.execute("SELECT distinct(ciudad) from ventas")
    dep = cur.fetchall()    
    dato = []
    
    importecsv = open("Acum_Ventas.csv","w")

    for i in dep:
        cur.execute("SELECT sum(importe) from ventas where ciudad = (?)", i)
        cat = cur.fetchall()
        
        dato.append(i)
        dato.append(cat)
    with importecsv:
        writer = csv.writer(importecsv, delimiter=",")
        writer.writerows(dato)
        
    con.commit()  
    importecsv.close()
  

def csvproductos(con):
    
    cur = con.cursor()
    
    cur.execute("SELECT * from productos")
    dep = cur.fetchall()    
    dato = [["Producto , Precio , Cantidad , importe total"]]

    
    importecsv = open("Acum_Productos.csv","w")
    dato.append(dep)
    with importecsv:
        writer = csv.writer(importecsv, delimiter=",")
        writer.writerows(dato)
        
        
    importecsv.close()
        
    con.commit()
    
  
  
  
  
  
  
  
  
  
  
  