# Validar_acceso

print("*** Validar Acceso de Usuario ***")  # Título de la consola

# Credenciales correctas predefinidas
usuario_correcto = "admin"
password_correcta = "1234"

# Entrada del usuario
usuario = input("Escriba su usuario: ")
password = input("Escriba su password: ")

# Validación
if usuario == usuario_correcto and password == password_correcta:
    print("✅ Acceso permitido")
else:
    print("❌ Acceso denegado")
