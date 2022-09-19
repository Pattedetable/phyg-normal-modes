#
# Copyright 2020-2022 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.animation as anim
import os, platform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, parent):

        self.figure = plt.figure()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # Quit
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 17, 0, 1, 3)

#        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # Export video
#        self.pushButton.setObjectName("pushButton")
#        self.gridLayout.addWidget(self.pushButton, 11, 0, 1, 3)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget) # Restart
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 16, 0, 1, 3)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget) # Fondamental
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setAutoExclusive(False)
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 3)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.horizontalSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 3)

        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget) # 2e harmonique
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.radioButton2, 3, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.horizontalSlider2 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.horizontalSlider2.setMinimum(0)
        self.horizontalSlider2.setMaximum(10)
        self.horizontalSlider2.setPageStep(5)
        self.horizontalSlider2.setObjectName("horizontalSlider2")
        self.gridLayout.addWidget(self.horizontalSlider2, 5, 0, 1, 3)

        self.radioButton3 = QtWidgets.QRadioButton(self.centralwidget) # 3e harmonique
        self.radioButton3.setObjectName("radioButton3")
        self.radioButton3.setAutoExclusive(False)
        self.gridLayout.addWidget(self.radioButton3, 6, 0, 1, 3)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.horizontalSlider3 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.horizontalSlider3.setMinimum(0)
        self.horizontalSlider3.setMaximum(10)
        self.horizontalSlider3.setPageStep(5)
        self.horizontalSlider3.setObjectName("horizontalSlider3")
        self.gridLayout.addWidget(self.horizontalSlider3, 8, 0, 1, 3)

        self.radioButton4 = QtWidgets.QRadioButton(self.centralwidget) # 4e harmonique
        self.radioButton4.setObjectName("radioButton4")
        self.radioButton4.setAutoExclusive(False)
        self.gridLayout.addWidget(self.radioButton4, 9, 0, 1, 3)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.horizontalSlider4 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.horizontalSlider4.setMinimum(0)
        self.horizontalSlider4.setMaximum(10)
        self.horizontalSlider4.setPageStep(5)
        self.horizontalSlider4.setObjectName("horizontalSlider4")
        self.gridLayout.addWidget(self.horizontalSlider4, 11, 0, 1, 3)

        self.radioButton5 = QtWidgets.QRadioButton(self.centralwidget) # 5e harmonique
        self.radioButton5.setObjectName("radioButton5")
        self.radioButton5.setAutoExclusive(False)
        self.gridLayout.addWidget(self.radioButton5, 12, 0, 1, 3)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)

        self.horizontalSlider5 = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self.centralwidget)
        self.horizontalSlider5.setMinimum(0)
        self.horizontalSlider5.setMaximum(10)
        self.horizontalSlider5.setPageStep(5)
        self.horizontalSlider5.setObjectName("horizontalSlider5")
        self.gridLayout.addWidget(self.horizontalSlider5, 14, 0, 1, 3)


        self.canvas = FigureCanvas(self.figure) # Graph
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 3, 18, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 25))
        self.menubar.setObjectName("menubar")
        self.menu_aide = QtWidgets.QMenu(self.menubar)
        self.menu_aide.setObjectName("menu_aide")
        MainWindow.setMenuBar(self.menubar)
        self.action_propos = QtGui.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menu_aide.addAction(self.action_propos)
        self.menubar.addAction(self.menu_aide.menuAction())

        # Initial parameters
        self.horizontalSlider.setValue(10)
        self.horizontalSlider2.setValue(0)
        self.horizontalSlider3.setValue(0)
        self.horizontalSlider4.setValue(0)
        self.horizontalSlider5.setValue(0)
        self.radioButton.toggle()



        # Operating system detection
        self.systeme_exploitation = platform.system()
