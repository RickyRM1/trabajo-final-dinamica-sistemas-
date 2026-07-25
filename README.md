# Contaminación ambiental en San Juan de Lurigancho: un enfoque de Dinámica de Sistemas

Trabajo final del curso **Dinámica de Sistemas**.

**Docente:** Mg. Maurice Frayssinet Delgado
**Integrantes:**
- Picón Ayala, Yan Levi
- Vizcardo Zegarra, Roberto Carlos
- Ruiz Meza, Ricardo Antonio
- Mamani Solorzano Sebastian Ernesto


## ¿De qué trata este proyecto?

San Juan de Lurigancho, el distrito más poblado de Lima Metropolitana, presenta niveles de contaminación por material particulado fino (PM2.5) entre los más altos de Sudamérica, superando de forma recurrente el Estándar de Calidad Ambiental (ECA-aire) establecido por el MINAM.

Este proyecto aborda el problema no como un evento aislado, sino como el resultado de la interacción de múltiples variables en el tiempo: el crecimiento del parque vehicular, la capacidad de respuesta regulatoria y la estacionalidad climática de Lima. Usando la metodología de Dinámica de Sistemas, se construye un modelo que permite entender por qué el problema persiste y qué tan efectiva puede ser una intervención antes de implementarla en la realidad.

Todo el análisis se calibra y valida contra **datos reales** de la red de monitoreo del SENAMHI (2020-2022), no contra supuestos hipotéticos.

## ¿Qué encontramos?

- La contaminación responde a tres fuerzas que interactúan constantemente: el crecimiento del parque vehicular (que la empuja hacia arriba), la presión regulatoria (que reacciona con retraso) y la estacionalidad del clima limeño (que la agrava en invierno).
- El sistema se comporta como una **"Tragedia de los comunes"**: ningún actor individual contamina lo suficiente para saturar el aire por sí solo, pero la suma de miles de decisiones individuales sí lo hace.
- La variable con mayor efecto sobre la concentración de PM2.5 es la densidad y tasa de emisión del parque vehicular.
- Proyectando distintos escenarios a 2025, una política de restricción vehicular y renovación de flota reduce el exceso acumulado de contaminación en torno a un 15% frente a no hacer nada, aunque no basta por sí sola para cumplir el estándar ambiental en ese plazo.

## Estructura del repositorio

```
trabajo-final-dinamica-sistemas/
├── README.md
├── informe/
│   └── informe-final.docx             Informe técnico completo (27 secciones, formato APA 7)
├── presentacion/
│   └── (pendiente)                    Presentación final .pptx
├── modelos/
│   ├── diagrama_causal.png            Diagrama causal del sistema (bucles de refuerzo y balance)
│   ├── modelo_stock_flow.png          Diagrama del modelo stock-flujo
│   ├── calibracion_modelo.ipynb       Calibración del modelo contra datos reales y simulación del escenario base
│   ├── escenarios_politica.ipynb      Proyección de escenarios futuros y política de intervención
│   ├── fig_escenarios_comparados.png  Comparación visual de los escenarios proyectados
│   ├── fig_politica_intervencion.png  Efecto de la política de intervención propuesta
│   ├── graficas_parte1/               Gráficas de comportamiento en el tiempo (BOT), datos reales 2020-2022
│   └── graficas_parte2/               Gráficas de calibración, flujos y pruebas de validación del modelo
└── datos/
    ├── pm25_sjl_mensual_2020_2022.csv Dataset agregado a promedio mensual, usado para calibrar el modelo
    └── procesar_datos_senamhi.py      Script de limpieza y agregación del dataset crudo de SENAMHI
```

## Fuente de datos

Dataset real: *Monitoreo de los contaminantes del aire en Lima Metropolitana* (SENAMHI), disponible en la Plataforma Nacional de Datos Abiertos del Estado Peruano (datosabiertos.gob.pe). El archivo crudo no se incluye en este repositorio por su tamaño; el CSV en `datos/` es el resultado ya filtrado para la estación de San Juan de Lurigancho y agregado a promedio mensual.

## Cómo reproducir el análisis

```bash
pip install pandas numpy scipy matplotlib --break-system-packages
python3 datos/procesar_datos_senamhi.py
# luego correr, en orden, modelos/calibracion_modelo.ipynb y modelos/escenarios_politica.ipynb
```
