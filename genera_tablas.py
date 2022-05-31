# importar librerias necesarias
from contextlib import nullcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


# se importa información del archivo configuracion
from configuration import cadena_base_datos

# se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    nombre = Column(String(100))

    # creacion de la relacion que se hara com Canton
    cantones = relationship("Canton", back_populates="provincia")

    # representacion que se dara al imprimir el objeto
    def __repr__(self):
        return "Provincia: Codigo=%s - Nombre=%s"  % (self.codigo, self.nombre)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    cod_distrito = Column(String(100))
    nombre = Column(String(100))

    # columna con la llave foranea
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # creacion de la relacion que se hara com Provincia
    provincia = relationship("Provincia", back_populates="cantones")
    # creacion de la relacion que se hara com Parroquia
    parroquia = relationship("Parroquia", back_populates="canton")

    # representacion que se dara al imprimir el objeto
    def __repr__(self):
        return "Canton: Codigo=%s - Nombre=%s - Codigo Distrito=%s " % (
                    self.codigo_div_pol,
                    self.nombre,
                    self.cod_distrito)


class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo_div_pol = Column(String(100))
    nombre = Column(String(100))

    # columna con la llave foranea
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # creacion de la relacion que se hara com Canton
    canton  = relationship("Canton", back_populates="parroquia")
    # creacion de la relacion que se hara com Establecimiento
    establecimiento  = relationship("Establecimiento", back_populates="parroquia")
    
    # representacion que se dara al imprimir el objeto
    def __repr__(self):
        return "Parroquia: codigo=%s - Nombre=%s " % (
                    self.codigo,
                    self.nombre)

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

    # columna con la llave foranea
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # creacion de la relacion que se hara com Parroquia
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    # representacion que se dara al imprimir el objeto
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