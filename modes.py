#
# Copyright 2020-2025 Manuel Barrette
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

""" Initialize windows and make the main window appear """
import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
import platform
import locale, ctypes
from glob import glob

results = glob(os.getcwd() + "/**/", recursive=True)
for result in results:
    if result[-2] != "_":
        sys.path.insert(1, result)

import modes_main_window
import dialog_modes

# Initialize windows
app = QApplication(sys.argv)
window_Modes = QMainWindow()
dialog = QDialog()

systeme_exploitation = platform.system()
if systeme_exploitation == 'Windows':
    langwin = ctypes.windll.kernel32
    langue_sys = locale.windows_locale[langwin.GetUserDefaultUILanguage()]
elif systeme_exploitation == 'Darwin' or 'Linux':
    langue_sys = locale.getlocale()[0]
langue_sys = langue_sys[0:2]
translator = QtCore.QTranslator()
directory = "locales"
if langue_sys == "fr":
    langue = "fr_CA"
else:
    langue = "en_CA"
translator.load(langue, directory)
app.installTranslator(translator)

ui_Modes = modes_main_window.Ui_MainWindow()
ui_Dial = dialog_modes.Ui_Dialog()

ui_Dial.setupUi(dialog)
ui_Modes.setupUi(window_Modes, dialog, None)

# Make main window appear
window_Modes.show()
sys.exit(app.exec())
