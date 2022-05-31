from sqlalchemy import create_engine, or_, and_, asc
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuration import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
print("\t\tConsulta 1")
print("Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores.")
establecimientos = session.query(Establecimiento.nombre, Establecimiento.num_estudiantes).filter(Establecimiento.num_docentes > 100)\
    .order_by(asc(Establecimiento.num_estudiantes)).all()

for elemento in establecimientos:
    cadena = "Nombre: %s || Num Estudiantes: %s" %(str(elemento[0]).replace("('",""), str(elemento[1]) )
    cadena = cadena.replace("',)", "")
    cadena = cadena.replace(")","")
    print(cadena)

print("\t\tConsulta 2")
print("Los establecimientos ordenados por número de profesores que tengan más de 100 profesores.")

establecimientos2 = session.query(Establecimiento.nombre, Establecimiento.num_docentes).filter(
    Establecimiento.num_docentes > 100).order_by(asc(Establecimiento.num_docentes)).all()

for elemento in establecimientos2:
    cadena = "Nombre: %s || Num Docentes: %s" %(str(elemento[0]).replace("('",""), elemento[1])
    cadena = cadena.replace("',)", "")
    cadena = cadena.replace(")","")
    print(cadena)