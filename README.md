**# Automatización de Formulario de Texto con Selenium

Este proyecto automatiza el llenado y envío de un formulario de texto en el sitio web de demostración [DemoQA](https://demoqa.com/text-box) utilizando Selenium WebDriver. El formulario incluye campos como el nombre, correo electrónico, dirección actual y dirección permanente. Posteriormente, se verifica que los datos enviados se reflejen correctamente.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- **Python 3.x**
- **Selenium**: Librería para interactuar con el navegador.
- **WebDriver** para el navegador de tu elección (por ejemplo, ChromeDriver para Google Chrome).

### Instalación

1. **Instalar Python 3.x**: Puedes descargarlo desde su [página oficial](https://www.python.org/downloads/).
2. **Configurar el entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En sistemas Unix/Linux/MacOS
   venv\Scripts\activate  # En sistemas Windows
**

## Instalar dependencias:
pip install -r requirements.txt

## Ejecucion 
behave tests/features/test_textbox.feature

