from tkinter import Tk, Button, Label, Entry

# Variables globales
cifra1 = ""
cifra2 = ""
operacion = ""


# Funciones de botones de operaciones
def suma_funcion():
    global cifra1
    global cifra2
    global operacion
    operacion = "suma"
    cifra2 = pantalla_box.get()
    cifra1 = ""
    pantalla_box.delete(0, "end")

def resta_funcion():
    global cifra1
    global cifra2
    global operacion
    operacion = "resta"
    cifra2 = pantalla_box.get()
    cifra1 = ""
    pantalla_box.delete(0, "end")

def multiplicacion_funcion():
    global cifra1
    global cifra2
    global operacion
    operacion = "multiplicacion"
    cifra2 = pantalla_box.get()
    cifra1 = ""
    pantalla_box.delete(0, "end")

def division_funcion():
    global cifra1
    global cifra2
    global operacion
    operacion = "division"
    cifra2 = pantalla_box.get()
    cifra1 = ""
    pantalla_box.delete(0, "end")

def borrar_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    str_rest = len(cifra1) - 1
    pantalla_box.delete(str_rest, "end")
    cifra1 = pantalla_box.get()

def borrar_pantalla_funcion():
    pantalla_box.delete(0, "end")

def borrar_todo_funcion():
    global cifra1
    global cifra2
    cifra2 = ""
    cifra1 = ""
    pantalla_box.delete(0, "end")

def porcentaje_funcion(): ## Sin programar
    global cifra1
    global cifra2
    global operacion
    if operacion == "multiplicacion":
        total = float(cifra1) / float(cifra2)
        pantalla_box.delete(0, "end")
        pantalla_box.insert(0, total)

def inverso_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 = 1 / float(cifra1)
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def cuadrado_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 = float(cifra1) * float(cifra1)
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def raiz_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 = float(cifra1) ** 0.5
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def cambio_signo_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 = float(cifra1)
    cifra1 = 0 - cifra1
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def resultado_funcion():
    global cifra1
    global cifra2
    global operacion
    if operacion == "suma":
        total = float(cifra2) + float(cifra1)
        pantalla_box.delete(0, "end")
        pantalla_box.insert(0, total)
    if operacion == "resta":
        total = float(cifra2) - float(cifra1)
        pantalla_box.delete(0, "end")
        pantalla_box.insert(0, total)
    if operacion == "multiplicacion":
        total = float(cifra2) * float(cifra1)
        pantalla_box.delete(0, "end")
        pantalla_box.insert(0, total)
    if operacion == "division":
        total = float(cifra2) / float(cifra1)
        pantalla_box.delete(0, "end")
        pantalla_box.insert(0, total)


# Funciones de botones numericos
def n1_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "1"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0,cifra1)

def n2_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "2"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n3_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "3"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n4_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "4"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n5_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "5"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n6_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "6"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n7_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "7"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n8_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "8"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n9_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "9"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def n0_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "0"
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

def punto_funcion():
    global cifra1
    cifra1 = pantalla_box.get()
    cifra1 += "."
    pantalla_box.delete(0, "end")
    pantalla_box.insert(0, cifra1)

# Declaracion de la ventana
ventana = Tk()
ventana.geometry("185x280")
ventana.title("Calculadora")


# Botones de comandos
suma_boton = Button(ventana, text="+", bg="blue", fg="white", command=suma_funcion)
suma_boton.place(x=140, y=210, width=40, heigh=30)

resta_boton = Button(ventana, text="-", bg="blue", fg="white", command=resta_funcion)
resta_boton.place(x=140, y=175, width=40, heigh=30)

multiplicacion_boton = Button(ventana, text="X", bg="blue", fg="white", command=multiplicacion_funcion)
multiplicacion_boton.place(x=140, y=140, width=40, heigh=30)

division_boton = Button(ventana, text="/", bg="blue", fg="white", command=division_funcion)
division_boton.place(x=140, y=105, width=40, heigh=30)

igual_boton = Button(ventana, text="=", bg="green", fg="white", command=resultado_funcion)
igual_boton.place(x=140, y=245, width=40, heigh=30)

borrar_boton = Button(ventana, text="Back", bg="red", fg="white", command=borrar_funcion)
borrar_boton.place(x=140, y=70, width=40, heigh=30)

cambio_signo_boton = Button(ventana, text="+/-", bg="black", fg="white", command=cambio_signo_funcion)
cambio_signo_boton.place(x=5, y=245, width=40, heigh=30)

porcentaje_boton = Button(ventana, text="%", bg="gray", fg="white", command=porcentaje_funcion)
porcentaje_boton.place(x=5, y=70, width=40, heigh=30)

borrar_todo_boton = Button(ventana, text="CE", bg="red", fg="white", command=borrar_todo_funcion)
borrar_todo_boton.place(x=50, y=70, width=40, heigh=30)

borrar_pantalla_boton = Button(ventana, text="C", bg="red", fg="white", command=borrar_pantalla_funcion)
borrar_pantalla_boton.place(x=95, y=70, width=40, heigh=30)

inverso_boton = Button(ventana, text="1/x", bg="gray", fg="white", command=inverso_funcion)
inverso_boton.place(x=5, y=105, width=40, heigh=30)

cuadrado_boton = Button(ventana, text="sqr.", bg="gray", fg="white", command=cuadrado_funcion)
cuadrado_boton.place(x=50, y=105, width=40, heigh=30)

raiz_boton = Button(ventana, text="root", bg="gray", fg="white", command=raiz_funcion)
raiz_boton.place(x=95, y=105, width=40, heigh=30)


# Botones de numeros
numero_0 = Button(ventana, text="0", bg="black", fg="white", command=n0_funcion)
numero_0.place(x=50, y=245, width=40, heigh=30)

numero_1 = Button(ventana, text="1", bg="black", fg="white", command=n1_funcion)
numero_1.place(x=5, y=210, width=40, heigh=30)

numero_2 = Button(ventana, text="2", bg="black", fg="white", command=n2_funcion)
numero_2.place(x=50, y=210, width=40, heigh=30)

numero_3 = Button(ventana, text="3", bg="black", fg="white", command=n3_funcion)
numero_3.place(x=95, y=210, width=40, heigh=30)

numero_4 = Button(ventana, text="4", bg="black", fg="white", command=n4_funcion)
numero_4.place(x=5, y=175, width=40, heigh=30)

numero_5 = Button(ventana, text="5", bg="black", fg="white", command=n5_funcion)
numero_5.place(x=50, y=175, width=40, heigh=30)

numero_6 = Button(ventana, text="6", bg="black", fg="white", command=n6_funcion)
numero_6.place(x=95, y=175, width=40, heigh=30)

numero_7 = Button(ventana, text="7", bg="black", fg="white", command=n7_funcion)
numero_7.place(x=5, y=140, width=40, heigh=30)

numero_8 = Button(ventana, text="8", bg="black", fg="white", command=n8_funcion)
numero_8.place(x=50, y=140, width=40, heigh=30)

numero_9 = Button(ventana, text="9", bg="black", fg="white", command=n9_funcion)
numero_9.place(x=95, y=140, width=40, heigh=30)

punto_boton = Button(ventana, text=".", bg="black", fg="white", command=punto_funcion)
punto_boton.place(x=95, y=245, width=40, heigh=30)

# TextBox
pantalla_box = Entry(ventana, bg="white", fg="black")
pantalla_box.place(x=5, y=5, width=175, heigh=60)

ventana.mainloop()
