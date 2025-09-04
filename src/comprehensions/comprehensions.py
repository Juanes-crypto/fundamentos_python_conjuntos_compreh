# ================================
# Ejemplos de List Comprehension
# ================================

# Crear una lista con los cuadrados de los números del 0 al 9 (bucle tradicional)
cuadrados = []
for numero in range(10):
    cuadrados.append(numero ** 2)
print("Cuadrados (bucle):", cuadrados)

# Con list comprehension
cuadrados = [numero ** 2 for numero in range(10)]
print("Cuadrados (list comprehension):", cuadrados)

# Números pares del 0 al 9
pares = [numero for numero in range(10) if numero % 2 == 0]
print("Pares:", pares)

# Transformación de datos: Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5) * temp + 32 for temp in celsius]
print("Temperaturas en Fahrenheit:", fahrenheit)

# Extraer nombres de usuarios
usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Elena", "edad": 23}
]
nombres = [usuario["nombre"] for usuario in usuarios]
print("Nombres de usuarios:", nombres)

# Manipulación de cadenas
palabras = ["python", "es", "genial"]
mayusculas = [palabra.upper() for palabra in palabras]
print("Palabras en mayúsculas:", mayusculas)

primeras_letras = [palabra[0] for palabra in palabras]
print("Primeras letras:", primeras_letras)

# Filtrado de datos
numeros = [2, 8, 1, 6, 3, 9, 4]
mayores_que_cinco = [num for num in numeros if num > 5]
print("Mayores que 5:", mayores_que_cinco)

frutas = ["manzana", "banana", "arándano", "pera", "aguacate"]
frutas_con_a = [fruta for fruta in frutas if fruta.startswith('a')]
print("Frutas con 'a':", frutas_con_a)

# Ejemplo real con ventas
ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

valor_por_producto = [item["unidades"] * item["precio"] for item in ventas]
print("Valor por producto:", valor_por_producto)

productos_alto_valor = [item["producto"] for item in ventas if item["unidades"] * item["precio"] > 1000]
print("Productos con alto valor:", productos_alto_valor)


# ================================
# Ejemplos de Dict Comprehension
# ================================

# Crear diccionario con cuadrados
cuadrados = {numero: numero ** 2 for numero in range(5)}
print("Diccionario cuadrados:", cuadrados)

# Diccionario de pares cuadrados
pares_cuadrados = {numero: numero ** 2 for numero in range(10) if numero % 2 == 0}
print("Diccionario pares cuadrados:", pares_cuadrados)

# Transformar diccionario existente
frutas = {"a": "apple", "b": "banana", "c": "cherry"}
frutas_mayusculas = {clave: valor.upper() for clave, valor in frutas.items()}
print("Frutas mayúsculas:", frutas_mayusculas)

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print("Diccionario invertido:", invertido)

# Crear diccionario a partir de listas
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]
persona = {clave: valor for clave, valor in zip(claves, valores)}
print("Persona:", persona)

# Filtrar diccionario
stock = {"manzanas": 10, "plátanos": 3, "naranjas": 25, "peras": 0}
disponibles = {fruta: cantidad for fruta, cantidad in stock.items() if cantidad > 0}
print("Stock disponible:", disponibles)

# Procesamiento de datos estructurados
estudiantes = [
    {"id": 1, "nombre": "Ana", "nota": 8.5},
    {"id": 2, "nombre": "Carlos", "nota": 7.2},
    {"id": 3, "nombre": "Elena", "nota": 9.3}
]

id_nombre = {estudiante["id"]: estudiante["nombre"] for estudiante in estudiantes}
print("ID -> Nombre:", id_nombre)

nombre_nota = {estudiante["nombre"]: estudiante["nota"] for estudiante in estudiantes}
print("Nombre -> Nota:", nombre_nota)


# ================================
# Ejemplos de Set Comprehension
# ================================

# Conjunto de cuadrados
cuadrados = {numero ** 2 for numero in range(5)}
print("Conjunto cuadrados:", cuadrados)

# Eliminar duplicados
numeros = [1, 2, 2, 3, 4, 3, 5, 5, 1]
numeros_unicos = {numero for numero in numeros}
print("Números únicos:", numeros_unicos)

# Conjunto de pares cuadrados
pares_cuadrados = {numero ** 2 for numero in range(10) if numero % 2 == 0}
print("Conjunto pares cuadrados:", pares_cuadrados)

# Primeras letras únicas
palabras = ["manzana", "banana", "mango", "melón", "mora", "naranja"]
primeras_letras = {palabra[0] for palabra in palabras}
print("Primeras letras únicas:", primeras_letras)

# Vocales únicas en texto
texto = "python es un lenguaje de programación versátil"
vocales = {letra for letra in texto.lower() if letra in "aeiou"}
print("Vocales únicas:", vocales)

# Longitudes únicas
palabras = ["casa", "perro", "sol", "luna", "mar", "montaña"]
longitudes_unicas = {len(palabra) for palabra in palabras}
print("Longitudes únicas:", longitudes_unicas)

# Operaciones con sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_doble = {elemento * 2 for elemento in A.union(B)}
print("Unión doble:", union_doble)

interseccion_cuadrado = {elemento ** 2 for elemento in A.intersection(B)}
print("Intersección cuadrado:", interseccion_cuadrado)

# Aplicación real con compras
compras = [
    {"cliente": "Ana", "producto": "laptop"},
    {"cliente": "Juan", "producto": "teléfono"},
    {"cliente": "Ana", "producto": "auriculares"},
    {"cliente": "Pedro", "producto": "laptop"},
    {"cliente": "Juan", "producto": "auriculares"},
    {"cliente": "Ana", "producto": "teléfono"}
]

productos_unicos = {compra["producto"] for compra in compras}
print("Productos únicos:", productos_unicos)

compradores_laptop = {compra["cliente"] for compra in compras if compra["producto"] == "laptop"}
print("Compradores de laptop:", compradores_laptop)

iniciales_clientes = {compra["cliente"][0] for compra in compras}
print("Iniciales de clientes:", iniciales_clientes)