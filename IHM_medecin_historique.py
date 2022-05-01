import sys, paramiko

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QLabel, QFormLayout, QRadioButton, QTextEdit, QGridLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

import matplotlib.pyplot as plt

class Historique(QWidget):
    def __init__(self, fenetre_precedente):
        super().__init__()

        self.fenetre_precedente = fenetre_precedente
        
        self.resize(300,300)

        self.nom = QLineEdit()
        self.nom.setReadOnly(True)
        self.prenom = QLineEdit()
        self.prenom.setReadOnly(True)
        self.age = QLineEdit()
        self.age.setReadOnly(True)
        self.histo = QTextEdit()
        self.histo.setReadOnly(True)

        self.fermer = QPushButton("Fermer")
        self.fermer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.fermer.setMinimumWidth(200)

        self.init_ui()
        self.show()

    def init_ui(self):

        h_box = QFormLayout()
        h_box.addRow(QLabel("Nom"), self.nom)
        h_box.addRow(QLabel("Prenom"), self.prenom)
        h_box.addRow(QLabel("Age"), self.age)

        j1_box = QVBoxLayout()
        j1_box.addWidget(self.fermer)
        j1_box.setAlignment(Qt.AlignCenter)

        j_box = QVBoxLayout()
        j_box.addLayout(h_box)
        j_box.addWidget(self.histo)
        j_box.addLayout(j1_box)

    
        self.setLayout(j_box)
        self.setWindowTitle("Historique du patient")

        self.fermer.clicked.connect(self.btn_fermer)


    def btn_fermer(self):
        self.hide()
        self.fenetre_precedente.show()
 


class HistoriqueController:
    def __init__(self, model):
        self.myModel = model

    def afficher_histo(self):
        self.myModel.afficher_histo_m()

    def fermer(self):
        self.myModel.fermer_m()

class HistoriqueModel:
    def __init__(self):
#        self.hostname = "192.168.1.87"
#        self.username = "etudiant"
#        self.password = "vitrygtr"
#        self.port = 22

        f = open('liste_poids.txt', 'a')
        f.close()

    def afficher_histo(self):
        a=2

    def fermer_m(self):
        a=1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = HistoriqueModel()
    controller = HistoriqueController(model)
    view = Historique(controller)
    sys.exit(app.exec_())