from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def UpdateResult1():
    text = str(amount1.text())
    result1.append(text + " PLN")
    row1.append(int(text))
    amount1.clear()
    sum1 = sum(row1, 0)
    add_up1.setText("SUMA               " + str(sum1))
    DifferenceUpdate()


def UpdateResult2():
    text1 = str(amount2.text())
    result2.append(text1 + " PLN")
    row2.append(int(text1))
    amount2.clear()
    sum2 = sum(row2, 0)
    add_up2.setText("SUMA               " + str(sum2))
    DifferenceUpdate()


def DifferenceUpdate():
    substraction = ((sum(row1, 0)) - (sum(row2, 0)))
    if substraction == 0:
        Difference.setText("Jesteśmy kwita")
    elif substraction > 0:
        Difference.setText("Daniel jest winny:  " + str(substraction))
    elif substraction < 0:
        Difference.setText("Ola jest winna:  " + str(-substraction))


# Empty Lists
row2 = [0]
row1 = [0]


# Main Window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Wydatki mieszkaniowe")
window.setFixedWidth(400)
window.setFixedHeight(250)


# Widgets
grid = QGridLayout()
result1 = QTextBrowser()
result1.setAlignment(Qt.AlignRight)
result1.setFont(QFont("Arial", 12))

result2 = QTextBrowser()
result2.setAlignment(Qt.AlignRight)
result2.setFont(QFont("Arial", 12))

amount1 = QLineEdit()
amount1.setValidator(QIntValidator())
amount1.setFont(QFont("Arial", 12))
amount1.setAlignment(Qt.AlignRight)

amount2 = QLineEdit()
amount2.setValidator(QIntValidator())
amount2.setFont(QFont("Arial", 12))
amount2.setAlignment(Qt.AlignRight)

description_row1 = QLabel("Wydatki Ola")
description_row1.setFont(QFont("Arial", 16))
description_row1.setAlignment(Qt.AlignCenter)

description_row2 = QLabel("Wydatki Daniel")
description_row2.setFont(QFont("Arial", 16))
description_row2.setAlignment(Qt.AlignCenter)

add_up1 = QLineEdit("SUMA                   ")
add_up1.setAlignment(Qt.AlignRight)
add_up1.setFont(QFont("Arial", 12))
add_up1.setReadOnly(True)

add_up2 = QLineEdit("SUMA                  ")
add_up2.setAlignment(Qt.AlignRight)
add_up2.setFont(QFont("Arial", 12))
add_up2.setReadOnly(True)

Difference = QLineEdit()
Difference.setReadOnly(True)
Difference.setFont(QFont("Arial", 12))
Difference.setAlignment(Qt.AlignCenter)

months = QComboBox()

# Layout
grid.addWidget(description_row1, 0, 0)
grid.addWidget(description_row2, 0, 1)
grid.addWidget(result1, 1, 0)
grid.addWidget(result2, 1, 1)
grid.addWidget(amount1, 2, 0)
grid.addWidget(amount2, 2, 1)
grid.addWidget(add_up1, 3, 0)
grid.addWidget(add_up2, 3, 1)
grid.addWidget(Difference, 4, 0, 1, 2)

grid.addWidget(months, 5, 0)
window.setLayout(grid)

# Value entering
amount1.returnPressed.connect(UpdateResult1)
amount2.returnPressed.connect(UpdateResult2)


window.show()
sys.exit(app.exec())
