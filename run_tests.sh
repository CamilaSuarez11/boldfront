#!/bin/bash

# Asegúrate de que el entorno virtual esté activado si usas uno
# source venv/bin/activate  # Si usas un entorno virtual (opcional)

# Asegúrate de que todas las dependencias estén instaladas
pip install -r requirements.txt

# Ejecutar las pruebas con Behave
behave tests/features/test_textbox.feature

# Devolverte un código de estado para CI/CD
if [ $? -eq 0 ]; then
    echo "Todas las pruebas pasaron correctamente!"
    exit 0
else
    echo "Algunas pruebas fallaron."
    exit 1
fi
