import os
import gdown
import zipfile


os.makedirs("downloads", exist_ok=True)
models = {
    "APCIVMAPCAs_3d_lowres.zip": "1b4CPFHz7J9oMBprjB3D1UrPG-7K_E8yX"  
}

for filename, file_id in models.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    zip_path = os.path.join("downloads", filename)
    print(f"Descargando {filename} desde Google Drive...")
    gdown.download(url, zip_path, quiet=False)

    if filename.endswith(".zip"):
        extract_dir = "modelo"
        os.makedirs(extract_dir, exist_ok=True)
        print(f"Descomprimiendo {filename} en la carpeta '{extract_dir}'...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print("Descompresión completada.")

        # Eliminar el archivo ZIP
        os.remove(zip_path)
        print(f"Archivo ZIP '{filename}' eliminado.")

# Eliminar la carpeta de descarga si está vacía
if os.path.exists("downloads") and not os.listdir("downloads"):
    os.rmdir("downloads")
