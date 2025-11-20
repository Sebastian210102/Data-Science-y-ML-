from task import task
import json
import os 

FILE_PATH = "./data/tasks.json"

class task_manager:
    #Constructor de ña cñase
    def __init__(self, file_path : str):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    

    def add_task(self, task_object):
        #Aseguramos que la lista de memoria se actualice
        self.tasks.append(task_object)

    #Guardar nuestras tareas en un json

    def save_tasks(self):
        try:
            
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            data = [t.to_dictionary() for t in self.tasks]

            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
                print(f"{len(self.tasks)} tarea(s) guardada() en {self.file_path}")
        except Exception as e:
            print("No se fue capaz de guardar los datos de las tareas Error: {e}")    


    def load_tasks(self):
        try: 
            with open(self.file_path, 'r') as f:
                tasks_data = json.load(f)
        except FileNotFoundError:
            #Devolvemos una lista vacia si el archivo no existe
            return []
        except json.JSONDecodeError:
            #Archivo corrupto
            print("Advertencia archivo corrompido")
            return []
        #Deserialización(Recontruccion del objeto)
        tasks_objects = []
        for task_dict in tasks_data:
            new_task = task(
                name=task_dict['name'],
                priority=task_dict['priority'],
                tag=task_dict['tag'],
                complete=task_dict['complete']
            )
            tasks_objects.append(new_task)

        return tasks_objects




#Prueba de como se usa

manager = task_manager(FILE_PATH)
t1 = task("Cuadri", 4, "Pierna")

# 1. Añadir la tarea a la lista en memoria
manager.add_task(t1) 

# 2. Guardar la lista interna (Crea tasks.json)
manager.save_tasks() 

# 3. Prueba de Deserialización: Crea una NUEVA instancia
manager_nuevo = task_manager(FILE_PATH)

# 4. Verificar que se cargó:
print(f"Cargadas {len(manager_nuevo.tasks)} tareas. Tarea 1: {manager_nuevo.tasks[0]}")