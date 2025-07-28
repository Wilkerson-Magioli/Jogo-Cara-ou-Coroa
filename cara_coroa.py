# O modulo random do Python fornece funções para gerar números aleatórios e 
# fazer operações relacionadas e aleatorias, como sorteios, escolhas aleatórias e embaralhamento de dados.
# Aqui no jogo ele foi necessário para usar a função random.choice, que sorteia aleatoriamente a moeda com cara ou coroa,
# que eu vou mostrar mais adiante.

import random

# Variável que define o nome do arquivo, onde as pontuações dos jogadores serão salvas.

ARQUIVO_RANKING = "ranking.txt"

# Abre o arquivo chamado "ranking.txt", através da variável "ARQUIVO_RANKING" e converte os pontos 
# (que estão como strings) para inteiros, gerando uma lista de tuplas do tipo (nome, pontos).
# Se o arquivo não existir, retorna uma lista vazia (FileNotFoundError).

def ler_ranking():
    try:
        with open(ARQUIVO_RANKING, "r") as arquivo:
            linhas = arquivo.readlines()
            ranking = [linha.strip().split(",") for linha in linhas]
            ranking = [(nome, int(pontos)) for nome, pontos in ranking]
            return ranking
    except FileNotFoundError:
        return []

# Salva a pontuação de um jogador no final do arquivo "ranking.txt".
# Abre o arquivo definido pela variável "ARQUIVO_RANKING" no modo append ("a"), 
# o que significa que o conteúdo será adicionado ao final do arquivo, sem apagar o que já existe.

def salvar_pontuacao(nome, pontuacao):
    with open(ARQUIVO_RANKING, "a") as arquivo:
        arquivo.write(f"{nome},{pontuacao}\n")

# Mostra o ranking de forma organizada, com os jogadores em ordem decrescente de pontos.

def mostrar_ranking():
    ranking = ler_ranking()
    if not ranking:
        print("\nNenhum jogador no ranking ainda.\n")
        return

    print("\n🏆 Ranking dos Jogadores 🏆")
    ranking.sort(key=lambda x: x[1], reverse=True)
    for i, (nome, pontos) in enumerate(ranking, 1):
        print(f"{i}. {nome} - {pontos} ponto(s)")
    print()

# Exibe as opções disponíveis com emojis.

def mostrar_opcoes_com_emojis():
    print("\nEscolha uma das opções:")
    print("1️⃣  🙂  Cara")
    print("2️⃣  👑  Coroa")



# Dá boas-vindas ao jogador e pede o nome do jogador.
# Define as opções possíveis e emojis associados.
# Também mostra o historico que guarda o resultado de cada jogada.
# A pontuacao começa em 0.

def jogar():
    print("🪙  Bem-vindo ao jogo de Cara ou Coroa!\n")
    nome = input("Digite seu nome: ")
    opcoes = ["cara", "coroa"]
    emojis = {"cara": "🙂", "coroa": "👑"}
    historico = []
    pontuacao = 0


# Loop contínuo até o jogador digitar "sair".

    while True:
        mostrar_opcoes_com_emojis()
        
        
# O usuário pode escolher a opção, cara ou coroa, sair do jogo ou ver o ranking.

        escolha_usuario = input("Digite 'cara' ou 'coroa' / 'sair' para encerrar / 'ranking' para ver ranking): ").lower()

        
# Esse trecho de código abaixo, não é uma função, mas usa funções como: "mostrar_ranking()" e "salvar_pontuacao()"
# dentro de uma estrutura de decisão (if) e controle de laço (continue ou break). 

        if escolha_usuario == "ranking":
            mostrar_ranking()
            continue

        if escolha_usuario == "sair":
            print(f"\n{nome}, você terminou com {pontuacao} ponto(s)!")
            salvar_pontuacao(nome, pontuacao)
            print("\nHistórico de jogadas:")
            for i, (escolha, resultado, acertou) in enumerate(historico, 1):
                status = "Acertou!" if acertou else "Errou!"
                print(f"{i}. Você escolheu {escolha} {emojis[escolha]}, saiu {resultado} {emojis[resultado]} → {status}")
            break

        if escolha_usuario not in opcoes:
            print("Escolha inválida. Tente novamente com 'cara' ou 'coroa'.\n")
            continue
        
# random.choice é uma função do módulo random do Python, que serve para escolher aleatoriamente um item de uma sequência.         
# A moeda é "jogada" com random.choice.
# È a lógica principal do jogo de cara ou coroa, realizar o sorteio e verificar se o jogador acertou ou não. 

        resultado = random.choice(opcoes)
        acertou = escolha_usuario == resultado

# Se o usuário acertar ganha ponto.
# Mostra o resultado da jogada e se acertou ou errou.

        if acertou:
            pontuacao += 1

        print(f"\n🪙 Jogando a moeda...")
        print(f"Resultado: {resultado.upper()} {emojis[resultado]}")
        print("🎉 Você acertou!\n" if acertou else "❌ Você errou!\n")

# Essa linha de código registra uma jogada, mas não definem uma função. 
# Guarda os dados de cada jogada para poder, por exemplo, exibir o histórico depois.
# Cada jogada é salva com a escolha, o resultado e se acertou ou não.
  
        historico.append((escolha_usuario, resultado, acertou))

# Essa linha de código inicia o jogo chamando a função jogar().

jogar()
