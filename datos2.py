from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuration import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("Consulta 1")
#Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
print("Establecimientos con el Código División Política Administrativa Parroquia con valor 110553") 

parroquia = session.query(Parroquia.nombre).join(Establecimiento).filter(Establecimiento.jornada == "Matutina y Vespertina").all()
for elemento in parroquia:
    cadena = "Nombre Establecimiento con codgio valor 110553: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(parroquia))


print("Consulta 2")
#Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459

canton = session.query(Canton.nombre).join(Parroquia,Establecimiento).filter(or_(Establecimiento.num_estudiantes == 448,Establecimiento.num_estudiantes == 450,
Establecimiento.num_estudiantes == 451,Establecimiento.num_estudiantes == 454,Establecimiento.num_estudiantes == 458,Establecimiento.num_estudiantes == 459)).all()
for c in parroquia:
    print(c)
print(len(parroquia))
