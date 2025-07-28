# Cara ou Coroa
### Jogo criado na cadeira de Algoritmos e Estrutura de Dados I no Terceiro Semestre.
🎮 Apresentação do Código: Jogo de Cara ou Coroa com Ranking
Este projeto é um jogo simples de cara ou coroa, desenvolvido em Python, com o objetivo de praticar conceitos fundamentais da linguagem como controle de fluxo, manipulação de arquivos e listas, além de interação com o usuário. A seguir, explico as principais partes do código:
🧠 Lógica do Jogo:
O jogo funciona da seguinte maneira:
•	O usuário escolhe entre “cara” ou “coroa”.
•	O programa simula um lançamento de moeda (usando random.choice).
•	Se a escolha do usuário for igual ao resultado sorteado, ele ganha um ponto.
•	O jogo continua até o jogador digitar “sair”.
📂 Ranking:
•	O jogo salva a pontuação do jogador em um arquivo chamado ranking.txt.
•	Quando o usuário digita "ranking", o programa exibe um ranking ordenado com os jogadores e suas pontuações.
•	Os dados são armazenados como: nome,pontuação e são carregados ao iniciar o jogo.
📋 Histórico:
•	Ao final do jogo, o sistema mostra o histórico de todas as jogadas, com os resultados e se o jogador acertou ou errou, junto de emojis que tornam o jogo mais visual e divertido.
🔧 Funções Importantes:
•	ler_ranking(): lê os dados do arquivo de ranking e os transforma em uma lista de tuplas.
•	salvar_pontuacao(): grava o nome e a pontuação do jogador no arquivo.
•	mostrar_ranking(): exibe o ranking ordenado por pontuação.
•	mostrar_opcoes_com_emojis(): imprime as opções com emojis para tornar a interface mais amigável.
•	jogar(): função principal que controla o fluxo do jogo e interage com o usuário.
