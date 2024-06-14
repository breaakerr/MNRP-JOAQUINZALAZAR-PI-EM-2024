import random
import builtins

class Assassin:

    def __init__(self) :
        self.vida = 100
        self.armadura = 300
        self.moral = 100
        self.suerte = 50
def obtener_accion():
 
  while True:
    accion = builtins.input("¿Qué quieres hacer con el Asesino? (ayudar/golpear): ").lower()
    if accion in ("ayudar", "golpear"):
      return accion
    else:
      print("Acción no válida. Ingresa 'ayudar' o 'golpear'.")
def ayudar_assassin(assassin):
   
    vida_aumentada = random.randint(1, 20)
    armadura_aumentada = random.randint(1, 30)
    moral_aumentada = random.randint(1, 15)

    assassin.vida += vida_aumentada
    assassin.armadura += armadura_aumentada
    assassin.moral += moral_aumentada

    print(f"Has ayudado al Assassin. Sus estadísticas han mejorado:")
    print(f"Vida: {assassin.vida}")
    print(f"Armadura: {assassin.armadura}")
    print(f"Moral: {assassin.moral}")

def golpear_assassin(assassin):
   
    vida_restada = random.randint(1, 15)
    moral_restada = random.randint(1, 15)

    assassin.vida -= vida_restada
    assassin.moral -= moral_restada

    print(f"Has golpeado al Assassin. Sus estadísticas han empeorado:")
    print(f"Vida: {assassin.vida}")
    print(f"Moral: {assassin.moral}")
      
def main():
 assassin = Assassin()

accion = obtener_accion()

if accion == "ayudar":
    
    print("Has decidido ayudar al Assassin.")
else:
    
    print("Has decidido golpear al Assassin.")

if __name__ == "__main__":
    main()