# Beginner-Friendly YOLO12 Training and Testing Script

# Step 0: Install ultralytics if not already installed
 
from ultralytics import YOLO
import yaml


# -------------------------------
# PART 1: Create data.yaml file
# -------------------------------

# IMPORTANT: Change these paths to match your dataset location
train_path = "your/dataset/path/images/train/"
val_path = "your/dataset/path/images/val/"

# Define your classes
classes = ["Fall Detected", "Walking", "Sitting"]

# Build the YAML dictionary
data_yaml = {
    "train": train_path,
    "val": val_path,
    "nc": len(classes),   # number of classes
    "names": classes      # list of class names
}

# Save to data.yaml
with open("data.yaml", "w") as f:
    yaml.dump(data_yaml, f)

print("data.yaml created successfully!")
print(yaml.dump(data_yaml))

# -------------------------------
# PART 2: Train the YOLO model
# -------------------------------

# Load a pre-trained YOLO12 model 
model = YOLO('yolo12n.pt')  

# Train the model on your custom dataset
results = model.train(
    data="data.yaml",         # path to dataset YAML
    epochs=100,               # number of training epochs
    imgsz=640,                # image size for training
    batch=16,                 # batch size
    name='yolo12n_model',     # name of this training run
    verbose=True,             # print detailed training info
    patience=0,               # stop early if no improvement (0 = disabled)
    lr0=0.001                 # initial learning rate
)

# After training, the best weights are saved in:
# runs/train/yolo12n_model/weights/best.pt

# -------------------------------
# PART 3: Test the model on a video or Image
# -------------------------------

# Load your trained model
model = YOLO("runs/train/yolo12n_model/weights/best.pt")

# Choose either a video or image
video_path = "path/to/your/test_video.mp4"     # CHANGE THIS PATH
image_path = "path/to/your/test_image.jpg"     # CHANGE THIS PATH

# Example: use video
source_path = video_path   # or switch to image_path if you want

# Make predictions and save output
result = model.predict(
    source=source_path,  # path to input video or image
    save=True,           # save output with predictions
    conf=0.6             # confidence threshold
)

# Check type and print message
if source_path.endswith((".jpg", ".png", ".jpeg")):
    print("Image processed. Predictions saved in the 'runs/predict' folder.")
else:
    print("Video processed. Predictions saved in the 'runs/predict' folder.")




