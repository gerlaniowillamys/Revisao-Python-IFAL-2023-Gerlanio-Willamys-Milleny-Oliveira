#Lista de Exercício 2 - Questão 25
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" #O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def interrogatorio():
    print("Interrogatório! Responda com \033[32ms\033[0m ou \033[31mn\033[0m!")
    p1 = input("Telefonou para a vítima? ")
    p2 = input("Esteve no local do crime? ")
    p3 = input("Mora perto da vítima? ")
    p4 = input("Devia para a vítima? ")
    p5 = input("Já trabalhou com a vítima? ")

    sus = 0

    if p1.lower() == "s":
        sus += 1

    if p2.lower() == "s":
        sus += 1

    if p3.lower() == "s":
        sus += 1

    if p4.lower() == "s":
        sus += 1

    if p5.lower() == "s":
        sus += 1

    if sus == 2:
        return "Suspeita"
    elif sus == 3 or sus == 4:
        return "Cúmplice"
    elif sus == 5:
        return "Assassino"
    else:
        return "Inocente"


def main():
    resultado = interrogatorio()
    print(resultado)


if __name__ == "__main__":
    main()
