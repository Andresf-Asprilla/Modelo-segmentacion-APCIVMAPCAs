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

## Training Loss

![Gráfico del entrenamiento mostrando la pérdida durante 100 épocas.](https://developer.download.nvidia.com/assets/Clara/Images/monai_spleen_ct_segmentation_train.png)

---

## Validation Dice

![Gráfico mostrando el Dice promedio en validación durante 1260 épocas.](https://developer.download.nvidia.com/assets/Clara/Images/monai_spleen_ct_segmentation_val.png)


## MONAI Bundle Commands
In addition to the Pythonic APIs, a few command line interfaces (CLI) are provided to interact with the bundle. The CLI supports flexible use cases, such as overriding configs at runtime and predefining arguments in a file.

For more details usage instructions, visit the [MONAI Bundle Configuration Page](https://docs.monai.io/en/latest/config_syntax.html).

#### Execute training:

```
python -m monai.bundle run --config_file configs/train.json
```

Please note that if the default dataset path is not modified with the actual path in the bundle config files, you can also override it by using `--dataset_dir`:

```
python -m monai.bundle run --config_file configs/train.json --dataset_dir <actual dataset path>
```

#### Override the `train` config to execute multi-GPU training:

```
torchrun --standalone --nnodes=1 --nproc_per_node=2 -m monai.bundle run --config_file "['configs/train.json','configs/multi_gpu_train.json']"
```

Please note that the distributed training-related options depend on the actual running environment; thus, users may need to remove `--standalone`, modify `--nnodes`, or do some other necessary changes according to the machine used. For more details, please refer to [pytorch's official tutorial](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html).

#### Override the `train` config to execute evaluation with the trained model:

```
python -m monai.bundle run --config_file "['configs/train.json','configs/evaluate.json']"
```

#### Override the `train` config and `evaluate` config to execute multi-GPU evaluation:

```
torchrun --standalone --nnodes=1 --nproc_per_node=2 -m monai.bundle run --config_file "['configs/train.json','configs/evaluate.json','configs/multi_gpu_evaluate.json']"
```

#### Execute inference:

```
python -m monai.bundle run --config_file configs/inference.json
```

#### Export checkpoint to TensorRT based models with fp32 or fp16 precision:

```
python -m monai.bundle trt_export --net_id network_def --filepath models/model_trt.ts --ckpt_file models/model.pt --meta_file configs/metadata.json --config_file configs/inference.json --precision <fp32/fp16> --dynamic_batchsize "[1, 4, 8]" --use_onnx "True" --use_trace "True"
```

#### Execute inference with the TensorRT model:

```
python -m monai.bundle run --config_file "['configs/inference.json', 'configs/inference_trt.json']"
```

# References
[1] Xia, Yingda, et al. "3D Semi-Supervised Learning with Uncertainty-Aware Multi-View Co-Training." arXiv preprint arXiv:1811.12506 (2018). https://arxiv.org/abs/1811.12506.

[2] Kerfoot E., Clough J., Oksuz I., Lee J., King A.P., Schnabel J.A. (2019) Left-Ventricle Quantification Using Residual U-Net. In: Pop M. et al. (eds) Statistical Atlases and Computational Models of the Heart. Atrial Segmentation and LV Quantification Challenges. STACOM 2018. Lecture Notes in Computer Science, vol 11395. Springer, Cham. https://doi.org/10.1007/978-3-030-12029-0_40

# License
Copyright (c) MONAI Consortium

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
