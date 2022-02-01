import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conexion = sqlite3.connect('database.db')
query = conexion.cursor()

class Login:
    
    def __init__(self, frame):
        self.frame = frame
        frame.title("Login")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x260")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.label1 = Label(frame, text="Email*")
        self.label1.place(x=160, y=10, width=130, height=30)
        self.label1.configure(background='white')

        self.label2 = Label(frame, text="Contraseña*")
        self.label2.place(x=160, y=90, width=130, height=30)
        self.label2.configure(background='white')

        self.entry1 = Entry(frame)
        self.entry1.place(x=100, y=40, width=250, height=30)

        self.entry2 = Entry(frame, show="*")
        self.entry2.place(x=100, y=120, width=250, height=30)

        self.button1 = Button(frame, text="Aceptar", command=self.aceptar)
        self.button1.place(x=50, y=180, width=103, height=35)

        self.button2 = Button(frame, text="Salír", command=self.salir)
        self.button2.place(x=260, y=180, width=103, height=35)

    def aceptar(self):
        if len(self.entry1.get()) == 0 and len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Campos de Texto Vacios")
        elif len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Uno de los Campo de Texto está Vacio")
        else:
            query.execute('select count(*) from usuarios where email = "' + str(self.entry1.get()) + '" and contrasena = "' + str(self.entry2.get()) + '";')
            data1 = query.fetchall()

            if(int(data1[0][0]) == 0):
                messagebox.showwarning("Mensaje de Advertencia", "Cuenta de Usuario no Encontrada")
            else:
                self.frame.destroy()
                objeto = Tk()
                Admin(objeto)
                objeto.mainloop()

    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            sys.exit()

class Admin:
    
    def __init__(self, frame):
        self.frame = frame
        frame.title("Administración")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("500x300")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.label1 = Label(frame, text="Panel de Administración de Empleados", font='Helvetica 9 bold')
        self.label1.place(x=0, y=10, width=250, height=25)
        self.label1.configure(background='white')

        self.table1 = ttk.Treeview(frame, columns = ('#0','#1','#2','#3','#4','#5'))
        self.table1.place(x=10, y=50, width=475, height=180)
        self.table1.column("#0", stretch=False, width=48)
        self.table1.column("#1", stretch=False, width=120)
        self.table1.column("#2", stretch=False, width=70)
        self.table1.column("#3", stretch=False, width=70)
        self.table1.column("#4", stretch=False, width=70)
        self.table1.column("#5", stretch=False, width=95)
        self.table1.heading('#0', text="Clave", anchor=CENTER)
        self.table1.heading('#1', text="Nombre", anchor=CENTER)
        self.table1.heading('#2', text="Nacimiento", anchor=CENTER)
        self.table1.heading('#3', text="Sexo", anchor=CENTER)
        self.table1.heading('#4', text="Profesión", anchor=CENTER)
        self.table1.heading('#5', text="Departamento", anchor=CENTER)
        query.execute('select id, nombre, nacimiento, (select nombre from sexo where id = id_sexo), (select nombre from profesion where id = id_profesion), (select nombre from departamento where id = id_departamento) from empleado order by 1 desc;')
        data1 = query.fetchall()
        for(clave, nombre, nacimiento, sexo, profesion, departamento) in data1:
        	self.table1.insert('', 0, text=clave, values=(nombre, nacimiento, sexo, profesion, departamento))

        self.button1 = Button(frame, text="Agregar", command=self.agregar)
        self.button1.place(x=80, y=250, width=103, height=35)

        self.button2 = Button(frame, text="Salír", command=self.salir)
        self.button2.place(x=290, y=250, width=103, height=35)

    def agregar(self):
        self.frame.destroy()
        objeto = Tk()
        AgregarEmpleado(objeto)
        objeto.mainloop()

    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            self.frame.destroy()
            objeto = Tk()
            Login(objeto)
            objeto.mainloop()


class AgregarEmpleado:
    
    def __init__(self, frame):
        self.frame = frame
        frame.title("Agregar")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x500")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.label1 = Label(frame, text="Nombre*")
        self.label1.place(x=160, y=10, width=130, height=30)
        self.label1.configure(background='white')

        self.label2 = Label(frame, text="Nacimiento (AAAA-MM-DD)*")
        self.label2.place(x=160, y=90, width=130, height=30)
        self.label2.configure(background='white')

        self.label3 = Label(frame, text="Sexo*")
        self.label3.place(x=160, y=170, width=130, height=30)
        self.label3.configure(background='white')

        self.label4 = Label(frame, text="Profesión*")
        self.label4.place(x=160, y=250, width=130, height=30)
        self.label4.configure(background='white')

        self.label5 = Label(frame, text="Departamento*")
        self.label5.place(x=160, y=330, width=130, height=30)
        self.label5.configure(background='white')

        self.entry1 = Entry(frame)
        self.entry1.place(x=100, y=40, width=250, height=30)

        self.entry2 = Entry(frame)
        self.entry2.place(x=100, y=120, width=250, height=30)

        self.combo1 = ttk.Combobox(frame)
        self.combo1.place(x=100, y=200, width=250, height=30)
        self.combo1['value'] = self.sexo_input()
        self.combo1.current(0)

        self.combo2 = ttk.Combobox(frame)
        self.combo2.place(x=100, y=280, width=250, height=30)
        self.combo2['value'] = self.profesion_input()
        self.combo2.current(0)

        self.combo3 = ttk.Combobox(frame)
        self.combo3.place(x=100, y=360, width=250, height=30)
        self.combo3['value'] = self.departamento_input()
        self.combo3.current(0)

        self.button1 = Button(frame, text="Aceptar", command=self.aceptar)
        self.button1.place(x=70, y=440, width=103, height=35)

        self.button2 = Button(frame, text="Salír", command=self.salir)
        self.button2.place(x=280, y=440, width=103, height=35)

    def aceptar(self):
        if len(self.entry1.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Uno de los Campos están Vacios.")
        else:
            query.execute('insert into empleado(nombre, nacimiento, id_sexo, id_profesion, id_departamento) values("' + str(self.entry1.get()) + '", "' + str(self.entry2.get()) + '", (select id from sexo where nombre = "' + str(self.combo1.get()) + '"), (select id from profesion where nombre = "' + str(self.combo2.get()) + '"), (select id from departamento where nombre = "' + str(self.combo3.get()) + '"));')
            self.frame.destroy()
            objeto = Tk()
            Admin(objeto)
            objeto.mainloop()

    def salir(self):
        self.frame.destroy()
        objeto = Tk()
        Admin(objeto)
        objeto.mainloop()

    def sexo_input(self):
        result = []
        query.execute('select * from sexo;')
        for row in query.fetchall():
            result.append(row[1])
        return result

    def profesion_input(self):
        result = []
        query.execute('select * from profesion;')
        for row in query.fetchall():
            result.append(row[1])
        return result

    def departamento_input(self):
        result = []
        query.execute('select * from departamento;')
        for row in query.fetchall():
            result.append(row[1])
        return result


class MainClass:
    objeto = Tk()
    Login(objeto)
    objeto.mainloop()

"""

Programa Visual que Gestiona el Personal de una Empresa Utilizando Bases de Datos.

Usuario: admin@gmail.com
Contraseña: admin12345

"""