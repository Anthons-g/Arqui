import tkinter as tk
def saludar():
    nombre = entradanombre.get() 
    if nombre.strip() == "":
        resultado.config(text="Por favor, Pon un Nombre para saludartexd",fg= "red") 
    elif any(char.isdigit() for char in nombre):
        resultado.config(text="El nombre no debe contener números.", fg="red")
    else:
        resultado.config(text=f"Holaaa, {nombre}! Qué gusto, saludos :D", fg="blue") #
        botonsaludo.config(state="disabled") 
        botoncerrar.pack(pady=10)
ventana = tk.Tk()
ventana.title("Ventana de saludos compas")
ventana.geometry("350x350") 

Etiquetapregunta = tk.Label(ventana, text="Holaaas, ¿como te llamas :)?", font=("Arial", 12))
Etiquetapregunta.pack(pady=10)

entradanombre = tk.Entry(ventana, font=("Arial", 12))
entradanombre.pack()

botonsaludo = tk.Button(ventana, text="Saludar", command=saludar)
botonsaludo.pack(pady=5) 

resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

botoncerrar = tk.Button(ventana, text="Cerrar", font=("Arial", 11), command=ventana.destroy)


ventana.mainloop()