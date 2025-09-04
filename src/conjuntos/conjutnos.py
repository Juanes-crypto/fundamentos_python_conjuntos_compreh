# creacion de conjuntos

# usando llaves:
colores = {"rojo","verde","azul"}
print(colores) # imprime {'rojo', 'verde', 'azul'}

#usando la funcion set():
numeros = set([1, 2, 3, 2, 1])#[]
print(numeros)

# ejemplo # 2:
#caracyeristicas de los elementos unicos:
usuarios = set(["ana","carlos","ana","elena","carlos"])
print(usuarios) # apesar de que ana se repite dos veces en el conjunto, este solo aparecera una sola vez

#verificacion de pertenencia eificiente:
frutas = {"naranja","manzana","platano"}
print("manzana" in frutas) #true
print("uva" in frutas) #false
# de esta forma podemos hacer una verificacion rapida de si un elemento esta o no en un conjunto

#inmutabiñlidad de los elementos_los elementos de un conjunto deben ser imnutables,esto quiere decir
#que no podemos incluir listas o diccionarios

#ejemplo de conjunto invalido:
#  conjunto_invalido = {1, [2,3]}


#caso de usos practricos:
# Eliminar duplicados de una lista manteniendo el orden original
def eliminar_duplicados(secuencia):
    return list(dict.fromkeys(secuencia))

lista_con_duplicados = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(eliminar_duplicados(lista_con_duplicados))  # [3, 1, 4, 5, 9, 2, 6]

# encontrar elementos unicos entre colecciones
grupo_a = {"ana","carlos","elena","deavid"}
grupo_b = {"elena","fernando","gabrieLA","CARLOS"}

# personas que estanen el grupo a:
solo_en_grupo_a = grupo_a - grupo_b
print(solo_en_grupo_a) #ana, david

# VERIFICAR SI TODOS LOS ELEMENTOS SON UNICOS

def todos_unicos(items):
    return len(items) == len(set(items))
print(todos_unicos([1,2,3,4]))
print(todos_unicos([1,2,3,1,4]))

# RESTRICCIONES DE LOS CONJUNTOS:
numeros = {3,1,4,1,5,9}
print(numeros)

colores = {"rojo", "verde", "azul"}

# Esto NO crea un conjunto vacío, sino un diccionario vacío
no_es_conjunto = {}
print(type(no_es_conjunto))  # <class 'dict'>

# Forma correcta de crear un conjunto vacío
conjunto_vacio = set()
print(type(conjunto_vacio))  # <class 'set'>

tecnologias = {"Python", "JavaScript", "SQL"}
tecnologias.add("Java")
print(tecnologias)  # {'Python', 'JavaScript', 'SQL', 'Java'}

lenguajes = {"Python", "Java"}
nuevos_lenguajes = ["Go", "Rust", "TypeScript"]
lenguajes.update(nuevos_lenguajes)
print(lenguajes)  # {'Python', 'Java', 'Go', 'Rust', 'TypeScript'}

numeros = {1, 2, 3}
numeros.add(2)  # Intentamos añadir un elemento que ya existe
print(numeros)  # {1, 2, 3} - No hay cambios

frutas = {"manzana", "naranja", "plátano"}
frutas.remove("naranja")
print(frutas)  # {'manzana', 'plátano'}

# Si intentamos eliminar un elemento que no existe:
# frutas.remove("uva")  # KeyError: 'uva'

animales = {"perro", "gato", "conejo"}
animales.discard("pájaro")  # No existe, pero no genera error
print(animales)  # {'perro', 'gato', 'conejo'}

colores = {"rojo", "verde", "azul"}
color_eliminado = colores.pop()
print(f"Se eliminó: {color_eliminado}")
print(f"Conjunto resultante: {colores}")

numeros = {1, 2, 3, 4, 5}
numeros.clear()
print(numeros)  # set()

planetas = {"Mercurio", "Venus", "Tierra", "Marte"}
print(len(planetas))  # 4

dias = {"lunes", "martes", "miércoles", "jueves", "viernes"}
print("sábado" in dias)  # False
print("lunes" in dias)   # True

original = {1, 2, 3}
copia = original.copy()
copia.add(4)
print(original)  # {1, 2, 3} - No se modifica
print(copia)     # {1, 2, 3, 4}

ciudades = {"Madrid", "Barcelona", "Valencia", "Sevilla"}
for ciudad in ciudades:
    print(f"Visitando {ciudad}")
    
    
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_sin_duplicados = set(lista_con_duplicados)
print(conjunto_sin_duplicados)  # {1, 2, 3, 4, 5}

conjunto = {"a", "b", "c", "d"}
lista = list(conjunto)
print(lista)  # ['a', 'b', 'c', 'd'] (el orden puede variar)


numeros_pares = {2, 4, 6, 8}
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros_pares.issubset(numeros))  # True

