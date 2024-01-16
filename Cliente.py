class Cliente():
    def __init__(self,cedula,nombre,apellido,fechaNacimiento,ciudad):#,edad):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.fechaNacimineto=fechaNacimiento
        self.ciudad=ciudad
       # self.edad=edad
        
        @property
        def cedula(self):
            return self.cedula
        
        @property
        def nombre(self):
            return self.nombre

        @property
        def apellido(self):
            return self.apellido   
        
        @property
        def fechaNacimiento(self):
            return self.fechaNacimiento

        @property
        def ciudad(self):
            return self.ciudad

        #@property
        #def edad(self):
         #   return self.edad

        @cedula.setter
        def cedula(self,c):
             self.cedula=c
        
        @nombre.setter        
        def nombre(self,n):
            self.nombre=n
            
        @apellido.setter
        def apellido(self,p):
             self.apellido=p
             
        @fechaNacimiento.setter
        def fechaNacimiento(self,Fn):
             self.fechaNacimiento=Fn

        @ciudad.setter
        def ciudad(self,cd):
             self.ciudad=cd

        #@edad.setter
        #def edad(self,e):
         #    self.edad=e             

def __str__(self):
        return self.cedula+"/"+self.nombre+"/"+self.apellido+"/"+self.fechaNacimineto+"/"+self.ciudad#+"/"+self.edad