print("=== PROGRAMA: ANÁLISIS DE ESTUDIANTES POR ASIGNATURA ===\n")

estudiantes_matematicas = {"juan", "esteban", "mateo", "santiago", "sebas"}
estudiantes_fisica = {"juan", "esteban", "mateo", "richi", "kevin"}
estudiantes_programacion = {"mundungus", "anonimous", "richi", "sebas", "brayan"}

print("="*25, "CONJUNTOS INICIALES", "="*25)
print(f"conjunto de estudiantes que cursan matematicas: {estudiantes_matematicas}")
print(f"conjunto de estudiantes que cursan fisica: {estudiantes_fisica}")
print(f"conjunto de estudiantes que cursan programacion: {estudiantes_programacion}")

print("Analisis de intersecciones y diferencias")

tres_asignaturas = estudiantes_matematicas & estudiantes_fisica & estudiantes_programacion
print(f"Estudiantes que cursan las tres asignaturas: {tres_asignaturas}")


mat_fis_no_prog = (estudiantes_matematicas & estudiantes_fisica) - estudiantes_programacion
print(f"Estudiantes que cursan matemáticas y física, pero no programación: {mat_fis_no_prog}")


solo_una_asignatura = (estudiantes_matematicas | estudiantes_fisica | estudiantes_programacion) - \
                      (estudiantes_matematicas & estudiantes_fisica) - \
                      (estudiantes_matematicas & estudiantes_programacion) - \
                      (estudiantes_fisica & estudiantes_programacion)
print(f"Estudiantes que solo cursan una asignatura: {solo_una_asignatura}")


todos_estudiantes = estudiantes_matematicas | estudiantes_fisica | estudiantes_programacion


print(f"Total de estudiantes únicos: {todos_estudiantes}")
print(f"Número total de estudiantes: {len(todos_estudiantes)}")