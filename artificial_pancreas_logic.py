# Simplified Artificial Pancreas Logic
def get_insulin_dose(glucose, target=100):
    # Logic: If glucose > target, deliver dose (Sensitivity = 0.05)
    error = glucose - target
    return round(error * 0.05, 2) if error > 0 else 0.0

# Example Readings
for g in [165, 95]:
    print(f"Glucose: {g} mg/dL | Dose: {get_insulin_dose(g)} units")
  
