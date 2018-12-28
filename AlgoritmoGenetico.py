import Datos
import Poblacion
from random import uniform
import copy
import Manejador
import HorarioFinal

class AlgoritmoGenetico:
	def __init__(self, datos = Datos.Datos()):
		self.datos = datos

	def cruzaPoblacion(self, poblacion = Poblacion.Poblacion()):
		cruzaPoblacion = Poblacion.Poblacion(tamPob = len(poblacion.listaHorariosFinales), datos = self.datos)

		for i in range(0, Manejador.numHFElite):
			cruzaPoblacion.listaHorariosFinales[i] = copy.deepcopy(poblacion.listaHorariosFinales[i])

		for i in range(Manejador.numHFElite, len(poblacion.listaHorariosFinales)):
			if Manejador.ratioCruza > uniform(0, 0.9):
				hf1 = self.ruletaPoblacion(poblacion = poblacion).ordenarFitness().listaHorariosFinales[0]
				hf2 = self.ruletaPoblacion(poblacion = poblacion).ordenarFitness().listaHorariosFinales[0]
				cruzaPoblacion.listaHorariosFinales[i] = copy.deepcopy(self.cruzaHorarioFinal(horarioF1 = hf1, horarioF2 = hf2))

			else:
				cruzaPoblacion.listaHorariosFinales[i] = copy.deepcopy(poblacion.listaHorariosFinales[i])

		return cruzaPoblacion

	def cruzaHorarioFinal(self, horarioF1 = HorarioFinal.HorarioFinal(), horarioF2 = HorarioFinal.HorarioFinal()):
		cruzaHorarioFinal = HorarioFinal.HorarioFinal(datos = self.datos).inicializarHF()

		for i in range(0, len(cruzaHorarioFinal.getClases())):
			if uniform(0, 0.9) > 0.5:
				cruzaHorarioFinal.getClases()[i] = copy.deepcopy(horarioF1.getClases()[i])

			else:
				cruzaHorarioFinal.getClases()[i] = copy.deepcopy(horarioF2.getClases()[i])

		return cruzaHorarioFinal

	def mutacionPoblacion(self, poblacion = Poblacion.Poblacion()):
		mutacionPoblacion = Poblacion.Poblacion(tamPob = len(poblacion.listaHorariosFinales), datos = self.datos)
		listaHF = mutacionPoblacion.listaHorariosFinales

		for i in range(0, Manejador.numHFElite):
			listaHF[i] = copy.deepcopy(poblacion.listaHorariosFinales[i])

		for i in range(Manejador.numHFElite, len(poblacion.listaHorariosFinales)):
			listaHF[i] = copy.deepcopy(self.mutacionHorarioFinal(poblacion.listaHorariosFinales[i]))

		return mutacionPoblacion

	def mutacionHorarioFinal(self, mutarHF = HorarioFinal.HorarioFinal()):
		horarioFinal = HorarioFinal.HorarioFinal(datos = self.datos).inicializarHF()

		for i in range(0, len(mutarHF.getClases())):
			if Manejador.ratioMutacion > uniform(0, 0.9):
				mutarHF.getClases()[i] = copy.deepcopy(horarioFinal.getClases()[i])
		
		return mutarHF

	def ruletaPoblacion(self, poblacion = Poblacion.Poblacion()):
		ruletaPoblacion = Poblacion.Poblacion(tamPob = Manejador.tamRuleta, datos = self.datos)

		for i in range(0, Manejador.tamRuleta):
			ruletaPoblacion.listaHorariosFinales[i] = copy.deepcopy(poblacion.listaHorariosFinales[int(uniform(0, 0.9) * len(poblacion.listaHorariosFinales))])

		return ruletaPoblacion

	def evolucionar(self, poblacion = Poblacion.Poblacion()):
		return self.mutacionPoblacion(self.cruzaPoblacion(poblacion))