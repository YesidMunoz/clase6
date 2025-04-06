from datetime import datetime
def pedir_fecha(mensaje):
    while True:
        fecha_input = input(mensaje)
        try:            
            fecha = datetime.strptime(fecha_input, "%d/%m/%Y")
            return fecha_input  
        except ValueError:
            print("Error: El formato debe ser dd/mm/aaaa. Intente de nuevo.")

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def eliminarMedicamento(self, nombre_medicamento):
        for medicamento in self.__lista_medicamentos:
            if medicamento.verNombre() == nombre_medicamento:
                self.__lista_medicamentos.remove(medicamento)
                return True 
        return False  
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
    
    def verificarExiste(self,historia): #Verifica en ambos dicc
        for m in self.__caninos:
            if m == historia:
                return True 
        for m in self.__felinos:
            if m == historia:
                return True
        return False
        
    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos)
    
    def ingresarMascota(self, mascota):
        if mascota.verTipo().lower() == "canino":
            self.__caninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo().lower() == "felino":
            self.__felinos[mascota.verHistoria()] = mascota
    

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__caninos:
            return self.__caninos[historia].verFecha()
        elif historia in self.__felinos:
            return self.__felinos[historia].verFecha()
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__caninos:
            return self.__caninos[historia].verLista_Medicamentos()
        elif historia in self.__felinos:
            return self.__felinos[historia].verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False
    

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir
                       \n7- Eliminar medicamento de una mascota 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha = pedir_fecha("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                contador = 0
                while contador < nm:
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    
                    nombre_ya_existe = False
                    for medicamento_existente in lista_med:
                        if medicamento_existente.verNombre() == nombre_medicamentos:
                            nombre_ya_existe = True
                            break 

                    if nombre_ya_existe:
                        print("Ya existe un medicamento con ese nombre. Ingrese un medicamento diferente.")
                        continue

                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    
                    contador += 1

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        elif menu == 7: 
            q = int(input("Ingrese la historia clínica de la mascota: "))
            lista_medicamentos = servicio_hospitalario.verMedicamento(q)
            
            if lista_medicamentos:  
                print("Los medicamentos suministrados son: ")
                for m in lista_medicamentos:
                    print(m.verNombre())

                nombre_medicamento = input("Ingrese el nombre del medicamento que desea eliminar: ")
                
                encontrado = False
                for medicamento in lista_medicamentos:
                    if medicamento.verNombre() == nombre_medicamento:
                        lista_medicamentos.remove(medicamento)
                        print("El medicamento ha sido eliminado correctamente.")
                        encontrado = True
                        break
                
                if encontrado == False:
                    print("El medicamento no se encontró en la lista.")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

