# pyqt6_user_manager.py

import sys

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (QApplication, 
    QListWidget, 
    QListWidgetItem, 
    QMessageBox, 
    QPushButton, 
    QWidget)

from userdao import UserDao

dao = UserDao()

users = dao.get_users()


app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(1200, 400, 600, 400)

btn = QPushButton("Press Me", window)
btn.setGeometry(50, 50, 80, 40)

def on_click():
    QMessageBox.information(window, "Clicked", "You clicked the button")


btn.clicked.connect(on_click)


user_list = QListWidget(window)
user_list.setGeometry(50, 100, 300, 250)
for user in users:
    list_item = QListWidgetItem(user.name)
    user_list.addItem(list_item)

window.show()
app.exec()