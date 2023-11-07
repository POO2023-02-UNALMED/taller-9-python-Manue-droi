from tkinter import *
from math import *
from tkinter import END, Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x260")



# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=55, padx=1, pady=1)


i = 0
operadores = 0

#A todo aquel que mire esto, lo encontre en un video de YouTube, pq la vdd, esta medio raro hacer eso (falta experiencia), se les quiere Oswaldo y David :')
#profe lo quiero, le puse 5 en la evaluación de docente, pa´ que me reciba el prox semestre :D

def obtenerNumeros(n):
    global i
    pantalla.insert(i, n)
    i+=1


def obtenerOperador(operador):
    global i
    global operadores
    if operadores == 0:
        pantalla.insert(i, operador)
        i+=1
        operadores+=1
    else:
        clear_pantalla()
        pantalla.insert(0, "ERROR")


def clear_pantalla():
    global i
    pantalla.delete(0, END)
    i = 0


def calcularOperacion():
    global i
    ecuacion = pantalla.get()

    if i!=0:
        try:
            result = str(eval(ecuacion))
            pantalla.delete(0, END)
            pantalla.insert(0, result)
            longitud = len(result)
            i = longitud
        
        except:
            result = "Error"
            pantalla.delete(0, END)
            pantalla.insert(0, result)
    else:
        pass


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda:obtenerNumeros(9)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command= lambda:calcularOperacion()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command= lambda:obtenerNumeros(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda:obtenerOperador("+")).grid(row=1, column=3, padx=2, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda:obtenerOperador("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda:obtenerOperador("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda:obtenerOperador("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
