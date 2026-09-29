# sprint-7-project

# Cuadro de Mando de Análisis de Vehículos (Streamlit App)

¡Bienvenido al repositorio del proyecto! Esta aplicación web interactiva proporciona herramientas de análisis exploratorio de datos (EDA) para un conjunto de datos sobre anuncios de venta de vehículos en EE. UU.

## Aplicación Desplegada en Render

Puedes acceder a la versión en vivo y probar la aplicación directamente en el siguiente enlace:
**[Ver aplicación en Render](https://sprint-7-project-u2df.onrender.com/)**

---

## Descripción del Proyecto

Esta es una pequeña aplicación web que crea 2 gráficos: un histograma para la distribución del Odómetro y un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches. Mismos que el usuario puede activar con el uso de casillas de verificación para analizar variables del mercado automotriz (como el odómetro, precio, tipo de vehículo y condición). 

### Tecnologías utilizadas:
* **Python**: Lenguaje principal de desarrollo.
* **Streamlit**: Framework utilizado para construir la interfaz web interactiva.
* **Pandas**: Para la manipulación, limpieza y análisis de los datos del dataset.
* **Plotly**: Para la creación de gráficos e histogramas interactivos y dinámicos.

---

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

* `app.py`: Archivo principal de la aplicación que contiene el código de Streamlit y la lógica de los gráficos.
* `vehicles_us.csv`: El conjunto de datos (dataset) con la información de los vehículos utilizados en el análisis.
* `requirements.txt`: Archivo que lista todas las dependencias y librerías de Python necesarias para ejecutar el proyecto.
* `.gitignore`: Configuración para evitar que Git rastree archivos innecesarios (como entornos virtuales o configuraciones locales).
* `notebooks/`: Carpeta que contiene los cuadernos de Jupyter (`EDA.ipynb`) utilizados durante la fase de análisis exploratorio inicial y pruebas de código.
* `.vscode/`: Carpeta con configuraciones específicas para el entorno de desarrollo en Visual Studio Code (opcional).

---

## Instrucciones para Ejecución Local

Si deseas clonar este repositorio y ejecutar la aplicación en tu entorno local, sigue estos pasos:

### 1. Requisitos previos
Asegúrate de tener instalado Python (versión 3.x recomendada) en tu sistema.

### 2. Clonar el repositorio
Abre tu terminal y ejecuta el siguiente comando:
```bash
git clone https://github.com
cd TU_REPOSITORIO
```

### 3. Crear y activar un entorno virtual (Recomendado)
* **En Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instalar las dependencias
Instala todas las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación
Inicia el servidor local de Streamlit con el siguiente comando:
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador web predeterminado.
