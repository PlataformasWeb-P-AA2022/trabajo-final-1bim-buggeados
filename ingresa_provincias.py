from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia, Canton

from configuration import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

provincias = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        if linea[2] not in provincias:
            provincias.append(linea[2])
            session.add(Provincia(codigo_div_pol=linea[2],nombre=linea[3]))

session.commit()