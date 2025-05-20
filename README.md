# Modelo Semiautomático para la Visualización 3D de MAPCAs y CIV en Pacientes Pediátricos con Atresia Pulmonar

Este proyecto implementa un sistema de segmentación médica semiautomático para la reconstrucción 3D de estructuras cardíacas (MAPCAs y CIV) en pacientes pediátricos con Atresia Pulmonar. Se utilizaron dos frameworks principales de segmentación médica: [MONAI Label](https://github.com/Project-MONAI/MONAILabel/tree/main), una plataforma interactiva basada en PyTorch diseñada para acelerar el entrenamiento y despliegue de modelos en entornos clínicos, y [nnU-Net](https://github.com/MIC-DKFZ/nnUNet), un marco autoajustable que configura automáticamente su arquitectura y parámetros según las características del conjunto de datos. Además, se desarrolló una interfaz de inferencia accesible vía Google Colab, orientada a personal médico asistencial.

---

### Tabla de Contenido
- [Motivación](#motivación)
- [Objetivo general](#objetivo-general)
- [Objetivos específicos](#objetivos-específicos)
- [Metodología](#metodología)
- [Requisitos](#requisitos)
- [Resultados](#resultados)
- [Puntos destacados](#puntos-destacados)
- [Acceso al Documento Oficial](#acceso-al-documento-oficial)
- [Referencias](#Referencias)

---

## Motivación

La complejidad de la AP-CIV y la variabilidad de las MAPCAs dificultan su diagnóstico y planificación quirúrgica. Esta herramienta busca reducir esas barreras mediante inteligencia artificial aplicada a imágenes de tomografía computarizada, generando modelos 3D que favorecen el entendimiento anatómico y la toma de decisiones clínicas.

---

## Objetivo general

Desarrollar un modelo semiautomático para la visualización tridimensional de las arterias colaterales aortopulmonares mayores y de la comunicación interventricular en pacientes pediátricos con atresia pulmonar.

---

## Objetivos específicos

- Establecer un banco de imágenes de tomografía computarizada cardíaca en pacientes pediátricos con atresia pulmonar y tetralogía de Fallot en estadios avanzados que presenten MAPCAs y CIV.
- Entrenar y validar un modelo para la segmentación semiautomática de imágenes de tomografía computarizada cardíaca.
- Desarrollar una interfaz que permita la ejecución de inferencias a partir de modelos previamente entrenados.

---

## Metodología

A continuación, se presenta el diagrama de flujo metodológico adoptado en este proyecto, organizado en múltiples etapas. Cada una de estas etapas comprende procesos específicos.

![flujo de trabajo](https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/digrama.png)

1. Conformación y anonimización del banco de imágenes.  
2. Entrenamiento de modelos de segmentación con MONAI y nnU-Net.  
3. Validación cruzada, ajuste de hiperparámetros y métricas.  
4. Desarrollo de la interfaz de inferencias en Google Colab.  
5. Evaluación de usabilidad con personal médico especializado.

---

## Requisitos

- Cuenta de Google con acceso a Google Colab  
- GPU disponible  
- [3D Slicer](https://www.slicer.org/) y/o visor WebGL compatible (.obj/.mtl)  
- Dataset de imágenes médicas en formato `.nii.gz` o `.dcm`

---

## Resultados

A continuación, se presentan ejemplos de segmentación y reconstrucción 3D generadas por el sistema:

<table>
  <tr>
    <td align="center"><strong>Prueba</strong><br><img src="https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/video_1.mp4.gif" width="400"/></td>
    <td align="center"><strong>AP-CIV y MAPCAs</strong><br><img src="https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/video_2.mp4.gif" width="400"/></td>
    <td align="center"><strong>Control</strong><br><img src="https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/images/video_3.mp4.gif" width="400"/></td>
  </tr>
</table>

- La inferencia de prueba corresponde a una imagen que no fue utilizada ni en el entrenamiento ni en la validación del modelo.  
- La inferencia AP-CIV y MAPCAs se refiere a una imagen representativa del caso clínico abordado en este proyecto.  
- La inferencia de control pertenece a un paciente sin anomalías estructurales, usada como referencia para validación.

---

## Puntos destacados

- El modelo entrenado es adecuado para la segmentación de estructuras cardíacas complejas en casos de AP-CIV y MAPCAs.  
- La interfaz permite ejecutar inferencias sin conocimientos técnicos, útil en entornos con recursos limitados.  
- Se recomienda expandir el banco de imágenes y estandarizar la adquisición para mejorar la generalización.  
- Su estructura modular facilita la adaptación a nuevas patologías con mínima modificación.  
- El sistema es ligero y puede integrarse fácilmente a flujos hospitalarios en la nube o local.

---

## Acceso al Documento Oficial

El documento formal completo que detalla el desarrollo de este proyecto de práctica académica —incluyendo el marco teórico, la metodología, los resultados y las conclusiones— está disponible públicamente en el repositorio institucional de la Universidad de Antioquia. Puedes acceder a él haciendo [clic aquí](https://bibliotecadigital.udea.edu.co/communities/aba95e15-009e-4b9a-a2b0-c8b390d5ad1f).

---

### Palabras clave
Cardiopatías congénitas, atresia pulmonar, reconstrucción 3D, segmentación de imágenes médicas, aprendizaje profundo, cardiología pediátrica.

---

## Referencias

**nnU-Net**  
> F. Isensee, P. F. Jaeger, S. A. A. Kohl, J. Petersen, K. H. Maier-Hein.  
> *"nnU-Net: A self-configuring method for deep learning-based biomedical image segmentation"*, Nature Methods, 18(2), 203–211, 2021.                
> DOI:[https://doi.org/10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z)

**MONAI Label**  
> A. Diaz-Pinto et al.  
> *"MONAI Label: A framework for AI-assisted interactive labeling of 3D medical images"*, Medical Image Analysis, vol. 95, p. 103207, Jul. 2024.  
> DOI: [https://arxiv.org/pdf/2203.12362.pdf](https://arxiv.org/pdf/2203.12362.pdf)

o utilice el BibTeX a continuación:  
```bibtex
@article{DiazPinto2022monailabel,
  author = {Diaz-Pinto, Andres and others},
  title = {{MONAI Label: A framework for AI-assisted Interactive Labeling of 3D Medical Images}},
  journal = {arXiv e-prints},
  year = 2022,
  url  = {https://arxiv.org/pdf/2203.12362.pdf}
}

```
Adicionalmente, se implementa el modelo de coartación aórtica (CoA) desarrollado en el proyecto  [CardioAR3D](https://github.com/doviedob/CardioAR3D)

>D. Oviedo Barreto, "CardioAR3D: Tomografía cardiaca 3D mejorada con realidad aumentada", Trabajo de grado profesional, Bioingeniería, Universidad de Antioquia, Medellín, Antioquia, Colombia, 2024.


o utilice el BibTeX a continuación:
```bibtex
@mastersthesis{OviedoBarreto2024,
  title = {CardioAR3D: Tomografía cardiaca 3D mejorada con realidad aumentada},
  author = {Oviedo Barreto, D.},
  school = {Universidad de Antioquia},
  address = {Medellín, Antioquia, Colombia},
  year = {2024},
  degree = {Trabajo de grado profesional},
  department = {Bioingeniería}
}
```
### Cite
Por favor  cite de la siguiente forma cuando use directamente este proyecto :

>A. Asprilla Mosquera, "Modelo semiautomático para la visualización 3D de MAPCAs y CIV en pacientes pediátricos con atresia pulmonar", Trabajo de grado, Universidad de Antioquia, 2025.


o utilice el BibTeX a continuación:

```bibtex
@thesis{asprilla2025visualizacion3D,
  title = {Modelo semiautomático para la visualización 3D de Arterias Colaterales Aortopulmonares Mayores y Comunicación Interventricular en pacientes pediátricos con Atresia Pulmonar},
  author = {Asprilla Mosquera, A.},
  year = {2025},
  address = {Medellín, Antioquia, Colombia},
  school = {Universidad de Antioquia},
  degree = {Trabajo de grado profesional},
  department = {Bioingeniería},
}
```
