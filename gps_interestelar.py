import math

class PlanetarySystem:
    def __init__(self, planets):
        self.planets = planets

    def get_position(self, planet_name, timestamp):
        # Implementar lógica para obter as coordenadas da posição de um planeta em um determinado momento
        # utilizando dados astronômicos e cálculos de órbita

class InterstellarGPS:
    def __init__(self, planetary_system):
        self.planetary_system = planetary_system
        self.earth_coordinates = (0, 0, 0)  # Coordenadas fixas da Terra

    def get_distance(self, planet_name, timestamp):
        planet_position = self.planetary_system.get_position(planet_name, timestamp)
        distance = math.sqrt(
            (self.earth_coordinates[0] - planet_position[0]) ** 2 +
            (self.earth_coordinates[1] - planet_position[1]) ** 2 +
            (self.earth_coordinates[2] - planet_position[2]) ** 2
        )
        return distance

    def get_direction(self, planet_name, timestamp):
        planet_position = self.planetary_system.get_position(planet_name, timestamp)
        direction = (
            planet_position[0] - self.earth_coordinates[0],
            planet_position[1] - self.earth_coordinates[1],
            planet_position[2] - self.earth_coordinates[2]
        )
        return direction

    def navigate(self, planet_name, timestamp):
        distance = self.get_distance(planet_name, timestamp)
        direction = self.get_direction(planet_name, timestamp)
        
        # Implementar lógica para navegar pelo espaço interestelar,
        # levando em conta a rotação dos planetas e os efeitos gravitacionais,
        # com base nas informações de distância e direção obtidas
        
        # Retornar as coordenadas de volta para a Terra

# Exemplo de uso
mercury = Planet("Mercury")
venus = Planet("Venus")
mars = Planet("Mars")
# ... adicionar mais planetas ao sistema

planetary_system = PlanetarySystem([mercury, venus, mars])
gps = InterstellarGPS(planetary_system)

planet_name = "Mars"
timestamp = 123456789  # Momento desejado

distance = gps.get_distance(planet_name, timestamp)
direction = gps.get_direction(planet_name, timestamp)

print("Distância até a Terra:", distance)
print("Direção para a Terra:", direction)

# Resultado esperado:
# Distância até a Terra: <valor em unidades de distância>
# Direção para a Terra: (<valor x>, <valor y>, <valor z>)
