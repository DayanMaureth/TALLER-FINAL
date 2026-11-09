import warnings

class Producto:
    PRECIO_MIN = 0
    PRECIO_MAX = 10000

    def __init__(self, nombre):
        # Atributos privados
        self.__nombre = nombre
        self.__precios_historicos = []

    # --- Nombre (solo lectura) ---
    @property
    def nombre(self):
        return self.__nombre

    # --- Historial (copia, para no exponer la lista privada) ---
    @property
    def precios_historicos(self):
        return list(self.__precios_historicos)

    # --- Precio actual: getter y setter con validación ---
    @property
    def precio_actual(self):
        if not self.__precios_historicos:
            return None
        return self.__precios_historicos[-1]

    @precio_actual.setter
    def precio_actual(self, valor):
        if valor < self.PRECIO_MIN or valor > self.PRECIO_MAX:
            warnings.warn(
                f"Precio inválido (${valor:,.2f}). Debe estar entre "
                f"${self.PRECIO_MIN:,} y ${self.PRECIO_MAX:,}. "
                f"El registro no fue modificado.",
                stacklevel=2,
            )
            return  # No altera el registro
        self.__precios_historicos.append(valor)

    # --- Método para registrar un nuevo precio ---
    def registrar_precio(self, precio):
        self.precio_actual = precio  # pasa por el setter (validación)

    # --- Precio promedio (propiedad) ---
    @property
    def precio_promedio(self):
        if not self.__precios_historicos:
            return 0
        return sum(self.__precios_historicos) / len(self.__precios_historicos)

    def __str__(self):
        return (f"Producto: {self.__nombre} | Historial: "
                f"{self.__precios_historicos} | Promedio: ${self.precio_promedio:,.2f}")


def demo_ejercicio_1():
    print("=" * 60)
    print("EJERCICIO 1: Inventario y Precios")
    print("=" * 60)

    p = Producto("Arroz Diana 1kg")
    p.registrar_precio(4500)
    p.registrar_precio(5200)
    p.precio_actual = 4800          # usando el setter directamente

    print(p)
    print(f"Precio actual: ${p.precio_actual:,}")

    print("\n-> Intentando registrar valores inválidos:")
    p.registrar_precio(-300)        # negativo
    p.registrar_precio(15000)       # superior a $10,000
    p.precio_actual = 10001         # superior a $10,000

    print("\n-> Estado final (sin cambios por los inválidos):")
    print(p)
    print(f"Precio promedio: ${p.precio_promedio:,.2f}\n")


# =====================================================================
# EJERCICIO 2: Sistema de Cotización de Envíos
# =====================================================================
class Envio:
    def __init__(self, peso_kg, distancia_km):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base):
        """Método base: sin recargo. Las subclases lo sobrescriben."""
        return monto_base

    def __str__(self):
        return f"{self.__class__.__name__} ({self.peso_kg} kg, {self.distancia_km} km)"


class EnvioEstandar(Envio):
    RECARGO = 0.05  # 5 %

    def calcular_costo(self, monto_base):
        return monto_base * (1 + self.RECARGO)


class EnvioExpress(Envio):
    RECARGO = 0.15  # 15 %

    def calcular_costo(self, monto_base):
        return monto_base * (1 + self.RECARGO)


def demo_ejercicio_2():
    print("=" * 60)
    print("EJERCICIO 2: Cotización de Envíos (Polimorfismo)")
    print("=" * 60)

    # Lista mixta de envíos
    envios = [
        EnvioEstandar(peso_kg=2.5, distancia_km=120),
        EnvioExpress(peso_kg=1.0, distancia_km=300),
        EnvioEstandar(peso_kg=10, distancia_km=45),
        EnvioExpress(peso_kg=5.5, distancia_km=80),
    ]

    monto_base = 20000  # monto base del paquete

    print(f"Monto base: ${monto_base:,.2f}\n")
    for envio in envios:
        costo = envio.calcular_costo(monto_base)   # polimorfismo
        print(f"{envio}  ->  Costo total: ${costo:,.2f}")


if __name__ == "__main__":
    demo_ejercicio_1()
    demo_ejercicio_2()
