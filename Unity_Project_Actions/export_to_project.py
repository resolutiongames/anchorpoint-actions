import anchorpoint as ap
import apsync as aps
import string
import random
import os

ctx = ap.get_context()
ui = ap.UI()

current_folder = ctx.path
username = ctx.username

path_name_var = "unitypath"
browse_button_var = "browse"
copy_button_var = "importfiles"

def create_action(dialog):
    action = ap.Action()
    action.unity_path = dialog.get_value(path_name_var)

    settings = aps.Settings()
    settings.set("unity_path", action.unity_path)
    settings.store()

def cb_path(dialog, value):
    dialog.set_enabled(browse_button_var, len(value) != 0)
    filename = get_filename(value)

def get_filename(action_name):
    return action_name.lower().replace(" ", "_")

settings = aps.Settings()

dialog = ap.Dialog()
dialog.title = "Copy files to Unity Project"
dialog.icon = ctx.icon

dialog.add_text("Folder to copy to:\t").add_input(placeholder="...\Local_Unity_Project\Assets\~selected_folder\..", var=path_name_var, callback=cb_path)
dialog.add_button("Copy", create_action, var = copy_button_var, enabled = False)
dialog.show()