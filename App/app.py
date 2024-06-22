import customtkinter as ct
from customtkinter import *
import numpy as np
import joblib

import warnings

# Suppress the warning
warnings.filterwarnings("ignore", message="X does not have valid feature names, but RandomForestClassifier was fitted with feature names")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

ct.set_appearance_mode("default")
ct.set_default_color_theme("blue")

root = ct.CTk()
root.title("Alzheimer's Disease Prediction")
root.geometry("1366x768")


frame1 = CTkFrame(master=root, width=200, height=10, fg_color="transparent", )
frame1.pack(padx=10, pady=(20, 40), fill="x" )

label1 = CTkLabel(master=frame1, text="Alzheimer's Disease Prediction", font=("Helvetica", 70, "bold"), text_color="#17AAEE")
label1.pack(padx=10, pady=10)

def predict_cdr(Age, Educ, SES, MMSE, nWBV):

    # Load the ML Model
    loaded_model = joblib.load(resource_path("D:\Anish\Projects\App\Random_forest.pkl"))
    
    # Convert user input to a numpy array
    user_input = np.array([[Age, Educ, SES, MMSE, nWBV]])

    # Use the loaded model to predict the CDR
    prediction = loaded_model.predict(user_input)[0]

    # Update the label with the prediction
    if prediction == 0:
        result_label.configure(text=f"No Alzheimer's Disease")
    elif prediction == 0.5:
        result_label.configure(text=f"Mild Alzheimer's Disease")
    else:
        result_label.configure(text=f"Severe Alzheimer's Disease")


frame = ct.CTkFrame(master=root,) #fg_color="transparent")
frame.pack(padx=10, pady=10, fill="both", expand=True)


# Labels and slider in a grid
labels = [
    ct.CTkLabel(master=frame,text="Age:",font=("",20,"bold")),
    ct.CTkLabel(master=frame,text="Education:",font=("",20,"bold")),
    ct.CTkLabel(master=frame,text="Socioeconomic Status:",font=("",20,"bold")),
    ct.CTkLabel(master=frame,text="Mini-Mental State Examination Score:",font=("",20,"bold")),
    ct.CTkLabel(master=frame,text="Normalized Whole Brain Volume:",font=("",20,"bold")),
]



slider = [
    ct.CTkSlider(
        master=frame,width=500, corner_radius=15, height=10, from_=0, to=100, number_of_steps=100, command=lambda value: sl1.set(int(value))
    ),
    ct.CTkSlider(
        master=frame,width=500, corner_radius=15, height=10, from_=0, to=30, number_of_steps=30, command=lambda value: sl2.set(int(value))
    ),
    ct.CTkSlider(
        master=frame,width=500, corner_radius=15, height=10, from_=0, to=5, number_of_steps=5, command=lambda value: sl3.set(int(value))
    ),
    ct.CTkSlider(
        master=frame,width=500, corner_radius=15, height=10, from_=0, to=20, number_of_steps=20, command=lambda value: sl4.set(int(value))
    ),
    ct.CTkSlider(
        master=frame,width=500, corner_radius=15, height=10, from_=0, to=1, number_of_steps=10, command=lambda value: sl5.set(round(value, 2))
    ),
]

sl1 = ct.StringVar(value="")
sl2 = ct.StringVar(value="")
sl3 = ct.StringVar(value="")
sl4 = ct.StringVar(value="")
sl5 = ct.StringVar(value="")

values = [
    ct.CTkLabel(master=frame, textvariable = sl1, font=("",20,"bold"), text_color="#17AAEE"),
    ct.CTkLabel(master=frame, textvariable = sl2, font=("",20,"bold"), text_color="#17AAEE"),
    ct.CTkLabel(master=frame, textvariable = sl3, font=("",20,"bold"), text_color="#17AAEE"),
    ct.CTkLabel(master=frame, textvariable = sl4, font=("",20,"bold"), text_color="#17AAEE"),
    ct.CTkLabel(master=frame, textvariable = sl5, font=("",20,"bold"), text_color="#17AAEE"),
]




labels[0].grid(row=0, column=0, padx=(270,10), pady=(150,5), sticky="w")
labels[1].grid(row=1, column=0, padx=(270,10), pady=5, sticky="w")
labels[2].grid(row=2, column=0, padx=(270,10), pady=5, sticky="w")
labels[3].grid(row=3, column=0, padx=(270,10), pady=5, sticky="w")
labels[4].grid(row=4, column=0, padx=(270,10), pady=5, sticky="w")


slider[0].grid(row=0, column=1, padx=12, pady=(150,5), sticky="we")
slider[1].grid(row=1, column=1, padx=12, pady=10, sticky="we")
slider[2].grid(row=2, column=1, padx=12, pady=10, sticky="we")
slider[3].grid(row=3, column=1, padx=12, pady=10, sticky="we")
slider[4].grid(row=4, column=1, padx=12, pady=10, sticky="we")


values[0].grid(row=0, column=2, padx=12, pady=(150,5), sticky="we")
values[1].grid(row=1, column=2, padx=12, pady=10, sticky="we")
values[2].grid(row=2, column=2, padx=12, pady=10, sticky="we")
values[3].grid(row=3, column=2, padx=12, pady=10, sticky="we")
values[4].grid(row=4, column=2, padx=12, pady=10, sticky="we")


# Button
button = ct.CTkButton(master=frame,text="Submit",font=("ariel",18),height=40,width=100,corner_radius=15,
                      command=lambda: predict_cdr(slider[0].get(), slider[1].get(), slider[2].get(), slider[3].get(), slider[4].get()))
button.grid(columnspan=2, padx=400, pady=10, sticky="e")



# Spacing label
result_label = ct.CTkLabel(master=frame,text="", font=("ariel",30,"bold"))
result_label.grid(row=6, column=1, pady=20, sticky="w")

root.mainloop()