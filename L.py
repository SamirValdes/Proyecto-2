import Cliente as c
import datetime as dt 
#import Agenda as a


try:
        file=open("ListadoClientes.csv","r")
        file2=open("ListadoClientes2.csv","w")
        line=file.readline()
        file2.write(line[:-1]+";Edad"+line[-1])
        line=file.readline()
        while line !="":
            A=line.split(";")
            cliente=c.Cliente(A[0],A[1], A[2], A[3],A[4])
            line=file.readline()
            L=A[3].split("/")
            fechaN=dt.datetime(int(L[2]),int(L[1]),int(L[0]))
            hoy=dt.datetime.now()
            dif=hoy-fechaN
            edad=dif.days//365           
            file2.write(A[0]+" "+A[1]+" "+A[2]+" "+str(fechaN)+" "+A[4][:-1]+" "+str(edad)+" "+line[-1])
            line=file.readline()     
        file.close()
        file2.close()
except:
        print("Error de Lectura")
        
#c1=a.Agenda
#print(cliente=a.buscar(A[4]))       


