import os
import sys
import random

from PyQt5 import QtCore, QtWidgets

import QT_fightWindow
import QT_login
import QT_mainwindow
import QT_asking_PageWindow
import library

"""
Copyright 2020 Qiaoyu Zhang
Version of python: Python 3.7
Version of the software: V0.1
"""

"""
The main function of this project. 
"""


class Py_login(QtWidgets.QWidget, QT_login.Ui_dialogLogin):
    def __init__(self):
        super(Py_login, self).__init__()
        self.setupUi(self)

    def loginMain(self):
        """
        :return: None
        :influence: Change the value of the global variable login.
        """
        # checkResut is a tuple that the first element is a bool.
        # If the first element is True, there will be a second element which is the user id of the login.
        checkReuslt = self.loginCheck()
        if checkReuslt[0]:
            library.label_text_update(self,
                                      self.input_AlertLabel,
                                      "")
            library.create_txt_file_and_write("PLAYERID", str(checkReuslt[1]))
            page_chaging("main")
            exit()
        else:
            library.label_text_update(self,
                                      self.input_AlertLabel,
                                      "Invalid Username or Password! ")

    def loginCheck(self):
        """
        Check if the input username exists in the database and if it
        :return: Bool
        """
        # Get from the window script.
        usernameText = self.inputUsername.text()
        passwrodText = self.inputPassword.text()

        temp = library.search_string_in_Database(usernameText,
                                                 "USER_INFORMATION",
                                                 "USER_NAME",
                                                 "USER_INFORMATION_TABLE")
        if temp[0] != "NF":  # Username founded
            username_SearchResult = temp
            # Check if the password matches with the one in the database.
            # 2 is the index for the third column in the database which is the password.
            if username_SearchResult[2] == passwrodText:
                return True, username_SearchResult[0]
            else:
                return (False, )
        else:  # Username not founded
            return (False, )

    def userRegister(self):
        pass

    def exit(self):
        page_chaging("exit")
        sys.exit()


class Py_mainWindow(QtWidgets.QMainWindow, QT_mainwindow.Ui_MainWindow):
    def __init__(self, player_ID):
        super(Py_mainWindow, self).__init__()
        self.setupUi(self)
        self.currentPlayer = library.Player(player_ID)
        library.label_text_update(self,
                                  self.label,
                                  "Welcome, " + self.currentPlayer.username + ".")

    def transfer_Rank(self):
        pass

    def exit(self):
        page_chaging("exit")
        exit()

    def transfer_Fight(self):
        page_chaging("fight")
        exit()


class Py_fightWindow(QtWidgets.QWidget, QT_fightWindow.Ui_windowFight):
    def __init__(self, player_ID):
        super(Py_fightWindow, self).__init__()
        self.setupUi(self)
        self.currentPlayer = library.Player(player_ID)
        self.is_fightReady = False
        self.player1_choice = "N"
        self.upper_label_text_update("Press start to find an enemy. ")
        self.lower_label_text_update("You have no enemy! ")
        library.label_text_update(self,
                                  self.player1_nameLabel,
                                  self.currentPlayer.username)

    def startFight(self):
        """
        Called when start the fight
        :return: None
        """
        player1_name = self.currentPlayer.username
        player2_name = "BOT"
        self.upper_label_text_update("Enemy founded! ")
        self.lower_label_text_update("I'm" + player2_name + "I'll beat you! ")
        is_first = library.flip_a_coin()
        if is_first:
            self.upper_label_text_update("Hey! " + player1_name + ", you'll go first")
            self.lower_label_text_update("Quick! I'll wait for you! ")
            self.is_fightReady = True
        else:
            self.upper_label_text_update("Hey! " + player1_name + ", you'll go second")
            self.lower_label_text_update("Hold on, let me think...")
            QtCore.QTimer.singleShot(random.randint(2000, 5000), self.print_rest_second_text)

    def print_rest_second_text(self):
        """
        Called in the startFight function by singleShot.
        :return: None
        """
        self.is_fightReady = True
        self.lower_label_text_update("I'm ready! ")
        self.upper_label_text_update("It's your turn now! ")

    def paperClicked(self):
        """
        Paper is clicked.
        :return: None
        """
        self.player1_choice = "P"
        self.fighting()

    def rockClicked(self):
        """
        Rock is clicked.
        :return:
        """
        self.player1_choice = "R"
        self.fighting()

    def scissorClicked(self):
        """
        Scissor is clicked.
        :return: None
        """
        self.player1_choice = "S"
        self.fighting()

    def fighting(self):
        """
        Real fight process.
        :return: bool
        """
        if self.is_fightReady:
            library.create_txt_file_and_write("PLAYERCHOICE", self.player1_choice)
            self.upper_label_text_update("Your choice is: " + self.player1_choice)
            self.player2_choice = library.random_Hand()
            self.lower_label_text_update("His choice is: " + self.player2_choice)
            QtCore.QTimer.singleShot(1000, self.fighted)
        else:
            self.upper_label_text_update("Fight is not ready! Find an enemy first! ")

    def upper_label_text_update(self, context):
        """
        The function is called too often. So, def a simpler version for it here to increase the readability.
        :param context:
        :return: None
        """
        library.label_text_update(self,
                                  self.first_SecondLabel,
                                  context)

    def lower_label_text_update(self, context):
        """
        Update the lower label
        :param context: string
        :return: None
        """
        library.label_text_update(self,
                                  self.player2_statusLabel,
                                  context)

    def fighted(self):
        library.create_txt_file_and_write("WINNINGSTATUS",
                                          str(library.PSR_Process(self.player1_choice, self.player2_choice)))
        library.create_txt_file_and_write("PAGE", "asking")
        exit()


