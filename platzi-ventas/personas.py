

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad  = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    def despedirse(self):
        return f"Adiós, {self.nombre} se despide."

if __name__ == "__main__":
    persona1 = Persona("Juan", 30)
    print(persona1.saludar())
    print(persona1.despedirse())