import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # Necesitamos Pillow para trabajar con imágenes

# Generar un número aleatorio del 1 al 25
numAL = random.randint(1, 25)
intentos = 5

# Función para procesar el intento del usuario
def verificar_numero():
    global intentos
    try:
        participante = int(entry.get())
        if participante < 1 or participante > 25:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un número entre 1 y 25.")
            return
        if participante == numAL:
            messagebox.showinfo("¡Felicidades!", "¡Has adivinado el número!")
            root.destroy()
        else:
            intentos -= 1
            if intentos > 0:
                label_intentos.config(text=f"Intentos restantes: {intentos}")
                messagebox.showinfo("Incorrecto", f"Ese no es el número correcto. Te quedan {intentos} intento(s).")
            else:
                messagebox.showinfo("Juego terminado", f"Lo siento, no has adivinado. El número era {numAL}.")
                root.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Adivinanza")

# Establecer el tamaño inicial de la ventana
root.geometry("900x980")

# Cargar la imagen de fondo
background_image = Image.open("fondo.png")  # Asegúrate de tener la imagen 'fondo.jpg' en el mismo directorio
background_image = background_image.resize((1024, 1024), Image.Resampling.LANCZOS)
# Redimensionar la imagen
bg = ImageTk.PhotoImage(background_image)

# Crear un label para colocar la imagen de fondo
label_background = tk.Label(root, image=bg)
label_background.place(relwidth=1, relheight=1)  # Coloca la imagen para que ocupe toda la ventana

# Configurar elementos de la interfaz
label_title = tk.Label(root, text="Adivina un número entre 1 y 25", font=("Arial", 18))
label_title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), width=10)
entry.pack(pady=10)

button_verificar = tk.Button(root, text="Intentar", command=verificar_numero, font=("Arial", 14))
button_verificar.pack(pady=20)

label_intentos = tk.Label(root, text=f"Intentos restantes: {intentos}", font=("Arial", 16))
label_intentos.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()


