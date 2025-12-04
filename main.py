import cv2
import argparse
from detection import detect_violations

# ---------------------------

# Command to Run

# python main.py --img samples/helmet.jpg

# python main.py --video samples/video.mp4

# ---------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--img", type=str, help="Image file to detect")
parser.add_argument("--video", type=str, help="Video file to detect")
args = parser.parse_args()

if args.img:
detect_violations(source=args.img, mode="image")

elif args.video:
detect_violations(source=args.video, mode="video")

else:
print("\nUsage Examples:")
print("python main.py --img samples/test.jpg")
print("python main.py --video samples/video.mp4")
