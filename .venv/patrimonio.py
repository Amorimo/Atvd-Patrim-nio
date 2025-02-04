from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # VAMOS CONFIGURAR A GEOMETRIA DA TELA. sETANDO OS VALORES DE POSIÇÃO X E Y ALÉM DE LARGURA E ALTURA
        self.setGeometry(10, 30, 400, 300)

        # UM TEXTO PARA A BARRA DE TITULO
        self.setWindowTitle("Cadastro de Patrimônio")

        # GERENCIADOR DE LAYOUT VERTICAL
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente
        self.label_id = QLabel("Id:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.label_serie = QLabel("Número de série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        self.label_npatrimonio = QLabel("Nome do patrimônio:")
        self.label_npatrimonio.setStyleSheet("QLabel{font-size:12pt}")

        self.label_tpatrimonio = QLabel("Tipo do patrimônio:")
        self.label_tpatrimonio.setStyleSheet("QLabel{font-size:12pt}")

        self.label_desc = QLabel("Descrição:")
        self.label_desc.setStyleSheet("QLabel{font-size:12pt}")

        self.label_local = QLabel("Localização:")
        self.label_local.setStyleSheet("QLabel{font-size:12pt}")

        self.label_datafab = QLabel("Data de fabricação:")
        self.label_datafab.setStyleSheet("QLabel{font-size:12pt}")

        self.label_dataaq = QLabel("Data de aquisição:")
        self.label_dataaq.setStyleSheet("QLabel{font-size:12pt}")

        # LINEEDIT PARA O NOME DO CLIENTE
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_npatrimonio = QLineEdit()
        self.edit_npatrimonio.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_tpatrimonio = QLineEdit()
        self.edit_tpatrimonio.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_datafab = QLineEdit()
        self.edit_datafab.setStyleSheet("QLineEdit{font-size:12px}")

        self.edit_dataaq = QLineEdit()
        self.edit_dataaq.setStyleSheet("QLineEdit{font-size:12px}")

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red; color:white; font-size:12pt; font-weight:bold;}")

        # CHAMAR A FUNÇÃO CADASTRO DO CLIENTE AO CLICAR NO BOTÃO
        self.button.clicked.connect(self.cadastrar)

        # ADICIONAR O LABEL NOME E O LINEEDIT AO LAYOUT VERTICAL
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_npatrimonio)
        self.layout_v.addWidget(self.edit_npatrimonio)

        self.layout_v.addWidget(self.label_tpatrimonio)
        self.layout_v.addWidget(self.edit_tpatrimonio)

        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)

        self.layout_v.addWidget(self.label_datafab)
        self.layout_v.addWidget(self.edit_datafab)

        self.layout_v.addWidget(self.label_dataaq)
        self.layout_v.addWidget(self.edit_dataaq)

        self.layout_v.addWidget(self.button)

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if (self.edit_id.text() == "" or self.edit_serie.text() == "" or self.edit_npatrimonio.text() == "" 
            or self.edit_tpatrimonio.text() == "" or self.edit_desc.text() == "" or self.edit_local.text() == "" 
            or self.edit_datafab.text() == "" or self.edit_dataaq.text() == ""):
            QMessageBox.critical(self, "Erro", "Você deve preencher todos os campos")
        else:
            # Criando variável que fará referência ao arquivo de texto
            arquivo = open("clientes.csv", "+a")
            arquivo.write(f"{self.edit_id.text()};")
            arquivo.write(f"{self.edit_serie.text()};")
            arquivo.write(f"{self.edit_npatrimonio.text()};")
            arquivo.write(f"{self.edit_tpatrimonio.text()};")
            arquivo.write(f"{self.edit_desc.text()};")
            arquivo.write(f"{self.edit_local.text()};")
            arquivo.write(f"{self.edit_datafab.text()};")
            arquivo.write(f"{self.edit_dataaq.text()}\n")
            arquivo.close()
            QMessageBox.information(self, "Salvo", "Dados Salvos")


# Iniciar a aplicação
# app = QApplication(sys.argv)
# tela = cadastropatrimonio()
# tela.show()
# app.exec()
