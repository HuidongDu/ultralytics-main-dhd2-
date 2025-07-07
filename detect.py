import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO



if __name__ == '__main__':
    model = YOLO(r'D:\ssj\ultralytics-main(ssj)\runs\dataset9\yolov11\weights\best.pt') # select your model.pt path
    model.predict(source=r'D:\ssj\dataset\images\test4',
                  imgsz=640,
                  project='runs/detect5',
                  name='yolov8',
                  save=True,
                  # conf=0.1,
                  # iou=0.7,
                  # agnostic_nms=True,
                  # visualize=True, # visualize model features maps
                  # line_width=2, # line width of the bounding boxes
                  # show_conf=False, # do not show prediction confidence
                  # show_labels=False, # do not show prediction labels
                  # save_txt=True, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )
