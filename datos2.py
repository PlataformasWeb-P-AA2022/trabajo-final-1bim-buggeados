from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia
from configuration import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")
print("Establecimientos con el Código División Política Administrativa Parroquia con valor 110553") 

parroquia = session.query(Parroquia.nombre).join(Establecimiento).filter(Establecimiento.jornada == "Matutina y Vespertina").all()
for elemento in parroquia:
    cadena = "Nombre Establecimiento con codgio valor 110553: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(parroquia))


print("Consulta 2")

canton = session.query(Canton.nombre).join(Parroquia,Establecimiento).filter(or_(Establecimiento.num_estudiantes == 448,Establecimiento.num_estudiantes == 450,
Establecimiento.num_estudiantes == 451,Establecimiento.num_estudiantes == 454,Establecimiento.num_estudiantes == 458,Establecimiento.num_estudiantes == 459)).all()
for c in parroquia:
    print(c)
print(len(parroquia))
