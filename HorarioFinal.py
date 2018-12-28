from operator import itemgetter
from random import uniform
import Datos
import Clase

#Individuo
class HorarioFinal:
	def __init__(self, datos = Datos.Datos()):
		self.datos = datos
		self.listaClases = []
		self.contadorClase = 0
		self.numConflictos = 0
		self.fitness = -1.0
		self.fitnessCambio = True

	def inicializarHF(self):
		for curso in self.datos.listaCursos:
			for grupo in curso.listaGrupos:
				self.contadorClase += 1
				nuevaClase = Clase.Clase(self.contadorClase, curso, grupo)
				nuevaClase.setHorario(itemgetter(int(uniform(0, 0.9) * len(self.datos.listaHorarios)))(self.datos.listaHorarios))
				nuevaClase.setSalon(itemgetter(int(uniform(0, 0.9) * len(self.datos.listaSalones)))(self.datos.listaSalones))
				nuevaClase.setMaestro(itemgetter(int(uniform(0, 0.9) * len(grupo.listaMaestros)))(grupo.listaMaestros))
				self.listaClases.append(nuevaClase)

		return self

	def getClases(self):
		fitnessCambio = True
		return self.listaClases
	
	def buscadorMasConflictos(self, instanciaX, instanciaY):
		if (instanciaX.horario.momento == instanciaY.horario.momento) and (instanciaX.IDClase != instanciaY.IDClase):
			if instanciaX.salon.IDSalon == instanciaY.salon.IDSalon:
				self.numConflictos += 1

			if instanciaX.maestro.IDMaestro == instanciaY.maestro.IDMaestro:
				self.numConflictos += 1
	
	def calcularFitness(self):
		self.numConflictos = 0
		
		for x in self.getClases():
			if x.salon.capacidad < x.grupo.maxNumEst:
				self.numConflictos += 1

			[self.buscadorMasConflictos(x, y) for y in self.getClases() if self.getClases().index(y) >= self.getClases().index(x)]
		
		return "{0:.2f}".format(1 / float(self.numConflictos + 1))

	def getFitness(self):
		if self.fitnessCambio == True:
			self.fitness = self.calcularFitness()
			self.fitnessCambio = False

		return self.fitness

	def retornarIndividuo(self):
		cadena = ""

		for i in self.getClases():
			cadena += i.retornarCromosoma() + ","

		return cadena