class Alojamiento:
    # Clase para gestionar la información de un alojamiento

    def __init__(self, nombre, tipo, precio, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.capacidad = capacidad

    def mostrar_info(self):
        # Devuelve la información formateada
        return f"Alojamiento: {self.nombre} | Tipo: {self.tipo} | Precio: ${self.precio} | Capacidad: {self.capacidad} personas"

    def precio_por_persona(self):
        # Devuelve None si los datos no son válidos
        if self.precio <= 0 or self.capacidad <= 0:
            return None
        # Calcula el costo por persona redondeado a 2 decimales
        return round(self.precio / self.capacidad, 2)

    # 2. precio_por_persona()

    # Debe devolver el precio que corresponde pagar por persona.
    # Si precio o capacidad no son válidos (capacidad o precio <= 0), 
    # no debe lanzar error: debe devolver None.
    # El resultado debe estar redondeado a 2 decimales.


# Objeto 1
casa = Alojamiento(
    "Casa Centro",
    "Casa",
    1800,
    6
)

# Objeto 2
departamento = Alojamiento(
    "Departamento Reforma",
    "Departamento",
    1200,
    4
)


# Completa las instrucciones necesarias para:
# 1. Mostrar la información de la casa.
# 2. Mostrar el precio por persona de la casa.
# 3. Mostrar la información del departamento.
# 4. Mostrar el precio por persona del departamento.