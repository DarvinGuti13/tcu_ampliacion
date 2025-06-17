# TCU Ampliación - Módulo de Control de Estudiantes TCU
Este módulo desarrollado en Odoo permite gestionar el control académico de estudiantes que realizan Trabajo Comunal Universitario (TCU). Fue diseñado para cubrir flujos administrativos entre estudiantes y profesores, con trazabilidad de estados y reportería en PDF.

## 🎯 Funcionalidades principales
Registro de estudiantes del TCU
Asignación de profesores responsables
Flujo de cambio de estados:
Solicitado → En Revisión → Aprobado → En Ejecución → Finalizado
Historial automático de cambios de estado (auditoría)
Registro de observaciones académicas por parte de profesores
Generación de constancia del estudiante en formato PDF
Control de acceso basado en roles (Profesor y Estudiante)

## 📝 Requisitos 

Odoo 17 
Python 3.8+
PostgreSQL 13+
pip (gestor de paquetes Python)

## 🚀 Instalación
Copiar o colonar la carpeta tcu_ampliacion dentro de modules/ o addons/ Reiniciar el servidor de Odoo "python odoo-bin -r user_db -w password_db --addons-path=addons -d name_db" ingresar a "localhost:8069" Activar el modo desarrollador Ir al menú Apps → Actualizar lista de aplicaciones Buscar TCU Ampliación e instalar

👤 Autor Darvin Gutiérrez Altamirano