frutas = {"manzana", "naranja", "plátano", "fresa", "kiwi"}
frutas_tropicales = {"plátano", "kiwi"}
print(frutas.issuperset(frutas_tropicales))  # True


# Registro inicial de asistentes
asistentes_dia1 = {"Ana", "Carlos", "Elena", "David", "Beatriz"}
asistentes_dia2 = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Añadir nuevos asistentes al día 1
asistentes_dia1.add("Héctor")
print(f"Asistentes día 1: {asistentes_dia1}")

# Personas que asistieron ambos días
asistentes_ambos_dias = asistentes_dia1.intersection(asistentes_dia2)
print(f"Asistieron ambos días: {asistentes_ambos_dias}")

# Eliminar a alguien que canceló su asistencia
asistentes_dia1.discard("David")
print(f"Asistentes día 1 actualizado: {asistentes_dia1}")

# Comprobar si todos los del día 2 asistieron también el día 1
todos_repiten = asistentes_dia2.issubset(asistentes_dia1)
print(f"¿Todos los del día 2 asistieron el día 1?: {todos_repiten}")

# Total de asistentes únicos en ambos días
total_asistentes = len(asistentes_dia1.union(asistentes_dia2))
print(f"Total de asistentes únicos: {total_asistentes}")

# Registro inicial de asistentes
asistentes_dia1 = {"Ana", "Carlos", "Elena", "David", "Beatriz"}
asistentes_dia2 = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Añadir nuevos asistentes al día 1
asistentes_dia1.add("Héctor")
print(f"Asistentes día 1: {asistentes_dia1}")

# Personas que asistieron ambos días
asistentes_ambos_dias = asistentes_dia1.intersection(asistentes_dia2)
print(f"Asistieron ambos días: {asistentes_ambos_dias}")

# Eliminar a alguien que canceló su asistencia
asistentes_dia1.discard("David")
print(f"Asistentes día 1 actualizado: {asistentes_dia1}")

# Comprobar si todos los del día 2 asistieron también el día 1
todos_repiten = asistentes_dia2.issubset(asistentes_dia1)
print(f"¿Todos los del día 2 asistieron el día 1?: {todos_repiten}")

# Total de asistentes únicos en ambos días
total_asistentes = len(asistentes_dia1.union(asistentes_dia2))
print(f"Total de asistentes únicos: {total_asistentes}")

grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Carlos", "Elena", "Fernando"}
comunes = grupo_a.intersection(grupo_b)
print(comunes)  # {'Carlos', 'Elena'}

equipo1 = {"Juan", "María", "Pedro"}
equipo2 = {"Ana", "Pedro", "Luis"}
todos = equipo1.union(equipo2)
print(todos)  # {'Juan', 'María', 'Pedro', 'Ana', 'Luis'}

inventario = {"laptop", "teléfono", "tablet", "auriculares"}
vendidos = {"laptop", "auriculares"}
disponibles = inventario.difference(vendidos)
print(disponibles)  # {'teléfono', 'tablet'}

ciencias = {"física", "química", "biología", "matemáticas"}
artes = {"literatura", "música", "pintura", "matemáticas"}
exclusivos = ciencias.symmetric_difference(artes)
print(exclusivos)  # {'física', 'química', 'biología', 'literatura', 'música', 'pintura'}

usuarios_activos = {"user1", "user2", "user3", "user4"}
usuarios_premium = {"user2", "user4", "user5"}
# Actualiza usuarios_activos para contener solo usuarios activos que también son premium
usuarios_activos.intersection_update(usuarios_premium)
print(usuarios_activos)  # {'user2', 'user4'}

frutas_locales = {"manzana", "pera", "naranja"}
frutas_importadas = {"piña", "mango", "kiwi"}
# Añade todas las frutas importadas a las locales
frutas_locales.update(frutas_importadas)
print(frutas_locales)  # {'manzana', 'pera', 'naranja', 'piña', 'mango', 'kiwi'}

todos_cursos = {"Python", "Java", "SQL", "JavaScript", "C++"}
cursos_completados = {"Python", "SQL"}
# Elimina los cursos completados de la lista total
todos_cursos.difference_update(cursos_completados)
print(todos_cursos)  # {'Java', 'JavaScript', 'C++'}

grupo1 = {"Ana", "Carlos", "David"}
grupo2 = {"Carlos", "Elena", "Fernando"}
# Actualiza grupo1 para contener solo personas que están en un grupo pero no en ambos
grupo1.symmetric_difference_update(grupo2)
print(grupo1)  # {'Ana', 'David', 'Elena', 'Fernando'}


vegetales = {"zanahoria", "pepino", "lechuga"}
frutas = {"manzana", "plátano", "naranja"}
print(vegetales.isdisjoint(frutas))  # True - No tienen elementos en común

