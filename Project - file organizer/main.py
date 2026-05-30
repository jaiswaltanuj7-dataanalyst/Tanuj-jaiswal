import os
import shutil
folder_path = os.getcwd()
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"]
}
for folder in file_types.keys():                
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
for filename in os.listdir(folder_path):
    file_extension = os.path.splitext(filename)[1].lower()
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, folder, filename))
            break 
