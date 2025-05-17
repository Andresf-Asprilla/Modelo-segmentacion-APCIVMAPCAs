
# Interfaz de Inferencias 

Este proyecto ofrece una interfaz interactiva para la inferencia de imágenes médicas 3D, empleando modelos de segmentación profunda entrenados con **MONAI Label** y **nnU-Net**, cuyos resultados pueden visualizarse en plataformas como **3D Slicer** o **3D Viewer**.

Diseñada para ejecutarse directamente en **Google Colab**, esta herramienta aprovecha recursos en la nube para ofrecer una experiencia accesible, sin necesidad de instalaciones locales complejas. 

---

## Funcionalidades principales

- **Instalación automática de dependencias**  
  (incluyendo `MONAI`, `MONAI Label`, `nnU-Net`, `ITK`, `PyVista`, `SimpleITK`, `ngrok`, entre otros).

- **Carga automática de modelos**  
  Carga automática de modelos desde Google Drive.

- **Inferencia sobre imágenes médicas 3D**  
  En formatos estándar como `.nii.gz`.

- **Exportación y descarga de resultados**  
  - Para **3D Slicer**: en formatos `.nrrd`, `.nii.gz`, `.obj`, etc.  
  - Para **3D Viewer/Web**: exportación en `.obj + .mtl`.

- **Video tutoriales incorporados**  
  Para una curva de aprendizaje más amigable.

- **Compatibilidad con ngrok**  
  Para exponer servidores locales y facilitar la conexión desde Slicer u otros clientes.

---

## Videos Tutoriales

| Uso general de la interfaz | Actualizaciones recientes |
|----------------------------|----------------------------|
| [![Tutorial](https://img.youtube.com/vi/B1_pAmnVFD4/0.jpg)](https://www.youtube.com/watch?v=B1_pAmnVFD4) | [![Actualización](https://img.youtube.com/vi/CCmLW8bEQ2U/0.jpg)](https://www.youtube.com/watch?v=CCmLW8bEQ2U) |

>Esta interfaz fue desarrollada con el apoyo del **Hospital Internacional de Colombia** y la **Clínica Cardio VID** para el análisis y visualización de patologías cardíacas complejas.

---

## Cómo ejecutar en Google Colab

1. Haz clic en este enlace para abrir la interfaz:  
[Abrir en Colab](https://github.com/Andresf-Asprilla/Modelo-segmentacion-APCIVMAPCAs/blob/main/Interfaz/Interfaz_Inferencias.ipynb)

2. Realiza una copia en goolge drive `Interfaz_Inferencias.ipynb`.

3. Sigue las instrucciones del tutorial  para iniciar  servidor MONAI Label, cargar imágenes y ejecutar inferencias.

4. Al finalizar, podrás:
   - Visualizar las segmentaciones directamente en 3D Slicer.
   - Exportar los resultados como archivos `.obj`, `.nrrd` o `.nii.gz`.
   - Usar herramientas de visualización web como 3D Viewer.

---

## Requisitos

- Navegador web con acceso a Google Colab.
- Opcional cuenta gratuita de  [Ngrok](https://ngrok.com/) (para exponer servidores locales).
- **3D Slicer** instalado (opcional, para visualización avanzada).
- Imágenes médicas 3D compatibles (`.nii.gz`).

---

## Casos de uso

- segmentación cardíaca.
- Pruebas de modelos clínicos en desarrollo sin instalar entornos complejos.
- Exportación rápida de modelos 3D para impresión, realidad aumentada o análisis morfológico.
- Entrenamiento médico en interpretación anatómica basada en IA.

---

## Agradecimientos

- **MONAI Team**  
  A. Diaz-Pinto, S. Alle, A. Ihsani, M. Asad, V. Nath, F. Pérez-García, P. Mehta, W. Li, H. R. Roth, T. Vercauteren, D. Xu, P. Dogra, S. Ourselin, A. Feng, M. J. Cardoso  
  *MONAI Label: A framework for AI-assisted Interactive Labeling of 3D Medical Images*, arXiv, 2022.  
  [https://arxiv.org/pdf/2203.12362.pdf](https://arxiv.org/pdf/2203.12362.pdf)

- **D. Oviedo Barreto**  
  *CardioAR3D: Tomografía cardiaca 3D mejorada con realidad aumentada*, Universidad de Antioquia, 2024.  
  [https://hdl.handle.net/10495/43745](https://hdl.handle.net/10495/43745)

---
