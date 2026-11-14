from pathlib import Path
from ultralytics import YOLO
from app.services.compliance_service import compliance_service

# Force absolute path pointing directly to backend/app/ai/models/visiondesk_ppe.pt
BASE_DIR = Path(__file__).resolve().parent.parent  # points to backend/app/
MODEL_PATH = BASE_DIR / "ai" / "models" / "visiondesk_ppe.pt"

print(f"Loading YOLO model from: {MODEL_PATH}")
model = YOLO(str(MODEL_PATH))
