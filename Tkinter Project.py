import tkinter as tk 

class GolfApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Golf Round App")
        
        # creates the widgets for first window
        self.label = tk.Label(master, text="Enter your round statistics:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.button = tk.Button(master, text="Enter", command=self.add_item)
        self.button.pack()
        self.quit_button = tk.Button(master, text="Quit", command=self.master.quit)
        self.quit_button.pack()
        
        # creates the widgets for second window
        self.second_window = tk.Toplevel(master)
        self.second_window.title("Golf Round Statistics")
        self.listbox = tk.Listbox(self.second_window)
        self.listbox.pack()
        
        # creates the list of items
        self.items = []
        
    def add_item(self):
        item = self.entry.get()
        self.items.append(item)
        self.listbox.insert(tk.END, item)
        self.entry.delete(0, tk.END)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = GolfApp(root)
    root.mainloop()
