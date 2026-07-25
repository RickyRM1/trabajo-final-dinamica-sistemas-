"""
Procesamiento de datos SENAMHI - Calidad del aire San Juan de Lurigancho
Trabajo Final Dinamica de Sistemas - Parte 1, Seccion 10 (Graficas BOT)

Dataset real descargado de datosabiertos.gob.pe (SENAMHI), cobertura 2015-2024.
Ventana de calibracion usada: 2020-2022 (mejor cobertura de datos).
"""

import pandas as pd
import matplotlib.pyplot as plt

RUTA_CSV = "senamhi_raw.csv"

# --------------------------------------------------------------------------
# 1. CARGA
# --------------------------------------------------------------------------
df = pd.read_csv(RUTA_CSV, usecols=["ESTACION", "FECHA", "HORA", "PM10", "PM2_5", "NO2", "DISTRITO"])

# --------------------------------------------------------------------------
# 2. FILTRADO: San Juan de Lurigancho
# --------------------------------------------------------------------------
sjl = df[df["ESTACION"] == "SAN_JUAN_DE_LURIGANCHO"].copy()

# --------------------------------------------------------------------------
# 3. LIMPIEZA DE FECHAS (formato real: aaaammdd en FECHA, hhmmss en HORA)
# --------------------------------------------------------------------------
sjl["FECHA_DT"] = pd.to_datetime(sjl["FECHA"].astype(str), format="%Y%m%d", errors="coerce")
sjl = sjl.dropna(subset=["FECHA_DT"])
sjl["anio"] = sjl["FECHA_DT"].dt.year
sjl["mes"] = sjl["FECHA_DT"].dt.month

# --------------------------------------------------------------------------
# 4. VENTANA DE CALIBRACION: 2020-2022 (mejor cobertura real de datos)
# --------------------------------------------------------------------------
ventana = sjl[(sjl["anio"] >= 2020) & (sjl["anio"] <= 2022)].copy()
ventana["anio_mes"] = ventana["FECHA_DT"].dt.to_period("M").astype(str)

mensual = ventana.groupby("anio_mes").agg(
    pm25_promedio=("PM2_5", "mean"),
    pm10_promedio=("PM10", "mean"),
    no2_promedio=("NO2", "mean"),
    horas_con_dato=("PM2_5", "count"),
).reset_index()

mensual.to_csv("pm25_sjl_mensual_2020_2022.csv", index=False)
print("Archivo guardado: pm25_sjl_mensual_2020_2022.csv")
print(mensual.head(12))

# --------------------------------------------------------------------------
# 5. GRAFICA BOT #1: Concentracion mensual de PM2.5 vs ECA-aire
# --------------------------------------------------------------------------
ECA_PM25_ANUAL = 25  # ug/m3 (verificar valor vigente en el D.S. del MINAM antes de citar en el informe)

plt.figure(figsize=(11, 5))
plt.plot(mensual["anio_mes"], mensual["pm25_promedio"], marker="o", color="darkorange", label="PM2.5 promedio mensual (SJL)")
plt.axhline(y=ECA_PM25_ANUAL, color="red", linestyle="--", label=f"ECA-aire PM2.5 ({ECA_PM25_ANUAL} ug/m3)")
plt.xticks(rotation=60, fontsize=8)
plt.ylabel("Concentracion PM2.5 (ug/m3)")
plt.title("BOT: PM2.5 en San Juan de Lurigancho (2020-2022) - datos reales SENAMHI")
plt.legend()
plt.tight_layout()
plt.savefig("bot_pm25_mensual.png", dpi=150)
plt.close()
print("Grafica guardada: bot_pm25_mensual.png")

# --------------------------------------------------------------------------
# 6. GRAFICA BOT #2: Estacionalidad (promedio por mes del anio, todo el rango)
# --------------------------------------------------------------------------
estacional = ventana.groupby("mes")["PM2_5"].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(estacional["mes"], estacional["PM2_5"], color="steelblue")
plt.xlabel("Mes del anio")
plt.ylabel("PM2.5 promedio (ug/m3)")
plt.title("Estacionalidad de PM2.5 en SJL (invierno vs verano limeno) 2020-2022")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("bot_pm25_estacional.png", dpi=150)
plt.close()
print("Grafica guardada: bot_pm25_estacional.png")

# --------------------------------------------------------------------------
# 7. GRAFICA BOT #3: Efecto COVID - comparacion anual completa 2019-2022
# --------------------------------------------------------------------------
comparacion = sjl[(sjl["anio"] >= 2019) & (sjl["anio"] <= 2022)]
anual = comparacion.groupby("anio")["PM2_5"].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(anual["anio"].astype(str), anual["PM2_5"], color=["gray", "seagreen", "goldenrod", "firebrick"])
plt.ylabel("PM2.5 promedio anual (ug/m3)")
plt.title("PM2.5 anual en SJL: efecto cuarentena COVID-19 y rebote posterior")
plt.tight_layout()
plt.savefig("bot_pm25_efecto_covid.png", dpi=150)
plt.close()
print("Grafica guardada: bot_pm25_efecto_covid.png")

print("\nListo.")
