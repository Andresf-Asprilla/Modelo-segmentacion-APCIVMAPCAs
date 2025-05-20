# Descripción general del modelo

Este modelo fue desarrollado para la **segmentación tridimensional de estructuras cardiovasculares** en pacientes pediátricos con **atresia pulmonar con comunicación interventricular (AP-CIV)**, a partir de **tomografías computarizadas (CT)**. Forma parte de un proyecto orientado a mejorar la visualización 3D en planificación quirúrgica pediátrica.

---

## Datos

- **Modalidad**: Tomografía Computarizada (CT)
- **Tamaño del conjunto**: 15 volúmenes 3D
  - 12 para entrenamiento
  - 3 para validación
- **Fuente**: Clínica Cardio VID
- **Condición clínica**: Casos pediátricos con AP-CIV y MAPCAs

---

## Configuración de entrenamiento

- **Modelo base**: `3d_lowres`
- **GPU recomendada**: mínimo 16 GB de memoria
- **Tamaño del input**: 96 × 160 × 160 voxeles
- **Optimizador**: SGD
- **Tasa de aprendizaje**: 1e-2
- **Épocas**: 100 (recomendadas)

---

### Entrada

- **Canales**: 1
  - Imagen CT axial normalizada

### Salida

- **Canales de salida**: 4
  - `Label 1`: Lado derecho del corazón
  - `Label 2`: Lado izquierdo del corazón
  - `Label 3`: Arteria Pulmonar
  - `Label 4`: Aorta

---

## Métricas de desempeño por segmento

**Métricas utilizadas**:  
- Dice Similarity Coefficient (DSC)  
- Hausdorff Distance (HD)

| Segmento          | DSC (%) | HD (mm)   |
|-------------------|---------|-----------|
| Lado derecho      | 86.92   | 41.1944   |
| Lado izquierdo    | 89.65   | 32.5892   |
| Arteria Pulmonar  | 79.13   | 31.1398   |
| Aorta             | 88.86   | 23.2813   |

---

## Perdida de entrenamiento

![Gráfico del entrenamiento mostrando la pérdida durante 100 épocas.](https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/loss.png)

---

## Dice validacion

![Gráfico mostrando el Dice promedio en validación durante 100 épocas.](https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/dice.png)


## Comandos de uso 
 Para hacer uso del modelo desarollado sin tener que usar la interfaz solo se debe de instarl las siguientes dependencias como uso del siguiente archivo setup_and_inference_apcivmapcas.py donde se puede realizar inferencias en un solo archivo niifti o mas.

#### Dependencias necesarias:

```bash
pip install -q git+https://github.com/Project-MONAI/MONAI#egg=monai
pip install -q gdown
pip install -q SimpleITK
pip install -q nnunetv2

```

#### Impotyacion y ejecucion  :
La entrada puede ser una imagen específica o una carpeta que contenga varias imágenes. Los resultados se guardarán en la carpeta indicada como destino, y tras el preprocesamiento, las segmentaciones finales se ubicarán en la ruta proporcionada.

Es importante que los datos de entrada estén normalizados y tengan un espaciado definido para que el modelo entrenado funcione correctamente.

```py
from setup_and_inference_apcivmapcas import correr_inferencia

correr_inferencia(
    input_path="/content/drive/MyDrive/baseDatos/imagen.nii.gz",
    output_folder="/content/salidatemporal",
    carpeta_segmentaciones_finales="/content/final",
    ejecutar_normalizacion=True,
    nuevo_espaciado=[1.0, 1.0, 1.0]
)
```
# Referencias 

> F. Isensee, P. F. Jaeger, S. A. A. Kohl, J. Petersen, K. H. Maier-Hein.  
> *"nnU-Net: A self-configuring method for deep learning-based biomedical image segmentation"*, Nature Methods, 18(2), 203–211, 2021.                
> DOI:[https://doi.org/10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z)
