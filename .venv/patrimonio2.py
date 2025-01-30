from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class patrimonioloc(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(10, 30, 400, 300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("Cadastro de localização de Patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente
        self.label_id = QLabel("Id:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        self.label_logra = QLabel("Logradouro:")
        self.label_logra.setStyleSheet("QLabel{font-size:12pt}")

        self.label_num = QLabel("Número:")
        self.label_num.setStyleSheet("QLabel{font-size:12pt}")

        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")

        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")

        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        # LINEEDIT PARA O NOME DO CLIENTE
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_logra = QLineEdit()
        self.edit_logra.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_num = QLineEdit()
        self.edit_num.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12px}")


        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(self.cadastrar)

        # ADICIONAR O LABEL NOME E O LINEEDIT AO LAYOUT VERTICAL
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        self.layout_v.addWidget(self.label_logra)
        self.layout_v.addWidget(self.edit_logra)

        self.layout_v.addWidget(self.label_num)
        self.layout_v.addWidget(self.edit_num)

        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)


        self.layout_v.addWidget(self.button)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Criando variável que fará referêcia ao arquivo de texto
        arquivo = open("localização.csv", "+a")

        arquivo.write(f"{self.edit_id.text()};")
        arquivo.write(f"{self.edit_empresa.text()};")
        arquivo.write(f"{self.edit_logra.text()};")
        arquivo.write(f"Número:{self.edit_num.text()}\n")
        arquivo.write(f"Prédio:{self.edit_predio.text()}\n")
        arquivo.write(f"Andar:{self.edit_andar.text()}\n")
        arquivo.write(f"Sala:{self.edit_sala.text()}\n")
        
        arquivo.write("-------------------------------------------------------------------------------------------------------")
        

        arquivo.close()

# Iniciar a aplicação
# app = QApplication(sys.argv)
# tela = cadastropatrimonioloc()
# tela.show()
# app.exec()
