import sys, paramiko, sqlite3

from PyQt5.QtWidgets import (QToolTip, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QLabel, QFormLayout, QRadioButton, QTextEdit, QGridLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *

from IHM_medecin_historique import Historique

class Dossier(QWidget):
    def __init__(self, fenetre_accueil, controller):
        super().__init__()

        self.fenetre_accueil = fenetre_accueil
        self.histo = Historique(self)
        self.myController = controller
        
        self.nom = QLineEdit()
        self.nom.setPlaceholderText("Entrez le nom")
        self.prenom = QLineEdit()
        self.prenom.setPlaceholderText("Entrez le prenom")
        self.age = QLineEdit()
        self.age.setPlaceholderText("Entrez l'age")

        self.homme = QRadioButton("M") 
        self.femme = QRadioButton("F")

        self.homme.setStyleSheet("QRadioButton::checked:hover"
                                    "{"
                                    "background-color : #0B848C"
                                    "}")
        self.femme.setStyleSheet("QRadioButton::checked:hover"
                                    "{"
                                    "background-color : #0B848C;"
                                    "}")

        self.historique = QPushButton("Historique")
        self.historique.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.historique.setMaximumWidth(200)
        self.symptomes = QTextEdit()
        self.symptomes.setPlaceholderText("Inscrivez les symptomes ici")

        self.medicaments = QTextEdit()
        self.medicaments.setReadOnly(True)
        self.medicaments.setPlaceholderText("Médicaments proposés")

        QToolTip.setFont(QFont('Arial', 14))
        self.enregistrer = QPushButton("Enregistrer")    
        self.enregistrer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.enregistrer.setToolTip('Cliquez ici pour enregistrer les symptomes')
        self.enregistrer.setMinimumWidth(200)
#        self.enregistrer.resize(enregistrer.sizeHint())

        self.fermer = QPushButton("Fermer")
        self.fermer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 7px ; color : white")
        self.fermer.setToolTip('Cliquez ici pour revenir au menu')
        self.fermer.setMinimumWidth(200)

        self.init_ui()
        self.show()

    def init_ui(self):

        g_box = QHBoxLayout()
        g_box.addWidget(self.homme)
        g_box.addWidget(self.femme)

        h_box = QFormLayout()
        h_box.addRow(QLabel("Nom"), self.nom)
        h_box.addRow(QLabel("Prenom"), self.prenom)
        h_box.addRow(QLabel("Age"), self.age)
        h_box.addRow(QLabel("Sexe"), g_box)

        i_box = QHBoxLayout()
        i_box.addWidget(self.historique)
        i_box.setAlignment(Qt.AlignCenter)

        j1_box = QVBoxLayout()
        j1_box.addWidget(self.enregistrer)
        j1_box.setAlignment(Qt.AlignCenter)

        j_box = QVBoxLayout()
        j_box.addWidget(self.symptomes)
        j_box.addLayout(j1_box)

        k1_box = QVBoxLayout()
        k1_box.addWidget(self.fermer)
        k1_box.setAlignment(Qt.AlignCenter)

        k_box = QVBoxLayout()
        k_box.addWidget(self.medicaments)
        k_box.addLayout(k1_box)

        m_box = QGridLayout()
        m_box.addLayout(h_box, 0, 0)
        m_box.addLayout(i_box, 0, 1)
        m_box.addLayout(j_box, 1, 0)
        m_box.addLayout(k_box, 1, 1)

        self.setLayout(m_box)
        self.setWindowTitle("Dossier du patient")

        self.historique.clicked.connect(self.btn_historique)
        self.enregistrer.clicked.connect(self.btn_enregistrer)
        self.fermer.clicked.connect(self.btn_fermer)

    def btn_historique(self):
        self.hide()
        self.histo.show()

    def btn_enregistrer(self):
        if (self.homme.isChecked()):
            self.myController.register(self.nom.text(), self.prenom.text(), self.age.text(), "homme", self.symptomes.toPlainText())
        else:
            self.myController.register(self.nom.text(), self.prenom.text(), self.age.text(), "femme", self.symptomes.toPlainText())

    def btn_fermer(self):
        self.hide()
        self.fenetre_accueil.show()
        self.histo.hide()
 
class DossierController:
    def __init__(self, model):
        self.myModel = model

    def historique(self):
        self.myModel.historique_m()

    def register(self, nom, prenom, age, sexe, symptomes):
        self.myModel.enregistrer_m(nom, prenom, age, sexe, symptomes)

class DossierModel:
    def __init__(self):
#        self.hostname = "192.168.1.87"
#        self.username = "etudiant"
#        self.password = "vitrygtr"
#        self.port = 22

        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nom TEXT,
            prenom TEXT,
            age INTEGER,
            sexe TEXT,
            symptomes TEXT
        )
        """)
        conn.commit()
        conn.close()

    def historique_m(self):
#        t = paramiko.Transport((self.hostname,self.port)) #connecter a la vm
#        t.connect(username=self.username,password=self.password)
#        sftp = paramiko.SFTPClient.from_transport(t) #naviguer dans les fichiers

#        fichier_machine = 'liste_poids.txt'

#        chemin = "/home/etudiant/liste_poids.txt"
#        sftp.get(chemin,fichier_machine) #prend le fichier

        f = open('liste_poids.txt', 'a')
        f.write("a")
        f.write('\n')
        f.close()
        
#        sftp.put(fichier_machine,chemin) #remet le fichier

#        t.close()

    def enregistrer_m(self, nom, prenom, age, sexe, symptomes):

#        t = paramiko.Transport((self.hostname,self.port))
#        t.connect(username=self.username,password=self.password)
#        sftp = paramiko.SFTPClient.from_transport(t)

#        fichier_machine = 'liste_poids.txt'

#        chemin = "/home/etudiant/liste_poids.txt"
#        sftp.get(chemin,fichier_machine)

        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()
        data = {"nom" :nom, "prenom" :prenom, "age" :age, "sexe" :sexe, "symptomes" :symptomes}
        cursor.execute("""
        INSERT INTO patients(nom, prenom, age, sexe, symptomes) VALUES(:nom, :prenom, :age, :sexe, :symptomes)""", data)
        conn.commit()
        conn.close()

#        sftp.put(fichier_machine,chemin)

#        t.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = DossierModel()
    controller = DossierController(model)
    view = Dossier(controller)
    sys.exit(app.exec_())