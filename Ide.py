import subprocess
import tkinter as tk

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