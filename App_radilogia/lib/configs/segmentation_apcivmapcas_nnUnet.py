# @title
import os
import shutil
import tempfile
import nibabel as nib
import SimpleITK as sitk
import monai.transforms as tf
import subprocess
from IPython.display import display, HTML, clear_output

def obtener_espaciados_originales(ruta_directorio):
    espaciados = {}
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith('.nii') or archivo.endswith('.nii.gz'):
            nombre_base = os.path.splitext(os.path.splitext(archivo)[0])[0] 
            ruta = os.path.join(ruta_directorio, archivo)
            img = sitk.ReadImage(ruta)
            espaciados[nombre_base] = {
                "spacing": img.GetSpacing(),
                "origin": img.GetOrigin(),
                "direction": img.GetDirection()
            }
    return espaciados

def NormalizacionyEspaciado(ruta_directorio, ruta_salida, nuevo_espaciado):
    os.makedirs(ruta_salida, exist_ok=True)
    nombres_originales = {}
    nombres_vistos = set()
    for idx, archivo in enumerate(os.listdir(ruta_directorio)):
        if archivo.endswith('.nii') or archivo.endswith('.nii.gz'):
            ruta_entrada = os.path.join(ruta_directorio, archivo)
            identificador = f"{idx:03d}"
            nombre_paciente = f"paciente_{identificador}_0000.nii.gz"
            ruta_salida_archivo = os.path.join(ruta_salida, nombre_paciente)

            imagen = sitk.ReadImage(ruta_entrada)
            imagen.SetSpacing(nuevo_espaciado)
            sitk.WriteImage(imagen, ruta_salida_archivo)

            nifti_imagen = nib.load(ruta_salida_archivo)
            datos_imagen = nifti_imagen.get_fdata()
            affine = nifti_imagen.affine

            escalar_intensidad = tf.ScaleIntensity()
            imagen_normalizada = escalar_intensidad(datos_imagen).numpy()

            nib.save(nib.Nifti1Image(imagen_normalizada, affine), ruta_salida_archivo)

            nombre_original = os.path.splitext(os.path.splitext(archivo)[0])[0]
            if nombre_original in nombres_vistos:
                raise ValueError(f"Nombre duplicado detectado: {nombre_original}. Los nombres deben ser únicos.")
            nombres_vistos.add(nombre_original)
            nombres_originales[nombre_paciente.replace('_0000.nii.gz', '')] = archivo

    return nombres_originales

def RestaurarEspaciadoSalida(ruta_segmentaciones, espaciados_originales, nombres_originales):
    for archivo in os.listdir(ruta_segmentaciones):
        if archivo.endswith('.nii') or archivo.endswith('.nii.gz'):
            nombre_base = os.path.splitext(os.path.splitext(archivo)[0])[0].replace('_0000', '')
            nombre_original = nombres_originales.get(nombre_base)
            if not nombre_original:
                print(f"⚠️ No se encontró nombre original para: {nombre_base}")
                continue
            nombre_original_base = os.path.splitext(os.path.splitext(nombre_original)[0])[0]
            info = espaciados_originales.get(nombre_original_base)
            if not info:
                print(f"⚠️ No se encontró info original para: {nombre_original_base}")
                continue

            ruta_archivo = os.path.join(ruta_segmentaciones, archivo)
            imagen = sitk.ReadImage(ruta_archivo)
            imagen.SetSpacing(info["spacing"])
            imagen.SetOrigin(info["origin"])
            imagen.SetDirection(info["direction"])
            sitk.WriteImage(imagen, ruta_archivo)



def renombrar_segmentaciones(ruta_segmentaciones, nombres_originales, carpeta_final):
    os.makedirs(carpeta_final, exist_ok=True)
    for archivo in os.listdir(ruta_segmentaciones):
        if archivo.endswith(".nii") or archivo.endswith(".nii.gz"):
            nombre_base = os.path.splitext(os.path.splitext(archivo)[0])[0].replace('_0000', '')
            nombre_original = nombres_originales.get(nombre_base)
            if nombre_original:
                nuevo_nombre = os.path.splitext(os.path.splitext(nombre_original)[0])[0] 
                ruta_origen = os.path.join(ruta_segmentaciones, archivo)
                ruta_destino_nrrd = os.path.join(carpeta_final, f"{nuevo_nombre}.nrrd")
                imagen = sitk.ReadImage(ruta_origen)
                sitk.WriteImage(imagen, ruta_destino_nrrd)
                os.remove(ruta_origen)

def renombrar_segmentaciones(ruta_segmentaciones, nombres_originales, carpeta_final):
    os.makedirs(carpeta_final, exist_ok=True)
    for archivo in os.listdir(ruta_segmentaciones):
        if archivo.endswith(".nii") or archivo.endswith(".nii.gz"):
            nombre_base = os.path.splitext(os.path.splitext(archivo)[0])[0].replace('_0000', '')
            nombre_original = nombres_originales.get(nombre_base)
            if nombre_original:
                nuevo_nombre = os.path.splitext(os.path.splitext(nombre_original)[0])[0]  
                ruta_origen = os.path.join(ruta_segmentaciones, archivo)
                ruta_destino_nrrd = os.path.join(carpeta_final, f"{nuevo_nombre}.nrrd")
                imagen = sitk.ReadImage(ruta_origen)
                sitk.WriteImage(imagen, ruta_destino_nrrd)
                os.remove(ruta_origen)
            


def correr_inferencia(input_path, output_folder, carpeta_segmentaciones_finales, ejecutar_normalizacion=False, nuevo_espaciado=[1.0, 1.0, 1.0]):
    if os.path.isfile(input_path):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_input = os.path.join(temp_dir, "archivo_input")
            os.makedirs(temp_input, exist_ok=True)
            ruta_copia = os.path.join(temp_input, os.path.basename(input_path))
            shutil.copy(input_path, ruta_copia)
            correr_inferencia(temp_input, output_folder, carpeta_segmentaciones_finales, ejecutar_normalizacion, nuevo_espaciado)
        return

    espaciados_originales = obtener_espaciados_originales(input_path)

    ruta_preprocesada = input_path
    nombres_originales = {}
    if ejecutar_normalizacion:
        ruta_preprocesada = os.path.join(output_folder, "preprocesado")
        os.makedirs(ruta_preprocesada, exist_ok=True)
        nombres_originales = NormalizacionyEspaciado(input_path, ruta_preprocesada, nuevo_espaciado)

    comando = [
        "nnUNetv2_predict",
        "-d", "Dataset506_APCIVMP",
        "-i", ruta_preprocesada,
        "-o", output_folder,
        "-f", "0", "1", "2", "3", "4",
        "-tr", "nnUNetTrainer_100epochs",
        "-c", "3d_lowres",
        "-p", "nnUNetPlans"
    ]

   
    subprocess.run(comando, check=True)
    display(HTML("<h1 style='color: green;'>🤖 Ejecución: Completada</h1>"))
    RestaurarEspaciadoSalida(output_folder, espaciados_originales, nombres_originales)

    if ejecutar_normalizacion:
        renombrar_segmentaciones(output_folder, nombres_originales, carpeta_segmentaciones_finales)
        for archivo in os.listdir(output_folder):
            if archivo.startswith("paciente_"):
                os.remove(os.path.join(output_folder, archivo))
