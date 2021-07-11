from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
import sys
import random

# variáveis
num_secreto = random.randrange(50)

class Janela(QMainWindow):
    tentativas = 1
    def __init__(self):
        super().__init__()
        # iniciando pontuação do jogo
        self.pontos = 250

        # tela
        self.__distancia_da_esquerda = 40
        self.__distancia_do_topo = 40
        self.__largura = 800
        self.__altura = 600
        self.__titulo = 'Jogo da Adivinhação'

        # botão
        self.botao = QPushButton('CHUTAR', self)
        self.botao.move(190, 350)  # posição x e y
        self.botao.resize(380, 30) # largura e altura
        self.botao.clicked.connect(self.botao_click)
        self.botao.setStyleSheet(
            'QPushButton{background-color:#eb4d4d; font-size:15px; color:#fff}')

            # texto 1
        self.label = QLabel(self)
        self.label.move(25, 40)  # posição x e y
        self.label.resize(1000, 80)  # largura e altura
        self.label.setStyleSheet('QLabel{color:#eb4d4d; font-size:30px}')
            # texto 2
        self.label2 = QLabel(self)
        self.label2.setText('⚠O número secreto está entre 0️ e 50⚠')
        self.label2.move(20, 100)  # posição x e y
        self.label2.resize(1000, 100) # largura e altura
        self.label2.setStyleSheet('QLabel{color:#eb4d4d; font:bold; font-size:30px}')
            # texto 3
        self.label3 = QLabel(self)
        self.label3.setText('🔻CHUTE UM NÚMERO ABAIXO🔻')
        self.label3.move(25, 160)  # posição x e y
        self.label3.resize(1000, 100) # largura e altura
        self.label3.setStyleSheet('QLabel{color:#eb4d4d; font-size:30px}')

        # caixa de texto
        self.textBox = QLineEdit(self)
        self.textBox.move(190, 300)  # posição x e y
        self.textBox.resize(380, 40) # largura e altura
        self.textBox.setStyleSheet('QLineEdit{color:#eb4d4d; font:bold; font-size:20px}')

    # carregando a janela do jogo
    def carregarJanela(self):
        self.setGeometry(self.__distancia_da_esquerda,self.__distancia_do_topo, self.__largura, self.__altura)
        self.setWindowTitle(self.__titulo)
        self.show()


    def botao_click(self):
        max_tentativas = 10
        chute = 0
        
        # 'try' 'except' para tentar armazenar o chute. Caso o chute seje vazio ou contenha letras, o código cai no 'except' (linha 96)
        try:
            chute = int(self.textBox.text())# lendo chute
            self.textBox.clear()# limpando caixa de texto
            self.label.setText(f'Número digitado👉 {chute}')

            if chute <= 0:
                self.label2.setText('Não digite números menores que zero!🤦‍♂️')
                self.label3.setText('')
                self.label.setText('')

            self.tentativas = self.tentativas+1
            print(self.tentativas)

            # calculando pontuação
            resultado = chute - num_secreto
            if resultado < 0:
                resultado *= -1
            self.pontos -= resultado
            self.label3.setText(f"Você possui 🎲{self.pontos}🎲 pontos ")

            # verificando número inserido
            if chute == num_secreto:
                self.label2.setText('🏆VOCÊ ACERTOU!🏆 toma aqui sua medalha 🏅🤏')
                self.label3.setText(f"Você ganhou com {self.pontos} pontos 👏👏👏")
                self.botao.setEnabled(False)
            else:
                if chute > num_secreto:
                    self.label2.setText('Seu chute é maior que o número secreto 🛫🛫')
                else:
                    self.label2.setText('Seu chute é menor que o número secreto ⛵⛵')

            if (self.tentativas >= max_tentativas) or (self.pontos <= 0):
                self.label2.setText('VOCÊ PERDEU!😭😭😭😭')
                self.label3.setText(f"Você perdeu com {self.pontos} pontos 💔")
                self.botao.setEnabled(False)
        except:
            chute = 0
            self.label.setText('Opa, digite um número mano...😂😂')
            self.label2.setText('')
            self.label3.setText('')
            self.textBox.clear()


def func():
    app = QApplication(sys.argv)
    janela = Janela()

    input()
    janela.carregarJanela()
    sys.exit(app.exec())


if __name__ == '__main__':
    func()
