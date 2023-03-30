from tutorialFUP.Modelos.Materias import Materias
from tutorialFUP.Modelos.Departamento import Departamento
from tutorialFUP.Repositorio.RepositorioMateria import RepositorioMateria
from tutorialFUP.Repositorio.RepositorioDepartamento import RepositorioDepartamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMaterias():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

   def __init__(self):
       self.repositorioMateria = RepositorioMateria()
       self.repositorioDepartamento = RepositorioDepartamento()
       print("Creando ControladorMateria")

   def index(self):
       print("listando materias")
       return self.repositorioMateria.findAll()

   def create(self, laMateria):
       print("Crear una materia")
       nuevaMateria = Materias(laMateria)
       return self.repositorioMateria.save(nuevaMateria)

   def show(self, id):
       print("Mostrando una materia con id ", id)
       laMateria = Materias(self.repositorioMateria.findById(id))
       return laMateria.__dict__

   def update(self, id, laMateria):
       print("Actualizando estudiante con id ", id)
       materiaActual = Materias(self.repositorioMateria.findById(id))
       materiaActual.nombre = laMateria["nombre"]
       materiaActual.creditos = laMateria["creditos"]
       return self.repositorioMateria.save(materiaActual)

   def delete(self, id):
       print("Elimiando materia con id ", id)
       return self.repositorioMateria.delete(id)


   def asignarDepartamento(self, id, id_departamento):
       materiaActual = Materias(self.repositorioMateria.findById(id))
       departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
       materiaActual.departamento = departamentoActual
       return self.repositorioMateria.save(materiaActual)




