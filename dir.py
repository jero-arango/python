import os
with open("a.txt", encoding="utf-8") as archivo:
	for i in archivo:
		print(i)
		name=i.rstrip(i[-2])
		name2=name[:-1]
		os.mkdir(name2)
		os.chdir(name2)
		os.mkdir('1.evidencias_de_aprendizaje')
		os.mkdir('2.sanciones_e_indiciplinas')
		os.mkdir('3.plan_concertado')
		os.mkdir('4.material_de_estudio')
		os.mkdir('5.planes_de_mejoramiento')
		os.chdir("C:\\Users\\302\\yo")