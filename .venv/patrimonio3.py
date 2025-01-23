from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class cadastropatrimonioverif(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(10, 30, 400, 300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("Cadastro de atualização de Patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente
        self.label_id = QLabel("Id:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.label_serie = QLabel("Número de série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        self.label_ultverif = QLabel("Data da última verificação:")
        self.label_ultverif.setStyleSheet("QLabel{font-size:12pt}")

        self.label_obs = QLabel("Observação:")
        self.label_obs.setStyleSheet("QLabel{font-size:12pt}")

    
        # LINEEDIT PARA O NOME DO CLIENTE
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_ultverif = QLineEdit()
        self.edit_ultverif.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_obs = QLineEdit()
        self.edit_obs.setStyleSheet("QLineEdit{font-size:12px}")


        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(self.cadastrar)

        # ADICIONAR O LABEL NOME E O LINEEDIT AO LAYOUT VERTICAL
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_ultverif)
        self.layout_v.addWidget(self.edit_ultverif)

        self.layout_v.addWidget(self.label_obs)
        self.layout_v.addWidget(self.edit_obs)



        self.layout_v.addWidget(self.button)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Criando variável que fará referêcia ao arquivo de texto
        arquivo = open("atualizações.txt", "+a")

        arquivo.write(f"Id:{self.edit_id.text()}\n")
        arquivo.write(f"Número de série:{self.edit_serie.text()}\n")
        arquivo.write(f"Última verificação:{self.edit_ultverif.text()}\n")
        arquivo.write(f"Observação:{self.edit_obs.text()}\n")
        
        
        arquivo.write("-------------------------------------------------------------------------------------------------------")
        

        arquivo.close()

# Iniciar a aplicação
app = QApplication(sys.argv)
tela = cadastropatrimonioverif()
tela.show()
app.exec()
