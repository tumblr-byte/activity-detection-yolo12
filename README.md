# Human Activity Detection using YOLO12

This project demonstrates **human activity detection** using a YOLO model.  
It can detect the following activities in **images and videos**:

- **Fall Detected** – Detects when a person has fallen.  
- **Walking** – Detects when a person is walking or standing.  
- **Sitting** – Detects when a person is sitting.  

The model used in this project is the pretrained file: `yolo12n.pt`.

---

# **Dataset Structure**

The dataset used is fall_dataset, organized as follows:

<img width="359" height="230" alt="Image" src="https://github.com/user-attachments/assets/66f5511a-49a6-48e7-8f5e-d406b2efdd25" />




# **How it Works**

- **Predicts bounding boxes** around detected people.  
- **Labels each person’s activity** as *Fall Detected*, *Walking*, or *Sitting*.  
- **Works for both images and videos**.  


# **Tips for Beginners**

- **Ensure correct paths** in `data.yaml`.  
- **Start with fewer epochs** to quickly test the setup.  
- **Use a smaller batch size** if GPU memory is limited.  
- **Check the `runs/train/` folder** to see training results and saved weights.  





# **Installation**

### 1. Clone the repository
```bash
git clone https://github.com/username/activity-detection-yolo12.git
cd activity-detection-yolo12


---


# **2. Install dependencies**
pip install -r requirements.txt





# **Usage**

Run the following commands to test the model:

- **Run on an image**
  ```bash
  python main.py --source path/to/image.jpg


- **Run on Video**
python main.py --source path/to/video.mp4


# **Contact**

If you find any issues, mistakes, or have questions, feel free to reach out by opening an issue in this repository.
I’d be happy to help!
