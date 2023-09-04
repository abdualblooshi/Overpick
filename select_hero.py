import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard
import time
import random

# Define all heroes and their coordinates
all_heroes = {
    "Ana": (1413, 831),
    "Lucio": (1474, 897),
    "Baptiste": (1477, 831),
    "Brigette": (1537, 835),
    "Mercy": (1538, 898),
    "Moira": (1603, 898),
    "Zenyetta": (1670, 899),
    "Kiriko": (1669, 830),
    "Illari": (1601, 829),
    "Lifeweaver": (1411, 892),
    "Pharah": (1248, 831),
    "Mei": (1180, 830),
    "Junkrat": (1119, 832),
    "Hanzo": (1055, 834),
    "Genji": (988, 829),
    "Echo": (924, 834),
    "Mcree": (861, 833),
    "Bastion": (799, 828),
    "Ashe": (735, 830),
    "Widowmaker": (1214, 897),
    "Tracer": (1147, 894),
    "Torbjorn": (1087, 893),
    "Symmetra": (1019, 897),
    "Sombra": (962, 894),
    "Soldier 76": (895, 891),
    "Soljurn": (838, 893),
    "Reaper": (756, 893),
    "Reinhardt": (572, 832),
    "Rammetra": (501, 831),
    "Orisa": (440, 837),
    "Junker Queen": (373, 828),
    "Doomfist": (313, 835),
    "DVA": (249, 835),
    "Zarya": (567, 896),
    "Hammond": (506, 898),
    "Winston": (435, 897),
    "Sigma": (374, 895),
    "Roadhog": (318, 894)
}

# Mapping of hero names to their categories
hero_to_category = {
    "Support": ["Ana", "Lucio", "Baptiste", "Brigette", "Mercy", "Moira", "Zenyetta", "Kiriko", "Illari", "Lifeweaver"],
    "DPS": ["Pharah", "Mei", "Junkrat", "Hanzo", "Genji", "Echo", "Mcree", "Bastion", "Ashe", "Widowmaker", "Tracer", "Torbjorn", "Symmetra", "Sombra", "Soldier 76", "Soljurn", "Reaper"],
    "Tank": ["Reinhardt", "Rammetra", "Orisa", "Junker Queen", "Doomfist", "DVA", "Zarya", "Hammond", "Winston", "Sigma", "Roadhog"]
}

# Organize heroes into categories based on the mapping
categories = {category: {hero: all_heroes[hero] for hero in heroes} for category, heroes in hero_to_category.items()}

# Coordinate for the select hero button
select_hero_button = (962, 995)

def select_hero():
    selected_hero = hero_var.get()
    if selected_hero in all_heroes:
        selected_hero_coordinates = all_heroes[selected_hero]
        
        pyautogui.moveTo(selected_hero_coordinates)
        pyautogui.click()
        
        time.sleep(0.1)
        
        pyautogui.moveTo(select_hero_button)
        pyautogui.click()

        status_label.config(text=f"You selected {selected_hero}.")
    else:
        status_label.config(text="Please select a valid hero from the dropdown.")

def update_label(event):
    selected_hero = hero_var.get()
    if selected_hero in all_heroes:
        status_label.config(text=f"{selected_hero} is ready for selection. Press 'M' in-game to choose.")
    else:
        status_label.config(text="Please select a valid hero from the dropdown.")

# Function to stop the "M" hotkey functionality
def stop_selecting():
    keyboard.remove_hotkey('m')
    hero_var.set("Select a hero")
    category_var.set("Select a category")
    status_label.config(text="Hero selection stopped. Choose a hero to start again.")


# Set up the hotkey to trigger the function when "M" is pressed
keyboard.add_hotkey('m', select_hero)

# Function to update the hero dropdown based on the selected category
def update_hero_dropdown(event):
    category = category_var.get()
    hero_dropdown['values'] = list(categories[category].keys())
    hero_dropdown.current(0)

def select_random_hero():
    category = category_var.get()
    hero = random.choice(list(categories[category].keys()))
    hero_var.set(hero)
    

def update_hero_status():
    selected_hero = hero_var.get()
    if selected_hero in all_heroes:
        status_label.config(text=f"{selected_hero} is ready for selection. Press 'M' in-game to choose.")
    else:
        status_label.config(text="Please select a valid hero from the dropdown.")

# Create the main application window
root = tk.Tk()
root.geometry("542x270")
root.minsize(542, 270)
root.title("Overpick")

# Instruction label at the top
instruction_label = ttk.Label(root, text="Choose a hero and press 'M' in-game to select.")
instruction_label.pack(pady=10)

# Status label 
status_label = ttk.Label(root, text="Select a hero from the dropdown.")
status_label.pack(pady=10)

# Category dropdown
category_var = tk.StringVar(root)
category_var.set("Select a category")
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=list(categories.keys()), state='readonly')
category_dropdown.pack(pady=10)
category_dropdown.bind("<<ComboboxSelected>>", update_hero_dropdown)

# Hero dropdown
hero_var = tk.StringVar(root)
hero_var.set("Select a hero")
hero_dropdown = ttk.Combobox(root, textvariable=hero_var, state='readonly')
hero_dropdown.pack(pady=10)
hero_dropdown.bind("<<ComboboxSelected>>", update_label)

# Button frame for horizontal alignment
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Update Hero Status button
update_status_button = ttk.Button(button_frame, text="Choose Hero", command=update_hero_status)
update_status_button.grid(row=0, column=0, padx=5)

# Stop Selecting button
stop_button = ttk.Button(button_frame, text="Stop Selecting", command=stop_selecting)
stop_button.grid(row=0, column=1, padx=5)

# Run the main application loop
root.mainloop()