#        if self.systeme_exploitation == "Darwin":
#            self.pushButton.setDisabled(True)

        self.retranslateUi(MainWindow)

        # Start animation
        self.animationTempsReel()

        # Buttons triggers
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider2.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider3.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider4.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.horizontalSlider5.valueChanged['int'].connect(lambda: self.stopAnim())
        self.horizontalSlider5.valueChanged['int'].connect(lambda: self.animationTempsReel())
        self.horizontalSlider5.valueChanged['int'].connect(lambda: self.retranslateUi(MainWindow))
        self.radioButton.toggled.connect(lambda: self.stopAnim())
        self.radioButton.toggled.connect(lambda: self.animationTempsReel())
        self.radioButton2.toggled.connect(lambda: self.stopAnim())
        self.radioButton2.toggled.connect(lambda: self.animationTempsReel())
        self.radioButton3.toggled.connect(lambda: self.stopAnim())
        self.radioButton3.toggled.connect(lambda: self.animationTempsReel())
        self.radioButton4.toggled.connect(lambda: self.stopAnim())
        self.radioButton4.toggled.connect(lambda: self.animationTempsReel())
        self.radioButton5.toggled.connect(lambda: self.stopAnim())
        self.radioButton5.toggled.connect(lambda: self.animationTempsReel())
        self.pushButton_3.clicked.connect(lambda: self.stopAnim())
        self.pushButton_3.clicked.connect(lambda: self.animationTempsReel())


#        self.pushButton.clicked.connect(lambda: self.stopAnim())
#        self.pushButton.clicked.connect(lambda: self.exporterAnimation())
        self.pushButton_2.clicked.connect(lambda: plt.close())
        self.pushButton_2.clicked.connect(lambda: self.fermerEtAfficher(MainWindow, parent))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Modes propres"))
        self.pushButton_2.setText(self._translate("MainWindow", "Quitter"))
        self.pushButton_3.setText(self._translate("MainWindow", "Redémarrer"))
#        self.pushButton.setText(self._translate("MainWindow", "Exporter en vidéo (.mp4)"))
        self.radioButton.setText(self._translate("MainWindow", "Fondamental"))
        self.radioButton2.setText(self._translate("MainWindow", "2e harmonique"))
        self.radioButton3.setText(self._translate("MainWindow", "3e harmonique"))
        self.radioButton4.setText(self._translate("MainWindow", "4e harmonique"))
        self.radioButton5.setText(self._translate("MainWindow", "5e harmonique"))
        self.label.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider.value()/10))
        self.label_2.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider2.value()/10))
        self.label_3.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider3.value()/10))
        self.label_4.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider4.value()/10))
        self.label_5.setText(self._translate("MainWindow", "Amplitude") + " [m] : " + str(self.horizontalSlider5.value()/10))
        self.menu_aide.setTitle(self._translate("MainWindow", "Aide"))
        self.action_propos.setText(self._translate("MainWindow", "À propos"))

    def disableAll(self, boolean):
        self.horizontalSlider.setDisabled(boolean)
        self.horizontalSlider2.setDisabled(boolean)
        self.horizontalSlider3.setDisabled(boolean)
        self.horizontalSlider4.setDisabled(boolean)
        self.horizontalSlider5.setDisabled(boolean)
#        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
        self.pushButton_3.setDisabled(boolean)
        self.menu_aide.setDisabled(boolean)
        self.radioButton.setDisabled(boolean)
        self.radioButton2.setDisabled(boolean)
        self.radioButton3.setDisabled(boolean)
        self.radioButton5.setDisabled(boolean)
        self.radioButton5.setDisabled(boolean)
        self.label.setDisabled(boolean)
        self.label_2.setDisabled(boolean)
        self.label_3.setDisabled(boolean)
        self.label_4.setDisabled(boolean)
        self.label_5.setDisabled(boolean)


    def fermerEtAfficher(self, MainWindow, window_autre):
        if window_autre:
            window_autre.show()
        MainWindow.close()
