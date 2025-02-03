import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
 
# Initialize Pandas DataFrames for exercises and recipes
exercises_df = pd.DataFrame(columns=['name', 'description'])
recipes_df = pd.DataFrame(columns=['name', 'ingredients', 'instructions'])
 
# Check if CSV files exist, and load data if they do
if os.path.exists('exercises.csv'):
   exercises_df = pd.read_csv('exercises.csv', index_col=0)
if os.path.exists('recipes.csv'):
   recipes_df = pd.read_csv('recipes.csv', index_col=0)
 
def add_exercise():
   global exercises_df
   exercise_name = exercise_name_var.get()
   exercise_description = exercise_description_var.get()
 
   # Add the exercise to the Pandas DataFrame
   new_exercise = {'name': exercise_name, 'description': exercise_description}
   exercises_df = exercises_df.append(new_exercise, ignore_index=True)
 
   # Update the exercise list
   update_exercise_list()
 
   # Clear the input fields
   exercise_name_var.set('')
   exercise_description_var.set('')
 
def add_recipe():
   global recipes_df
   recipe_name = recipe_name_var.get()
   recipe_ingredients = recipe_ingredients_var.get()
   recipe_instructions = recipe_instructions_var.get()
 
   # Add the recipe to the Pandas DataFrame
   new_recipe = {'name': recipe_name, 'ingredients': recipe_ingredients, 'instructions': recipe_instructions}
   recipes_df = recipes_df.append(new_recipe, ignore_index=True)
 
   # Update the recipe list
   update_recipe_list()
 
   # Clear the input fields
   recipe_name_var.set('')
   recipe_ingredients_var.set('')
   recipe_instructions_var.set('')
 
def show_details():
   selected_index_exercise = exercise_list.curselection()
   selected_index_recipe = recipe_list.curselection()
 
   if selected_index_exercise:
       index = selected_index_exercise[0]
       exercise_name = exercise_list.get(index)
       exercise_row = exercises_df[exercises_df['name'] == exercise_name]
       description = exercise_row['description'].values[0]
       show_details_window("Exercise Description", description)
   elif selected_index_recipe:
       index = selected_index_recipe[0]
       recipe_name = recipe_list.get(index)
       recipe_row = recipes_df[recipes_df['name'] == recipe_name]
       ingredients = recipe_row['ingredients'].values[0]
       instructions = recipe_row['instructions'].values[0]
       show_details_window("Recipe Details", f"Ingredients: {ingredients}\n\nInstructions: {instructions}")
 
def show_details_window(title, text):
   details_window = tk.Toplevel(root)
   details_window.title(title)
 
   details_label = tk.Label(details_window, text=text)
   details_label.pack()
 
def delete_selected_exercise():
   selected_index_exercise = exercise_list.curselection()
   if selected_index_exercise:
       index = selected_index_exercise[0]
       exercise_name = exercise_list.get(index)
       exercises_df.drop(exercises_df[exercises_df['name'] == exercise_name].index, inplace=True)
       update_exercise_list()
 
def delete_selected_recipe():
   selected_index_recipe = recipe_list.curselection()
   if selected_index_recipe:
       index = selected_index_recipe[0]
       recipe_name = recipe_list.get(index)
       recipes_df.drop(recipes_df[recipes_df['name'] == recipe_name].index, inplace=True)
       update_recipe_list()
 
def update_exercise_list():
   exercise_list.delete(0, 'end')
   for index, row in exercises_df.iterrows():
       exercise_list.insert('end', row['name'])
 
def update_recipe_list():
   recipe_list.delete(0, 'end')
   for index, row in recipes_df.iterrows():
       recipe_list.insert('end', row['name'])
 
def save_data():
   exercises_df.to_csv('exercises.csv')
   recipes_df.to_csv('recipes.csv')
 
def calculate_bmi():
   height = float(height_entry.get())
   weight = float(weight_entry.get())
   bmi = weight / ((height / 100) ** 2)  # Convert height to meters
   bmi_result_label.config(text=f"BMI: {bmi:.2f}")
 
# Create the main window
root = tk.Tk()
root.title("Fitness and Nutrition Planner")
 
# Double the size of the window
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")
 
# Create Notebook for Exercises, Recipes, and BMI Calculator
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
 
