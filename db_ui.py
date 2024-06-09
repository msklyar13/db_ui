from tkinter import *
from tkinter import ttk 
import sqlite3

# Створити новий графічний (віконний) проєкт мовою Python
window = Tk()
window.title('db_ui')
window.configure(bg='light pink')

# Додати на форму: кнопку (Button); напис (Label); спадний список (ComboBox); таблицю для даних (TreeView або інші варіанти)
buttonGetWord = Button(window, text = 'Get more words!', font=("Arial", 20), bg='white', fg='black')
buttonGetWord.grid(pady=4)

labelWord = Label(window, text = '--', font = ('Arial', 16), bg='white', fg='black')
labelWord.grid(pady=4)

comboWords = ttk.Combobox(window, textvariable = StringVar()) 
comboWords.grid(pady=4)

col = ['id', 'sgN', 'sgG']
dictW = ttk.Treeview(window, columns=col, show='headings')
dictW.heading('id', text='INDEX')
dictW.heading('sgN', text='WORD Nom')
dictW.heading('sgG', text='WORD Gen')
dictW.grid(pady=4)

# Створити під’єднання до БД
conn = sqlite3.connect('C://Users//masha//OneDrive//Desktop//TPOLPH//pol_lab02.s3db')
c = conn.cursor()

# Знайти будь-яке одне слово в початковій формі (sgN) та вивести його в напис
# Вивести слово, яке починається на літеру "L"
c.execute("SELECT sgN from tnoun WHERE sgN LIKE 'l%'")
result = c.fetchone()[0]
labelWord.configure(text=result)

# Створити обробник натискання на кнопку, який виконує другий SQL-запит до БД
# і наповнює таблицю інформацією для будь-яких 15 слів із БД
# Якщо слово не має потрібної форми в БД, вивести в комірку прочерк (тире)

def getNouns():
    c.execute("SELECT id, sgN, sgG from tnoun LIMIT 15")
    nounList = c.fetchall()
    for i in range(len(nounList)):
        words = [w if w else '—' for w in nounList[i]]
        dictW.insert("", END, values=words)

buttonGetWord.configure(command=getNouns)


# У першій колонці виводити не ID слова з відповідного поля в БД,
# а його порядковий номер у створеній таблиці на формі
def getNouns():
    c.execute("SELECT sgN, sgG from tnoun LIMIT 15")
    nounList = c.fetchall()
    for i, r in enumerate(nounList, start=1):
        words = [i] + [w if w else '—' for w in r]
        dictW.insert("", "end", values=words)

# У спадний список мають завантажитись усі слова, які починаються на літеру "L"
    c.execute("SELECT sgN from tnoun WHERE sgN LIKE 'l%'")
    noun_list = c.fetchall()
    comboWords.configure(values=noun_list)

buttonGetWord.configure(command=getNouns)

window.mainloop()
conn.close()