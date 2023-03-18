frutas = {'Plátano':800, 'Manzana':1000, 'Pera':1000, 'Naranja':2000, 'Granadilla':1200, 'Mamonsillo':3000, 'Limon':400,'Uchua':100 }
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")