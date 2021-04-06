#создай приложение для запоминания информации
from random import shuffle , randint
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout ,QLabel,QMessageBox,QRadioButton,QGroupBox, QButtonGroup

#Создание класса Question
class Question ():
    def __init__ (self,quest,right_answer,wrong1,wrong2,wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list= []
question_list.append(Question('Государственный язык Бразилии','Португальский','Бразильский','Испанский','Английский'))
question_list.append(Question('Выбери перевод слова "переменная"','variable','variation','variant','changing'))
question_list.append(Question('Страна восходящего солнца','Япония','Китай','Сев.Корея','Южн.Корея'))
question_list.append(Question('Этой расы не существует','Арийцы','Негроиды','Европеоиды','Азиаты'))
question_list.append(Question('Материал у которого больше всего сплавов','Железо','Олово','Медь','Латунь'))
question_list.append(Question('Большинство фараонов Египта не говорили на','Египетском','Греческом','Греческом и Египетском','Говорили на обоих'))
question_list.append(Question('Красный барон был родом из','Пруссия','России','Англии','Америки'))
question_list.append(Question('Главным злом во вселенной "Хоббит" является','Саурон','Саруман','Смауг','Олог-хай'))
question_list.append(Question('В этой стране право жить присуждалось не всем детям','Спарта','Персия','Афины','Рим'))
question_list.append(Question('В этой стране появилось больше всего метал-групп','Швеция','Швейцария','Финляндия','Дания'))
question_list.append(Question('Этой техники дыхания не существует','Хамон','Вайвейшн','Оксисайз','Рыдающее дыхание'))
question_list.append(Question('Альбом "Power Up" написала группа из этой страны','Австралия(AC\DC)','Америка(Imagine Dragons)','Англия(Beatles)','Швеция(Sabaton)'))

app =QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo Card')
main_win.resize(800 , 400)
main_win.cur_question= -1

btn_ok = QPushButton('Ответить')
question = QLabel('что? где? когда?')

RadioGroupBox = QGroupBox('Варианты ответов')

#Создание кнопок
btn_answer1 = QRadioButton('1')
btn_answer2 = QRadioButton('2')
btn_answer3 = QRadioButton('3')
btn_answer4 = QRadioButton('4')

#Радиобаттоны в группу
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

#Лэйауты , их создание и привязка к кнопкам
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()
layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)

RadioGroupBox.setLayout(layout_ans1)

#Ответы
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

#Лэйауты для Ответов
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter , stretch = 2)
AnsGroupBox.setLayout(layout_res)

#Создание Лейаутов горизонтальных
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

#Объединение Лейаутов
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2 , stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

#Функции для обработки событий
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')

def start_test():
    if 'Ответить'== btn_ok.text():
        show_result()
    else:
        show_question()

answers=[btn_answer1,btn_answer2,btn_answer3,btn_answer4]

def ask(q:Question):
    shuffle(answers)
    print(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.quest)
    lb_Correct.setText(q.right_answer)
    show_question()

#Счётчик кол-ва вопросов и правильных ответов
main_win.total = 0
main_win.score = 0

def next_question ():
    main_win.total +=1
    print('Статистика: ',main_win.score/main_win.total*100)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    

def show_correct(res):
    lb_Result.setText(res)
    show_result()
    

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score +=1
        print('Статистика\nВсего вопросов:',main_win.total ,'\nПравильных ответов:', main_win.score)
        print('Рейтинг:',(main_win.score/main_win.total*100),'%')

    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
         

def click_OK():
    if btn_ok.text()== 'Ответить':
        check_answer()
    else:
        next_question()

btn_ok.clicked.connect(click_OK)
next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()