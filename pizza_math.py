import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("360x390")
app.title("Pizza Calculator")
app.resizable(False, False)


total_area1_var = ctk.StringVar()
total_price1_var = ctk.StringVar()
price_cm21_var = ctk.StringVar()
total_area2_var = ctk.StringVar()
total_price2_var = ctk.StringVar()
price_cm22_var = ctk.StringVar()

def entry_validation(event=None):

    valid_entry=(entry_diameter1.get().strip() and entry_quantity1.get().strip() and  entry_price1.get().strip() and entry_diameter2.get().strip() and entry_quantity2.get().strip() and  entry_price2.get().strip())

    if valid_entry:
        button.configure(state="normal")





# calculation
def main():
    try:
        a1 = float(entry_diameter1.get())
        b1 = float(entry_quantity1.get())
        c1 = float(entry_price1.get())
        a2 = float(entry_diameter2.get())
        b2 = float(entry_quantity2.get())
        c2 = float(entry_price2.get())

        if a1<0 or b1<0 or c1<0 or a2<0 or b2<0 or c2<0:
            total_area1_var.set("Error!")
            total_price1_var.set("Error!")
            price_cm21_var.set("Error!")        
            total_area2_var.set("Error!")
            total_price2_var.set("Error!")
            price_cm22_var.set("Error!")
        
        else:

            area1 = ((0.5 * a1) ** 2 * 3.14) * b1
            total1 = c1 * b1
            price1_cm2 = total1 / area1

            area2 = ((0.5 * a2) ** 2 * 3.14) * b2
            total2 = c2 * b2
            price2_cm2 = total2 / area2

            total_area1_var.set(f"{area1:.2f}")
            total_price1_var.set(f"{total1:.2f}")
            price_cm21_var.set(f"{price1_cm2:.4f}")

            total_area2_var.set(f"{area2:.2f}")
            total_price2_var.set(f"{total2:.2f}")
            price_cm22_var.set(f"{price2_cm2:.4f}")

        # condition colouring
        if price1_cm2 < price2_cm2:
            price_cm21_lbl.configure(fg_color="#02cc10")  
            price_cm22_lbl.configure(fg_color="#cc0202")  
        elif price1_cm2 > price2_cm2:
            price_cm21_lbl.configure(fg_color="#cc0202")
            price_cm22_lbl.configure(fg_color="#02cc10")
        else:
            price_cm21_lbl.configure(fg_color="#fa6705")  
            price_cm22_lbl.configure(fg_color="#fa6705")

    except Exception as e:
        total_area1_var.set("Error!")
        total_price1_var.set("Error!")
        price_cm21_var.set("Error!")
        total_area2_var.set("Error!")
        total_price2_var.set("Error!")
        price_cm22_var.set("Error!")

# headers
ctk.CTkLabel(app, text="Parameters", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=1, column=1, padx=10, pady=10)
ctk.CTkLabel(app, text="1.Pizza", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=1, column=2, padx=10, pady=10)
ctk.CTkLabel(app, text="2.Pizza", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=1, column=3, padx=10, pady=10)

# parameter labels
labels = ["Diameter[CM]", "Quantity[PCS]", "Cost[/PCS]"]
for i, text in enumerate(labels, start=2):
    ctk.CTkLabel(app, text=text, text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=i, column=1, padx=10, pady=5)

# parameters
entry_diameter1 = ctk.CTkEntry(app, width=100)
entry_quantity1 = ctk.CTkEntry(app, width=100)
entry_price1 = ctk.CTkEntry(app, width=100)
entry_diameter2 = ctk.CTkEntry(app, width=100)
entry_quantity2 = ctk.CTkEntry(app, width=100)
entry_price2 = ctk.CTkEntry(app, width=100)

entry_diameter1.grid(row=2, column=2)
entry_quantity1.grid(row=3, column=2)
entry_price1.grid(row=4, column=2)

entry_diameter2.grid(row=2, column=3)
entry_quantity2.grid(row=3, column=3)
entry_price2.grid(row=4, column=3)

# button
button= ctk.CTkButton(app, text="Calculate", text_color="black", fg_color="#05f5dd", width=100, command=main)
button.grid(row=5, column=2, pady=10)
button.configure(state="disabled")

# headers
ctk.CTkLabel(app, text="Results", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=6, column=1, padx=10, pady=10)
ctk.CTkLabel(app, text="1.Pizza", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=6, column=2, padx=10, pady=10)
ctk.CTkLabel(app, text="2.Pizza", text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=6, column=3, padx=10, pady=10)

# output labels
results = ["T.Area[CM²]", "T.Cost", "Cost/CM²"]
for i, text in enumerate(results, start=7):
    ctk.CTkLabel(app, text=text, text_color="black", fg_color="#f5b105", width=100, corner_radius=8).grid(row=i, column=1, padx=10, pady=5)

# output display
ctk.CTkLabel(app, textvariable=total_area1_var, width=100, height=25, corner_radius=8).grid(row=7, column=2)
ctk.CTkLabel(app, textvariable=total_price1_var, width=100, height=25, corner_radius=8).grid(row=8, column=2)
price_cm21_lbl = ctk.CTkLabel(app, textvariable=price_cm21_var, width=100, height=25, corner_radius=8)
price_cm21_lbl.grid(row=9, column=2)

ctk.CTkLabel(app, textvariable=total_area2_var, width=100, height=25, corner_radius=8).grid(row=7, column=3)
ctk.CTkLabel(app, textvariable=total_price2_var, width=100, height=25, corner_radius=8).grid(row=8, column=3)
price_cm22_lbl = ctk.CTkLabel(app, textvariable=price_cm22_var, width=100, height=25, corner_radius=8)
price_cm22_lbl.grid(row=9, column=3)

entry_diameter1.bind("<KeyRelease>",entry_validation)
entry_quantity1.bind("<KeyRelease>",entry_validation)
entry_price1.bind("<KeyRelease>",entry_validation)
entry_diameter2.bind("<KeyRelease>",entry_validation)
entry_quantity2.bind("<KeyRelease>",entry_validation)
entry_price2.bind("<KeyRelease>",entry_validation)


app.mainloop()
