import tkinter as tk
import time
from datetime import date
from time import strftime
import calendar


ventana = tk.Tk()
ventana.title('Aplicación Multifuncional')
ventana.geometry('600x400')
ventana.configure(background='white') 


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label='Opciones', menu=submenu)


frame_reloj = tk.Frame(ventana, background='white')  
frame_reloj.pack_forget()  


frame_tareas = tk.Frame(ventana, background='white')
frame_tareas.pack_forget()  


frame_calculadora = tk.Frame(ventana, background='white')
frame_calculadora.pack_forget()  

def mostrar_reloj_con_calendario():
    frame_tareas.pack_forget()  
    frame_calculadora.pack_forget()  
    frame_reloj.pack(fill='both', expand=True)  
    
    def hora():
        tiempo = time.strftime('%H:%M:%S %p')
        hora_Actual.config(text=tiempo)
        frame_reloj.after(1000, hora)

    def fecha():
        hoy = date.today()
        fecha_formateada = hoy.strftime("%d/%m/%Y")
        
        dia = strftime('%A')
        dias_espanol = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miércoles',   
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo'
        }
        
        dia_espanol = dias_espanol.get(dia, dia)
        
        fecha_Actual.config(text=f"{dia_espanol}, {fecha_formateada}")
        
        mes_actual = hoy.month
        año_actual = hoy.year
        calendario_mensual = calendar.TextCalendar(calendar.SUNDAY).formatmonth(año_actual, mes_actual)
        
        dias_ingles = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        dias_espanol = ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa']
        for i in range(len(dias_ingles)):
            calendario_mensual = calendario_mensual.replace(dias_ingles[i], dias_espanol[i])
        
        meses_ingles = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        meses_espanol = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        mes_ingles = calendar.month_name[mes_actual]
        mes_espanol = dict(zip(meses_ingles, meses_espanol)).get(mes_ingles, mes_ingles)
        calendario_mensual = calendario_mensual.replace(mes_ingles, mes_espanol)
        
        calendario_Actual.config(text=calendario_mensual)
        
        boton_fecha.pack_forget()
        fecha_Actual.pack(anchor='center', pady=10)
        calendario_Actual.pack(anchor='center', pady=10)

    
    hora_Actual = tk.Label(frame_reloj, font=('Digital-7', 40, 'bold'), background='white', foreground='black')  # Texto negro
    hora_Actual.pack(anchor='center', pady=10)

    boton_fecha = tk.Button(frame_reloj, text='Ver Fecha', command=fecha, font=('Arial', 12, 'bold'), background='white', foreground='black')  # Botón con texto negro
    boton_fecha.pack(pady=10)

    fecha_Actual = tk.Label(frame_reloj, font=('Arial', 20, 'bold'), background='white', foreground='black')  # Texto negro
    fecha_Actual.pack_forget()

    calendario_Actual = tk.Label(frame_reloj, font=('Courier New', 10), background='white', foreground='black')  # Texto negro
    calendario_Actual.pack_forget()

    hora()

def mostrar_lista_tareas():
    frame_reloj.pack_forget()  
    frame_calculadora.pack_forget()  
    frame_tareas.pack(fill='both', expand=True)  
    
    ingreso_tarea = tk.Entry(frame_tareas, background='white', foreground='black')
    ingreso_tarea.pack()

    def agregar_tarea():
        tarea = ingreso_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
        ingreso_tarea.delete(0, tk.END)

    boton_agregar = tk.Button(frame_tareas, text='Agregar tarea', command=agregar_tarea, background='white', foreground='black')
    boton_agregar.pack(pady = 10)

    def eliminar_tarea():
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion)

    boton_eliminar = tk.Button(frame_tareas, text='Eliminar tarea', command=eliminar_tarea, background='white', foreground='black')
    boton_eliminar.pack(pady=10 )

    lista_tareas = tk.Listbox(frame_tareas, background='white', foreground='black')
    lista_tareas.pack(fill='both', padx = 50)


