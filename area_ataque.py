# Área de ataque
print("*** Ejercicio de Python aplicado a Ciberseguridad ***")

# Datos de red simulados
red = "Servidor_Web"
ip_inicial = "192.168.1.10"
hosts = 50
puertos_abiertos = 10

# Cálculo del área de ataque potencial
area_ataque = hosts * puertos_abiertos

# Mostrar el resultado
print(f"La red {red} con IP {ip_inicial} tiene un área de ataque de {area_ataque}")
