import tkinter as tk

miracle = []


class Geto:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.entry_Label = tk.Label(self.root, text="Input:")
        self.entry_Label.pack()
        self.entry_Entry = tk.Entry(self.root, borderwidth=5)
        self.entry_Entry.pack()
        self.entry_Button = tk.Button(self.root, text="Enter", command=self.get)
        self.entry_Button.pack()
        self.entry_Button1 = tk.Button(
            self.root, text="Quit", command=self.quit
        )
        self.entry_Button1.pack()
        self.miracle = miracle

    def get(self):
        data = self.entry_Entry.get()
        self.Display = tk.Label(self.root, text=data)
        self.Display.pack()
        miracle.append(data)
        return data

    def quit(self):
        self.root.destroy()


root = tk.Tk()
Geto(root)
root.mainloop()