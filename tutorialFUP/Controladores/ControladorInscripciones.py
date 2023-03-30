from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Modelos.Estudiante import Estudiante
from tutorialFUP.Modelos.Materias import Materias
from tutorialFUP.Repositorio.RepositorioInscripcion import RepositorioInscripcion
from tutorialFUP.Repositorio.RepositorioEstudiante import RepositorioEstudiante
from tutorialFUP.Repositorio.RepositorioMateria import RepositorioMateria


class ControladorInscripcion():

   def __init__(self) -> object:
       self.repositorioInscipcion = RepositorioInscripcion()
       self.repositorioEstudiantes = RepositorioEstudiante()
       self.repositorioMaterias = RepositorioMateria()

   def index(self):
       return self.repositorioInscipcion.findAll()

   def create(self, infoInscripcion, id_estudiante, id_materia):
       nuevaInscripcion = Inscripcion(infoInscripcion)
       elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
       laMateria = Materias(self.repositorioMaterias.findById(id_materia))
       nuevaInscripcion.estudiante = elEstudiante
       nuevaInscripcion.materia = laMateria
       return self.repositorioInscipcion.save(nuevaInscripcion)

   def show(self, id):
       elInscripcion = Inscripcion(self.repositorioInscipcion.findById(id))
       return elInscripcion.__dict__

   def update(self, id, infoInscripcion, id_estudiante, id_materia):
       laInscripcion = Inscripcion(self.repositorioInscipcion.findById(id))
       laInscripcion.anio = infoInscripcion["año"]
       laInscripcion.semestre = infoInscripcion["semestre"]
       laInscripcion.notaFinal = infoInscripcion["nota_final"]
       elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
       laMateria = Materias(self.repositorioMaterias.findById(id_materia))
       laInscripcion.estudiante = elEstudiante
       laInscripcion.materia = laMateria
       return self.repositorioInscipcion.save(laInscripcion)

   def delete(self, id):
       return self.repositorioInscipcion.delete(id)

