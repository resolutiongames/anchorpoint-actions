import anchorpoint as ap
import apsync as aps
import shutil
import string
import random
import os

ctx = ap.get_context()
ui = ap.UI()

selected_files = ctx.selected_files
selected_folders = ctx.selected_folders

export_path_name_var = "exportpath"
browse_button_var = "browse"
copy_button_var = "copy"

def create_action(dialog):
    settings.store()
    success, error = copy_all_files_and_folders(dialog.get_value(export_path_name_var))
    if (success):
            ui.show_success("Sucess!", "Files and folders copied to Unity Project", 3000)
    else:
        ui.show_error("Error!", "Could not copy files and folders to Unity Project " + error, 3000)
    dialog.close()

def browse_action(dialog):
    path = ui.open_tab(export_path_name_var)
    if path is not None:
        dialog.set_value(export_path_name_var, path)
        settings = aps.Settings()
        settings.set("unity_path", path)

def cb_path(dialog, value):
    dialog.set_enabled(copy_button_var, len(value) != 0)

def get_folder(action_name):
    return action_name.lower().replace(" ", "_")

def copy_all_files_and_folders(path):
    for d in selected_folders:
        try:
            shutil.copytree(d, path, dirs_exist_ok=True)
        except Exception as error:
            return (False, str(error))
    for f in selected_files:
        try:
            shutil.copy(f, path)
        except Exception as error:
            return (False, str(error))
    return True, ""

settings = aps.Settings()
folder = ""
dialog = ap.Dialog()
dialog.title = "Export files to Unity Project..."
dialog.icon = ctx.icon

dialog.add_text("Folder to copy to:\t").add_input(placeholder="...\Local_Unity_Project\Assets\~selected_folder\..", var = export_path_name_var, enabled=False, callback=cb_path, browse=ap.BrowseType.Folder, browse_path = export_path_name_var)
dialog.add_button("Export", create_action, var = copy_button_var, enabled = False)
dialog.show()