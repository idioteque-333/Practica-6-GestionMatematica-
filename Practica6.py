import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Elipse, Polygon
import numpy as np
import turtle

print ("1.- Figuras Geometricas")
print ("2.- Graficas")
print ("3.- Turtle")

Opcion = int(input("Ingrese el número correspondiente (1-3) "))

if Opcion == 1:
	S = "S"
	while S == "S":
		print ("1.- Rectángulo")
		print ("2.- Círculo")
		print ("3.- Elipse")
		print ("4.- Polígono")
		Opcion = int(input("Ingrese el número correspondiente (1-4) "))
		if Opcion == 1:
			fig, ax = plt.subplots(figsize=(6,6))
			rect = Rectangle((1, 1), 3, 2, facecolor='lightblue', edgecolor='black', linewidth=2, label='Rectángulo')
			ax.add_patch(rect)
			ax.set_xlim(0, 10)
			ax.set_ylim(0, 10)
			ax.set_aspect('equal')
			ax.grid(True)
			ax.legend(loc='lower left')
			plt.title('Figuras geométricas con Matplotlib')
			plt.show()
		elif Opcion == 2:
			fig, ax = plt.subplots(figsize=(6, 6))
			circ = Circle((6, 2), radius=1.5, facecolor='lightgreen', edgecolor='black', linewidth=2, label='Círculo')
			ax.add_patch(circ)
			ax.set_xlim(0, 10)
			ax.set_ylim(0, 10)
			ax.set_aspect('equal')
			ax.grid(True)
			ax.legend(loc='lower left')
			plt.title('Figuras geométricas con Matplotlib')
			plt.show()
		elif Opcion == 3:
			fig, ax = plt.subplots(figsize=(6, 6))
			elli = Ellipse((3, 6), width=4, height=2, facecolor='salmon', edgecolor='black', linewidth=2, label='Elipse')
			ax.add_patch(elli)
			ax.set_xlim(0, 10)
			ax.set_ylim(0, 10)
			ax.set_aspect('equal')
			ax.grid(True)
			ax.legend(loc='lower left')
			plt.title('Figuras geométricas con Matplotlib')
			plt.show()
		elif Opcion == 4:
			fig, ax = plt.subplots(figsize=(6, 6))
			triangulo = Polygon([[7, 5], [9, 5], [8, 8]], closed=True, facecolor='gold', edgecolor='black', linewidth=2, label='Triángulo')
			ax.add_patch(triangulo)
			ax.set_xlim(0, 10)
			ax.set_ylim(0, 10)
			ax.set_aspect('equal')
			ax.grid(True)
			ax.legend(loc='lower left')
			plt.title('Figuras geométricas con Matplotlib')
			plt.show()
		else:
			print ("Eliga una Opción Válida")
		C = input("¿Desea continuar viendo otra figura? (S / N) ")
elif Opcion == 2:
	S = "S"
	while S == "S"
		print ("Gráfica de Barras")
		print ("Gráfica de Ondas")
		print ("Gráfica de Pastel")
		print ("Gráfica Continua (Investigada)")
		Opcion = int(input("Ingrese el número correspondiente (1-4) "))
		if Opcion == 1:
