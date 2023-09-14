import os
import tkinter as tk
from tkinter import filedialog

def listar_archivos_y_carpetas(path, archivo_salida, nivel=0):
  
    #si es archivo escribe le nombre en el archivo salida
    
    if os.path.isfile(path):
        archivo_salida.write("   "*nivel+os.path.basename(path) + '\n')
      
    elif os.path.isdir(path):
        archivo_salida.write("   "*nivel+ os.path.basename(path) + '/' + '\n')
        elementos = os.listdir(path) # lista de todos los elementos
        for elemento in elementos:
            elemento_path = os.path.join(path, elemento)
            listar_archivos_y_carpetas(elemento_path, archivo_salida,nivel+1)

def guardar_arbol_en_archivo(ruta, archivo_salida):
    
    with open(archivo_salida, 'w') as archivo:
        arbol = listar_archivos_y_carpetas(ruta, archivo)
  
    print(f"Los datos se han guardado en '{archivo_salida}'.")



# Poner la ruta y el archivo de salida
ruta = 'venv'
archivo_salida=input("Nombre del archivo:")
#archivo_salida = 'arbol.txt'
"""
def seleccionar_carpeta():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    # Abre el explorador de archivos para seleccionar una carpeta
    carpeta_seleccionada = filedialog.askdirectory()
    # Verificar si el usuario seleccionó una carpeta
    if carpeta_seleccionada:
        return carpeta_seleccionada
    else:
        return None

# Carpeta para el path y llamada a funcion 
carpeta = seleccionar_carpeta()
if carpeta:
    print("Carpeta seleccionada:", carpeta)
else:
    print("No se seleccionó ninguna carpeta.")

"""
guardar_arbol_en_archivo(ruta, archivo_salida)