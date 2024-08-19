import tkinter as tk
import time
from datetime import datetime, timedelta

ventana = tk.Tk()
ventana.title('Reloj')
ventana.geometry('400x200')



barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Horarios', menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Paises', menu=submenu)


def reloj_argentina():
 reloj = tk.Label(ventana, font = ('Arial', 20), bg = 'white', fg = 'black')

 def hora():
  tiempo_actual = time.strftime('%H:%M:%S')
  reloj.config(text = f"{tiempo_actual} Argentina")
  ventana.after(1000, hora)

 reloj.pack(expand=True)
 hora()


def reloj_china():
 reloj = tk.Label(ventana, font = ('Arial', 20), bg = 'white', fg = 'black')

 def hora():
  hora_actual = datetime.now()
  nueva_hora = hora_actual + timedelta(hours=11)
  tiempo_formateado = nueva_hora.strftime('%H:%M:%S')
  reloj.config(text= f"{tiempo_formateado} China")
  
  ventana.after(1000, hora)
 reloj.pack(expand=True)
 hora()



submenu.add_command(label = 'Argentina', command=reloj_argentina )
submenu.add_command(label = 'China', command=reloj_china)

ventana.mainloop()


