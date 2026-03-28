import time

forca = 5
velocidade = 10
destreza = 78
vitalidade = 67
carisma = 69
inteligencia = 41

def Train():
    print("O que você deseja treinar?")
    time.sleep(1)
    print()
    print("Força = 1")
    time.sleep(0.5)
    print("Velocidade = 2")
    time.sleep(0.5)
    print("Destreza = 3")
    time.sleep(0.5)
    print("Vitalidade = 4")
    time.sleep(0.5)
    print()
    while True:
        escol = input("> ")
        if escol in["1", "2", "3", "4"]:
            break
        else:
            print("Resposta inválida")
            time.sleep(3)

def Status():
    global forca, velocidade, destreza, vitalidade, carisma, inteligencia 
    print("Força = ", forca)
    time.sleep(0.5)
    print("Velocidade =", velocidade)
    time.sleep(0.5)
    print("Destreza =", destreza)
    time.sleep(0.5)
    print("Vitalidade =", vitalidade)
    time.sleep(0.5)
    print("Carisma =", carisma)
    time.sleep(0.5)
    print("Inteligência =", inteligencia)
    input("")

def TrainingLands():
    while True:
        print("Você se encontra no campo de treinamentos")
        time.sleep(0.5)
        print("O que você deseja fazer?")
        time.sleep(1)
        print("Treinar = 1")
        time.sleep(0.5)
        print("Sparring = 2")
        time.sleep(0.5)
        print("Status = 3")
        time.sleep(0.5)
        print("Dar o fora = 4")
        time.sleep(0.5)
        print()
        while True:
            escol = input("> ")
            if escol in["1", "2", "3", "4"]:
                break
            else:
                print("Resposta Inválida!!!")
                time.sleep(3)
                print()
        if escol == "1":
            print()
            Train()
        elif escol == "2":
            print("Sem função ainda")
        elif escol == "3":
            print()
            Status()

TrainingLands()