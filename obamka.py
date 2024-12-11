import tkinter as tk
from tkinter import ttk, messagebox


def add_word():
    word = entry_word.get()
    if word:
        text_area_word.insert("1.0", word + "\n")  
        entry_word.delete(0, tk.END)  


def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

def calculate_sum():
    try:
        n = int(entry_sum.get())
        if n < 1:
            messagebox.showerror("Ошибка", "Число N должно быть больше или равно 1.")
        else:
            result = sum_recursive(n)
            label_result.config(text=f"Сумма: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число.")


def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

def on_reverse():
    user_input = entry_reverse.get()
    reversed_text = reverse_string(user_input)
    text_area_reverse.delete(1.0, tk.END)  
    text_area_reverse.insert(tk.END, reversed_text)  


root = tk.Tk()
root.title("Объединенное приложение")
root.geometry("400x400")


tab_control = ttk.Notebook(root)


tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Вывод фразы')
entry_word = tk.Entry(tab1)
entry_word.pack(pady=10)

button_word = tk.Button(tab1, text="ввести", command=add_word)
button_word.pack(pady=5)

text_area_word = tk.Text(tab1, height=10, width=30)
text_area_word.pack(pady=10)


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Сумма чисел')
entry_sum = tk.Entry(tab2, width=10)
entry_sum.pack(pady=10)

button_calculate = tk.Button(tab2, text="Вычислить сумму", command=calculate_sum)
button_calculate.pack(pady=5)

label_result = tk.Label(tab2, text="")
label_result.pack(pady=10)


tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Переворот строки')
entry_reverse = tk.Entry(tab3, width=40)
entry_reverse.pack(pady=10)

reverse_button = tk.Button(tab3, text="Перевернуть", command=on_reverse)
reverse_button.pack(pady=5)

text_area_reverse = tk.Text(tab3, height=5, width=40)
text_area_reverse.pack(pady=10)


tab_control.pack(expand=1, fill='both')


root.mainloop()