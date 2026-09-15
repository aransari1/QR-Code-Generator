import tkinter as tk
import customtkinter as ctk
from backend import check_color, qr_generate
from PIL import Image
from CTkColorPicker import AskColor
from CTkMessagebox import CTkMessagebox


def switch_theme():
    switch_val = switch_var.get()
    if switch_val == 'dark':
        ctk.set_appearance_mode("dark")
        switch._text = "Dark"
    elif switch_val == 'light':
        ctk.set_appearance_mode("light")
        switch._text = "Light"
    else:
        ctk.set_appearance_mode("System")
        switch._text = "System"


def custom_color_pick(button_name):
    color_picker = AskColor()
    color = color_picker.get()

    if color:
        match button_name:
            case "pattern":
                Pattern_Input.delete(0, "end")
                Pattern_Input.insert(0, color)
            case "background":
                Background_Input.delete(0, 'end')
                Background_Input.insert(0, color)


def validate_fields():
    data = Data_Input.get()
    pattern = Pattern_Input.get()
    background = Background_Input.get()
    if not data:
        CTkMessagebox(title="Error!",
                      message="Data Field is Required",
                      icon='cancel')
        return None
    if not pattern:
        CTkMessagebox(title="Error!",
                      message="Pattern Color Field is Required",
                      icon='cancel')
        return None

    if not check_color(pattern):  # check if input is a valid color or not
        CTkMessagebox(title="Error!",
                      message="Enter valid pattern colour",
                      icon='cancel')
        return None
    if not background:
        CTkMessagebox(title="Error!",
                      message="Background Color Field is Required",
                      icon='cancel')
        return None
    if not check_color(background):  # check if input is a valid color or not
        CTkMessagebox(title="Error!",
                      message="Enter valid background colour",
                      icon='cancel')
        return None

    return qr_generate(data, pattern, background, qr_preview)


def clear_field():
    Data_Input.delete(0, "end")
    Data_Input.configure(placeholder_text="Insert Data")
    Pattern_Input.delete(0, "end")
    Pattern_Input.configure(placeholder_text="Color Name or Code")
    Background_Input.delete(0, "end")
    Background_Input.configure(placeholder_text="Color Name or Code")
    # qr_preview.configure(image=None, text="")
    # qr_preview.image = None


def save_qr():
    img = validate_fields()
    if img:
        path = tk.filedialog.asksaveasfilename(defaultextension="*.png",
                                               filetypes=[("PNG files", '*.png'), ("JPG files", '*.jpg'),
                                                          ("All files", '*')],
                                               initialdir="Saved QR Codes",
                                               title="Save"
                                               )
        if path:
            img.save(path)
            CTkMessagebox(title="Success!",
                          message="QR code is saved in %s successfully." % path,
                          icon='check')
        else:
            CTkMessagebox(title="Error!",
                          message="Path is Required",
                          icon='cancel')


def help_dialogue():
    CTkMessagebox(title="How to use it?",
                  message="1. Insert your data in the data field."
                          "\n2. Insert the color in the pattern field."
                          "\n Insert the color in the background field"
                          "\n4. Generate Button : used to generate the preview of the QR."
                          "\n5. Clear Button: Used to clear all the input fields."
                          "\n6. Save Button : used to save the QR code in the storage in image file."
                          "\n7. Color Wheel : used to insert the custom color in the QR code.",
                  icon='question')


app = ctk.CTk()
app.geometry("700x400")
app.title("QR Code Generator")
app.iconbitmap("Icons/qr.ico")
ctk.set_default_color_theme("green")

# Image Loading
color_wheel_icon = ctk.CTkImage(light_image=Image.open("Icons/color_wheel.png"),
                                dark_image=Image.open("Icons/color_wheel.png"),
                                size=(30, 30))

light_mode_icon = ctk.CTkImage(light_image=Image.open("Icons/light_mode_dark.png"),
                               dark_image=Image.open("Icons/light_mode_light.png"),
                               size=(30, 30))
dark_mode_icon = ctk.CTkImage(light_image=Image.open("Icons/dark_mode_dark.png"),
                              dark_image=Image.open("Icons/dark_mode_light.png"),
                              size=(30, 30))
