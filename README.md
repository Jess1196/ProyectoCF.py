
[![](https://www.osi.es/sites/default/files/actualidad/blog/2018/image-3046639_960_720.png)](http://https://www.osi.es/sites/default/files/actualidad/blog/2018/image-3046639_960_720.png)
#Conversor de moneda a criptomoneda
### Editor utilizado
#####  Visual Studio Code 
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png)](http://https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png)
### Lenguaje utilizado
##### Python
[![](https://logos-marcas.com/wp-content/uploads/2021/10/Python-Logo.png)](http://https://logos-marcas.com/wp-content/uploads/2021/10/Python-Logo.png)
## Proceso de crear la interfaz gráfica para el coversión de moneda a criptomoneda
### Paso 1
##### Importé tkinter, ttk,messagebox y  Path
    from tkinter import *
    from tkinter import  ttk
    from tkinter import messagebox
    from pathlib import Path # Descargo Path de Pathlib para poder crear el archivo con los resultados del conversor
### Paso 1
##### Creé la parte visual del conversor dividiéndolo en dos secciones: moneda y conversión; en la sección de moneda diseñé una primera caja para tipificar el nombre dea moneda a convertir, porteriormente cree dos cajas más abajo; una para la crypto seleccionada y otra paraa agregar el valor de la moneda al cambio de la crypto elegida.
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
### Paso 3
##### Agregué algunas funciones extras, como:
##### Alerta si la persona ni rellena todas las cajas. Utilizada para advertir a la persona que el. Programa no funcionará si no está cumplimentado correctamente.
    def lock():
        if not Moneda_entry.get() or not Conversion_entry.get() or not rate_entry.get():
            messagebox.showwarning("¡DETENTE!", "No cumplimentaste todas las casillas")
            # Si la persona no cumplimenta las tres casillas no puede pasar a la sección de Conversión
### Paso 4
##### Botones de bloqueo y desbloqueo. Estos botones fueron creador para fijar los datos introducidos o desbloquearlos para cambiarlos.
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
    def unlock():
        # ENABLE ENTRY BOXES
        Moneda_entry.config(state="normal")
        Conversion_entry.config(state="normal")
        rate_entry.config(state="normal")
        # ENABLE TAB
        El_Recuadro.tab(1, state="disabled")
##### Para lograr esto utilicé if y else, utilizando como argumento que si los datos ni están cumplimentados y bloqueados con el botón de "bloqueo" en la pantalla, el usuario no puede acceder a la sección de conversión. 
### Paso 5
##### Definí una función para realizar la operación matemática y lograr el valor en crypto de la moneda seleccionada.
    def convert():
    
        converted_entry.delete(0, END)
    
        # Crear la operacion matematica para lograr la conversion
        Conversion = (float (rate_entry.get()) * float(amount_entry.get()))
    
        converted_entry.insert(0, Conversion)
## Funcionamiento del programa
##### 1.	Al correr el programa aparecerá el siguiente recuadro con de secciones;  la primera identificada como “Moneda” y la segunda como “Conversión”.
##### En la sección de Moneda la persona tipificará:
##### -	Moneda de conversión: USD, MEX, EUR,…
##### -	Cryptomoneda a convertir: BTC,ETH, XRP,…
##### -	Valor de la moneda al cambio de la cryptomoneda indicada.
##### Ejemplo:  
##### 1 Dólar son 0.000029 BTC
##### 1 Dólar son 0.00045 ETH.
##### 2.	Al agregar los datos anteriores se debe presionar en el botón de Lock o “Bloquear”, esto hará que los datos no se puedan editar y habilita la entrada a la sección de Conversión.
##### Si no se cumplimentan las tres casillas no se habilita la sección de Conversión y aparece una alerta avisando que hay un error.
##### 3.	Dentro de la sección de Conversión se debe agregar:
##### -	Cantidad de USD, MEX, EUR, … a convertir. 
##### Al agregarlo hay que dar clic e el botón de Convertir y en la casilla inferior saldrá la cantidad de criptomoneda equivalente.


