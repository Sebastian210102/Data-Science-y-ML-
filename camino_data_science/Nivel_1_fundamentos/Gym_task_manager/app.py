from task import task
from task_manager import task_manager

FILE_PATH = "./data/tasks.json"

manager = task_manager(FILE_PATH)
def listado_tareas():
    print("---------Tareas listadas ----------")
    if manager.tasks:
        for idx, task_obj in enumerate(manager.tasks):
            print(f"{idx + 1}.- {task_obj}")                
    else:
            print("No hay tareas guardadas ¡Añande una!")





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
        
        match selection:
            case "1":
                #Agregar tarea
                print("Agreguemos una tarea")
                name = input("Tarea que quieres desempeñar: ")
                tag = input("Grupo en el que quiere que la tara se ubique: ")

                while True: 
                    priority = input("La prioridad de tu tarea( 1- 5): ")
                    try: 
                        priority = int(priority)
                        if 1<= priority <= 5: 
                            break
                        else:
                            print("Favor de escoger un valor de 1 - 5 ")                
                    except ValueError:
                        #Manejo del error
                        print("Favor de poner un valor entero numérico del 1-5")

                #Creando la nueva tarea
                new_task = task(name, priority,tag)
                manager.add_task(new_task)
                print(f'Tarea {name} guardada')
                print("-------Tarea completada con éxito-------")
                
            case "2":
                #Listar tareas 
               listado_tareas()
            case "3":
                #Marcar como completada
                listado_tareas()                

                while manager.tasks:    
                    try:
                        index_completed = input("¿Que tarea (indice) desea completar?")
                        index_completed = int(index_completed)

                        if index_completed == 0:
                            break

                        index_para_completar = index_completed - 1

                        task_to_complete = manager.tasks[index_para_completar]
                        task_to_complete.mark_as_completed()
                        print(f"""
                                Tarea '{task_to_complete.name}' marcada como completada 
                                """)
                        break
                    except ValueError:
                        print("Entrada no valida favor de introducir un numeor entero")
                    except IndexError:
                        print("Númeor de tarea invalido  favor de poner un número de la lista de tareas")


            case "4":
                manager.save_tasks()
                print("Tareas guardadas")
                print("Saliendo del programa....")
                break
            case _:
                print("Comando no valido")

if __name__ == "__main__":
    main()