exercise_frame = tk.Frame(notebook)
recipe_frame = tk.Frame(notebook)
bmi_frame = tk.Frame(notebook)  # New frame for BMI calculator
 
notebook.add(exercise_frame, text="Exercises")
notebook.add(recipe_frame, text="Recipes")
notebook.add(bmi_frame, text="BMI Calculator")  # New tab for BMI calculator
 
# Exercise Entry Fields
exercise_name_label = tk.Label(exercise_frame, text="Exercise Name", font=("Helvetica", 16))
exercise_name_label.pack()
exercise_name_var = tk.StringVar()
exercise_name_entry = tk.Entry(exercise_frame, textvariable=exercise_name_var, font=("Helvetica", 16))
exercise_name_entry.pack()
 
exercise_description_label = tk.Label(exercise_frame, text="Exercise Description", font=("Helvetica", 16))
exercise_description_label.pack()
exercise_description_var = tk.StringVar()
exercise_description_entry = tk.Entry(exercise_frame, textvariable=exercise_description_var, font=("Helvetica", 16))
exercise_description_entry.pack()
 
add_exercise_button = tk.Button(exercise_frame, text="Add Exercise", command=add_exercise, font=("Helvetica", 16))
add_exercise_button.pack()
 
delete_exercise_button = tk.Button(exercise_frame, text="Delete Exercise", command=delete_selected_exercise,
                                  font=("Helvetica", 16))
delete_exercise_button.pack()
 
# Recipe Entry Fields
recipe_name_label = tk.Label(recipe_frame, text="Recipe Name", font=("Helvetica", 16))
recipe_name_label.pack()
recipe_name_var = tk.StringVar()
recipe_name_entry = tk.Entry(recipe_frame, textvariable=recipe_name_var, font=("Helvetica", 16))
recipe_name_entry.pack()
 
recipe_ingredients_label = tk.Label(recipe_frame, text="Ingredients", font=("Helvetica", 16))
recipe_ingredients_label.pack()
recipe_ingredients_var = tk.StringVar()
recipe_ingredients_entry = tk.Entry(recipe_frame, textvariable=recipe_ingredients_var, font=("Helvetica", 16))
recipe_ingredients_entry.pack()
 
recipe_instructions_label = tk.Label(recipe_frame, text="Instructions", font=("Helvetica", 16))
recipe_instructions_label.pack()
recipe_instructions_var = tk.StringVar()
recipe_instructions_entry = tk.Entry(recipe_frame, textvariable=recipe_instructions_var, font=("Helvetica", 16))
recipe_instructions_entry.pack()
 
add_recipe_button = tk.Button(recipe_frame, text="Add Recipe", command=add_recipe, font=("Helvetica", 16))
add_recipe_button.pack()
 
delete_recipe_button = tk.Button(recipe_frame, text="Delete Recipe", command=delete_selected_recipe,
                                font=("Helvetica", 16))
delete_recipe_button.pack()
 
# Exercise Listbox
exercise_list = tk.Listbox(exercise_frame, font=("Helvetica", 16))
exercise_list.pack()
update_exercise_list()
 
# Recipe Listbox
recipe_list = tk.Listbox(recipe_frame, font=("Helvetica", 16))
recipe_list.pack()
update_recipe_list()
 
# BMI Calculator Entry Fields
height_label = tk.Label(bmi_frame, text="Height (cm):", font=("Helvetica", 16))
height_label.pack()
height_entry = tk.Entry(bmi_frame, font=("Helvetica", 16))
height_entry.pack()
 
weight_label = tk.Label(bmi_frame, text="Weight (kg):", font=("Helvetica", 16))
weight_label.pack()
weight_entry = tk.Entry(bmi_frame, font=("Helvetica", 16))
weight_entry.pack()
 
calculate_bmi_button = tk.Button(bmi_frame, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 16))
calculate_bmi_button.pack()
 
bmi_result_label = tk.Label(bmi_frame, text="", font=("Helvetica", 16))
bmi_result_label.pack()
 
# Show Details Button
show_details_button = tk.Button(root, text="Show Details", command=show_details, font=("Helvetica", 16))
show_details_button.pack()
 
# Save and Exit Buttons
exit_button = tk.Button(root, text="Exit", command=save_data, font=("Helvetica", 16))
exit_button.pack()
 
root.mainloop()
 
