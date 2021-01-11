#Actividad 4
import csv

import sqlite3
from sqlite3 import Error

def conexion(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conexion realizada a ", filename)
    except Error:
        print(Error)
        con = None 
    finally:
        return con

def insertaremple(con, dic):
    try:
        cur = con.cursor()
            
        cur.execute("insert into empleados values (?,?,?,?,?,?)", dic)
        con.commit()
    
    except sqlite3.IntegrityError as err:
        print("Error --> ", err )
        print("No se aniadieron los registros")


def importarcsv(con):
        
    cur = con.cursor()
    emplecsv = open("empleados.csv","w")
    cur.execute("SELECT * from empleados")
    rows = cur.fetchall()

    
    datos = [["ID,Nombre,Salario anual,Departamento,Categoria,Fecha de contratacion"]]
    datos.append(rows)
    with emplecsv:
        writer = csv.writer(emplecsv)
        writer.writerows(datos)
        
        
    emplecsv.close()
    con.commit()   
        
        
        
def importeencsv(con):
    
    cur = con.cursor()
    
    cur.execute("SELECT distinct(departamento) from empleados")
    dep = cur.fetchall()    
    dato = []
    
    for i in dep:
        cur.execute("SELECT distinct(categoria) from empleados where departamento = (?)", i)
        cat = cur.fetchall()
        for y in cat:
            
            cur.execute("SELECT sum(salario) from empleados where categoria = (?)", y)
            suel = cur.fetchall()
            importecsv = open("Resumen.csv","w")
            dato.append(i)
            dato.append(cat)
            dato.append(suel)
    
            with importecsv:
                writer = csv.writer(importecsv, delimiter=",")
                writer.writerows(dato)
        
        
    importecsv.close()
        
    con.commit()   
    
    
def borrar(con):

    cur = con.cursor()
        
    cur.execute("delete from empleados") 
    con.commit()
    

    
    
    
