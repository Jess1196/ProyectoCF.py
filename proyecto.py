from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from pathlib import Path # Descargo Path de Pathlib para poder crear el archivo con los resultados del conversor


#Agrego medidad y titulo de la inerfaz grafica  asi como el cuadro de la moneda 
root = Tk()
root.title("CONOCE EL VALOR DE TU MONEDA EN CRYPTO")
root.geometry("500x500")

El_Recuadro = ttk.Notebook(root)
El_Recuadro.pack(pady= 5)

Cuadro_de_Moneda= Frame(El_Recuadro, width=480, height=480)
Cuadro_de_Conversion= Frame(El_Recuadro, width=480, height=480)

Cuadro_de_Moneda.pack(fill="both", expand=1)
Cuadro_de_Conversion.pack(fill="both", expand=1)

El_Recuadro.add(Cuadro_de_Moneda, text="Moneda")
El_Recuadro.add(Cuadro_de_Conversion, text="Conversión")

El_Recuadro.tab(1, state="disabled")

## Defino funcion que bloquea las casillas de Moneda despues de que las tres casillas esten cumplimentadas por la moneda, la crytomoneda y el valor d la moneda en a crypto indicada

def lock():
    if not Moneda_entry.get() or not Conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("¡DETENTE!", "No cumplimentaste todas las casillas")
        # Si la persona no cumplimenta las tres casillas no puede pasar a la sección de Conversion
    else:
        # DISABLED ENTRY BOXES
        Moneda_entry.config(state="disabled")
        Conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        # ENABLE TAB
        El_Recuadro.tab(1, state="normal")
        # Creo etiquetas para que al rellenar las dos primeras casillas la moneda y cryto indicada se vean en la seccion de Conversion. 
        amount_label.config(text=f"Cantidad de {Moneda_entry.get()} ha convertir a {Conversion_entry.get()}")
        converted_label.config(text=f"Iguales a {Conversion_entry.get()}")
        amount_entry.config(text=f"Convertido {Moneda_entry.get()}")
        
#Defino funcion que desbloquea las casillas en moneda para poder editar los datos
def unlock():
    # ENABLE ENTRY BOXES
    Moneda_entry.config(state="normal")
    Conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    # ENABLE TAB
    El_Recuadro.tab(1, state="disabled")
    
# Creo primer recuadro donde va el nombre de la moneda seleccionada
Moneda = LabelFrame(Cuadro_de_Moneda, text="Indica la moneda de conversión")
Moneda.pack(pady=20)

Moneda_entry = Entry(Moneda, font=("Helvetica", 24))
Moneda_entry.pack(pady=10, padx=10)

# Creo segundo recuadro donde ira la franja para añadir el nombre de la cryto y el valor de la moneda al cambio
Conversion = LabelFrame(Cuadro_de_Moneda, text= "Crytomoneda a convertir")
Conversion.pack(pady=20)

Conversion_label = Label(Conversion, text= "Indica la cryptomoneda")
Conversion_label.pack(pady=10)

#Entrada  para que en este recuadro la persona escria el nmbre de la crytomoneda deseada
Conversion_entry = Entry(Conversion, font=("Helvetica", 24)) #Fuente y tamaño del texto al escribir en la franja 
Conversion_entry.pack(pady=10, padx=10)

# Etiqueta para indicar el valor de la moneda contra la cryto seleccionada 
rate_label = Label(Conversion, text= "Valor actual de la moneda en la crypto indicada" )
rate_label.pack(pady=10)

rate_entry = Entry(Conversion, font=("Helvetica", 24)) #Fuente y tamaño del texto al escribir en la franja 
rate_entry.pack(pady=10, padx=10)


#Button frame
button_frame = Frame(Cuadro_de_Moneda)
button_frame.pack(pady=20)

#Diseño de los botones de bloqueo y desbloqueo

Lock_button = Button(button_frame, text = "Bloquear", command=lock)
Lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text= "Desbloquear", command= unlock)
unlock_button.grid(row=0, column=1, padx = 10)


# ETAPA DE CONVERSION

def convert():
    
    converted_entry.delete(0, END)
    
    # Crear la operacion matematica para lograr la conversion
    Conversion = (float (rate_entry.get()) * float(amount_entry.get()))
    
    converted_entry.insert(0, Conversion)
    with open("Resultado.txt", "w") as archivo:
        archivo.write(str(Conversion))
        archivo.close
    
    
def clear(): # Declaro funcion para que el boton de limpiar borre todo lo escirto en la seccion de "Conversion"
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(Cuadro_de_Conversion, text ="Cantidad a convertir")
amount_label.pack(pady=20)

#Entrada para la caja de cantidad
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

#Convetir button
convert_button = Button(amount_label, text ="Convertir", command=convert)
convert_button.pack(pady=20)

#EQUALS FRAME
converted_label = LabelFrame(Cuadro_de_Conversion, text="Moneda convertida")
converted_label.pack(pady=20)

converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="white")
converted_entry.pack(pady=10, padx=10)

#Clear button
clear_button = Button(Cuadro_de_Conversion, text="Limpiar", command=clear)
clear_button.pack(pady=20)

root.mainloop()

""" with open("Resultado.txt", "w") as archivo:
    resultado_proyecto= (str(rate_entry.get()) + "dolares" + (str(convert)))
    print(resultado_proyecto)
    archivo.write(resultado_proyecto)
    archivo.close"""

"""Conversion = (float (rate_entry.get())) * (float(amount_entry.get()))
resultado_proyecto= (str(rate_entry.get()) + "dolares" + (str(Conversion) + amount_entry))
registro_resultado= open("Resultado.txt", "w")
print(resultado_proyecto)
datos_resultado = resultado_proyecto +"\n"
registro_resultado.write((datos_resultado))
registro_resultado.close"""