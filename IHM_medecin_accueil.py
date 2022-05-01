import sys, paramiko, sqlite3

from PyQt5.QtWidgets import (QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QApplication, QWidget, QLabel, QFormLayout)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import *

from IHM_medecin_dossier import Dossier, DossierController, DossierModel
from IHM_medecin_importer import Importer, ImporterController, ImporterModel

class accueilMenu(QWidget):
    def __init__(self, controller, dossierController, importerController):
        super().__init__()

        self.myController = controller
        self.dossier = Dossier(self, dossierController)
        self.importer2 = Importer(self, importerController)

        self.resize(300,200)

        self.logo = QLabel(self)
        self.pixmap = QPixmap('logo2.png')
        self.logo.setPixmap(self.pixmap.scaled(100,100))
        self.logo.setAlignment(Qt.AlignCenter)

        self.nom_plateforme = QLabel("e-platforme \n")
        self.nom_plateforme.setAlignment(Qt.AlignCenter)
        self.nom_plateforme.setStyleSheet("color : #0B848C")
        self.message_bienvenue = QLabel("Bienvenue sur votre e-plateforme")
        self.message_bienvenue.setAlignment(Qt.AlignCenter)

        self.creer = QPushButton("Créer un dossier")
        self.creer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
    
        self.importer = QPushButton("Importer un dossier")
        self.importer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()
        self.show()

    def init_ui(self):

        h_box = QVBoxLayout()
        h_box.addWidget(self.logo)
        h_box.addWidget(self.nom_plateforme)
        h_box.addWidget(self.message_bienvenue)
        h_box.addWidget(self.creer)
        h_box.addWidget(self.importer)
        h_box.setAlignment(Qt.AlignCenter)

        self.setLayout(h_box)

        self.creer.clicked.connect(self.btn_creer)
        self.importer.clicked.connect(self.btn_importer)

    def btn_creer(self):
        self.hide()
        self.dossier.show()
        print("btn creer")

    def btn_importer(self):
        self.hide()
        self.importer2.show()
        print("btn importer")


class accueilController:
    def __init__(self, model):
        self.myModel = model

    def importer(self):
        self.myModel.importer_m()

class accueilModel:
    def __init__(self):
#        self.hostname = "192.168.1.87"
#        self.username = "etudiant"
#        self.password = "vitrygtr"
#        self.port = 22

        conn = sqlite3.connect('patients.db')
        conn.close()
        
#        sftp.put(fichier_machine,chemin) #remet le fichier
#        t.close()

    
    def importer_m(self):

#        t = paramiko.Transport((self.hostname,self.port))
#        t.connect(username=self.username,password=self.password)
#        sftp = paramiko.SFTPClient.from_transport(t)

        a=1

#        chemin = "/home/etudiant/liste_poids.txt"
#        sftp.get(chemin,fichier_machine)
#        sftp.put(fichier_machine,chemin)

#        t.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = accueilModel()
    dossierModel= DossierModel()
    importerModel = ImporterModel()
    dossierController = DossierController(dossierModel)
    importerController = ImporterController(importerModel)
    controller = accueilController(model)
    menu = accueilMenu(controller, dossierController, importerController)
    sys.exit(app.exec_())