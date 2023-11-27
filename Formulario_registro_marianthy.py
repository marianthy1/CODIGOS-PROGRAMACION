"""
Registro de visitas del area de urgencias de la unidad medica de la universidad Chapingo 

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 


import sqlite3

class Registro:
    db_name='databaseurgencias.db'
    
    def __init__(self,vetana):
        self.window=ventana   
        self.window.title("FORMULARIO DE REGISTRO")
        self.window.geometry("500x700")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana, text="Registro servicio de urgencias ",fg="black",font=("Comic Sans", 13,"bold"),pady=5).pack()

        
        "--------------- Marco --------------------"
        marco = LabelFrame(ventana, text="Datos personales",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2,pady=5)
        marco.pack()

        "--------------- Formulario --------------------"
        label_matricula=Label(marco,text="Mátricula: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.matricula=Entry(marco,width=25)
        self.matricula.focus()
        self.matricula.grid(row=0, column=1, padx=5, pady=8)

        label_nombres=Label(marco,text="Nombre(s): ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=8)
        self.nombres=Entry(marco,width=25)
        self.nombres.grid(row=1, column=1, padx=10, pady=8)

        label_apellido_ma=Label(marco,text="Apellido Paterno: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=8)
        self.apellido_ma=Entry(marco,width=25)
        self.apellido_ma.grid(row=2, column=1, padx=10, pady=8)
        
        label_apellido_pa=Label(marco,text="Apellido Materno: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=8)
        self.apellido_pa=Entry(marco,width=25)
        self.apellido_pa.grid(row=2, column=1, padx=10, pady=8)

        label_departamento=Label(marco,text="Departamento: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_departamento=ttk.Combobox(marco,values=["Irrigacion", "Preparatoria", "Suelos", "DICIFO", "DICEA", "DIMA", "Zootecnia", "Agroecologia", "Sociologia", "Agroindustrias", "Fitotecnia", "Parasitologia"], width=22,state="readonly")
        self.combo_departamento.current(0)
        self.combo_departamento.grid(row=3,column=1,padx=10,pady=8)

        label_tipo_alum=Label(marco,text="Tipo de alumno: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_tipo_alum=ttk.Combobox(marco,values=["BEX", "INT", "EXT"], width=22,state="readonly")
        self.combo_tipo_alum.current(0)
        self.combo_tipo_alum.grid(row=3,column=1,padx=10,pady=8)

        label_asunto=Label(marco,text="Asunto: ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_asunto=ttk.Combobox(marco,values=["Consulta general", "Consulta admision continua (urgencia)", "Aplicacion de inyeccion", "Sutura", "Vendaje", "Curacion"], width=22,state="readonly")
        self.combo_asunto.current(0)
        self.combo_asunto.grid(row=3,column=1,padx=10,pady=8)

        label_edad=Label(marco,text="Edad: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=8)
        self.edad=Entry(marco,width=25)
        self.edad.grid(row=4, column=1, padx=10, pady=8)

        label_fecha_dia=Label(marco,text="Fecha(día): ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_fecha_dia=ttk.Combobox(marco,values=["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"], width=22,state="readonly")
        self.combo_fecha_dia.current(0)
        self.combo_fecha_dia.grid(row=3,column=1,padx=10,pady=8)

        label_fecha_mes=Label(marco,text="Fecha (mes): ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=8)
        self.combo_fecha_mes=ttk.Combobox(marco,values=["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], width=22,state="readonly")
        self.combo_fecha_mes.current(0)
        self.combo_fecha_mes.grid(row=3,column=1,padx=10,pady=8)

        label_fecha_an=Label(marco,text="Fecha(Año): ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=8)
        self.fecha_an=Entry(marco,width=25)
        self.fecha_an.grid(row=4, column=1, padx=10, pady=8)
        
       
       
        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar=Button(frame_botones,text="REGISTRAR",command=self.Registrar_usuario ,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_limpiar=Button(frame_botones,text="LIMPIAR",command=self.Limpiar_formulario ,height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_cancelar=Button(frame_botones,text="CERRAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)
            conexion.commit()
        return result 
    
    def Limpiar_formulario(self):
        self.matricula.delete(0, END)
        self.nombres.delete(0, END)
        self.apellido_pa.delete(0, END)
        self.apellido_ma.delete(0, END)
        self.combo_departamento.delete(0, END)
        self.combo_tipo_alum.delete(0, END)
        self.combo_asunto.delete(0, END)
        self.edad.delete(0, END)
        self.combo_fecha_dia.delete(0, END)
        self.combo_fecha_mes.delete(0, END)
        self.fecha_an.delete(0, END)
    
        
        
    def Validar_formulario_completo(self):
        if len(self.matricula.get()) !=0 and len(self.nombres.get()) !=0 and len(self.apellido_pa.get()) !=0 and len(self.apellido_ma.get()) !=0 and len(self.combo_departamento.get()) !=0 and len(self.combo_tipo_alum.get()) !=0 and len(self.combo_asunto.get()) !=0 and len(self.edad.get()) !=0 and len(self.combo_fecha_dia.get()) !=0 and len(self.combo_fecha_mes.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR EN REGISTRO", "Complete todos los campos del formulario")
             

 

    
    

    def Registrar_visita(self):
        if self.Validar_formulario_completo():
            query='INSERT INTO Usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.matricula.get(),self.nombres.get(),self.apellido_pa.get(),self.apellido_ma.get(),self.combo_departamento.get(),self.combo_tipo_alum.get(),self.combo_asunto.get(),self.edad.get(),self.combo_fecha_dia.get(),self.combo_fecha_mes.get(),self.fecha_an.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Bienvenido {self.nombres.get()}')
            print('VISITA REGISTRADA')
            self.Limpiar_formulario()
            
if __name__ == '__main__':
    ventana=Tk()
    application=Registro(ventana)
    ventana.mainloop()
