import random
import os
import sqlite3
from PyQt5.QtGui import QPixmap
from PIL import Image
from Variables import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from Interface.StartMenuWindow import Ui_StartMenu
from Interface.AnswerWindow import Ui_Answer
from Interface.SettingsWindow import Ui_Settings
from Interface.AddTaskWindow import Ui_AddTask
from Interface.TaskWindow import Ui_Task
from Interface.DecisionWindow import Ui_decision
from Interface.CorrectAnswerWindow import Ui_CorrectAnswer
from Interface.InCorrectAnswerWindow import Ui_InCorrectAnswer
from Interface.DelTaskWindow import Ui_DelTask
from Interface.StatisticsWindow import Ui_Statistics
from Interface.ResetStatisticsWindow import Ui_ResetStatistics
from Interface.StartOptionWindow import Ui_StartOption
from Interface.FirstAnswerOptionWindow import Ui_FirstAnswerOption
from Interface.SecondAnswerOptionWindow import Ui_SecondAnswerOption
from Interface.AnswerOptionWindow import Ui_AnswerOption
from Interface.ResultOptionWindow import Ui_ResultOption

connect = sqlite3.connect("Task.db")
curs = connect.cursor()


def check_gif_task(number):
    result = []
    array_on_res = os.listdir(directory.format("Res"))
    array_on_task = os.listdir(directory.format("Task"))
    array_on_res = list(set(array_on_res) & set(array_on_task))
    array_on_task[:] = array_on_res[:]
    array = []
    for i in range(len(array_on_res)):
        if array_on_res[i].split('.')[0] != str(number):
            continue
        array.append(array_on_res[i])
    array_on_res[:] = array[:]
    if len(array_on_res) == 0:
        return 0
    array = curs.execute(f"""SELECT LinkTask FROM TaskAnswer""").fetchall()
    for i in range(len(array)):
        if array[i][0].split('.')[0] == str(number):
            result.append(array[i][0])
    if len(result) == 0:
        return 0
    array_on_task = result[random.randint(0, len(result) - 1)]
    array_on_task += ".png"
    if array_on_task in array_on_res:
        creative_file(array_on_task.split('.png')[0])
        return array_on_task.split('.png')[0]


def input_in_db(file_name, user_answer):
    number = curs.execute(f"""
            SELECT id FROM TaskAnswer WHERE LinkTask = {file_name}
    """).fetchall()
    if len(number) == 0:
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({file_name}, {user_answer})
                """)
    else:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE id == {number[0][0]}""")
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({file_name}, {user_answer})
                """)
    connect.commit()


def if_db_is_clear():
    curs.execute(f"""
                    INSERT INTO Statistics(number_of_tasks, correct_answer, incorrect_answer) VALUES(0, 0, 0)
                    """)
    connect.commit()


def check_len_db():
    check_len = curs.execute(f"""
                SELECT * FROM Statistics
        """).fetchall()
    if len(check_len) == 0:
        if_db_is_clear()


def take_values():
    first_id = curs.execute(f"""
                SELECT * FROM Statistics WHERE id = 1
        """).fetchall()[0]
    return first_id


def check(user_answer, file_name):
    real_answer = curs.execute(f"""
                SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {file_name}
        """).fetchall()[0][0]
    curs.execute(f"""
            UPDATE Statistics SET number_of_tasks = {take_values()[1] + 1} WHERE id = 1
            """)
    if str(real_answer) == str(user_answer):
        curs.execute(f"""
                UPDATE Statistics SET correct_answer = {take_values()[2] + 1} WHERE id = 1
                """)
        answer_value = True

    else:
        curs.execute(f"""
                UPDATE Statistics SET incorrect_answer = {take_values()[3] + 1} WHERE id = 1
                """)
        answer_value = False
    connect.commit()
    return answer_value


def del_in_db(name_task):
    all_task = curs.execute(f"""
                SELECT LinkTask FROM TaskAnswer WHERE id >= 1
        """).fetchall()
    all_task = list_link_task(all_task)
    if name_task in all_task:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE LinkTask == {name_task}""")
    connect.commit()


def list_link_task(array):
    result_list = []
    for i in array:
        result_list.append(i[0])
    return result_list


def getting_statistics():
    all_information = curs.execute(f"""
                SELECT * FROM Statistics WHERE id = 1
        """).fetchall()[0]
    return all_information


def reset_all_statistics():
    curs.execute(f"""DELETE FROM Statistics WHERE id == 1""")
    connect.commit()


def add_in_option_db():
    for i in range(1, 20):
        name_task = check_gif_task(int(i))
        if name_task != 0 and int(i) == int(name_task.split('.')[0]):
            answer_img = curs.execute(f"""
                SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {str(name_task)}
        """).fetchall()[0][0]
            curs.execute(f"""
                            INSERT INTO Option(id, name_img, answer_img, user_answer) VALUES({name_task.split('.')[0]}, {name_task}, {str(answer_img)}, '')
                            """)
    connect.commit()


def clear_option_db():
    curs.execute(f"""DELETE FROM Option WHERE id >= 1""")
    connect.commit()


def check_len_option_db():
    check_len = curs.execute(f"""
                SELECT * FROM Option
        """).fetchall()
    if len(check_len) == 0:
        add_in_option_db()
    else:
        return


def picture_on_lable(self, link):
    link_task = link + ".png"
    width = self.label.width()
    height = self.label.height()
    image = Image.open(link_task)
    size = (width, height - 100)
    im = image.resize(size)
    im.save(link_task)
    self.pixmap = QPixmap(link_task)
    self.image = self.label
    self.image.setPixmap(self.pixmap)


def giv_link_picture(name_task, directory):
    return name_file.format(directory, name_task)


def giv_name_task(name_task):
    name_task = curs.execute(f"""
                SELECT name_img FROM Option WHERE id = {name_task}
        """).fetchall()
    if len(name_task) == 0:
        return incorrect_answer
    else:
        return name_task[0][0]


def record_answer(text, name_task):
    curs.execute(f"""
            UPDATE Option SET user_answer = {str(text)} WHERE id = {int(name_task)}
            """)
    connect.commit()


def creative_file(name_task):
    file = open(f"file\{'name_task.txt'}", 'w', encoding='utf-8')
    file.write(str(name_task))
    file.close()
    read_file()


def read_file():
    file = open(f"file\{'name_task.txt'}", 'r', encoding='utf-8')
    name_task = file.read().splitlines()
    return name_task[0]


def result_true_answer():
    array_result = curs.execute(f"""
                SELECT * FROM Option
        """).fetchall()
    result = 0
    for i in array_result:
        if str(i[2]) == str(i[3]):
            result += 1
    return str(result)
