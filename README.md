# Extrator de Paletas de Cores

Projeto desenvolvido em Python para extrair paletas de cores predominantes a partir de imagens, utilizando processamento de pixels e técnicas de aprendizado de máquina.

## Como funciona

O programa analisa os pixels da imagem, representando cada um por seus valores RGB (vermelho, verde e azul). Em seguida, utiliza o algoritmo **K-Means** para agrupar pixels com cores semelhantes.

O K-Means divide os dados em *K grupos (clusters)*, buscando aproximar os pontos de cada grupo de um centroide. Nesse projeto, cada centroide representa uma cor predominante da imagem, permitindo gerar uma paleta com as principais tonalidades encontradas.

## Tecnologias utilizadas

- **Python:** desenvolvimento do projeto.
- **NumPy:** manipulação dos dados numéricos dos pixels.
- **Pillow:** carregamento e processamento das imagens.
- **Matplotlib:** visualização das paletas de cores geradas.
- **Scikit-learn:** aplicação do algoritmo K-Means.

## Objetivo

Explorar aplicações de aprendizado de máquina não supervisionado e processamento de imagens, transformando informações visuais em dados que podem ser analisados e visualizados.
