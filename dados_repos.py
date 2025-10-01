import requests
import pandas as pd
from dados import DadosRepositorios
from repositorios import ManipulaRepositorios
from math import ceil

amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_df_linguagens()

# Salvando os dados 
ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')

# instanciando um objeto
novo_repo = ManipulaRepositorios('VictorHNascimento')

# Criando o repositório
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')

