import os
import cv2
import pandas as pd
import time
import json
import argparse
from pdf2image import convert_from_path
import numpy as np



from modules import YOLO_Det
import easyocr
from extract_feature import resume_extract

import warnings
warnings.filterwarnings("ignore")

def pdf2image(pdf_path):
    pages = convert_from_path(pdf_path)
    # merge all pages into one image
    image = np.vstack([np.asarray(page) for page in pages])
    return image

def docx2image(docx_path):
    pass

# main
def main(args):
    # Load image
    if args.input_path.endswith(('.png', '.jpg', '.jpeg')):
        image = cv2.imread(args.input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif args.input_path.endswith('.pdf'):
        image = pdf2image(args.input_path)
    elif args.input_path.endswith('.docx', '.doc'):
        image = docx2image(args.input_path)
    else:
        raise ValueError("Invalid input path")

    # Detect text
    yolo_det_weight = args.yolo_det_weight
    det_model = YOLO_Det(weight_path=yolo_det_weight)
    boxes_list, label_list= det_model(image, output_path=args.output_path, return_result=True)

    # OCR and correct
    texts, labels = [], []
    reader = easyocr.Reader(['vi'])
    for i, box in enumerate(boxes_list):
        cropped_img = image[int(box[1]):int(box[3]), int(box[0]):int(box[2]), :]
        if label_list[i] == 'Avatar':
            avatar_path = args.output_path.replace('results.json', 'avatar.png')
            avatar = cropped_img.copy()
        else:
            text = '\n'.join([t[1] for t in reader.readtext(cropped_img)])
            texts.append(text)
            labels.append(label_list[i])

    result = resume_extract(avatar_path, texts, labels)
    # save result
    if not os.path.exists('./results'):
        os.mkdir('./results')

    cv2.imwrite(avatar_path, cropped_img)

    with open(args.output_path, 'w') as f:
        json.dump(result, f, ensure_ascii=False) 
    return result

if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='./dataset/u_cv_1681868842.png', help='Path to image')
    parser.add_argument('--output_path', type=str, default='./results/results.json', help='Path to output')
    parser.add_argument('--yolo_det_weight', type=str, default='./weights/yolov8n_50ep.pt', help='Path to YOLO weight')

    args = parser.parse_args()
    main(args)