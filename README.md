# Gerador de Paleta de Cores (Python)

Um programa em **Python** que recebe uma imagem e extrai as suas cores dominantes usando **K-Means**, um algoritmo de clustering. Além da paleta, ele mostra como os pixels se agrupam por meio de gráficos.

> Segundo projeto de uma série em que exploro o lado menos óbvio de cada linguagem: **Julia** (sistema solar 3D com GLMakie), **Python** (este aqui) e **R** (flow field com ggplot2).

## Como funciona

1. A imagem é redimensionada e convertida numa matriz de pixels (**Pillow** + **NumPy**).
2. Cada pixel é tratado como um ponto no espaço RGB, e os pontos são agrupados com **K-Means** (**Scikit-learn**).
3. O centro de cada cluster vira uma das cores dominantes da imagem.
4. Tudo é visualizado com **Matplotlib**:
   - distribuição 3D dos pixels no espaço de cor;
   - contagem de pixels por cluster;
   - proporção percentual de cada cor.

## Requisitos

- Python 3.9 ou superior
- Bibliotecas:

```bash
pip install pillow numpy scikit-learn matplotlib
```

## O que dá pra mexer

- **Número de clusters:** define quantas cores dominantes você quer extrair. Poucos clusters resumem a imagem, muitos capturam nuances.
- **Tamanho da imagem redimensionada:** imagens menores rodam mais rápido, com pequena perda de precisão nas cores.
- **A imagem de entrada:** fotos, ilustrações e capturas de tela dão paletas bem diferentes.
