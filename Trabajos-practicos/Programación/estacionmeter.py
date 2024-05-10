class EstacionMeteorologica:

  def __init__(self, latitud, longitud, estado_bateria):
 
    self.latitud = latitud
    self.longitud = longitud
    self.estado_bateria = estado_bateria
    self.temperatura = None
    self.lluvia_caida = 15

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
      return "SW"
    elif direccion < 292.5:
      return "W"
    elif direccion < 337.5:
      return "NW"
    else:
      return "N"


estacion_meteorologica = EstacionMeteorologica(37.7833, -122.4167, 100)

estacion_meteorologica.temperatura = 20.5
estacion_meteorologica.lluvia_caida = 15

direccion_viento = 180

direccion_cardinal = estacion_meteorologica.convertir_direccion_viento(direccion_viento)

print(f"Latitud: {estacion_meteorologica.latitud}")
print(f"Longitud: {estacion_meteorologica.longitud}")
print(f"Estado de batería: {estacion_meteorologica.estado_bateria}%")
print(f"Temperatura: {estacion_meteorologica.temperatura}°C")
print(f"Lluvia caída: {estacion_meteorologica.lluvia_caida} mm")
print(f"Dirección del viento: {direccion_cardinal}")
