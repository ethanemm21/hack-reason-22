from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# CONSTANTS
PEACH = "#FAD9C3"
LIGHT_GREEN = "#D4E6C9"
FONT_NAME = "Algerian"

# WRITE INPUT PROLOG SCRIPT   
def write():
    user_industry = industry_clicked.get()
    user_noun = noun_clicked.get()
    user_adj = adj_clicked.get()

    if user_industry == industry_options[0] or user_noun == noun_options[0] or user_adj == adj_options[0]:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        query = f"\ninput({user_industry}, {user_noun}, {user_adj})"
        with open("color_facts.txt", "a") as prolog_script:
            prolog_script.write(query)

# UI
window = Tk()
window.title("Chroma")
window.config(padx=50, pady=150, bg="black")

title_label = Label(text="CHROMA", fg=LIGHT_GREEN, bg="black", font=(FONT_NAME, 50))
title_label.grid(row=1, column=1)

canvas = Canvas(height=200, width=200, bg="black")

# LABELS
industry_label = Label(text="Industry/Purpose:", fg=PEACH, bg="black", font=(FONT_NAME, 25))
industry_label.grid(row=2, column=0)
noun_company = Label(text="Noun/Logo:", fg=PEACH, bg="black", font=(FONT_NAME, 25))
noun_company.grid(row=3, column=0) 
adj_company = Label(text="Describe/Adjective:", fg=PEACH, bg="black", font=(FONT_NAME, 25))
adj_company.grid(row=4, column=0)

# DROPDOWN OPTIONS
industry_options = ["Choose an option", "Food", "Health", "Agriculture", "Education", "Technology", "Engineering", "Entertainment", "Manufacturing", "Media", "Transportation", "Finance"]
noun_options = ["Choose an option", "Snake", "Bull", "Cat", "Bear", "Dove", "Buffalo", "Lion", "Horse", "Wolf", "Owl"]
adj_options = ["Choose an option", "Classy", "Sophisticated", "Creative", "Dependable", "Secure", "Positive", "Friendly", "Bold", "Devoted", "Quality", "Confident", "Affordable", "Clean", "Simple"]

# DROPDOWN
industry_clicked = StringVar()
industry_clicked.set(industry_options[0])
industry_drop = OptionMenu(window, industry_clicked, *industry_options)
industry_drop.config(width=35)
industry_drop.grid(row=2, column=1)

noun_clicked = StringVar()
noun_clicked.set(noun_options[0])
noun_drop = OptionMenu(window, noun_clicked, *noun_options)
noun_drop.config(width=35)
noun_drop.grid(row=3, column=1)

adj_clicked = StringVar()
adj_clicked.set(adj_options[0])
adj_drop = OptionMenu(window, adj_clicked, *adj_options)
adj_drop.config(width=35)
adj_drop.grid(row=4, column=1)

# BUTTONS
submit_btn = Button(text="Submit", fg="black", bg=PEACH, command=write)
submit_btn.grid(row=5, column=1)

window.mainloop()