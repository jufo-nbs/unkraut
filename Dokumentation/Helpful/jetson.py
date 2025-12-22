import cv2
import numpy as np
import pyrealsense2 as rs
from ultralytics import YOLO
import torch
from ultralytics.utils import LOGGER


LOGGER.setLevel("ERROR")

frame_width = 640
frame_height = 480

x_average =[]
y_average =[]


if __name__ == "__main__":

    model = YOLO("yolo11m-seg.pt")

    pipeline = rs.pipeline()
    config = rs.config()

    config.enable_stream(rs.stream.depth, frame_width, frame_height, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, frame_width, frame_height, rs.format.bgr8, 30)

    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()
    print("Device", device)

    # start data stream
    pipeline.start(config)
    polygon_memory = []
    
    # quit when q is pressed
    while cv2.waitKey(1) != ord("q"):
        # get color and depth frame
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        # if not color_frame:
        if not depth_frame or not color_frame:
            continue

        # Farbbild
        img = np.asanyarray(color_frame.get_data())
        depth_img = np.asanyarray(depth_frame.get_data())
        depth_image_8u = cv2.normalize(depth_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        heatmap_img = cv2.applyColorMap(depth_image_8u, cv2.COLORMAP_JET)
        

        cv2.imshow("depth_frame", img)

        # YOLO-Inferenz
        result = model(img, device="cuda", half=True)
        boxes = result[0].boxes
        masks = result[0].masks

        cls = boxes.cls

        is_cls_bottle = cls == 39.  # Klasse 39 = Flasche in COCO

        if is_cls_bottle.any():
            bottle_boxes = boxes[is_cls_bottle]
            max_bottle_idx = torch.argmax(bottle_boxes.conf)
            best_mask = masks[max_bottle_idx]

            #print(best_mask.xy[0].shape)
            depth_frame_mask = np.zeros(depth_img.shape)
            depth_frame_mask[best_mask.xy[0].astype(np.int32)] = heatmap_img[np.flip(best_mask.xy[0].astype(np.int32), axis=1)]
            #print(depth_frame_mask.shape)
            cv2.imshow("maked Tiefenbild", depth_frame_mask)
            cv2.imshow("tiefenbild", heatmap_img)


            best_box = bottle_boxes[max_bottle_idx]
            x, y, w, h = best_box.xywh[0]

            x_pos = x.item()# + (w.item()/2) Das ist scheiße
            y_pos = y.item()# - (h.item()/2)

            average_number = 7



            for i in range(average_number): # Immer 5 bilder averagen
                x_average.append(x_pos)
                y_average.append(y_pos)
                if len(x_average) > average_number:
                    x_average.pop(0)
                    y_average.pop(0)

                cv2.circle(img, ((int(np.mean(x_average)), int(np.mean(y_average)))), 5, (255, 0, 0), 3)

        #img = result[0].plot()
        cv2.imshow("Flaschen-Erkennung", img)
