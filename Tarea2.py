class Nodo(object):

    def __init__(self, valor, siguiente = None):
        self.siguiente = siguiente
        self.valor = valor

class Lista(object):

    def __init__(self):
        self.cabeza = None

    def longitud (self):
        lon = 0
        cursor = self.cabeza
        while cursor :
            lon += 1
            cursor = cursor.siguiente
        return lon
    
    def insertar(self,elemento):
        if self.cabeza is None:
            self.cabeza = Nodo(elemento)
        else:
            cursor = self.cabeza        
            while cursor.siguiente:
                cursor = cursor.siguiente

            cursor.siguiente = Nodo(elemento)
    
    def insertar_pos (self,elemento,pos):        
        if pos < 0 | pos > self.longitud():
            print ("Posición no valida")
            return  
        
        cursor = self.cabeza
        nodo = Nodo(elemento)
       
        if pos == 0:            
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            pos_cursor = 0
            while  (pos_cursor+1 != pos) & (cursor != None):
                pos_cursor = pos_cursor+1
                cursor = cursor.siguiente
            
            nodo.siguiente = cursor.siguiente
            cursor.siguiente = nodo

    def insertar_inicio(self,elemento):
        if self.cabeza is None:
            self.cabeza = Nodo(elemento)
        else:
            cursor = self.cabeza
            self.cabeza = Nodo(elemento)
            self.cabeza.siguiente = cursor


    def mostrar(self):
        cursor = self.cabeza
        while cursor:
            print(cursor.valor, end=" -> ")
            cursor = cursor.siguiente
        print("None")

    def insertar_siguiente(self, elemento):

        pass

    def eliminar(self, posición):

        pass

    def esta_vacia(self):
        return self.cabeza is None        


lis = Lista()
lis.insertar(5)
lis.insertar(10)
print(lis.mostrar())

lis.insertar_inicio(89)
lis.insertar(12)
lis.insertar_inicio(19)

lis.mostrar()

lis.insertar_pos(100,2)

lis.mostrar()