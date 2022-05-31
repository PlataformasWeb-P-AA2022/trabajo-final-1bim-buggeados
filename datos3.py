from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia
from configuration import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


print("Consulta 1")
print("\033[0;m"+"Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores"+'\033[0;m') 

cantones = session.query(Canton.nombre).join(Parroquia,Establecimiento)\
    .filter(or_(Establecimiento.num_docentes == 0 , Establecimiento.num_docentes == 5 , Establecimiento.num_docentes == 11)).all()

cantones = set(cantones)
for elemento in cantones:
    cadena = "Nombre Canton con 0,5 u 11 profesores: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(cantones))

print("Consulta 2")
print("Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21") 

establecimiento = session.query(Establecimiento.nombre).join(Parroquia).filter(and_(Establecimiento.num_estudiantes >= 21,
        Parroquia.nombre == "PINDAL")).all()

for elemento in establecimiento:
    cadena = "Nombre establecimiento : %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(establecimiento))
