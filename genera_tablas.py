from contextlib import nullcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey



# se importa información del archivo configuracion
from configuration import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Relacion de uno a muchos 

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    nombre = Column(String(100))

    cantones = relationship("Canton", back_populates="provincia")
    def __repr__(self):
        return "Provincia: codigo=%s - Nombre=%s"  % (self.codigo, self.nombre)

# Un cantón pertence a un provincia.
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    cod_distrito = Column(String(100))
    nombre = Column(String(100))
    # se agrega la columna provincia_id como ForeignKey
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Mapea la relación entre las clases
    # Canton puede acceder a las provincias asociados
    # por la llave foránea
    provincia = relationship("Provincia", back_populates="cantones")
    # Mapea la relación entre las clases
    # Canton puede acceder a las parroquias asociados
    # por la llave foránea
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigo=%s - Nombre=%s " % (
                    self.codigo,
                    self.cod_distrito, 
                    self.nombre)

# Una parroquia pertence a un cantón.

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    nombre = Column(String(100))
    # se agrega la columna canton_id como ForeignKey
    # se hace referencia al id de la entidad canton
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Mapea la relación entre las clases
    # Parroquia tiene una relación con Canton
    canton  = relationship("Canton", back_populates="parroquia")
    # Mapea la relación entre las clases
    # Parroquia puede acceder a los establecimientos asociados
    # por la llave foránea
    establecimiento  = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: codigo=%s - Nombre=%s " % (
                    self.codigo,
                    self.nombre)

# Un establecimiento pertenece a una parroquia.

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_AMIE = Column(String(100))
    nombre = Column(String(100))
    sostenimiento = Column(String(100))
    tipo_educacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    acceso = Column(String(100))
    num_estudiantes = Column(Integer)
    num_docentes = Column(Integer)
    # se agrega la columna parroquia_id como ForeignKey
    # se hace referencia al id de la entidad parroquia
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Mapea la relación entre las clases
    # Establecimiento tiene una relación con Parroquias
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    def __repr__(self):
        return "Establecimiento: Codigo AMIE=%s - Nombre=%s - Sostenimiento=%s - Tipo educacion=%s - Modalidad=%s - Jornada=%s - Acceso=%s - Numero estudiantes=%d - Numero docentes=%d " % (
                          self.codigo_AMIE, 
                          self.nombre, 
                          self.sostenimiento,
                          self.tipo_educacion,
                          self.modalidad,
                          self.jornada,
                          self.acceso,
                          self.num_estudiantes,
                          self.num_docentes)

Base.metadata.create_all(engine)