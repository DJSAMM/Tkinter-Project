import tkinter as tk
from PIL import ImageTk, Image  

class GolfApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Golf Round App")
        self.parent.configure(bg='green')
        self.parent.geometry("")

        # images were supposed to go here. Evry time I attempted to input images they would appear as a white box (I'm assuming they would not properly load?)
        # after a number of differnet methods to input images and it failing each time I have decided to move along without the use of images 

        # creates the widgets for the first window, includes text, colors, and font
        self.number_label = tk.Label(self.parent, text="Enter your round statistics!", font=('Times New Roman',14,'bold'), bg='green', fg='yellow',)
        self.number_label_1 = tk.Label(self.parent, text="                                            Score:", font=('Times New Roman', 12), bg='green', fg='yellow')
        self.number_entry_1 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_2 = tk.Label(self.parent, text="                                             Putts:", font=('Times New Roman', 12), bg='green', fg='yellow')
        self.number_entry_2 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_3 = tk.Label(self.parent, text="                                       Fairways:", font=('Times New Roman', 12), bg='green', fg='yellow')
        self.number_entry_3 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.number_label_4 = tk.Label(self.parent, text="                       Greens in regulation:", font=('Times New Roman', 12), bg='green', fg='yellow')
        self.number_entry_4 = tk.Entry(self.parent, borderwidth=3, bg='green', fg='yellow')
        self.enter_button = tk.Button(self.parent, text="Enter", font=('Times New Roman', 12), bg='green', fg='yellow', command=self.submit, borderwidth=2)

        # layout for the widgets on the first window
        self.number_label.grid(row=0, column=1, columnspan=3)
        self.number_label_1.grid(row=1, column=1)
        self.number_entry_1.grid(row=1, column=2)
        self.number_label_2.grid(row=2, column=1)
        self.number_entry_2.grid(row=2, column=2)
        self.number_label_3.grid(row=3, column=1)
        self.number_entry_3.grid(row=3, column=2)
        self.number_label_4.grid(row=4, column=1)
        self.number_entry_4.grid(row=4, column=2)
        self.enter_button.grid(row=5, column=2)

    # submits the user enterd information into the second window list
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

        # creates the listbox on the second window
        self.number_listbox = tk.Listbox(self.parent, bg='green', fg='yellow')
        for number in self.numbers:
            self.number_listbox.insert(tk.END, number)

        # sets the layout for the listbox
        self.number_listbox.grid(row=0, column=0)

        # creates the "Add More" button
        self.add_more_button = tk.Button(self.parent, text="Add More Rounds", font=('Times New Roman', 12), bg='green', fg='yellow', command=self.add_more, borderwidth=2)
        self.add_more_button.grid(row=1, column=0)

        # creates the "Exit" button
        self.exit_button = tk.Button(self.parent, text="Exit", font=('Times New Roman', 12), bg='green', fg='yellow', command=self.parent.destroy, borderwidth=2)
        self.exit_button.grid(row=2, column=0)

    # creates a new GolfApp window if button is pressed
    def add_more(self):
        GolfApp(tk.Toplevel())

if __name__ == "__main__":
    root = tk.Tk()
    GolfApp(root)
    root.mainloop()
