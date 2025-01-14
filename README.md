# Conversor de Imagens Online

Este é um projeto desenvolvido como parte de um **Desafio de Projeto:** **Redução de Dimensionalidade em Imagens para Redes Neurais** da [DIO.me](https://www.dio.me/) em parceria com a Bairedevs.  
O objetivo é criar um programa em Python que processa imagens de uma URL fornecida pelo usuário, convertendo-as para escala de cinza e binarizando-as.  

## Funcionalidades
- Faz o download de uma imagem a partir de uma URL.
- Converte a imagem original para tons de cinza.
- Realiza a binarização da imagem (preto e branco) com base na média dos valores de pixel.
- Exibe as três versões da imagem (original, escala de cinza, binarizada) lado a lado.

## Tecnologias Utilizadas
- **Python 3.10+**
- **Bibliotecas:**
  - `Pillow` para manipulação de imagens.
  - `numpy` para processamento de arrays de pixels.
  - `matplotlib` para exibição das imagens.
  - `requests` para realizar o download da imagem.

## Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/pexize/reducao_dimensionalidade.git
   cd redução_dimensionalidade
   ```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o programa:
```bash
python Image_Binarization.py
```
4. Siga as instruções no terminal:

Insira a URL de uma imagem para processar.
Escolha se deseja processar outra imagem ou encerrar o programa.
Exemplo de Entrada e Saída
Entrada:
URL da imagem:
https://example.com/imagem.jpg

Saída:
O programa exibirá as três versões da imagem:

  1- Original (colorida).
  2- Escala de cinza.
  3- Preto e branco.

  4. Desafio de Projeto
Este projeto faz parte do bootcamp na DIO.me e tem como objetivo aplicar conhecimentos em manipulação de imagens, lógica de programação e interação com APIs.

Licença
Este projeto é de uso livre e aberto a melhorias. Fique à vontade para contribuir!
