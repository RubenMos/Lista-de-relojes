import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

frame_temporizador = tk.Frame(ventana, background='white')
frame_temporizador.pack_forget()

frame_notas = tk.Frame(ventana, background='white')
frame_notas.pack_forget()

def mostrar_frame(frame):
    frame_reloj.pack_forget()
    frame_tareas.pack_forget()
    frame_calculadora.pack_forget()
    frame_temporizador.pack_forget()
    frame_notas.pack_forget()
    frame.pack(fill='both', expand=True)

def mostrar_reloj_con_calendario():
    mostrar_frame(frame_reloj)

    if not hasattr(mostrar_reloj_con_calendario, 'inicializado'):
        
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

        hora_Actual = tk.Label(frame_reloj, font=('Digital-7', 40, 'bold'), background='white', foreground='black')
        hora_Actual.pack(anchor='center', pady=10)

        boton_fecha = tk.Button(frame_reloj, text='Ver Fecha', command=fecha, font=('Arial', 12, 'bold'), background='white', foreground='black')
        boton_fecha.pack(pady=10)

        fecha_Actual = tk.Label(frame_reloj, font=('Arial', 20, 'bold'), background='white', foreground='black')
        fecha_Actual.pack_forget()

        calendario_Actual = tk.Label(frame_reloj, font=('Courier New', 10), background='white', foreground='black')
        calendario_Actual.pack_forget()

        hora()

        
        mostrar_reloj_con_calendario.inicializado = True
    else:
        
        hora()


def mostrar_lista_tareas():
    mostrar_frame(frame_tareas)

    if not hasattr(mostrar_lista_tareas, 'inicializado'):
        
        ingreso_tarea = tk.Entry(frame_tareas, background='white', foreground='black')
        ingreso_tarea.pack()

        def agregar_tarea():
            tarea = ingreso_tarea.get()
            if tarea:
                lista_tareas.insert(tk.END, tarea)
            ingreso_tarea.delete(0, tk.END)

        boton_agregar = tk.Button(frame_tareas, text='Agregar tarea', command=agregar_tarea, background='white', foreground='black')
        boton_agregar.pack(pady=10)

        def eliminar_tarea():
            seleccion = lista_tareas.curselection()
            if seleccion:
                lista_tareas.delete(seleccion)

        boton_eliminar = tk.Button(frame_tareas, text='Eliminar tarea', command=eliminar_tarea, background='white', foreground='black')
        boton_eliminar.pack(pady=10)

        lista_tareas = tk.Listbox(frame_tareas, background='white', foreground='black')
        lista_tareas.pack(fill='both', padx=50)

        
        mostrar_lista_tareas.inicializado = True

