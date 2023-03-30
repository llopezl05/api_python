from flask import jsonify

from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorio.RepositorioDepartamento import RepositorioDepartamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorDepartamentos():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self) -> object:
       self.repositorioDepartamento = RepositorioDepartamento()
       print("Creando ControladorDepatameto")


   def index(self):
       print("Listar todos los departamentos")
       return self.repositorioDepartamento.findAll()

   def create(self, Eldepartamento):
       print("Crear un departamento")
       Eldepartamento = Departamento(Eldepartamento)
       return self.repositorioDepartamento.save(Eldepartamento)

   def show(self, id):
       print("Mostrando un departamento con id ", id)
       elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
       return jsonify(elDepartamento)

   def update(self, id, infoDepartamento):
       DepartamentoActual = Departamento(self.repositorioDepartamento.findById(id))
       DepartamentoActual.nombre = infoDepartamento["nombre"]
       DepartamentoActual.descripcion = infoDepartamento["descripcion"]
       return self.repositorioDepartamento.save(DepartamentoActual)

   def delete(self, id):
       print("Elimiando departamento con id ", id)
       return self.repositorioDepartamento.delete(id)

