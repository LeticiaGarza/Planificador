import Datos
import AlgoritmoGenetico
import Poblacion

tamPoblacion = 9
ratioMutacion = 0.1
ratioCruza = 0.9
tamRuleta = 3
numHFElite = 1

datos = Datos.Datos()

def main():
	numGeneracion = 1

	datos.inicializarDatos()

	print "Cursos disponibles:"
	
	for i in datos.listaCursos:
		print "Nombre: " + i.nombreCurso + ", Grupos:"
		
		for j in i.listaGrupos:
			print j.nombreGrupo
		
	print "\nGrupos disponibles:"

	for i in datos.listaGrupos:
		print "Grupo #: " + i.IDGrupo + ", Nombre: " + i.nombreGrupo + ", Max # de estudiantes: " + str(i.maxNumEst)
		print "Maestros:"
		
		for j in i.listaMaestros:
			print j.nombreMaestro

	print "\nSalones disponibles:"

	for i in datos.listaSalones:
		print "Salon #: " + i.IDSalon + ", Capacidad: " + str(i.capacidad)

	print "\nMaestros disponibles:"

	for i in datos.listaMaestros:
		print "ID: " + i.IDMaestro + ", Nombre: " + i.nombreMaestro

	print "\nHorarios disponibles:"

	for i in datos.listaHorarios:
		print "ID: " + i.IDHorario + ", Horario: " + i.momento

	print "-----------------------------------------------------------------"
	print "-----------------------------------------------------------------"

	print "\nGeneracion: ", numGeneracion
	print "						Clases [curso,grupo,salon,maestro,horario]							      | F  |C"
	print "---------------------------------------------------------------------------------------------------------------------------------------------------------------"

	ag = AlgoritmoGenetico.AlgoritmoGenetico(datos = datos)
	poblacion = Poblacion.Poblacion(tamPob = tamPoblacion, datos = datos).ordenarFitness()

	for i in poblacion.listaHorariosFinales:
		print i.retornarIndividuo() + "|" + i.getFitness() + "|" + str(i.numConflictos)

	while poblacion.listaHorariosFinales[0].getFitness() != "1.00":
		numGeneracion += 1
		print "\nGeneracion: ", numGeneracion
		print "						Clases [curso,grupo,salon,maestro,horario]							      | F  |C"
		print "---------------------------------------------------------------------------------------------------------------------------------------------------------------"
		poblacion = ag.evolucionar(poblacion = poblacion).ordenarFitness()

		for i in poblacion.listaHorariosFinales:
			print i.retornarIndividuo() + "|" + i.getFitness() + "|" + str(i.numConflictos)

	print "\nHorario generado:\n"
	if poblacion.listaHorariosFinales[0].getFitness() == "1.00":
		for i in poblacion.listaHorariosFinales[0].getClases():
			print i.curso.nombreCurso + "	" + i.grupo.IDGrupo + "," + str(i.grupo.maxNumEst) + "	" + i.salon.IDSalon + "," + str(i.salon.capacidad) + "	" \
			+ i.maestro.IDMaestro + "," + i.maestro.nombreMaestro + "		" + i.horario.IDHorario + "," + i.horario.momento
	
if __name__ == '__main__':
	main()