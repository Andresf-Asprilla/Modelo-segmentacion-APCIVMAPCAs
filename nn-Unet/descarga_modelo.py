import os
import shutil
import gdown
from nnunetv2.paths import nnUNetv2_install_pretrained_model_from_zip


mount_dir = os.getcwd()
def make_if_dont_exist(folder_path, overwrite=False):
    """
    Crea una carpeta si no existe. Si 'overwrite' es True, la sobrescribe.
    """
    if os.path.exists(folder_path):
        if overwrite:
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)

path_dict = {
    "nnUNet_raw": os.path.join(mount_dir, "nnUNet_raw"),
    "nnUNet_preprocessed": os.path.join(mount_dir, "nnUNet_preprocessed"),
    "nnUNet_results": os.path.join(mount_dir, "nnUNet_results"),
    "RAW_DATA_PATH": os.path.join(mount_dir, "RawData"),
}

for env_var, path in path_dict.items():
    os.environ[env_var] = path
    make_if_dont_exist(path, overwrite=False)
os.makedirs("downloads", exist_ok=True)

models = {
    "APCIVMAPCAs_3d_lowres.zip": "1NYfEutP5l01w-7YGXQzP5Boo5MNzw7CO"
}

for filename, file_id in models.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    zip_path = os.path.join("downloads", filename)
    gdown.download(url, zip_path, quiet=False)
    nnUNetv2_install_pretrained_model_from_zip(zip_path)
    os.remove(zip_path)
if os.path.exists("downloads") and not os.listdir("downloads"):
    os.rmdir("downloads")

