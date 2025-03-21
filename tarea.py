class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listo = False


    def obtenerNombre(self):
        return self.nombre

    def estaLista(self):
        return self.listo
    
    def terminar(self):
        return "termino"
    
    def __str__(self):
    # Retorna una representación legible del objeto
        return "algún texto o información sobre el objeto"