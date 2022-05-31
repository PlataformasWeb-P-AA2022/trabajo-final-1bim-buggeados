# importar librerias y archivos necesarios
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Canton ,Parroquia

from configuration import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

parroquias = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        if linea[6] not in parroquias:
            parroquias.append(linea[6])
            id_c = session.query(Canton).filter_by(codigo_div_pol=linea[4]).first()
            session.add(Parroquia(codigo_div_pol=linea[6],nombre=linea[7], canton_id=id_c.id))
session.commit()