from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
import csv

class LocalizarPatrimonio(QWidget):
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

        
        # ADICIONAR O LABEL NOME E O LINEEDIT AO LAYOUT VERTICAL
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.btnbuscar=QPushButton("Buscar Patrimônio")
        self.layout_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)

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

        

        # ADICIONAR O LAYOUT V NA TELA
        self.setLayout(self.layout_v)
    
    def localizar(self):
        # Abrir o arquivo csv e atribuir á uma variável
        arquivo=open("clientes.csv","r",encoding="utf8")
        linhas=csv.reader(arquivo)


        for i in linhas:
            lin=str(i).replace("['","").replace("']","").split(";")
            if(lin[0]==self.edit_id.text()):
                self.edit_serie.setText(lin[1])
                self.edit_npatrimonio.setText(lin[2])
                self.edit_tpatrimonio.setText(lin[3])
                self.edit_desc.setText(lin[4])
                self.edit_local.setText(lin[5])
                self.edit_datafab.setText(lin[6])
                self.edit_dataaq.setText(lin[7])
    
    


# Iniciar a aplicação
# app = QApplication(sys.argv)
# tela = LocalizarPatrimonio()
# tela.show()
# app.exec()
