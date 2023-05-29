import math

class GPSInterestelar:
    def __init__(self, ponto_de_partida):
        self.ponto_de_partida = ponto_de_partida

    def calcular_coordenadas(self, destino):
        # Coordenadas do ponto de partida (Terra)
        latitude_partida = self.ponto_de_partida[0]
        longitude_partida = self.ponto_de_partida[1]

        # Coordenadas do destino
        latitude_destino = destino[0]
        longitude_destino = destino[1]

        # Converter as coordenadas para radianos
        latitude_partida_rad = math.radians(latitude_partida)
        longitude_partida_rad = math.radians(longitude_partida)
        latitude_destino_rad = math.radians(latitude_destino)
        longitude_destino_rad = math.radians(longitude_destino)

        # Calcular a diferença entre as longitudes
        dif_longitude = longitude_destino_rad - longitude_partida_rad

        # Calcular a distância angular entre os pontos
        dist_angular = math.acos(math.sin(latitude_partida_rad) * math.sin(latitude_destino_rad) +
                                 math.cos(latitude_partida_rad) * math.cos(latitude_destino_rad) *
                                 math.cos(dif_longitude))

        # Calcular a distância em unidades astronômicas (UA)
        distancia_ua = dist_angular * 6371  # Raio médio da Terra em km

        # Calcular a direção em relação ao ponto de partida
        direcao = math.atan2(math.sin(dif_longitude) * math.cos(latitude_destino_rad),
                             math.cos(latitude_partida_rad) * math.sin(latitude_destino_rad) -
                             math.sin(latitude_partida_rad) * math.cos(latitude_destino_rad) *
                             math.cos(dif_longitude))

        # Converter a direção de radianos para graus
        direcao_graus = math.degrees(direcao)
        direcao_graus = (direcao_graus + 360) % 360

        # Retornar as coordenadas de volta para a Terra
        return distancia_ua, direcao_graus


# Ponto de partida (Terra)
ponto_de_partida = (0, 0)

# Destino (planeta distante)
destino = (45, 180)  # Exemplo: latitude 45°N, longitude 180°E

# Criar uma instância do GPSInterestelar
gps = GPSInterestelar(ponto_de_partida)

# Calcular as coordenadas de volta para a Terra
distancia_ua, direcao_graus = gps.calcular_coordenadas(destino)

# Exibir as coordenadas
print("Coordenadas de volta para a Terra:")
print("Distância: {:.2f} UA".format(distancia_ua))
print("Direção: {:.2f}°".format(direcao_graus))
```
