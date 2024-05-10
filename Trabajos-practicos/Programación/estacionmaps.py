import random
class EstacionMeteorologica:


  def __init__(self):
   
    self.latitud = -31.604444
    self.longitud = -64.448889
    self.estado_bateria = random.randint(1, 100)
    self.temperatura = random.randint(5, 40)
    self.lluvia_caida = random.randint(5, 30)

  def convertir_direccion_viento(self, direccion):
   
    if direccion < 0 or direccion >= 360:
      raise ValueError("La dirección del viento debe estar entre 0 y 360 grados.")

    if direccion < 22.5:
      return "N"
    elif direccion < 67.5:
      return "NE"
    elif direccion < 112.5:
      return "E"
    elif direccion < 157.5:
      return "SE"
    elif direccion < 202.5:
      return "S"
    elif direccion < 247.5:
      return "SO"
    elif direccion < 292.5:
      return "O"
    elif direccion < 337.5:
      return "NO"
    else:
      return "N"

# Ejemplo de uso
temporal = EstacionMeteorologica()

print(f"Latitud: {temporal.latitud}")
print(f"Longitud: {temporal.longitud}")
print(f"Estado de batería: {temporal.estado_bateria}%")
print(f"Temperatura: {temporal.temperatura}°C")
print(f"Lluvia caída: {temporal.lluvia_caida} mm")

direccion_viento = random.randint(1, 360)

direccion_cardinal = temporal.convertir_direccion_viento(direccion_viento)

print(f"Dirección del viento: {direccion_cardinal}")
