# importar librerias y archivos necesarios
from ast import If
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Canton
from configuration import cadena_base_datos
from genera_tablas import Provincia
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

cantones = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        if linea[4] not in cantones:
            cantones.append(linea[4])
            id_p = session.query(Provincia).filter_by(codigo_div_pol = linea[2]).first()
            session.add(Canton(codigo_div_pol=linea[4],nombre=linea[5], cod_distrito=linea[8], provincia_id=id_p.id))

session.commit()