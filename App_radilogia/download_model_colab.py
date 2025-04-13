import os
import gdown


os.makedirs("model", exist_ok=True)

models = {
    "segmentation_coa.pt": "1-m5lLKEiwziJO8E5_x80-8c25EAW7F1D",
    "pretrained_segmentation_spleen.pt": "10Ik1x_PQH45ysGxMkPpYwk09IecJix2"
}
for filename, file_id in models.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output = os.path.join("model", filename)
    print(f"Descargando {filename}...")
    gdown.download(url, output, quiet=False)