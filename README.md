# Predicción del despacho de unidades de emergencia en incidentes viales de la CDMX mediante modelos de Machine Learning

Clasificación Binaria: Incidentes Viales CDMX (C5)
Fuente: Portal de Datos Abiertos de la Ciudad de México — Centro de Comando C5 URL: https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5 Descripción: Registro de incidentes viales desde 2014, actualizado mensualmente. Incluye: folio, fecha/hora de creación y cierre, motivo del incidente, alcaldía, latitud/longitud, código de cierre, clasificación, y origen del incidente.

Variable respuesta (a construir): requirio_despacho — binaria, indica si el incidente generó despacho de unidad de emergencia (código de cierre A = Afirmativo) o no (N, F, D).

Motivación: Modelar la probabilidad de despacho permite estimar la demanda de recursos de emergencia y calcular tarifas de seguros de responsabilidad civil vial. El desbalance de clases es pronunciado y obliga a decisiones metodológicas cuidadosas.

Reto técnico: desbalance de clases, variables temporales, coordenadas geoespaciales, categorías con alta cardinalidad (motivo del incidente).

Modelos evaluados

• Regresión Logística
• Random Forest
• XGBoost
• Soft Voting Ensemble


## Comparación de modelos

| Modelo | Accuracy | Precision | Recall | F1-score | Comentario |
|:----------------------|:--------:|:---------:|:------:|:--------:|:--------------------------------------------|
| **Regresión Logística** | 0.555 | 0.476 | 0.803 | 0.598 | Baseline con alto recall y gran interpretabilidad. |
| **Random Forest** | **0.571** 🥇 | **0.486** 🥇 | 0.768 | 0.596 | Mayor precisión y accuracy, sacrificando recall. |
| **XGBoost** | 0.563 | 0.482 | 0.804 | **0.602** 🥇 | Mejor equilibrio entre precisión y recall. |
| **Soft Voting Ensemble** | 0.561 | 0.480 | **0.805** 🥇 | 0.601 | Mayor recall, objetivo principal del problema. |

> **Nota:** El umbral de clasificación se fijó en **0.30** para priorizar el **recall** de la clase positiva (incidentes que requieren despacho), reduciendo la probabilidad de omitir emergencias reales.