numeros_pares = {2, 4, 6, 8}
numeros_primos = {2, 3, 5, 7}
print(numeros_pares.isdisjoint(numeros_primos))  # False - Comparten el 2


original = {1, 2, (3, 4)}
copia = original.copy()
original.add(5)
print(original)  # {1, 2, (3, 4), 5}
print(copia)     # {1, 2, (3, 4)} - No se ve afectado por cambios en el original


#ejemplo practico: analisis de datos de ventas:
# Productos vendidos en diferentes tiendas
tienda_centro = {"laptop", "teléfono", "tablet", "auriculares", "cámara"}
tienda_norte = {"laptop", "teléfono", "smartwatch", "altavoces"}
tienda_sur = {"tablet", "auriculares", "smartwatch", "monitor"}

# Productos que se venden en todas las tiendas
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
print(f"Productos vendidos en todas las tiendas: {productos_comunes}")

# Productos únicos de la tienda centro (que no se venden en las otras)
productos_exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
print(f"Productos exclusivos de tienda centro: {productos_exclusivos_centro}")

# Productos que se venden en al menos una tienda
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
print(f"Catálogo completo: {catalogo_completo}")

# Comprobar si todas las tiendas venden productos distintos
son_disjuntos = tienda_centro.isdisjoint(tienda_norte) and tienda_centro.isdisjoint(tienda_sur) and tienda_norte.isdisjoint(tienda_sur)
print(f"¿Todas las tiendas venden productos distintos? {son_disjuntos}")

# Productos que se venden en exactamente una tienda
solo_centro = tienda_centro - (tienda_norte | tienda_sur)
solo_norte = tienda_norte - (tienda_centro | tienda_sur)
solo_sur = tienda_sur - (tienda_centro | tienda_norte)
productos_exclusivos = solo_centro | solo_norte | solo_sur
print(f"Productos que se venden en una sola tienda: {productos_exclusivos}")

# encadenamiento de datos:
grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7}
grupo_c = {1, 5, 7, 9}

# Elementos que están en grupo_a y grupo_b, pero no en grupo_c
resultado = grupo_a.intersection(grupo_b).difference(grupo_c)
print(resultado)  # {4}


#RENDIMIENTO DE LOS METODOS DE CONJUNTOS:
# Ejemplo de rendimiento con conjuntos grandes
import time

# Crear dos conjuntos grandes
conjunto_a = set(range(10000))
conjunto_b = set(range(5000, 15000))

# Medir tiempo para operación de intersección
inicio = time.time()
interseccion = conjunto_a.intersection(conjunto_b)
fin = time.time()

print(f"Elementos en la intersección: {len(interseccion)}")
print(f"Tiempo para calcular intersección: {(fin - inicio)*1000:.2f} ms")

#OPERADORES MATEMATEMATICOS:
ciudades_europa = {"Madrid", "París", "Roma", "Berlín"}
ciudades_asia = {"Tokio", "Pekín", "Seúl", "Bangkok"}

todas_ciudades = ciudades_europa | ciudades_asia
print(todas_ciudades)  # {'Madrid', 'París', 'Roma', 'Berlín', 'Tokio', 'Pekín', 'Seúl', 'Bangkok'}

#OPERADORES DE INTERSECCION:
estudiantes_matematicas = {"Ana", "Carlos", "Elena", "David"}
estudiantes_fisica = {"Carlos", "Elena", "Fernando", "Gabriela"}

estudiantes_ambas = estudiantes_matematicas & estudiantes_fisica
print(estudiantes_ambas)  # {'Carlos', 'Elena'}

#OPERADOR DE DIFERENCIA:
ingredientes_disponibles = {"harina", "huevos", "azúcar", "leche", "mantequilla"}
ingredientes_usados = {"harina", "huevos", "azúcar"}

ingredientes_restantes = ingredientes_disponibles - ingredientes_usados
print(ingredientes_restantes)  # {'leche', 'mantequilla'}

#OPERADOR DE DIFERENCIA  SIMETRICA:
equipo_a = {"Juan", "María", "Carlos", "Ana"}
equipo_b = {"Carlos", "Ana", "Pedro", "Lucía"}

miembros_exclusivos = equipo_a ^ equipo_b
print(miembros_exclusivos)  # {'Juan', 'María', 'Pedro', 'Lucía'}

#OPERADORES DE ASIGNACION COMBINADOS:
lenguajes = {"Python", "Java", "C++"}
nuevos_lenguajes = {"Go", "Rust", "TypeScript"}

# Equivalente a: lenguajes = lenguajes | nuevos_lenguajes
lenguajes |= nuevos_lenguajes
print(lenguajes)  # {'Python', 'Java', 'C++', 'Go', 'Rust', 'TypeScript'}

