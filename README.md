# Human Activity Detection using YOLO12

This project demonstrates **human activity detection** using a YOLO12 model. It can detect the following activities in **images and videos**:

- **Fall Detected** - Detects when a person has fallen
- **Walking** - Detects when a person is walking or standing
- **Sitting** - Detects when a person is sitting

The model used in this project is the pretrained file: `yolo12n.pt`.

https://github.com/user-attachments/assets/65cc490a-d571-4640-98f4-0d81878fad6e

## Dataset Structure

The dataset used is fall_dataset, organized as follows:

<img width="359" height="230" alt="Dataset Structure" src="https://github.com/user-attachments/assets/66f5511a-49a6-48e7-8f5e-d406b2efdd25" />

## How it Works

- **Predicts bounding boxes** around detected people
- **Labels each person's activity** as Fall Detected, Walking, or Sitting
- **Works for both images and videos**

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/tumblr-byte/activity-detection-yolo12.git
cd activity-detection-yolo12
```

### 2. Install dependencies
```bash
pip install -r requirements.txt

```

### 3. Run the script
```bash
python main.py
```

## Usage

The main.py script handles everything automatically:

1. **Update paths in main.py** - Change dataset and test file paths
2. **Run the script** - It will train and test automatically
3. **Check results** - Look in the `runs/` folder for outputs

## Tips for Beginners

- **Update file paths** in `main.py` before running
- **Start with fewer epochs** to quickly test the setup
- **Use a smaller batch size** if GPU memory is limited
- **Check the `runs/train/` folder** to see training results and saved weights

## Live Webcam Detection

Want to use your webcam for real-time detection? Once you're comfortable with images and videos, just ask! I can show you how to modify the script for live webcam detection.

## Contact

If you find any issues, mistakes, or have questions, feel free to reach out by opening an issue in this repository. I'd be happy to help!
