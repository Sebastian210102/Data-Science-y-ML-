class task:
    def __init__(self, name : str, priority : int, tag: str, complete : bool = False):
       
        self.name = name
        self.priority = priority
        self.tag = tag
        self.complete = complete


    #Dar un reporte de como esta el estatus de la tarea
    def __repr__(self):
        
        status = "Completado" if self.complete else "En espera"
        return f'Estatus de la tarea {status} | Prioridad: {self.priority}| Tarea : {self.name} ({self.tag})  '

    def mark_as_completed(self):
        self.complete = True

        
    def to_dictionary(self):
        task_properties = {
            "name": self.name,
            "priority": self.priority,
            "tag": self.tag,
            "complete" : self.complete
        }

        return task_properties


#Objeto de prueba

pierna = task("Cuadri",4,"Pierna")

print(pierna)
pierna.mark_as_completed()
print(pierna)
