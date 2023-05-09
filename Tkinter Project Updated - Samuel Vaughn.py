import tkinter as tk

class GolfApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Golf Round App")
        self.parent.configure(bg='green')
        # creates the widgets for the first window
        self.number_label = tk.Label(self.parent, text="Enter your round statistics!", font='bakersville, 14', bg='green', fg='yellow')
        self.number_label_1 = tk.Label(self.parent, text="                                            Score:", font='baskerville', bg='green', fg='yellow')
        self.number_entry_1 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_2 = tk.Label(self.parent, text="                                             Putts:", font='baskerville', bg='green', fg='yellow')
        self.number_entry_2 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_3 = tk.Label(self.parent, text="                                      Fairways:", font='baskerville', bg='green', fg='yellow')
        self.number_entry_3 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_4 = tk.Label(self.parent, text="                   Greens in regulation:", font='baskerville', bg='green', fg='yellow')
        self.number_entry_4 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.enter_button = tk.Button(self.parent, text="Enter", font='baskerville', bg='green', fg='yellow', command=self.submit, borderwidth=2)

        # layout for the widgets on the first window
        self.number_label.grid(row=0, column=0, columnspan=3)
        self.number_label_1.grid(row=1, column=0)
        self.number_entry_1.grid(row=1, column=1)
        self.number_label_2.grid(row=2, column=0)
        self.number_entry_2.grid(row=2, column=1)
        self.number_label_3.grid(row=3, column=0)
        self.number_entry_3.grid(row=3, column=1)
        self.number_label_4.grid(row=4, column=0)
        self.number_entry_4.grid(row=4, column=1)
        self.enter_button.grid(row=5, column=1)

    def submit(self):
        entries = [self.number_entry_1.get(), self.number_entry_2.get(), self.number_entry_3.get(), self.number_entry_4.get()]
        numbers_and_words = []
        for entry in entries:
            words = entry.split()
            if len(words) > 1:
                numbers_and_words.append(words[0] + " " + words[1])
            else:
                numbers_and_words.append(entry)
        self.parent.destroy()
        NumberListWindow(numbers_and_words)

# creates the second window
class NumberListWindow:
    def __init__(self, numbers):
        self.numbers = numbers
        self.parent = tk.Tk()
        self.parent.title("Golf Round Statistics")
        self.parent.configure(bg='green')

        # creates the widgets on second window
        self.number_listbox = tk.Listbox(self.parent, bg='green', fg='yellow')
        for number in self.numbers:
            self.number_listbox.insert(tk.END, number)

        # layout for the widgets on second window
        self.number_listbox.grid(row=0, column=0)

        # creates the "Add More" button
        self.add_more_button = tk.Button(self.parent, text="Add More Rounds", font='baskerville', bg='green', fg='yellow', command=self.add_more, borderwidth=2)
        self.add_more_button.grid(row=1, column=0)

        # creates the "Exit" button
        self.exit_button = tk.Button(self.parent, text="Exit", font='baskerville', bg='green', fg='yellow', command=self.parent.destroy, borderwidth=2)
        self.exit_button.grid(row=2, column=0)

    def add_more(self):
        # creates a new GolfApp window if button is pressed
        GolfApp(tk.Toplevel())

if __name__ == "__main__":
    root = tk.Tk()
    GolfApp(root)
    root.mainloop()
