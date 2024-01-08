import subprocess
import tkinter as tk
import os
import urduscript

#GUI
def run_command():
    output_box.delete("1.0", tk.END)
    result = subprocess.run(['python', 'urduscript.py', 'test.us'], capture_output=True, text=True)
    output_box.insert(tk.END, result.stdout)

def save_file():
    with open('test.us', 'w') as f:
        f.write(text_box.get("1.0", "end-1c"))

root = tk.Tk()

text_box = tk.Text(root)
text_box.pack()

output_box = tk.Text(root)
output_box.pack()

def save_and_run():
    save_file()
    run_command()

run_button = tk.Button(root, text="Run", command=save_and_run)
run_button.pack()

root.mainloop()

#SHELL
# def execute_command(command):
#     return urduscript.run("<stdin>", command)

# while True:
#     text = input("US>").strip()

#     if text == "clear":
#         os.system('clear' if os.name == 'posix' else 'cls')
#         continue

#     if text == "":
#         continue

#     result, error = execute_command(text)

#     if error:
#         print(error.as_string())
#     elif result:
#         if len(result.elements) == 1:
#             print(repr(result.elements[0]))
#         else:
#             print(repr(result))