# Реализация графического интерфейса и формы для приложения
# «Гостевая книга» с возможностью сохранения данных из полей формы в
# файл. Сформировать отчет по выполненной самостоятельной работе и
# опубликовать его в портфолио.
import tkinter as tk


def form_submit(author, text):
    author = author.get()
    msg = text.get("1.0", "end-1c")
    with open("data.bd", "at") as file:
        file.write(f"{author}: {msg}\n")

    author.delete(0, "end")
    text.delete("1.0", tk.END)


root = tk.Tk()
root.title("Гостевая книга")
author_entry = tk.Entry(root)
text = tk.Text(root)
submit = tk.Button(root, text="Сохранить", command=lambda: form_submit(author_entry, text))

author_entry.pack()
text.pack()
submit.pack()

root.mainloop()