import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
import keyboard
import pyautogui

def translate_text(text, dest_language='zh-tw'):
    translator = Translator()
    try:
        result = translator.translate(text, dest=dest_language)
        return result.text
    except Exception as e:
        return f"翻譯失敗: {e}"

def on_ctrl_space():
    try:
        # 模擬 Ctrl+C 操作來複製選中的文本
        pyautogui.hotkey('ctrl', 'c')
        root.after(100)  # 等待剪貼板更新
        selected_text = root.clipboard_get()
        translated_text = translate_text(selected_text)
        # 創建一個新的 Toplevel 窗口來顯示訊息框
        top = tk.Toplevel(root)
        top.withdraw()  # 隱藏 Toplevel 窗口
        top.attributes('-topmost', True)  # 確保在最前面
        messagebox.showinfo("翻譯結果", translated_text, parent=top)
        top.destroy()  # 關閉 Toplevel 窗口
    except Exception as e:
        top = tk.Toplevel(root)
        top.withdraw()
        top.attributes('-topmost', True)
        messagebox.showerror("錯誤", f"無法獲取選中文本: {e}", parent=top)
        top.destroy()

def print_usage():
    print("使用方式：")
    print("1. 選擇要翻譯的文字。")
    print("2. 按下 Ctrl+* 來翻譯滑鼠反白的文字。")

root = tk.Tk()
root.withdraw()  # 隱藏主窗口

# 使用 keyboard 庫綁定 Ctrl+Space 事件
keyboard.add_hotkey('ctrl+*', on_ctrl_space)

# 打印使用方式
print_usage()

# 保持窗口運行
root.mainloop()
