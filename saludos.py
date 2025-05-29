import tkinter as tk
import os
def saludar():
    nombre = entradanombre.get() #se llama cuando haces click en saludar
    temp=10
    if nombre.strip() == "":
        resultado.config(text="Por favor, Pon un Nombre para saludartexd",fg= "red") # si no pusistes nombre salgra un mensaje para que pongas el nombre
    elif any(char.isdigit() for char in nombre):
        resultado.config(text="El nombre no debe contener números.", fg="red")
    else:
        resultado.config(text=f"Holaaa, {nombre}! Qué gusto, saludos :D", fg="blue") #
        botonsaludo.config(state="disable") #este lo que hace es desactivar el boton saludar
        botoncerrar.pack(pady=10) #muestra el boton cerrar
def mensajesaludo():
    resultado.config(text="jordan es mio")
#crwcion de la ventana con tkinter
ventana = tk.Tk()
ventana.title("Ventana de saludos compas")# nombre de la ventana 
ventana.geometry("350x350") # el tamaño con el que salgra la ventana 

#aqui es donde se muestra la primer tiqueta que seria la primer etiqueta
Etiquetapregunta = tk.Label(ventana, text="Holaaas, ¿como te llamas :)?", font=("Arial", 12))
Etiquetapregunta.pack(pady=10)

# Entrada-nombre
entradanombre = tk.Entry(ventana, font=("Arial", 12))# comando que crea la caja de texto y vendo estara(ventana), tipo de letra
entradanombre.pack()

# Botón saludo
botonsaludo = tk.Button(ventana, text="Saludar", font=("Arial", 11), command=saludar)
botonsaludo.pack(pady=5) 

botonsaludooos = tk.Button(ventana, text="jordan meco", font=("Arial", 11), command=mensajesaludo)
botonsaludooos.pack(pady=5)
# Etiqueta que sale cuando no pones nombre 
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

#boton cerrar
botoncerrar = tk.Button(ventana, text="Cerrar", font=("Arial", 11), command=ventana.destroy)

#inicio mantiene la ventana abierta y si se da el destroy la cierra
ventana.mainloop()
