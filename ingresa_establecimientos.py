# importar librerias y archivos necesarios
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Establecimiento,Parroquia
from configuration import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

establecimientos = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        if linea[0] not in establecimientos:
            id_parr = session.query(Parroquia).filter_by(codigo_div_pol=linea[6]).first()
            establecimientos.append(linea[0])
            session.add(Establecimiento(codigo_AMIE=linea[0], nombre=linea[1],sostenimiento=linea[9], tipo_educacion=linea[10], modalidad=linea[11], jornada=linea[12], acceso=linea[13],num_estudiantes=int(linea[14]), num_docentes=int(linea[15]), parroquia_id = id_parr.id))
session.commit()
