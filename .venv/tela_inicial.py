import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from patrimonio3 import patrimonioverif
from patrimonio2 import patrimonioloc
from localizar_patrimonio import LocalizarPatrimonio

class telainicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v=QVBoxLayout()
        

        self.label_titulo=QLabel("Clique para abrir a janela")
        self.buttoncad=QPushButton("Abrir patrimonio")
        self.buttonloc=QPushButton("Abrir Localização de patrimônio")
        self.buttonatt=QPushButton("Abrir Atualizações de patrimônio")
        self.buttonlocalizar=QPushButton("Localizar")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.buttoncad)
        self.layout_v.addWidget(self.buttonloc)
        self.layout_v.addWidget(self.buttonatt)
        self.layout_v.addWidget(self.buttonlocalizar)


        self.buttoncad.clicked.connect(self.abrir_cadastro)
        self.buttonloc.clicked.connect(self.abrir_local)
        self.buttonatt.clicked.connect(self.abrir_att)
        self.buttonlocalizar.clicked.connect(self.abrir_localizar)

        self.setLayout(self.layout_v)
    def abrir_att (self):
        self.pat=patrimonioverif()

        self.setLayout(self.layout_v)
    def abrir_local (self):
        self.pat=patrimonioloc()
        self.pat.show()

        self.setLayout(self.layout_v)
    def abrir_cadastro (self):
        self.pat=Patrimonio()
        self.pat.show()

        self.setLayout(self.layout_v)
    def abrir_localizar (self):
        self.pat=LocalizarPatrimonio()
        self.pat.show()

app=QApplication(sys.argv)
tela=telainicial()
tela.show()
app.exec()