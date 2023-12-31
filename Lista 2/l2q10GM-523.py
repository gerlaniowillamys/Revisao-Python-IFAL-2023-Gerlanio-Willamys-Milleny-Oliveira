#Lista de Exercício 2 - Questão 10
#Dupla: 2021316110 - Gerlânio Willamys e 2021317055 - Milleny Oliveira
#Disciplina: Programação Web
#Professor: Ítalo Arruda
#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def saudacao_turno(turno):
    turno = turno.lower()

    if turno == "m":
        return "Bom dia!"
    elif turno == "v":
        return "Boa tarde!"
    elif turno == "n":
        return "Boa noite!"
    else:
        return "Turno inválido."


def main():
    try:
        turno = input("[M] Matutino\n[V] Vespertino\n[N] Noturno\nDigite seu turno: ")
        mensagem_saudacao = saudacao_turno(turno)
        print(mensagem_saudacao)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")


if __name__ == "__main__":
    main()
