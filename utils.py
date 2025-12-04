import os
import pandas as pd
from datetime import datetime

# Creates folder if doesn't exist

def create_folder(path):
os.makedirs(path, exist_ok=True)

# Save violation logs for record

def log_violation(vehicle_type, violation_type):
data = {
"Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
"Vehicle": [vehicle_type],
"Violation": [violation_type]
}


df = pd.DataFrame(data)

if not os.path.exists("violation_logs.csv"):
    df.to_csv("violation_logs.csv", index=False)
else:
    df_existing = pd.read_csv("violation_logs.csv")
    df = pd.concat([df_existing, df], ignore_index=True)
    df.to_csv("violation_logs.csv", index=False)

print(f"[LOGGED] {violation_type} violation recorded.")
```

# Future expansion (plate recognition)

def number_plate_recognition(img):
# placeholder for OCR model integration later
return None
