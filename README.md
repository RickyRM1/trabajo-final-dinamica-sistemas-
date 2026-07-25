# Trabajo Final — Dinámica de Sistemas
## Contaminación por PM2.5 en San Juan de Lurigancho

**Curso:** Dinámica de Sistemas — Mg. Maurice Frayssinet Delgado
**Fuente de datos:** SENAMHI / MINAM — "Monitoreo de los contaminantes del aire en Lima Metropolitana", Portal Nacional de Datos Abiertos del Estado Peruano (datosabiertos.gob.pe).

## Descripción del proyecto

Se modela la dinámica de la concentración de PM2.5 (µg/m³) en el distrito de San Juan de Lurigancho, usando datos horarios reales de SENAMHI (2010-2020, ventana de calibración 2020-2022), con un horizonte de simulación de 36 meses y paso mensual. El proyecto identifica los bucles de refuerzo y balance del sistema (R1, B1, B2), construye un modelo stock-flujo calibrado contra la serie real, y evalúa 4 escenarios (base, pesimista, optimista, con intervención) para proponer una política de restricción/renovación del parque vehicular.

## Estructura del repositorio

```
trabajo-final-dinamica-sistemas/
├── README.md
├── informe/
│   └── informe-final.docx              → Informe consolidado, 27 secciones (Partes 1+2+3)
├── presentacion/
│   └── (pendiente) exposicion-final.pptx
├── modelos/
│   ├── diagrama_causal.png             → Diagrama causal con bucles R1/B1/B2 (Parte 1)
│   ├── modelo_stock_flow.png           → Diagrama del modelo stock-flujo (Parte 2)
│   ├── procesar_datos_senamhi.py       → Script de limpieza y agregación mensual del dataset SENAMHI
│   ├── Parte2_Modelo_Simulacion_PM25_SJL.ipynb  → Calibración del modelo (k_emis, CD) y validación
│   ├── Parte3_Escenarios_Politica_PM25_SJL.ipynb → Simulación de los 4 escenarios y política de intervención
│   ├── bot_pm25_mensual.png / bot_pm25_estacional.png / bot_pm25_efecto_covid.png → Gráficas BOT (Parte 1)
│   ├── fig1_escenarios_comparados.png / fig2_politica_intervencion.png → Gráficas de escenarios (Parte 3)
│   ├── matriz_validacion_real_vs_simulado.csv → Serie real vs. simulada por año (validación de comportamiento)
│   ├── matriz_sensibilidad.csv         → Análisis de sensibilidad (Parte 2, sección 19)
│   ├── matriz_escenarios_supuestos.csv → Supuestos narrativos de cada escenario (Parte 3, sección 20)
│   └── matriz_escenarios_resultados.csv → Indicadores por escenario: promedio, pico, % meses > ECA, exceso acumulado
└── datos/
    ├── datos_horarios_senamhi_SJL_2010_2020.csv → Dataset de SENAMHI, ya filtrado solo a la estación San Juan de Lurigancho (crudo, sin agregar)
    ├── diccionario_datos_senamhi.xlsx       → Diccionario de datos oficial de SENAMHI
    ├── metadatos_senamhi.docx               → Metadatos oficiales del dataset
    └── sjl_mensual_2020_2022.csv            → Dataset filtrado (solo SJL) y agregado a promedios mensuales
```

> Nota: el modelo se construyó íntegramente en Python/Jupyter (no en Vensim/Stella/Insight Maker), lo cual está permitido según la guía del curso ("Archivo del modelo en Vensim, Stella, Insight Maker, Python u otra herramienta").

## Parámetros calibrados (fuente de verdad para todo el proyecto)

- `k_emis` (tasa de emisión vehicular) = 0.00473 µg/m³ por vehículo
- `CD` (capacidad de dispersión natural) = 0.01425
- Bondad de ajuste: RMSE = 7.66 µg/m³ · MAE = 6.43 µg/m³ · R² = 0.607 · MAPE = 24.0%

## Consistencia entre partes

- Frontera del sistema, variables, unidades y bucles (R1, B1, B2): definidos en la Parte 1, sin cambios.
- Parámetros calibrados heredados sin modificación de la Parte 2 a la Parte 3.
- Todos los valores numéricos de este repositorio fueron verificados re-ejecutando los notebooks contra los datos reales.

## Pendiente para el cierre final del grupo

1. Agregar la presentación final (`presentacion/exposicion-final.pptx`, 10-15 min).
2. Subir esta carpeta tal cual a un repositorio de GitHub (ver instrucciones abajo).
3. Revisar que `informe-final.docx` tenga carátula y numeración de página continua para las 27 secciones.

## Cómo subir esto a GitHub (sin usar la línea de comandos)

1. Entra a github.com, inicia sesión (o crea una cuenta gratuita).
2. Clic en el botón verde **"New"** (o el **+** arriba a la derecha → "New repository").
3. Nombra el repositorio `trabajo-final-dinamica-sistemas`, márcalo como público o privado, y dale "Create repository" (sin agregar README, para no chocar con el que ya tienes).
4. En la página del repo vacío, clic en **"uploading an existing file"**.
5. Arrastra esta carpeta completa (o cada subcarpeta: `informe/`, `presentacion/`, `modelos/`, `datos/`, más el `README.md` suelto) y confirma el commit.
6. Comparte el link del repositorio con tu grupo y con el profesor.
