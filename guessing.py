import random
# Guessing Game v.1.0
print("--------------------------------------")
print("          M&M Guessing game!")
print("--------------------------------------")

mm_count = random.randint(1, 100)
chances = 5
while(chances > 0 ):
    intento = int(input("Di tu propuesta: "))
    if (intento == mm_count):
        chances = -1;
        print(f"Lo conseguiste! El número correcto era {intento}")
    else:
        if (intento > mm_count):
            print(f"Lo lamento, no es correcto, el número buscado es menor que {intento}")
            chances -= 1
        else:
            print(f"Lo lamento, no es correcto, el número buscado es mayor que {intento}")
            chances -= 1

if (chances == 0):
    print(f"GAME OVER"
          f"1: No has sido capaz de encontrar el número. El número correcto era {mm_count}")