def mostrar_calculadora():
    frame_reloj.pack_forget()  
    frame_tareas.pack_forget()  
    frame_calculadora.pack(fill='both', expand=True) 

    
    tx1 = tk.Entry(frame_calculadora, font=("Calibri 20"), background="white", foreground="black")
    tx1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    
    i = 0

    
    def click(valor):
        nonlocal i
        tx1.insert(i, valor)
        i += 1

    
    def borrar():
        nonlocal i
        tx1.delete(0, tk.END)
        i = 0

    
    def operaciones():
        pedido = tx1.get()
        resultado = eval(pedido)
        tx1.delete(0, tk.END)
        tx1.insert(0, resultado)
        i = 0

    
    B1 = tk.Button(frame_calculadora, text="1", width=5, height=2, background="white", foreground="black", command=lambda: click(1))
    B2 = tk.Button(frame_calculadora, text="2", width=5, height=2, background="white", foreground="black", command=lambda: click(2))
    B3 = tk.Button(frame_calculadora, text="3", width=5, height=2, background="white", foreground="black", command=lambda: click(3))
    B4 = tk.Button(frame_calculadora, text="4", width=5, height=2, background="white", foreground="black", command=lambda: click(4))
    B5 = tk.Button(frame_calculadora, text="5", width=5, height=2, background="white", foreground="black", command=lambda: click(5))
    B6 = tk.Button(frame_calculadora, text="6", width=5, height=2, background="white", foreground="black", command=lambda: click(6))
    B7 = tk.Button(frame_calculadora, text="7", width=5, height=2, background="white", foreground="black", command=lambda: click(7))
    B8 = tk.Button(frame_calculadora, text="8", width=5, height=2, background="white", foreground="black", command=lambda: click(8))
    B9 = tk.Button(frame_calculadora, text="9", width=5, height=2, background="white", foreground="black", command=lambda: click(9))
    B0 = tk.Button(frame_calculadora, text="0", width=5, height=2, background="white", foreground="black", command=lambda: click(0))

    Bborrar = tk.Button(frame_calculadora, text="AC", width=5, height=2, background="white", foreground="black", command=borrar)
    Bparentesis1 = tk.Button(frame_calculadora, text="(", width=5, height=2, background="white", foreground="black", command=lambda: click("("))
    Bparentesis2 = tk.Button(frame_calculadora, text=")", width=5, height=2, background="white", foreground="black", command=lambda: click(")"))
    Bpunto = tk.Button(frame_calculadora, text=".", width=5, height=2, background="white", foreground="black", command=lambda: click("."))

    Bdiv = tk.Button(frame_calculadora, text="/", width=5, height=2, background="white", foreground="black", command=lambda: click("/"))
    Bmulti = tk.Button(frame_calculadora, text="*", width=5, height=2, background="white", foreground="black", command=lambda: click("*"))
    Bsuma = tk.Button(frame_calculadora, text="+", width=5, height=2, background="white", foreground="black", command=lambda: click("+"))
    Bresta = tk.Button(frame_calculadora, text="-", width=5, height=2, background="white", foreground="black", command=lambda: click("-"))
    Bigual = tk.Button(frame_calculadora, text="=", width=5, height=2, background="white", foreground="black", command=operaciones)

    
    Bborrar.grid(row=1, column=0, padx=5, pady=5)
    Bparentesis1.grid(row=1, column=1, padx=5, pady=5)
    Bparentesis2.grid(row=1, column=2, padx=5, pady=5)
    Bsuma.grid(row=1, column=3, padx=5, pady=5)

    B1.grid(row=2, column=0, padx=5, pady=5)
    B2.grid(row=2, column=1, padx=5, pady=5)
    B3.grid(row=2, column=2, padx=5, pady=5)
    Bresta.grid(row=2, column=3, padx=5, pady=5)

    B4.grid(row=3, column=0, padx=5, pady=5)
    B5.grid(row=3, column=1, padx=5, pady=5)
    B6.grid(row=3, column=2, padx=5, pady=5)
    Bmulti.grid(row=3, column=3, padx=5, pady=5)

    B7.grid(row=4, column=0, padx=5, pady=5)
    B8.grid(row=4, column=1, padx=5, pady=5)
    B9.grid(row=4, column=2, padx=5, pady=5)
    Bdiv.grid(row=4, column=3, padx=5, pady=5)

    B0.grid(row=5, column=1, padx=5, pady=5)
    Bpunto.grid(row=5, column=2, padx=5, pady=5)
    Bigual.grid(row=5, column=3, padx=5, pady=5)


submenu.add_command(label='Reloj con calendario', command=mostrar_reloj_con_calendario)
submenu.add_command(label='Lista de tareas', command=mostrar_lista_tareas)
submenu.add_command(label='Calculadora', command=mostrar_calculadora)
submenu.add_command(label= 'Block de notas')


ventana.mainloop()