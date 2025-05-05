# AI Event Detection Demo

This is a sample project that demonstrates the structure of a fall, fire/smoke, and violence detection system from video footage using pretrained AI models.

## Key Features

- Upload video files through a simple web interface
- Backend built using Flask (can be upgraded to FastAPI)
- Placeholder logic for detecting:
  - Falls using Pose/YOLOv8
  - Fire/smoke using FireNet
  - Violence using 3D CNN / RWF-2000 data
- Results include timestamp + confidence score
- Manual labeling for refining results

## Technologies Used

- Python
- Flask
- HTML/CSS (basic UI)
- YOLOv8 (planned)
- SQLite (planned)
- Public datasets referenced

## Note

This is a simplified version meant to showcase structure and ability to handle AI projects. Dataset integration and models can be added in production.

## Author

Temmyproo
