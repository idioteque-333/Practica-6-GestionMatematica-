import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Polygon
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
		print ("5.- Todas")
		Opcion = int(input("Ingrese el número correspondiente (1-5) "))
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
		elif Opcion == 5:
			fig, ax = plt.subplots(figsize=(6, 6))
			rect = Rectangle((1, 1), 3, 2, facecolor='lightblue', edgecolor='black', linewidth=2, label='Rectángulo')
			ax.add_patch(rect)
			circ = Circle((6, 2), radius=1.5, facecolor='lightgreen', edgecolor='black', linewidth=2, label='Círculo')
			ax.add_patch(circ)
			elli = Ellipse((3, 6), width=4, height=2, facecolor='salmon', edgecolor='black', linewidth=2, label='Elipse')
			ax.add_patch(elli)
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
		S = input("¿Desea continuar viendo otra figura? (S / N) ")
elif Opcion == 2:
	S = "S"
	while S == "S":
		print ("1.- Gráfica de Barras")
		print ("2.- Gráfica de Ondas")
		print ("3.- Gráfica de Pastel")
		print ("4.- Gráfica Continua (Investigada)")
		Opcion = int(input("Ingrese el número correspondiente (1-4) "))
		if Opcion == 1:
			categorias = ['Manzanas', 'Plátanos', 'Cerezas', 'Dátiles']
			ventas = [400, 350, 300, 450]
			plt.bar(categorias, ventas, color='skyblue', edgecolor='black')
			plt.title('Venta de Frutas')
			plt.xlabel('Frutas')
			plt.ylabel('Cantidad')
			plt.grid(axis='y', linestyle='--', alpha=0.7)
			plt.show()
		elif Opcion == 2:
			categorias = ['Manzanas', 'Plátanos', 'Cerezas', 'Dátiles']
			ventas = [400, 350, 300, 450]
			x = np.linspace(0, 10, 100)
			y = np.sin(x)
			plt.plot(x, y, label='seno(x)', color='blue', linewidth=2)
			plt.title('Gráfica de una función seno')
			plt.xlabel('Eje X')
			plt.ylabel('Eje Y')
			plt.grid(True)
			plt.legend()
			plt.show()
		elif Opcion == 3:
			etiquetas = ['Manzanas', 'Plátanos', 'Cerezas', 'Dátiles']
			tamanios = [30, 25, 20, 25]
			plt.pie(tamanios, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
			plt.title('Distribución de Venta de Frutas')
			plt.axis('equal')
			plt.show()
		elif Opcion == 4:
			x = np.linspace(0, 10, 100)
			y = np.sin(x)
			plt.figure(figsize=(8, 4))
			plt.plot(x, y, label = 'sin (x)', color = 'blue', linewidth = 2)
			plt.title ('Grafica Continua Hecha por Oscar :b')
			plt.xlabel ('Eje X')
			plt.ylabel ('Eje Y')
			plt.grid (True)
			plt.legend()
			plt.show()
		else:
			print ("Eliga una Opcion Valida")
		S = input("Quiere imprimir otra grafica? (S / N) ")
elif Opcion == 3:
	S = "S"
	while S == "S":
		print ("1.- Cuadrado")
		print ("2.- Estrella")
		Opcion = int(input("Ingrese el numero correspondiente (1-2) "))
		t = turtle.Turtle()
		t.speed(3)
		if Opcion == 1:
			for i in range(4):
				t.forward(100)
				t.right(90)
		elif Opcion == 2:
			t.begin_fill()
			for i in range(5):
				t.forward(100)
				t.right(144)
				t.end_fill()
		else:
			print ("Eliga Una Opcion Valida")
		S = input("Desea ilustrar otra figura (S / N) ")
