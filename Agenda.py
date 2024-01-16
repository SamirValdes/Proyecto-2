import numpy as np
class Agenda():
    def __init__(self,c):
        self.nR==0
        self.dom=np.empty(c,dtype=object)
        
def buscar (self,):
    if self.nR==0:
        return None
    else: 
        i=0
        while i<self.nR and self.dom[i].nombre.ciudad !=id:
            i+=1
            
    if i==self.nR:
        return None 
    else:
        return self.dom[i]
    
def eliminarId(self,id):
        if self.nR==0:
            return None
        else: 
            i=0
            while i<self.nR and self.dom[i].nombre.cedula !=id:
                i+=1
                
                
            if i==self.nR:
                return None 
            else:
                temp= self.dom[i]
                for j in range (i,self.nR-1):
                    self.dom[j]= self.dom[j+1]
                    
                self.dom[self.nR-1]=None 
                self.nR-=1
                return temp