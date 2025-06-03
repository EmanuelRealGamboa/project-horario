#!/bin/bash

# ===========================
# Configuración inicial
# ===========================

# URL de tu repositorio (ajustado con tu usuario real)
REPO_URL="https://github.com/EmanuelRealGamboa/project-horario.git"
PROJECT_FOLDER="project-horario"

# ===========================
# Clonar el repositorio
# ===========================
echo "🚀 Clonando repositorio..."
git clone $REPO_URL
cd $PROJECT_FOLDER

# ===========================
# Crear entorno virtual
# ===========================
echo "🐍 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual (solo funciona en Linux/Mac)
source venv/bin/activate

# ===========================
# Instalar dependencias
# ===========================
echo "📦 Instalando dependencias de backend..."
pip install --upgrade pip
pip install -r requirements.txt

# ===========================
# Crear rama personal
# ===========================
echo ""
read -p "👤 Ingresa tu nombre para crear tu rama personal (feature/tu-nombre): " nombre

# Nos aseguramos de estar actualizados
git checkout develop
git pull origin develop

# Creamos la rama de trabajo personal
git checkout -b feature/$nombre
git push -u origin feature/$nombre

# ===========================
# Fin del proceso
# ===========================
echo ""
echo "✅ Setup completo."
echo "Estás listo para empezar a trabajar en tu rama feature/$nombre"
