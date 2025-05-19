import os
import zipfile
import gdown

# Detectar automáticamente el directorio base donde se ejecuta el usuario
base_dir = os.getcwd()

# Definir rutas a partir del directorio actual
raw_data = os.path.join(base_dir, "nnUNet_raw")
preprocessed = os.path.join(base_dir, "nnUNet_preprocessed")
results = os.path.join(base_dir, "nnUNet_results")

# Establecer variables de entorno
os.environ["NNUNET_RAW_DATA"] = raw_data
os.environ["NNUNET_PREPROCESSED"] = preprocessed
os.environ["NNUNET_RESULTS"] = results

# Crear carpetas necesarias
for path in [raw_data, preprocessed, results]:
    os.makedirs(path, exist_ok=True)

# Descargar el modelo desde Google Drive
url = "https://drive.google.com/uc?id=1NYfEutP5l01w-7YGXQzP5Boo5MNzw7CO"
zip_path = "APCIVMAPCAs_3d_lowres.zip"
gdown.download(url, zip_path, quiet=False)

# Extraer el modelo en la carpeta de resultados
def extract_model_to_results(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(results)

extract_model_to_results(zip_path)
os.remove(zip_path)
