from task import task
import json
import os 
FILE_PATH = "./data/tasks.json"

class task_manager:
    def __init__(self, file_path : str):
        self.file_path = file_path
    
    def save_tasks(self, tasks):

        
        data = [t.to_dictionary() for t in tasks]

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
            print(f"{len(tasks)} tarea(s) guardada() en {self.file_path}")
            


#Prueba de como se usa

t1 = task("Cuadri",4,"Pierna")
#Crear el manager
manager = task_manager(FILE_PATH)

#Guardar la tareas

manager.save_tasks([t1])