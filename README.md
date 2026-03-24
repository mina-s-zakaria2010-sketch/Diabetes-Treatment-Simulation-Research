[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19210899.svg)](https://doi.org/10.5281/zenodo.19210899)
# 🩺 The Journey of Diabetes Treatment: From Insulin to the Artificial Pancreas
### *A Centennial Analysis (1921–2026) & Computational Simulation*
---

## 📋 Abstract
This repository contains a comprehensive academic research paper exploring the evolution of diabetes care over the last century. It bridges the gap between historical medical milestones and future healthcare technologies, featuring a **Python-based control algorithm** that simulates the logic of modern **Closed-Loop Systems**.

## 🚀 Key Research Pillars
* **Historical Foundation:** The impact of Banting, Best, and Macleod’s discovery (1921) on global health.
* **Technological Shift:** Evolution from the "Biostator" (1970s) to the **MiniMed 780G** and DIY **Loop** communities.
* **Computational Medicine:** Using logic-based algorithms to automate insulin delivery and reduce human error.
* **Socio-Economic Gaps:** Analysis of insulin affordability and the barriers to advanced diabetes technology.

## 💻 Simulation Logic (Appendix)
The included script, `artificial_pancreas_logic.py`, demonstrates the fundamental mathematical model of an **Automated Insulin Delivery (AID)** system.

### **Algorithm Mechanics:**
* **Input:** Continuous Glucose Monitor (CGM) readings ($mg/dL$).
* **Process:** Calculates the deviation from the **Target Glucose** (Set at $100$ $mg/dL$).
* **Output:** Determines the precise insulin dose using a predefined **Sensitivity Factor** ($0.05$).

```python
# Simplified Artificial Pancreas Logic
def get_insulin_dose(glucose, target=100):
    # Logic: If glucose > target, deliver dose (Sensitivity = 0.05)
    error = glucose - target
    return round(error * 0.05, 2) if error > 0 else 0.0

# Example Readings
for g in [165, 95]:
    print(f"Glucose: {g} mg/dL | Dose: {get_insulin_dose(g)} units")