#        app = QtWidgets.QApplication.instance()
#        app.closeAllWindows()

    def stopAnim(self):
        self.oscillation.event_source.stop()

    def enregistrer(self):
        if self.systeme_exploitation == 'Windows':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOMEPATH'), 'Vidéos (*.mp4)')
        elif self.systeme_exploitation == 'Darwin' or 'Linux':
            fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregister sous..."), os.getenv('HOME'), 'Vidéos (*.mp4)')
        else:
            print("Système non supporté officiellement.  Enregistrement dans le dossier de travail sous le nom 'animation.mp4'.")
            fichier = ['animation', None]
        return fichier[0]

    def exporterAnimation(self):
        nom_anim = self.enregistrer()
        if nom_anim[-4:] != ".mp4":
            nom_anim = nom_anim + ".mp4"
        self.oscillation.save(nom_anim)
        self.animationTempsReel()


    def initAnimation(self):
        """ Define parameters and setup the base graphic """

        self.figure.clear()

        # Important parameters
        nb_particules = 1
        num_frames = 90
        longueur = 10
        vitesse = 1
        couleur = 'k'

        grillex = np.linspace(0, longueur, 200)

        ax2 = self.figure.add_subplot(111)

#        ax2.set_ylabel(self._translate("MainWindow", "Position") + " (m)")
#        ax2.set_xlabel(self._translate("MainWindow", "Temps") + " (s)")
#        ax2.grid(True)
#        ax2.set_yticks([-amplitude, 0, amplitude])

        ax2.axis([-1, longueur+1, -10, 10])
        ax2.set_xticks([])
        ax2.set_yticks([])

        deplacement = 0*grillex
        graph2, = ax2.plot(grillex, deplacement, color=couleur)

        return num_frames, grillex, deplacement, longueur, vitesse, graph2


    def animationTempsReel(self):
        """ Display the animation in real time """

        [num_frames, grillex, deplacement, longueur, vitesse, graph2] = self.initAnimation()

        period = 2*np.pi/(2*np.pi*vitesse/(2*longueur))
#        period = 2*period
#        num_frames = int(num_frames*period)

        tempss = np.linspace(0, period, num_frames)

        def update(i):
            temps = tempss[i]
            deplacement = 0
            if self.radioButton.isChecked():
                amplitude = self.horizontalSlider.value()/10
                vecteur_onde = 2*np.pi/(2*longueur)
                omega = 2*np.pi*vitesse/(2*longueur)
                deplacement = deplacement + 2*amplitude*np.sin(vecteur_onde*grillex)*np.cos(omega*temps)
            if self.radioButton2.isChecked():
                amplitude = self.horizontalSlider2.value()/10
                vecteur_onde = 2*np.pi/(longueur)
                omega = 2*2*np.pi*vitesse/(2*longueur)
                deplacement = deplacement + 2*amplitude*np.sin(vecteur_onde*grillex)*np.cos(omega*temps)
            if self.radioButton3.isChecked():
                amplitude = self.horizontalSlider3.value()/10
                vecteur_onde = 2*np.pi/(2*longueur/3)
                omega = 3*2*np.pi*vitesse/(2*longueur)
                deplacement = deplacement + 2*amplitude*np.sin(vecteur_onde*grillex)*np.cos(omega*temps)
            if self.radioButton4.isChecked():
                amplitude = self.horizontalSlider4.value()/10
                vecteur_onde = 2*np.pi/(longueur/2)
                omega = 4*2*np.pi*vitesse/(2*longueur)
                deplacement = deplacement + 2*amplitude*np.sin(vecteur_onde*grillex)*np.cos(omega*temps)
            if self.radioButton5.isChecked():
                amplitude = self.horizontalSlider5.value()/10
                vecteur_onde = 2*np.pi/(2*longueur/5)
                omega = 5*2*np.pi*vitesse/(2*longueur)
                deplacement = deplacement + 2*amplitude*np.sin(vecteur_onde*grillex)*np.cos(omega*temps)
            graph2.set_ydata(deplacement)
        self.oscillation = anim.FuncAnimation(self.figure, update, frames=num_frames, repeat=True, interval=40)
        self.canvas.draw()

