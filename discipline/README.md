# Fokus - Self-Discipline Boost Module

Este módulo forma parte de la aplicación **Fokus**, un asistente en terminal para ayudarte a mantener el foco y mejorar hábitos personales. El módulo **Self-Discipline Boost** está diseñado para ayudarte a desarrollar autodisciplina mediante una rutina diaria guiada y una progresión semanal.

---

## 🔄 Instalación y configuración inicial

1. Copia el archivo `self_discipline_boost.json` en la carpeta principal de Fokus o dentro de `data/`.
2. Asegúrate de que el script `discipline_module.py` está disponible y correctamente importado en tu archivo principal (`main.py` o similar).

---

## 🚀 Uso básico

Desde la terminal de Fokus, puedes ejecutar:
```bash
fokus discipline
```

Esto mostrará la rutina diaria del módulo, incluyendo:
- Tu propósito personal (WHY)
- Tarea de victoria diaria
- Bloques de enfoque (Pomodoro)
- Límite de distracciones
- Registro y notas del día

Podrás actualizar tu progreso interactívamente.

---

## ⚖️ Integración con Fokus

1. En tu `main.py`, importa la función:
```python
from discipline_module import show_boost_routine
```

2. Añade una opción al menú de comandos:
```python
elif cmd == "discipline":
    show_boost_routine()
```

3. (Opcional) Inclúde la rutina como parte de la rutina diaria general de Fokus.

---

## ⏱️ Progresión semanal (personalizable)

El módulo está diseñado para avanzar semana a semana, aumentando el nivel de compromiso:

- **Semana 1**: Conciencia y estructura
- **Semana 2**: Compromiso y constancia
- **Semana 3**: Recompensas y retos
- **Semana 4**: Autonomía y consistencia

Puedes modificar manualmente el campo `"week"` en el JSON o automatizarlo con una función.

---

## 📂 Estructura del archivo JSON

```json
{
  "enabled": true,
  "week": 1,
  "why": "I want to be more consistent and focused to reach my goals.",
  "victory_task": "Make your bed",
  "focus_blocks": 1,
  "distraction_limit": "Airplane mode during focus block",
  "daily_log": {
    "2025-04-25": {
      "victory_task": false,
      "focus_blocks_completed": 0,
      "distraction_limit_respected": false,
      "notes": ""
    }
  }
}
```

---

## 📆 Sugerencia

Usa este módulo junto con otros de Fokus para construir una rutina diaria personalizada que combine productividad, bienestar y mejora continua.

---

## ✉️ Contribuciones

Este módulo está en desarrollo inicial. Si tienes ideas para mejorarlo, como retos semanales automáticos, integración con calendario o visualizaciones, no dudes en compartirlas.

