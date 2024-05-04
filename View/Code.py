import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QGridLayout, \
    QStackedWidget, QApplication
import pymysql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.reg = "Зарегистрироватся"
        self.log = "Войти"

        self.setWindowTitle("VPN")
        self.setFixedSize(QSize(270, 200))
        self.setStyleSheet("background-color: black;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget()
        self.stack1 = self.widget_one()
        self.stacked_widget.addWidget(self.stack1)
        self.stack2 = self.widget_two()
        self.stacked_widget.addWidget(self.stack2)

        self.swap = QPushButton("Войти")
        self.swap.setStyleSheet("""
            QPushButton {
                    background-color: "black";
                    color: "white";
                    }""")

        self.swap.clicked.connect(self.swap_to_widget)
        self.swap.setFixedSize(150, 40)
        self.swap.setCheckable(True)

        self.layout = QGridLayout(self.central_widget)
        self.layout.addWidget(self.stacked_widget)
        self.layout.addWidget(self.swap, 4, 0)

    def widget_one(self):
        widget_one = QWidget()
        layout = QGridLayout(widget_one)

        self.Login_one = QLineEdit(self)
        self.Qlabel_Login_one = QLabel("Логин: ")
        self.Qlabel_Login_one.setStyleSheet("color: white")
        self.Login_one.setFixedSize(100, 23)
        self.Qlabel_Login_one.setFixedSize(100, 23)

        self.Login_one.setStyleSheet("QLineEdit"
                                      "{"
                                      "background : White"
                                      "}")

        self.Password_one = QLineEdit(self)
        self.Qlabel_Password_one = QLabel("Пароль:  ")
        self.Qlabel_Password_one.setStyleSheet("color: white")
        self.Password_one.setFixedSize(100, 23)
        self.Qlabel_Password_one.setFixedSize(100, 23)

        self.Password_one.setStyleSheet("QLineEdit"
                                      "{"
                                      "background : White"
                                      "}")

        self.Email_one = QLineEdit(self)
        self.Qlabel_Email_one = QLabel("Почта: ")
        self.Qlabel_Email_one.setStyleSheet("color: white")
        self.Email_one.setFixedSize(100, 23)
        self.Qlabel_Email_one.setFixedSize(100, 23)

        self.Email_one.setStyleSheet("QLineEdit"
                                      "{"
                                      "background : White"
                                      "}")


        self.button_upload = QPushButton("Подтвердить")
        self.button_upload.setStyleSheet("""
            QPushButton {
                    background-color: "black";
                    color: "white";
                    }""")
        self.button_upload.clicked.connect(self.Insert_to_db)
        self.button_upload.setFixedSize(75, 40)


        layout.addWidget(self.Qlabel_Login_one, 0, 0)
        layout.addWidget(self.Login_one, 0, 1)

        layout.addWidget(self.Qlabel_Password_one, 1, 0)
        layout.addWidget(self.Password_one, 1, 1)

        layout.addWidget(self.Qlabel_Email_one, 2, 0)
        layout.addWidget(self.Email_one, 2, 1)

        layout.addWidget(self.button_upload, 3, 0)


        return widget_one

    def widget_two(self):
        widget_two = QWidget()
        layout = QGridLayout(widget_two)

        self.Login_two = QLineEdit(self)
        self.Qlabel_Login_two = QLabel("Логин: ")
        self.Qlabel_Login_two.setStyleSheet("color: white")
        self.Login_two.setFixedSize(100, 23)
        self.Qlabel_Login_two.setFixedSize(100, 23)
        self.Login_two.setStyleSheet("QLineEdit { background : White }")

        self.Password_two = QLineEdit(self)
        self.Qlabel_two_Password = QLabel("Пароль: ")
        self.Qlabel_two_Password.setStyleSheet("color: white")
        self.Password_two.setFixedSize(100, 23)
        self.Qlabel_two_Password.setFixedSize(100, 23)
        self.Password_two.setStyleSheet("QLineEdit { background : White }")

        self.button_upload_two = QPushButton("Подтвердить")
        self.button_upload_two.setStyleSheet("""
            QPushButton {
                    background-color: "black";
                    color: "white";
                    }""")
        self.button_upload_two.clicked.connect(self.check_registration)
        self.button_upload_two.setFixedSize(75, 40)

        layout.addWidget(self.Qlabel_Login_two, 0, 0)
        layout.addWidget(self.Login_two, 0, 1)
        layout.addWidget(self.Qlabel_two_Password, 1, 0)
        layout.addWidget(self.Password_two, 1, 1)
        layout.addWidget(self.button_upload_two, 2, 0)

        return widget_two

    def Insert_to_db(self):
        try:
            with pymysql.connect(host='localhost', port=3306, user="root", password="") as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""USE rl""")

                    Email = self.Email_one.text()
                    Login = self.Login_one.text()
                    Password = self.Password_one.text()

                    print(Login)
                    print(Password)
                    print(Email)

                    app = QApplication(sys.argv)
                    if Login == "" or Password == "":
                        print("Вы не написали данные")
                        app.exec()
                    else:
                        cursor.execute(f"""INSERT INTO `users`(`user_login`, `user_password`, `email`) VALUES ('{Login}', '{Password}', '{Email}');""")
                        connection.commit()

        except pymysql.Error as e:
            pass


    def swap_to_widget(self, state):
        if state:
            self.stacked_widget.setCurrentIndex(1)
            self.swap.setText("Заригистрироваться")
        else:
            self.stacked_widget.setCurrentIndex(0)
            self.swap.setText("Войти")

    def check_registration(self):
        try:
            with pymysql.connect(host='localhost', port=3306, user="root", password="") as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""USE rl""")

                    password = self.Password_two.text()
                    login = self.Login_two.text()

                    app = QApplication(sys.argv)
                    if login == "" or password == "":
                        print("Вы не написали данные")
                        app.exec()

                    cursor.execute(f"""SELECT `user_password`, `user_login` FROM `users` WHERE `user_password` = '{password}' AND `user_login` = '{login}' """)
                    for data in cursor:
                        if data[0] == password and data[1] == login:
                            print("Всё окей")
                        else:
                            app = QApplication(sys.argv)
                            app.exec()



        except pymysql.Error as e:
            pass