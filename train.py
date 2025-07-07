import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO(r'D:\ssj\ultralytics-main(dhd2)\ultralytics\cfg\models\v8\yolov8-sed.yaml')
    # model.load('yolov8n.pt') # loadin.g pretrain weights
    model.train(data=r'D:\ssj\ultralytics-main(dhd2)\ultralytics\cfg\datasets\coco.yaml',
                task='detect',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16,
                close_mosaic=0,
                workers=4, # Windows下出现莫名其妙卡主的情况可以尝试把workers设置为0
                device='0',
                optimizer='SGD', # using SGD

                project='runs/dataset12',
                name='yolov10',
                )