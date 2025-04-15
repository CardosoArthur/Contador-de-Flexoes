# 🤖 Contador de Flexões com Visão Computacional

Projeto desenvolvido para a disciplina de AI ENGENEERING, COGNITIVE AND SEMANTIC COMPUTATION & IOT, com o objetivo de aplicar técnicas de **visão computacional** para detectar e contar flexões automaticamente usando vídeo.

Equipe: 
Anna Cristina Doná Araujo (RM: 94795)
Arthur de Mesquita Cardoso (RM: 93186)
Felipe Palmeira Feitosa (RM: 92835)
Roberta Roman Ferreira da Costa (RM: 93803)
Felipe Coelho Tiepo (RM:95026)


## 📹 Demonstração

O sistema utiliza um vídeo de uma pessoa realizando flexões e, por meio da biblioteca [MediaPipe](https://google.github.io/mediapipe/), detecta os movimentos do corpo e conta cada repetição com precisão.


---

## 🛠 Tecnologias Utilizadas

- [Python 3.9](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [NumPy](https://numpy.org/)

---

## 📦 Instalação

> **Requisitos:** Python 3.7 ~ 3.10 (MediaPipe não funciona com 3.11 ou superior)

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/contador-flexoes-visao.git
cd contador-flexoes-visao

```

### 2. (Opcional) Crie um ambiente virtual com Python 3.9 usando Conda

```bash
conda create -n visao39 python=3.9
conda activate visao39

```
### 3. Instale as dependências
```bash
pip install opencv-python mediapipe numpy
```
---

## ▶️ Como Executar

1. Certifique-se de que o vídeo flexao.mp4 está na mesma pasta do arquivo app.py.

2. Execute o script:

```bash
python app.py

```

3. O vídeo será analisado em loop infinito até você pressionar a tecla q.

4. O número de flexões será mostrado na tela em tempo real.
