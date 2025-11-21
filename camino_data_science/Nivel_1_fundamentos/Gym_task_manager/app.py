from task import task
from task_manager import task_manager

FILE_PATH = "./data/tasks.json"

manager = task_manager(FILE_PATH)

def main():

    while(True):
        selection = input("""
              Bievenido al organizador de Tareas. Escribe el numero de las siguientes opciones a la que 
              desees acceder:
            \n1.Agregar tarea.
            \n2.Listar tareas.
            \n3.Marcar como completada.
            \n4.Salir
              
              """)
        



if __name__ == "__main__":
    main()
