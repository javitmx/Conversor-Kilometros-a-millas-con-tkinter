import tkinter as tk
from tkinter import ttk


def convertir():
    try:
        km = float(entrada_km.get())
        millas = km * 0.621371
        etiqueta_resultado.config(
            text=f"{km} kilómetros equivalen a {millas:.2f} millas.")
    except ValueError:
        etiqueta_resultado.config(
            text="Por favor, introduce un número válido.")


def exit_app():
    ventana.destroy()


# Crear la ventana
ventana = tk.Tk()
ventana.title("Conversor de Kilómetros a Millas")
ventana.geometry("400x400")

# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
posicion_x = int((ventana.winfo_screenwidth() / 2) - (ancho_ventana / 2))
posicion_y = int((ventana.winfo_screenheight() / 2) - (alto_ventana / 2))
ventana.geometry(f"+{posicion_x}+{posicion_y}")

estilo = ttk.Style()
estilo.configure('TLabel', font=('Helvetica', 12))
estilo.configure('TButton', font=('Helvetica', 12), foreground='darkgreen',
                 background='#4CAF50')  # Cambia el color del botón

# Crear elementos de la interfaz
etiqueta_km = ttk.Label(ventana, text="Kilómetros:")
etiqueta_km.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entrada_km = ttk.Entry(ventana)
entrada_km.grid(row=0, column=1, padx=10, pady=5)

boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=0, columnspan=2,
                     padx=10, pady=5, sticky="we")

etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

exit_button = ttk.Button(ventana, text="Salir", command=exit_app)
exit_button.grid(row=3, column=0, columnspan=2,
                 padx=10, pady=5, sticky="we")

# Centrar los widgets en la ventana
for child in ventana.winfo_children():
    child.grid_configure(padx=40, pady=40)

# Ejecutar la ventana
ventana.mainloop()