productos_tienda_a = {"laptop", "teléfono", "tablet", "auriculares"}
productos_oferta = {"laptop", "auriculares", "cámara"}

# Mantiene solo los productos que están en oferta
productos_tienda_a &= productos_oferta
print(productos_tienda_a)  # {'laptop', 'auriculares'}

tareas_pendientes = {"informe", "reunión", "correos", "presentación"}
tareas_completadas = {"informe", "correos"}

# Elimina las tareas completadas
tareas_pendientes -= tareas_completadas
print(tareas_pendientes)  # {'reunión', 'presentación'}

inventario_actual = {"mesa", "silla", "lámpara", "estantería"}
nueva_entrega = {"mesa", "sofá", "alfombra", "estantería"}

# Actualiza el inventario: elimina duplicados y añade nuevos
inventario_actual ^= nueva_entrega
print(inventario_actual)  # {'silla', 'lámpara', 'sofá', 'alfombra'}

#OPERADORES DE COMPARACION:
conjunto_a = {1, 2, 3}
conjunto_b = {3, 1, 2}  # Mismo contenido, diferente orden
conjunto_c = {1, 2, 3, 4}

print(conjunto_a == conjunto_b)  # True
print(conjunto_a == conjunto_c)  # False

numeros_pares = {2, 4, 6}
numeros = {1, 2, 3, 4, 5, 6, 7}

print(numeros_pares <= numeros)  # True - todos los elementos están en el segundo conjunto

conjunto_a = {1, 2}
conjunto_b = {1, 2, 3}
conjunto_c = {1, 2}

print(conjunto_a < conjunto_b)  # True - subconjunto propio
print(conjunto_a < conjunto_c)  # False - son iguales

frutas = {"manzana", "naranja", "plátano", "fresa"}
frutas_seleccionadas = {"manzana", "naranja"}

print(frutas >= frutas_seleccionadas)  # True - contiene todos los elementos del segundo

conjunto_a = {1, 2, 3, 4}
conjunto_b = {2, 3}
conjunto_c = {1, 2, 3, 4}

print(conjunto_a > conjunto_b)  # True - superconjunto propio
print(conjunto_a > conjunto_c)  # False - son iguales


#EJEMPLO PRACTICO: ANALISIS DE PREFERENCIAS:
# Preferencias de usuarios sobre géneros de películas
usuario1 = {"acción", "comedia", "ciencia ficción", "aventura"}
usuario2 = {"drama", "comedia", "romance", "documental"}
usuario3 = {"acción", "aventura", "fantasía", "ciencia ficción"}

# Géneros comunes entre usuario1 y usuario3
generos_comunes_1_3 = usuario1 & usuario3
print(f"Géneros comunes entre usuario1 y usuario3: {generos_comunes_1_3}")

# Todos los géneros que le gustan al usuario1 o al usuario2
todos_generos_1_2 = usuario1 | usuario2
print(f"Todos los géneros de usuario1 y usuario2: {todos_generos_1_2}")

# Géneros que le gustan al usuario1 pero no al usuario2
solo_usuario1 = usuario1 - usuario2
print(f"Géneros exclusivos del usuario1: {solo_usuario1}")

# Géneros que le gustan a exactamente uno de usuario2 o usuario3
exclusivos_2_3 = usuario2 ^ usuario3
print(f"Géneros que gustan a usuario2 o usuario3, pero no a ambos: {exclusivos_2_3}")

# Verificar si usuario1 tiene más preferencias que usuario2
tiene_mas_preferencias = len(usuario1) > len(usuario2)
print(f"¿Usuario1 tiene más preferencias que usuario2? {tiene_mas_preferencias}")

# Verificar si todas las preferencias de usuario3 están incluidas en usuario1
todas_incluidas = usuario3 <= usuario1
print(f"¿Todas las preferencias de usuario3 están en usuario1? {todas_incluidas}")



#COMBINACION DE OPERADORES:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

# Elementos que están en A y B, pero no en C
resultado = (A & B) - C
print(resultado)  # {3, 4}

# Elementos que están en A o en C, pero no en B
resultado2 = (A | C) - B
print(resultado2)  # {1, 2, 7, 8}

#RENDIMIENTO DE LOS OPERADORES VS. METODOS:
#EM TERMINOS DE RENDIMIENTO, LSO OPERADORES Y LOS METODOS CORRESPONDIENTES SON EQUIVALENTES,YA QUE INTWENAMWNTW LOS OPERADOES LLAMAN A LOS METODOS
#O METODOS ES PRINCIPALMENTE UNA CUESTION DE ESTILO Y LEGIBILIDAD:

# Estas dos expresiones son equivalentes en funcionalidad y rendimiento
resultado1 = conjunto_a.union(conjunto_b).difference(conjunto_c)
resultado2 = (conjunto_a | conjunto_b) - conjunto_c