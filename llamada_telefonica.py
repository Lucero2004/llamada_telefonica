#llamada_telefonica
#Ingresar el tiempo de duración de una llamada telefonica y determinar la cantidad a pagar de acuerdo con lo siguiente:
#Toda llamada que dure tres minutos o menos tiene un costo de 300 pesos
#toda llamada con minuto  adicional cuesta 50 pesos de mas.

#input
dL=int(input("ingrese el tiempo de duración de la llamada: "))

#procesing
if(dL<=3):
    CL=300
else:
     CL=300+50*(dL-3)

#output
print("-------------------------------")
print("El costo de la llamada en pesos es: " +str(CL))
print("---------------------------")    
        
