import sys, paramiko, sqlite3

from PyQt5.QtWidgets import (QToolTip, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QLabel, QFormLayout, QRadioButton, QTextEdit, QGridLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *

from IHM_medecin_dossier_importe import Dossier_importe, Dossier_importeController, Dossier_importeModel
#from IHM_medecin_accueil import Menu

class Importer(QWidget):
    def __init__(self, fenetre_accueil2, controller):
        super().__init__()

        self.myController = controller
        self.fenetre_accueil2 = fenetre_accueil2

        model = Dossier_importeModel()
        controller2 = Dossier_importeController(model)

        self.resize(300,400)

        self.liste_patients = QTextEdit()
        self.liste_patients.setReadOnly(True)
        self.liste_patients.setPlaceholderText("Liste des patients :")
        self.liste_patients.setText(str(self.myController.getList()))

        self.id_selectionne = QLineEdit()
        self.id_selectionne.setPlaceholderText("Entrez l'id")
        self.dossier_importe = Dossier_importe(self, controller2, self.id_selectionne.text())

        QToolTip.setFont(QFont('Arial', 14))

        self.importer_id = QPushButton("Importer ce dossier")
        self.importer_id.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.importer_id.setMaximumWidth(200)
        self.importer_id.setToolTip("Cliquez ici pour importer le dossier de l'id entré")

        self.fermer = QPushButton("Fermer")
        self.fermer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.fermer.setToolTip('Cliquez ici pour revenir au menu')
        self.fermer.setMinimumWidth(200)

        self.init_ui()
#        self.show()

    def init_ui(self):

        i_box = QHBoxLayout()
        i_box.addWidget(self.id_selectionne)
        i_box.addWidget(self.importer_id)

        f_box = QVBoxLayout()
        f_box.addWidget(self.liste_patients)
        f_box.addLayout(i_box)
        f_box.addWidget(self.fermer)

        self.setLayout(f_box)
        self.setWindowTitle("Dossier du patient")

        self.importer_id.clicked.connect(self.btn_importer_id)
        self.fermer.clicked.connect(self.btn_fermer)

    def btn_importer_id(self):
        self.hide()
        self.dossier_importe.show()


    def btn_fermer(self):
        self.hide()
        self.fenetre_accueil2.show()
#        self.histo.hide()

    
 
class ImporterController:
    def __init__(self, model):
        self.myModel = model

    def historique(self):
        self.myModel.historique_m()

    def register(self, nom, prenom, age, sexe, symptomes):
        self.myModel.enregistrer_m(nom, prenom, age, sexe, symptomes)

    def getList(self):
        return self.myModel.getList()


class ImporterModel:
    def __init__(self):
#        self.hostname = "192.168.1.87"
#        self.username = "etudiant"
#        self.password = "vitrygtr"
#        self.port = 22

        conn = sqlite3.connect('patients.db')
        conn.close()


    def historique_m(self):
#        t = paramiko.Transport((self.hostname,self.port)) #connecter a la vm
#        t.connect(username=self.username,password=self.password)
#        sftp = paramiko.SFTPClient.from_transport(t) #naviguer dans les fichiers

#        fichier_machine = 'liste_poids.txt'

#        chemin = "/home/etudiant/liste_poids.txt"
#        sftp.get(chemin,fichier_machine) #prend le fichier

        print("historique")
        
#        sftp.put(fichier_machine,chemin) #remet le fichier
#        t.close()


    def getList(self):
        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT id, prenom, nom, sexe FROM patients""")
        list = []
        for row in cursor:
            list.append((str(row[0]), str(row[1]), str(row[2]), str(row[3])))
            list.append("/n")
        conn.close()
        return list
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("main ezoeo a")
    model = ImporterModel()
    controller = ImporterController(model)
    view = Importer(controller)
    
    sys.exit(app.exec_())