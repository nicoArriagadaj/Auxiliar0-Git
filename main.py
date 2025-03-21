from tarea import Tarea
from usuario import Usuario

# Crear un usuario
usuario = Usuario("tito", "gossip123", "titos.kahuin.embassy@gmail.com")

# Crear tareas
tarea1 = Tarea("Instalar Git en mi PC")
tarea2 = Tarea("Terminar auxiliar 1 Ingeniería de Software")

# Agregar tareas al usuario
usuario.agregarTarea(tarea1)
tarea1.terminar()  # Marcar tarea1 como terminada
usuario.agregarTarea(tarea2)

# Listar tareas del usuario
usuario.listarTareas()
