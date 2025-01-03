import tkinter as tk
from googletrans import Translator


def show_text():
    global new_window
    # 獲取輸入文本
    input_text = text_input.get()
    translated_text = ""

    if translate_var.get():
        translator = Translator()
        # 使用 Google 翻譯將文本翻譯成英文
        translated_text = translator.translate(input_text, dest='en').text

    if new_window is None or not new_window.winfo_exists():
        # 創建新窗口
        new_window = tk.Toplevel(root)
        new_window.title("顯示文字")
        new_window.geometry("400x200")
        # 設置新窗口的背景顏色為綠色
        new_window.configure(bg='green')

        # 結果顯示區域
        canvas = tk.Canvas(new_window, bg='green', highlightthickness=0)
        canvas.pack(pady=10)

        # 顯示原文和翻譯文字，加上黑邊
        for x_offset in (-1, 0, 1):
            for y_offset in (-1, 0, 1):
                if x_offset != 0 or y_offset != 0:
                    canvas.create_text(200 + x_offset, 60 + y_offset, text=input_text, font=("Arial", 14, "bold"),
                                       fill='black', width=380, justify='center')
                    if translate_var.get():
                        canvas.create_text(200 + x_offset, 140 + y_offset, text=translated_text,
                                           font=("Arial", 14, "bold"), fill='black', width=380, justify='center')
        canvas.create_text(200, 60, text=input_text, font=("Arial", 14, "bold"), fill='white', width=380,
                           justify='center')
        if translate_var.get():
            canvas.create_text(200, 140, text=translated_text, font=("Arial", 14, "bold"), fill='white', width=380,
                               justify='center')
    else:
        # 更新結果顯示區域的文本
        canvas = new_window.children['!canvas']
        canvas.delete("all")
        for x_offset in (-1, 0, 1):
            for y_offset in (-1, 0, 1):
                if x_offset != 0 or y_offset != 0:
                    canvas.create_text(200 + x_offset, 60 + y_offset, text=input_text, font=("Arial", 14, "bold"),
                                       fill='black', width=380, justify='center')
                    if translate_var.get():
                        canvas.create_text(200 + x_offset, 140 + y_offset, text=translated_text,
                                           font=("Arial", 14, "bold"), fill='black', width=380, justify='center')
        canvas.create_text(200, 60, text=input_text, font=("Arial", 14, "bold"), fill='white', width=380,
                           justify='center')
        if translate_var.get():
            canvas.create_text(200, 140, text=translated_text, font=("Arial", 14, "bold"), fill='white', width=380,
                               justify='center')


# 創建主窗口
root = tk.Tk()
root.title("文字顯示應用")
root.geometry("400x200")

# 設置主窗口的背景顏色為綠色
root.configure(bg='green')

# 輸入框
text_input = tk.Entry(root, font=("Arial", 14))
text_input.pack(pady=10)

# 勾選開關
translate_var = tk.BooleanVar(value=True)
translate_checkbox = tk.Checkbutton(root, text="顯示翻譯", variable=translate_var, font=("Arial", 14), bg='green')
translate_checkbox.pack(pady=10)

# 按鈕
input_button = tk.Button(root, text="Input", command=show_text, font=("Arial", 14))
input_button.pack(pady=10)

# 初始化全局變數
new_window = None

# 開始主循環
root.mainloop()
