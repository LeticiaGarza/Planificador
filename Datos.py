import Curso
import Grupo
import Salon
import Maestro
import Horario

class Datos:
	def inicializarDatos(self):
		salon1 = Salon.Salon(IDSalon = "S1", capacidad = 25)
		salon2 = Salon.Salon(IDSalon = "S2", capacidad = 45)
		salon3 = Salon.Salon(IDSalon = "S3", capacidad = 35)
		self.listaSalones = [salon1, salon2, salon3]

		horario1 = Horario.Horario(IDHorario = "H1", momento = "LIV 09:00-10:00")
		horario2 = Horario.Horario(IDHorario = "H2", momento = "LIV 10:00-11:00")
		horario3 = Horario.Horario(IDHorario = "H3", momento = "MJ 09:00-10:30")
		horario4 = Horario.Horario(IDHorario = "H4", momento = "MJ 10:30-12:00")
		self.listaHorarios = [horario1, horario2, horario3, horario4]

		maestro1 = Maestro.Maestro(IDMaestro = "M1", nombreMaestro = "Alan Fox")
		maestro2 = Maestro.Maestro(IDMaestro = "M2", nombreMaestro = "Mario Paz")
		maestro3 = Maestro.Maestro(IDMaestro = "M3", nombreMaestro = "Sandra Pasteur")
		maestro4 = Maestro.Maestro(IDMaestro = "M4", nombreMaestro = "Pierre Dumont")
		self.listaMaestros = [maestro1, maestro2, maestro3, maestro4]

		grupo1 = Grupo.Grupo(IDGrupo = "G1", nombreGrupo = "GI1", listaMaestros = [maestro1, maestro2], maxNumEst = 25)
		grupo2 = Grupo.Grupo(IDGrupo = "G2", nombreGrupo = "GF1", listaMaestros = [maestro1, maestro2, maestro3], maxNumEst = 35)
		grupo3 = Grupo.Grupo(IDGrupo = "G3", nombreGrupo = "GI2", listaMaestros = [maestro1, maestro2], maxNumEst = 25)
		grupo4 = Grupo.Grupo(IDGrupo = "G4", nombreGrupo = "GF2", listaMaestros = [maestro3, maestro4], maxNumEst = 30)
		grupo5 = Grupo.Grupo(IDGrupo = "G5", nombreGrupo = "GF3", listaMaestros = [maestro4], maxNumEst = 35)
		grupo6 = Grupo.Grupo(IDGrupo = "G6", nombreGrupo = "GA1", listaMaestros = [maestro1, maestro3], maxNumEst = 45)
		grupo7 = Grupo.Grupo(IDGrupo = "G7", nombreGrupo = "GA2", listaMaestros = [maestro2, maestro4], maxNumEst = 45)
		self.listaGrupos = [grupo1, grupo2, grupo3, grupo4, grupo5, grupo6, grupo7]

		curso1 = Curso.Curso(nombreCurso = "Ingles", listaGrupos = [grupo1, grupo3])
		curso2 = Curso.Curso(nombreCurso = "Frances", listaGrupos = [grupo2, grupo4, grupo5])
		curso3 = Curso.Curso(nombreCurso = "Aleman", listaGrupos = [grupo6, grupo7])
		self.listaCursos = [curso1, curso2, curso3]

		self.numClases = len(self.listaGrupos)

		return self

	def __init__(self):
		self.listaCursos = []
		self.listaGrupos = []
		self.listaSalones = []
		self.listaMaestros = []
		self.listaHorarios = []
		self.numClases = 0