from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton ,Parroquia
# se importa información del archivo configuracion
from configuration import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
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
            # print(linea[5], ";;;;;", linea[5].id)
            #id_c = session.query(Canton).filter_by(nombre=linea[5]).first()
            session.add(Parroquia(codigo_div_pol=linea[6],nombre=linea[7], canton_id=id_c.id))
session.commit()