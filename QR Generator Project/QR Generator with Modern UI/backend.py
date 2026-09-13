# Imports
import qrcode
from colour import Color
import customtkinter as ctk


def check_color(picked):
    """This function is used for checking if the user input is colour or not.

    check_color:
    check_color(picked): first it replaces the spaces with empty space in the given input.\nAfter that checks if the input is color or not with Color(picked) method.\n The try and except block are used for error correction.

    Returns:
        True: If the input is color.
        False: if the input is not color.
    """
    try:
        picked = picked.replace(" ", "")
        Color(picked)
        return True
    except ValueError:
        return False


def qr_generate(data, pattern_color, background_color, label=None):
    qr = qrcode.QRCode(
        version=1,
        box_size=20,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=pattern_color,
        back_color=background_color
    ).convert("RGB")

    qr_make = img

    if label is not None:
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(220, 220))
        label.configure(image=ctk_img, text="")
        label.image = ctk_img

    return qr_make
