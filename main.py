import random
import dearpygui.dearpygui as dpg
import pyperclip as pc

current_password = ""

def random_pass(length):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']

    all = (lower + upper + num + special)
    
    return "".join(random.choices(all, k=length))

def button_callback(sender, app_data):
    global current_password
    length = dpg.get_value("length_slider")
    x = dpg.get_value("result_input")
    pc.copy(x)

def on_slider_change(sender, app_data):
    global current_password
    password = random_pass(app_data)
    current_password = password
    dpg.set_value("result_input", current_password)

def result(sender,app_data):
    pass
    
def main():
    dpg.create_context()

    with dpg.window(tag="f"):
        dpg.add_text("random password generator")
        dpg.add_slider_int(label="words",default_value=1,max_value=128, callback=on_slider_change,tag="length_slider")
        dpg.add_input_text(label="result",callback=result,tag="result_input")        
        dpg.add_button(label="Copy", callback=button_callback)

    dpg.create_viewport(title='Custom Title', width=600, height=200)
    dpg.set_primary_window("f",True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()



