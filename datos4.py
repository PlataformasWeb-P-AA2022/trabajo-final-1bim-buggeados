from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_ 


# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton, Provincia, Parroquia, Establecimiento

# se importa información del archivo configuracion
from configuration import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación.") 

establecimientos = session.query(Establecimiento.nombre, Parroquia.nombre).join(Parroquia).filter(
    and_(Establecimiento.num_docentes > 40, Establecimiento.tipo_educacion.like(
        'Educación regular'))).order_by(Parroquia.nombre).all()

for elemento in establecimientos:
    cadena = "Nombre: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    cadena = cadena.replace("'", "")
    cadena = cadena.replace(")", "")
    print(cadena)


print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.")

establecimientos2 = session.query(Establecimiento.nombre).filter(Establecimiento.cod_establecimiento.like('11D04')).order_by(Establecimiento.sostenimiento)

for elemento in establecimientos2:
    cadena = "Nombre: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)