help_icon = ctk.CTkImage(light_image=Image.open("Icons/help_dark.png"),
                         dark_image=Image.open("Icons/help_light.png"),
                         size=(30, 30))
save_icon = ctk.CTkImage(light_image=Image.open("Icons/save_light.png"),
                         dark_image=Image.open("Icons/save_light.png"),
                         size=(30, 30))
clear_icon = ctk.CTkImage(light_image=Image.open("Icons/delete_sweep_light.png"),
                          dark_image=Image.open("Icons/delete_sweep_light.png"),
                          size=(30, 30))
generate_icon = ctk.CTkImage(light_image=Image.open("Icons/qr.png"),
                             dark_image=Image.open("Icons/qr.png"),
                             size=(30, 30))

# Top Row
Light_Mode_Icon = ctk.CTkLabel(app, image=light_mode_icon, text="", width=10)
Light_Mode_Icon.place(relx=0.05, rely=0.06, anchor=tk.CENTER)

switch_var = ctk.StringVar(value="system")
switch = ctk.CTkSwitch(app, command=switch_theme, text='',
                       variable=switch_var, onvalue="dark", offvalue="light")
switch.place(relx=0.15, rely=0.06, anchor=tk.CENTER)

Dark_Mode_Icon = ctk.CTkLabel(app, image=dark_mode_icon, text="", width=10)
Dark_Mode_Icon.place(relx=0.16, rely=0.06, anchor=tk.CENTER)

Help_Button = ctk.CTkButton(app, text="", image=help_icon, command=help_dialogue, width=10)
Help_Button.place(relx=0.95, rely=0.06, anchor=tk.CENTER)

# Data Input
Data_Label = ctk.CTkLabel(app, text="Data :", fg_color="transparent")
Data_Label.place(relx=0.054, rely=0.25, anchor=tk.CENTER)

Data_Input = ctk.CTkEntry(app, placeholder_text="Insert Data")
Data_Input.place(relx=0.3, rely=0.25, anchor=tk.CENTER)

# Pattern Input
Pattern_Label = ctk.CTkLabel(app, text="Pattern colour :", fg_color="transparent")
Pattern_Label.place(relx=0.088, rely=0.35, anchor=tk.CENTER)

Pattern_Input = ctk.CTkEntry(app, placeholder_text="Color Name or Code")
Pattern_Input.place(relx=0.3, rely=0.35, anchor=tk.CENTER)

Pattern_Custom_Color_Button = ctk.CTkButton(app, image=color_wheel_icon, text="", width=10,
                                            command=lambda: custom_color_pick('pattern'))
Pattern_Custom_Color_Button.place(relx=0.45, rely=0.35, anchor=tk.CENTER)

# Background Input
Background_Label = ctk.CTkLabel(app, text="Background colour :", fg_color="transparent")
Background_Label.place(relx=0.11, rely=0.45, anchor=tk.CENTER)

Background_Input = ctk.CTkEntry(app, placeholder_text="Color Name or Code")
Background_Input.place(relx=0.3, rely=0.45, anchor=tk.CENTER)

Background_Custom_Color_Button = ctk.CTkButton(app, image=color_wheel_icon, text="", width=10,
                                               command=lambda: custom_color_pick('background'))
Background_Custom_Color_Button.place(relx=0.45, rely=0.45, anchor=tk.CENTER)

# Buttons
Generate_Button = ctk.CTkButton(master=app, text="Generate QR", command=validate_fields, image=generate_icon)
Generate_Button.place(relx=0.15, rely=0.9, anchor=tk.CENTER)

Clear_Button = ctk.CTkButton(master=app, text="Clear All", command=clear_field, image=clear_icon)
Clear_Button.place(relx=0.38, rely=0.9, anchor=tk.CENTER)

Save_Button = ctk.CTkButton(master=app, text="Save QR", command=save_qr, image=save_icon)
Save_Button.place(relx=0.62, rely=0.9, anchor=tk.CENTER)

qr_preview = ctk.CTkLabel(app, text='')
qr_preview.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

app.mainloop()