def mostrar_calculadora():
    mostrar_frame(frame_calculadora)

    if not hasattr(mostrar_calculadora, 'inicializado'):
        
        class HoverButton(tk.Button):
            def __init__(self, master, **kw):
                tk.Button.__init__(self, master=master, **kw)
                self.defaultBackground = self["background"]
                self.bind("<Enter>", self.on_enter)
                self.bind("<Leave>", self.on_leave)

            def on_enter(self, e):
                self["background"] = self["activebackground"]

            def on_leave(self, e):
                self["background"] = self.defaultBackground

        def obtener(dato):
            resultado.insert(tk.END, dato)

        def operacion():
            try:
                ecuacion = resultado.get()
                result = str(eval(ecuacion))
                resultado.delete(0, tk.END)
                resultado.insert(0, result)
            except:
                resultado.delete(0, tk.END)
                resultado.insert(0, "ERROR")

        def borrar_uno():
            contenido = resultado.get()
            if contenido:
                resultado.delete(len(contenido) - 1, tk.END)

        def borrar_todo():
            resultado.delete(0, tk.END)

        def convertir_a_dolar():
            try:
                monto_en_pesos = float(resultado.get())
                conversion = monto_en_pesos / valor_dolar
                resultado.delete(0, tk.END)
                resultado.insert(0, f"{conversion:.2f} USD")
            except ValueError:
                resultado.delete(0, tk.END)
                resultado.insert(0, "ERROR")

        def convertir_a_euro():
            try:
                monto_en_pesos = float(resultado.get())
                conversion = monto_en_pesos / valor_euro
                resultado.delete(0, tk.END)
                resultado.insert(0, f"{conversion:.2f} EUR")
            except ValueError:
                resultado.delete(0, tk.END)
                resultado.insert(0, "ERROR")

        valor_dolar = 949
        valor_euro = 1054

        resultado = tk.Entry(frame_calculadora, bg='#a5fbae', width=18, relief='groove', font='Roboto 16', justify='center')
        resultado.grid(columnspan=3, row=0, pady=3, padx=30, ipadx=30, ipady=3)

        botones = [
            ('1', 1, 3), ('2', 1, 4), ('3', 1, 5), ('4', 2, 3), ('5', 2, 4), ('6', 2, 5),
            ('7', 3, 3), ('8', 3, 4), ('9', 3, 5), ('0', 4, 3), ('.', 4, 4), 
            ('+', 1, 6), ('-', 2, 6), ('*', 3, 6), ('/', 4, 6),
            ('C', 0, 4), ('CE', 0, 5), ('=', 4, 5),
            ('Dólar', 5, 3), ('Euro', 5, 4)
        ]

        for (text, row, col) in botones:
            if text == '=':
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#2dd926', activebackground='#2dd926', command=operacion)
            elif text == 'C':
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#f73030', activebackground='#e22828', command=borrar_todo)
            elif text == 'CE':
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#f73030', activebackground='#e22828', command=borrar_uno)
            elif text == 'Dólar':
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#00a8f0', activebackground='#00a8f0', command=convertir_a_dolar)
            elif text == 'Euro':
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#00a8f0', activebackground='#00a8f0', command=convertir_a_euro)
            else:
                btn = HoverButton(frame_calculadora, text=text, borderwidth=2, height=2, width=5,
                                  font=('Roboto', 12, 'bold'), relief="raised", bg='#9d40f6', activebackground='#eb70f2', command=lambda t=text: obtener(t))

            btn.grid(row=row, column=col, pady=1)

        
        mostrar_calculadora.inicializado = True

def mostrar_temporizador():
    mostrar_frame(frame_temporizador)

    if not hasattr(mostrar_temporizador, 'inicializado'):
        
        def iniciar_temporizador():
            try:
                tiempo = int(ingreso_tiempo.get())
                if tiempo > 0:
                    cuenta_regresiva(tiempo)
                else:
                    messagebox.showwarning("Advertencia", "Ingrese un tiempo válido.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número entero.")

        def cuenta_regresiva(tiempo):
            if tiempo > 0:
                minutos, segundos = divmod(tiempo, 60)
                tiempo_formateado = f"{minutos:02}:{segundos:02}"
                etiqueta_tiempo.config(text=tiempo_formateado)
                ventana.after(1000, cuenta_regresiva, tiempo-1)
            else:
                messagebox.showinfo("Temporizador", "¡El tiempo finalizó!")

        etiqueta_tiempo = tk.Label(frame_temporizador, text="00:00", font=('Digital-7', 40, 'bold'), background='white', foreground='black')
        etiqueta_tiempo.pack(pady=20)

        ingreso_tiempo = tk.Entry(frame_temporizador, background='white', foreground='black')
        ingreso_tiempo.pack()

        boton_iniciar = tk.Button(frame_temporizador, text="Iniciar Temporizador", command=iniciar_temporizador, background='white', foreground='black')
        boton_iniciar.pack(pady=10)

        
        mostrar_temporizador.inicializado = True

def mostrar_block_de_notas():
    mostrar_frame(frame_notas)

    if not hasattr(mostrar_block_de_notas, 'inicializado'):
        
        texto = tk.Text(frame_notas, wrap="word")  
        texto.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_notas, orient="vertical", command=texto.yview)
        scrollbar.pack(side="right", fill="y")

        texto.config(yscrollcommand=scrollbar.set)

        
        mostrar_block_de_notas.inicializado = True

submenu.add_command(label='Reloj con calendario', command=mostrar_reloj_con_calendario)
submenu.add_command(label='Lista de tareas', command=mostrar_lista_tareas)
submenu.add_command(label='Calculadora', command=mostrar_calculadora)
submenu.add_command(label='Block de notas', command=mostrar_block_de_notas)
submenu.add_command(label='Temporizador', command=mostrar_temporizador)

ventana.mainloop()
