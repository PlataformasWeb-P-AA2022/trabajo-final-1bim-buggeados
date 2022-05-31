from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia
# se importa información del archivo configuracion
from configuration import cadena_base_datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
establecimiento = session.query(Establecimiento).all()
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


print("\t\tConsulta 1")
#Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553
print("Establecimientos con el Código División Política Administrativa Parroquia con valor 110553") 

establecimiento = session.query(Establecimiento.nombre).join(Parroquia, Canton, Provincia).filter(Parroquia.codigo_div_pol == '110553').all()
for elemento in establecimiento:
    cadena = "Nombre Establecimiento: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)

print("\t\tConsulta 2")
#Todos los establecimientos de la provincia de EL ORO.
print("Establecimientos de la provincia de EL ORO") 

# Consulta que devuelve  los establecimientos de la provincia de EL ORO.
establecimiento = session.query(Establecimiento.nombre).join(Parroquia, Canton, Provincia).filter(Provincia.nombre == 'EL ORO').all()
for elemento in establecimiento:
    cadena = "Nombre Establecimiento: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(establecimiento))

print("\t\tConsulta 3")
#Todos los establecimientos del cantón de Portovelo.
print("Establecimientos de la cantón de Portovelo") 

# Consulta que devuelve  los establecimientos del cantón de Portovelo.
establecimiento = session.query(Establecimiento.nombre).join(Parroquia, Canton, Provincia).filter(Canton.nombre == 'PORTOVELO').all()
for elemento in establecimiento:
    cadena = "Nombre Establecimiento: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(establecimiento))


print("\t\tConsulta 4")
#Todos los establecimientos del cantón de Zamora.
print("Establecimientos de la cantón de Zamora") 

# Consulta que devuelve  los establecimientos del cantón de Zamora.
establecimiento = session.query(Establecimiento.nombre).join(Parroquia, Canton, Provincia).filter(Canton.nombre == 'ZAMORA').all()
for elemento in establecimiento:
    cadena = "Nombre Establecimiento: %s" %(str(elemento).replace("('",""))
    cadena = cadena.replace("',)", "")
    print(cadena)
print(len(establecimiento))


