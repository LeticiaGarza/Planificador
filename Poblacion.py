import HorarioFinal
import Datos

class Poblacion:
	def __init__(self, tamPob = 0, datos = Datos.Datos()):
		self.tamPob = tamPob
		self.datos = datos
		self.listaHorariosFinales = []
		
		for i in range(0, self.tamPob):
			self.listaHorariosFinales.append(HorarioFinal.HorarioFinal(datos = self.datos).inicializarHF())

	def ordenarFitness(self):
		self.listaHorariosFinales.sort(key = lambda x: x.getFitness(), reverse = True)

		return self