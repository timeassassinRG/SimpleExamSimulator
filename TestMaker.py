from multiprocessing.spawn import prepare
import random
import time

def MakeARandomQuestion(ListaDomande, ListaRisposte, ListaRisposteCorrette, questionLen, questionCounter):
    point = 0
    n = random.randint(0, questionLen-1)
    print("-----------------------------------------------------------------")
    print("Domanda numero ", questionCounter)
    print(ListaDomande[n], "\n")
    risposte = ListaRisposte[n]
    for i in risposte.split(";"):
        print(i)
    risposta = input("Risposta: ")
    risposta.upper()
    if risposta == ListaRisposteCorrette[n]:
        print("Corretto! \n")
        point = point + 1
    else:
        print("Incorretto! \n")
        print("la risposta corretta e'", ListaRisposteCorrette[n] , "\n")
    ListaDomande.pop(n)
    ListaRisposte.pop(n)
    ListaRisposteCorrette.pop(n)
    return point

def PreparaTest():
    print("inizio a prepare il test")
    time.sleep(0.5)
    print("ricorda che in caso di risposte multiple devi mettere le risposte come seguono (es. A B C)")
    time.sleep(1.5)
    print("Test pronto")


exitCondition = False
while(exitCondition == False):
    ListaDomande = []
    ListaRisposte = []
    ListaRisposteCorrette = []
    questionLen = 0
    with open("Questions.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            ListaDomande.append(line)
    with open("Answers.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip(";")
            ListaRisposte.append(line)
    with open("CorrectAnswers.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            ListaRisposteCorrette.append(line)

    questionLen = len(ListaDomande)
    str = input("quante domande vuoi fare? ")
    nDomande = int(str)
    point = 0
    if nDomande > questionLen:
        nDomande = questionLen
        print("hai inserito troppe domande, farai il test con tutte le domande a disposizione cioe' ", questionLen)
    questionCounter = 1
    PreparaTest()
    for i in range(nDomande):
        point += MakeARandomQuestion(ListaDomande, ListaRisposte, ListaRisposteCorrette, questionLen, questionCounter)
        questionCounter += 1
        questionLen = questionLen - 1
    print("hai ottenuto ", point, " punti su ", nDomande)

    stop = input("\n 1)scrivi stop per uscire \n 2)scrivi start per ripartire \n qualunque altro input chiuderà il simulatore ")
    if stop != "start":
        exitCondition = True
exit