
# 📘 Interfaz de Inferencias 3D con MONAI Label y Modelos Personalizados

## 🧠 Descripción

Esta interfaz ha sido desarrollada para facilitar la implementación, visualización y exportación de modelos de segmentación médica 3D, utilizando como base la librería [MONAI Label](https://monai.io/label/) y modelos entrenados para el corazón y estructuras vasculares.  

La herramienta fue diseñada en Google Colab para aprovechar recursos en la nube y permitir una experiencia interactiva, sin necesidad de instalaciones locales complejas.

---

## 🚀 Funcionalidades principales

- 🔧 Instalación automática de dependencias (MONAI, MONAI Label, ITK, PyVista, etc.)
- 💾 Carga automática de modelos desde Google Drive o repositorios
- 🧠 Inferencia sobre imágenes médicas 3D
- 🔍 Visualización interactiva en 3D (con exportación `.obj`)
- 📤 Descarga de resultados segmentados como archivos `.obj` y `.mtl`
- 🎞️ Video tutorial incorporado para el uso de la interfaz

---

## 📼 Tutoriales en Video

| Tutorial de uso | Actualización de la interfaz |
|-----------------|------------------------------|
| [![Tutorial](https://img.youtube.com/vi/B1_pAmnVFD4/0.jpg)](https://www.youtube.com/watch?v=B1_pAmnVFD4) | [![Actualización](https://img.youtube.com/vi/CCmLW8bEQ2U/0.jpg)](https://www.youtube.com/watch?v=CCmLW8bEQ2U) |

> **📢 Nota:** Esta interfaz fue desarrollada con el apoyo del **Hospital Internacional de Colombia** y la **Clínica Cardio VID**.

---

## 🏥 Agradecimientos

<div align="center">
  <img src="https://www.foscal.com.co/wp-content/uploads/2021/02/hic-logo-1.png" alt="Hospital Internacional de Colombia" width="180">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://cardiovid.org/wp-content/uploads/2020/08/logo-cardiovid.png" alt="Clínica Cardio VID" width="180">
</div>

---

## 📂 Estructura de Archivos Exportados

- `*.obj`: Modelo 3D de la segmentación
- `*.mtl`: Asignación de colores por segmento (visualización avanzada)
- Compatible con:
  - ✅ 3D Slicer (`.obj`)
  - ✅ 3DViewer Web (`.obj` + `.mtl`)

---

## 📚 Trabajos que hicieron posible esta herramienta

- A. Diaz-Pinto, S. Alle, A. Ihsani, M. Asad, V. Nath, F. Pérez-García, P. Mehta, W. Li, H. R. Roth, T. Vercauteren, D. Xu, P. Dogra, S. Ourselin, A. Feng, M. J. Cardoso.  
  📄 *MONAI Label: A framework for AI-assisted Interactive Labeling of 3D Medical Images*, arXiv, 2022.  
  [https://arxiv.org/pdf/2203.12362.pdf](https://arxiv.org/pdf/2203.12362.pdf)

- D. Oviedo Barreto  
  📄 *CardioAR3D: Tomografía cardiaca 3D mejorada con realidad aumentada*  
  Universidad de Antioquia, 2024.

- A. Asprilla Mosquera  
  📄 *Modelo semiautomático para la visualización 3D de MAPCAs y CIV en pacientes pediátricos con atresia pulmonar*  
  Universidad de Antioquia, 2025.

---

## 🧪 Cómo ejecutar en Google Colab

1. Ve a [Google Colab](https://colab.research.google.com/)
2. Abre el archivo `Interfaz_Inferencias.ipynb`
3. Ejecuta las celdas una a una, siguiendo los mensajes en pantalla
4. Al finalizar, podrás descargar los modelos 3D y abrirlos en herramientas como **3D Slicer** o **3DViewer**

---

## 📬 Contacto

Para más información, sugerencias o colaboración, puedes escribir a:

- ✉️ `nombre@dominio.com`
- 🏫 Universidad de Antioquia
