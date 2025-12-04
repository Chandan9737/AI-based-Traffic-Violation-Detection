# Traffic Violation Detection System 

A deep learning-based traffic violation detection system that identifies **helmet violation, triple riding, and signal jumping** using **YOLOv8 and OpenCV**. The model detects vehicles/people from images or videos and highlights violation cases.

---

##  Tech Stack

* **Python**
* **OpenCV**
* **YOLOv8**
* **NumPy, Pandas**
* **Deep Learning**

---

##  Features

✔ Detect No Helmet violation
✔ Detect Triple Riding
✔ Detect Signal Jumping
✔ Works with video/image input
✔ Saves output result images with bounding boxes
✔ Extendable for number plate / speed detection

---

##  Project Structure

```
traffic-violation-detection/
│── README.md
│── requirements.txt
│── main.py
│── detection.py
│── utils.py
│── yolov8_model/     # add model here later
│── samples/          # input images/videos
│── output/           # results saved here
```

---

##  How to Run

```
pip install -r requirements.txt
python main.py --img samples/helmet.jpg
```

---

## Future Enhancements

* Automatic challan generation
* License plate recognition (OCR)
* Real-time CCTV integration
* Dashboard visualization

---



---