class Py_askingWindow(QtWidgets.QWidget, QT_asking_PageWindow.Ui_asking_PageWindow):
    def __init__(self, winningStatus, playerID, winningHand):
        super(Py_askingWindow, self).__init__()
        self.setupUi(self)
        if winningStatus >= 0:
            if winningStatus < 2:
                # Player 1 wins or a tie
                if winningStatus == 1:
                    # Player 1 wins
                    library.label_text_update(self, self.winning_StatusLabel, "You win! Congratulation! ")
                    self.winning_status_updates(playerID, winningHand)
                else:
                    # It is a tie
                    library.label_text_update(self, self.winning_StatusLabel, "It's a tie! Try harder next time!  ")
            else:
                # Player 2 wins.
                library.label_text_update(self, self.winning_StatusLabel, "You loss! Is that what you can do?  ")
        else:
            library.label_text_update(self, self.winning_StatusLabel, "You Cheater! ")
            raise TypeError("A stupid cheater is discovered!!!")

    def winning_status_updates(self, playerID, winningHand):
        print(winningHand)
        if winningHand == "P":
            # Direct related to the position in the database
            coded_winning_hand = 2
            column_name = "PAPER_WINNING"
        elif winningHand == "R":
            coded_winning_hand = 3
            column_name = "STONE_WINNING"
        elif winningHand == "S":
            coded_winning_hand = 4
            column_name = "SCISSOR_WINNING"
        else:
            raise TypeError("Stupid Cheater! ")
        library.update_int_value_in_Database(playerID,
                                             "USER_ID",
                                             "USER_INFORMATION",
                                             column_name,
                                             "WINNING_STATUS_RECORD",
                                             str(int(library.search_string_in_Database(playerID,
                                                                               "USER_INFORMATION",
                                                                               "USER_ID",
                                                                               "WINNING_STATUS_RECORD")[coded_winning_hand]) + 1))
        library.update_int_value_in_Database(playerID,
                                             "USER_ID",
                                             "USER_INFORMATION",
                                             "OVERALL_COUNTS",
                                             "WINNING_STATUS_RECORD",
                                             str(int(library.search_string_in_Database(playerID,
                                                                               "USER_INFORMATION",
                                                                               "USER_ID",
                                                                               "WINNING_STATUS_RECORD")[1]) + 1))

    def anotherRound(self):
        library.create_txt_file_and_write("PAGE", "fight")
        exit()

    def transferMain(self):
        library.create_txt_file_and_write("PAGE", "main")
        exit()


def loginWindowCreation():
    """
    Create the login window. Called in another script
    :return: None
    """
    loginApp = QtWidgets.QApplication(sys.argv)
    loginWindow = Py_login()
    loginWindow.show()
    sys.exit(loginApp.exec_())


def mainWindowCreation():
    """
    Create the main window. Called in another script
    :return: None
    """
    playerID = library.read_txt_file("PLAYERID", False)
    mainApp = QtWidgets.QApplication(sys.argv)
    mainWindow = Py_mainWindow(playerID)
    mainWindow.show()
    sys.exit(mainApp.exec_())


def fightWindowCreation():
    playerID = library.read_txt_file("PLAYERID", False)
    fightApp = QtWidgets.QApplication(sys.argv)
    fightWindow = Py_fightWindow(playerID)
    fightWindow.show()
    sys.exit(fightApp.exec_())


def askingWindowCreation():
    askingApp = QtWidgets.QApplication(sys.argv)
    askingWindow = Py_askingWindow(int(library.read_txt_file("WINNINGSTATUS", False)),
                                   int(library.read_txt_file("PLAYERID", False)),
                                   library.read_txt_file("PLAYERCHOICE", False))
    askingWindow.show()
    sys.exit(askingApp.exec_())


def page_chaging(new_page):
    """
    Change the page record in the directory txt file.
    :param new_page: String
    :return: None
    """
    os.remove(os.getcwd() + "/PAGE.txt")
    library.create_txt_file_and_write("PAGE", str(new_page))


def deleting_temp_text_files():
    """
    This function is specifically designed for this program. Will delete the temp txt file generated during the program.
    :return: None
    """
    if library.is_file_exists("PAGE"):
        library.read_txt_file_and_delete("PAGE")
    if library.is_file_exists("PLAYERID"):
        library.read_txt_file_and_delete("PLAYERID")
    if library.is_file_exists("WINNINGSTATUS"):
        library.read_txt_file_and_delete("WINNINGSTATUS")
    if library.is_file_exists("PLAYERCHOICE"):
        library.read_txt_file_and_delete("PLAYERCHOICE")


def main():
    library.create_txt_file_and_write("PAGE", "login")
    while True:
        page = library.read_txt_file("PAGE", False)
        if page == "login":
            os.system("python3 AUTO_loginMain.py")
        elif page == "main":
            os.system("python3 AUTO_mainMain.py")
        elif page == "fight":
            os.system("python3 AUTO_fightMain.py")
        elif page == "asking":
            os.system("python3 AUTO_askingMain.py")
        else:
            break
    deleting_temp_text_files()


if __name__ == '__main__':
    main()
