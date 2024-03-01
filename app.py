import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0 
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        while True:
            numero = prompt("prompt", "Ingrese un numero")
            numero = float(numero)
            suma_positivos += (numero + (numero > 0))
            suma_negativos += (numero + (numero < 0))
            cantidad_positivos += (numero + (numero > 0))
            cantidad_negativos += (numero + (numero < 0))
            cantidad_ceros += (numero == 0)

            if numero == "Cancelar":
                break

            diferencia = cantidad_positivos - cantidad_negativos

            mensaje = f"Suma acumulada de los negativos: {suma_negativos}\n"
            mensaje += f"Suma acumulada de los positivos: {suma_positivos}\n"
            mensaje += f"Cantidad de números positivos ingresados: {cantidad_positivos}\n"
            mensaje += f"Cantidad de números negativos ingresados: {cantidad_negativos}\n"
            mensaje += f"Cantidad de ceros ingresados: {cantidad_ceros}\n"
            mensaje += f"Diferencia entre la cantidad de números positivos y negativos: {diferencia}"

            alert(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()