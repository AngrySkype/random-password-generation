import dearpygui.dearpygui as dpg
import pyperclip
import secrets

dpg.create_context()


preset = ["Normal", "Strong", "Very Strong"]

lower = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?"]

all_chars = lower + upper + number + special

def random_words(length):
    chars = []

    if dpg.get_value("lower"):
        chars += lower

    if dpg.get_value("upper"):
        chars += upper

    if dpg.get_value("number"):
        chars += number

    if dpg.get_value("special"):
        chars += special

    if not chars:
        return "Minimum one checkbox needed !"

    return "".join(secrets.choice(chars) for _ in range(length))

def slider_callback(sender, app_data):
    random_number = random_words(app_data)
    dpg.set_value("result", value=random_number)

def button_callback(sender, app_data):
    x = dpg.get_value("result")
    pyperclip.copy(x)

def random_callback(sender, app_data):
    length = dpg.get_value("slider")
    dpg.set_value("result", random_words(length))

def preset_callback(sender, app_data):
    dpg.set_value("lower", app_data in ["Normal", "Strong", "Very Strong"])
    dpg.set_value("upper", app_data in ["Normal", "Strong", "Very Strong"])
    dpg.set_value("number", app_data in ["Strong", "Very Strong"])
    dpg.set_value("special", app_data in ["Very Strong"])
    random_callback(sender,app_data)

def main():
    with dpg.window(tag="f"):
        dpg.add_text("Simple password generator")
        dpg.add_slider_int(label="Words",min_value=1,max_value=128, callback=slider_callback, tag="slider")
        dpg.add_input_text(label="Result",tag="result",readonly=True)

        with dpg.group(horizontal=True):
            dpg.add_button(label="Copy", callback=button_callback)
            dpg.add_button(label="Random", callback=random_callback, tag="random")
            with dpg.tooltip("random"):
                dpg.add_text("Randomize current length password")
            dpg.add_combo(label="Select preset", items=preset, callback=preset_callback,tag="preset")

        with dpg.group(horizontal=True):
            dpg.add_checkbox(label="Lowercase", tag="lower")
            dpg.add_checkbox(label="Uppercase", tag="upper")
            dpg.add_checkbox(label="Numbers", tag="number")
            dpg.add_checkbox(label="Special", tag="special")

    dpg.create_viewport(title='Simple password generator', width=600, height=200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("f", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
