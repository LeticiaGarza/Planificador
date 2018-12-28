import Curso
import Grupo
import Salon
import Maestro
import Horario

#Cromosoma
class Clase:
	def __init__(self, IDClase = 0, curso = Curso.Curso(), grupo = Grupo.Grupo()):
		self.IDClase = IDClase
		self.curso = curso
		self.grupo = grupo
		self.maestro = Maestro.Maestro()
		self.horario = Horario.Horario()
		self.salon = Salon.Salon()

	def setMaestro(self, maestro):
		self.maestro = maestro

	def setHorario(self, horario):
		self.horario = horario

	def setSalon(self, salon):
		self.salon = salon

	def retornarCromosoma(self):
		return "[" + self.curso.nombreCurso + "," + self.grupo.IDGrupo + "," + self.salon.IDSalon + "," + self.maestro.IDMaestro + "," + self.horario.IDHorario + "]"
		