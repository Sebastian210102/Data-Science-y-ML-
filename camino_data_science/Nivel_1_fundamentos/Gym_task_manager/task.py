class task:
    def __init__(self, name : str, priority : int, tag: str, complete : bool = False):
       
        self.name = name
        self.priority = priority
        self.tag = tag
        self.complete = complete

    def mark_as_completed(self):
        self.complete = True
        print(f"Ejercicio {self.name} completado")
    
    def to_dictionary():
        pass


#Objeto de prueba

pierna = task("Cuadri",4,"Pierna")

pierna.task_is_complete()
        