from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_ 
from sqlalchemy import asc


# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuration import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores.")
establecimientos = session.query(Establecimiento.nombre).filter(Establecimiento.num_docentes > 100)\
    .order_by(asc(Establecimiento.num_estudiantes)).all()

for elemento in establecimientos:
    cadena = "Nombre: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)

print("\t\tConsulta 2")
print("\nLos establecimientos ordenados por número de profesores que tengan más de 100 profesores.")

establecimientos2 = session.query(Establecimiento.nombre, Establecimiento.num_docentes).filter(
    Establecimiento.num_docentes > 100).order_by(asc(Establecimiento.num_docentes)).all()

for elemento in establecimientos2:
    cadena = "Nombre: %s || Num Docentes: %s" %(str(elemento[0]).replace("('",""), elemento[1])
    cadena = cadena.replace("',)", "")
    cadena = cadena.replace(")","")
    print(cadena)