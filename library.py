import random
import time
import _sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import os
"""
Copyright 2020 Qiaoyu Zhang
Version of python: Python 3.7
Version of the software: V0.1
"""

"""
This library named library is created by KuangPi for the MINI IA project on the computer science class. This includes
several objects that used in the project.
"""


class Player:
    """
    When creating the player object, it won't create a new user in the data base. It will only contents the user
    information while the program is running.
    :argument userID: integer
    """
    def __init__(self, userID):
        search_resultUserInformation = search_string_in_Database(str(userID),
                                                                 "USER_INFORMATION",
                                                                 "USER_ID",
                                                                 "USER_INFORMATION_TABLE")
        search_resultWinning_Status_record = search_string_in_Database(str(userID),
                                                                       "USER_INFORMATION",
                                                                       "USER_ID",
                                                                       "WINNING_STATUS_RECORD")
        self.username = search_resultUserInformation[1]
        self.ALLwinningcounts = search_resultWinning_Status_record[1]

        # Find the best hand of the current player.
        temp = 0
        for i in range(2, 5, 1):
            if search_resultWinning_Status_record[i] >= temp:
                self.bestHand = i
                temp = search_resultWinning_Status_record[i]



def PSR_Process(hand1, hand2):
    """
    Take two arguments(“P”, “S”, “R”), compare and returns integer value. Return 1 for first arguments win, 2 for
    second arguments win, 0 for a tight, -1 for an invalid input.

    :parameter hand1: string
    :parameter hand2: string
    :return : integer
    """
    if hand1 == "P":
        if hand2 == "P":
            return 0
        elif hand2 == "S":
            return 2
        elif hand2 == "R":
            return 1
        else:
            return -1
    elif hand1 == "S":
        if hand2 == "P":
            return 1
        elif hand2 == "S":
            return 0
        elif hand2 == "R":
            return 2
        else:
            return -1
    elif hand1 == "R":
        if hand2 == "P":
            return 2
        elif hand2 == "S":
            return 1
        elif hand2 == "R":
            return 0
        else:
            return -1
    else:
        return -1


def random_Hand():
    """
    No need for input, return a string randomly from "P", "S", or "R"
    :return : string
    """
    temp = random.randrange(1.0, 4.0)
    if 1.0 <= temp < 2.0:
        return "P"
    elif 2.0 <= temp < 3.0:
        return "S"
    else:
        return "R"


def probability_test(trial):
    """
    Test the probability for the choice of the bots
    :param trial:
    :return results: tuple of floats
    """
    P = 0
    S = 0
    R = 0
    for i in range(trial):
        temp = random_Hand()
        if temp == "P":
            P += 1
        elif temp == "S":
            S += 1
        elif temp == "R":
            R += 1
    result = (P/trial, S/trial, R/trial)
    return result


def flip_a_coin():
    """
    Return True or False randomly.
    :return: bool
    """
    if random.randint(1, 2) == 1:
        return True
    else:
        return False


def wait_second(wait_time, function_afterwards):
    """
    Wait several seconds, then call the function at the second one
    :param wait_time: integer
    :param function_afterwards: function
    :return: None
    """
    lower_bound = wait_time * 0.5
    upper_bound = wait_time * 1.5
    random_wait_time = random.uniform(lower_bound, upper_bound)
    time.sleep(random_wait_time)


def binary_sort(unsorted_list, inverse):
    """
    Sort a list with binary sort algorithm.
    :param unsorted_list: list
    :param inverse: Boolean
    :return sorted_list: list
    """
    pass


def user_register(username, passwrod):
    """
    Insert the data of the user into the data base.
    :argument username: string
    :argument passwrod: string
    :return: None
    """
    pass


def search_string_in_Database(searchkey, database_name, column_name, table_name):
    """
    :parameter objectName: user_defined_object
    :parameter searchkey: Any
    :parameter database_name: string
    :parameter table_name: string
    :parameter column_name: String
    :return result: list
    """
    connection = _sqlite3.connect(database_name)
    usernameSearch = "SELECT * FROM " + table_name + " WHERE " + column_name + "='" + str(searchkey) + "'"
    temp = connection.execute(usernameSearch).fetchall()
    connection.close()
    if len(temp) != 0:
        return temp.pop()
    else:
        return ["NF"]  # NF stands for not founded.


def update_int_value_in_Database(primary_key, primary_keyName, database_name, column_name, table_name, context):
    """
    Change an int value of an existing data in the data base.
    :param primary_keyName:
    :param primary_key: int
    :param database_name:
    :param column_name:
    :param table_name:
    :param context: int
    :return: None
    """
    connection = _sqlite3.connect(database_name)
    update = "UPDATE " + \
                     table_name + \
                     " SET " + \
                     column_name + \
                     " = " + \
                     str(context) + \
                     " WHERE " + \
                     primary_keyName + \
                     " = " + \
                     str(primary_key)
    connection.execute(update)
    connection.commit()
    connection.close()


def label_text_update(windowName, labelName, newText):
    """
    Change the label name of an window.
    :param windowName:
    :param labelName: An sub variable under windowName
    :return: None
    """
    _translate = QtCore.QCoreApplication.translate
    labelName.setText(_translate(str(windowName), str(newText)))
    # Refresh the window to present the update on UI.
    windowName.hide()
    windowName.show()


def create_txt_file_and_write(Filename, context):
    """
    This function will create a txt file in the current directory and write the context into it.
    :param Filename: string
    :param context: string
    :return: None
    """
    cwd = os.getcwd()
    filePath = cwd + "/" + Filename + ".txt"
    file = open(filePath, "w")
    file.write(context)
    file.close()


def read_txt_file_and_delete(Filename):
    """
    This function will read a txt file in the current directory and delete it.
    :param Filename: string
    :return context: string
    """
    temp = read_txt_file(Filename, True)
    context = temp[0]
    filePath = temp[1]
    os.remove(filePath)
    return context


def read_txt_file(Filename, needPath):
    """
    This function will read a txt file in the current directory.
    :param Filename: String
    :param needPath: Bool
    :return context, file path: Tuple of String
    """
    cwd = os.getcwd()
    filePath = cwd + "/" + Filename + ".txt"
    tempFile = open(filePath, "r")
    context = tempFile.read()
    tempFile.close()
    if needPath:
        return context, filePath
    else:
        return context


def is_file_exists(filename):
    """
    Check if a file in the cwd exists.
    :param filename: string
    :return result: bool
    """
    return os.path.exists(os.getcwd() + "/" + filename + ".txt")


if __name__ == '__main__':
    pass
