import os
import cv2 as cv
import numpy as np

global_image_counter = 1


def show_image_wait(image, window_name='Image'):
    global global_image_counter
    window_name += str(global_image_counter)
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    cv.imshow(window_name, image)
    global_image_counter += 1
    cv.waitKey(0)
    cv.destroyAllWindows()


def show_image(image, window_name='Image'):
    global global_image_counter
    window_name += str(global_image_counter)
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    cv.imshow(window_name, image)
    global_image_counter += 1


def validate_mask_json_fields(mask_json):
    for shape in mask_json:
        if "type" not in shape:
            return False
        if "coordinate" not in shape:
            return False
        if shape["type"] == "RECT":
            if len(shape["coordinate"]) != 4:
                return False
        if shape["type"] == "CIRCLE":
            if len(shape["coordinate"]) != 3:
                return False
        if shape["type"] == "POLYGON":
            if len(shape["coordinate"]) < 3:
                return False
    return True


def draw_mask_image(mask_image, mask_json):
    if mask_image is None:
        return mask_image, False
    if not validate_mask_json_fields(mask_json):
        print("Invalid mask json file")
        return mask_image, False
    mask_image = np.asarray(mask_image, np.uint8)
    for shape in mask_json:
        if shape["type"] == "RECT":
            crop_bbox = np.asarray(shape["coordinate"])
            img_h = mask_image.shape[0]
            img_w = mask_image.shape[1]
            x_start = max(0, int(round(crop_bbox[0])))
            y_start = max(0, int(round(crop_bbox[1])))
            x_finish = min(img_w, int(round(crop_bbox[2])))
            y_finish = min(img_h, int(round(crop_bbox[3])))
            mask_image[
            y_start:y_finish,
            x_start:x_finish
            ] = 255
        if shape["type"] == "CIRCLE":
            circle = np.asarray(shape["coordinate"], np.int)
            if circle[2] > 0:
                cv.circle(  # pylint: disable=no-member
                    mask_image,
                    (circle[0], circle[1]),
                    circle[2],
                    255,
                    -1
                )
        if shape["type"] == "POLYGON":
            # TODO: validate polygon shape
            print("POLYGON")
            polygon = np.asarray(shape["coordinate"], np.int)
            if len(polygon) > 2:
                cv.fillPoly(  # pylint: disable=no-member
                    mask_image,
                    [polygon],
                    255
                )
    return mask_image, True


# class_index, x_center, y_center, x_width, y_height
# to: x_start, y_start, x_finish, y_finish
def prase_yolo_format(rect, img_width, img_height):
    centerX = float(rect[1])
    centerY = float(rect[2])
    bbox_width = float(rect[3])
    bbox_height = float(rect[4])
    x_start = int(img_width * centerX - img_width * bbox_width / 2.0)
    x_finish = int(img_width * centerX + img_width * bbox_width / 2.0)
    y_start = int(img_height * centerY - img_height * bbox_height / 2.0)
    y_finish = int(img_height * centerY + img_height * bbox_height / 2.0)
    return np.array([x_start, y_start, x_finish, y_finish])


def convert_yolo_2_mask_json(data, img_width, img_height):
    data = np.asarray(data)
    mask_json = []
    if data.ndim == 1:
        # only one record
        mask_json.append({
            "type": "RECT",
            "coordinate": prase_yolo_format(data, img_width, img_height)
        })
    else:
        r, c = data.shape
        for i in range(r):
            mask_json.append({
                "type": "RECT",
                "coordinate": prase_yolo_format(data[i, :], img_width, img_height)
            })
    return mask_json


baseline_image_path = "./baseline_image"
mask_json_path = "./masks/yolo_labels"

test_image_path = "./test_image"
output_image_path = "./output_image"

flag_export_image = False
flag_export_image = True

if flag_export_image:
    # create output directory
    if not os.path.isdir(output_image_path):
        os.makedirs(output_image_path)

print('-' * 55)
file_names = os.listdir(baseline_image_path)
print("Number of baseline images found:", len(file_names))
file_names.sort()

for file_name in file_names:
    baseline_image_file_path = os.path.join(baseline_image_path, file_name)
    if not os.path.isfile(baseline_image_file_path):
        continue

    print('-' * 55)
    print(file_name)
    print('')
    if file_name == '4.png':
        break

    # check test image
    # which has the same name as that in the base line image
    test_image_file_path = os.path.join(test_image_path, file_name)
    if not os.path.isfile(test_image_file_path):
        print(f"Missing test image file.")
        continue

    # load image
    input_image_1 = cv.imread(baseline_image_file_path)
    input_image_2 = cv.imread(test_image_file_path)

    flag_NG = False
    # TODO: checking image size
    if input_image_1.shape != input_image_2.shape:
        flag_NG = True
        print("Image Size Not Match!!")

    # load image mask if exist
    # the mask file name is 'image name.txt'
    mask_json = []
    label_file_name = file_name.split('.')[0] + '.txt'
    label_file_path = os.path.join(mask_json_path, label_file_name)
    if os.path.isfile(label_file_path):
        labels = []
        with open(label_file_path, encoding='utf-8') as f:
            labels = np.loadtxt(f, delimiter=" ")

        if len(labels) == 0:
            print("Empty label file")
        else:
            print(f"labels:\n{labels}")
            # construct the json type for the draw mask function
            mask_json = convert_yolo_2_mask_json(
                labels, input_image_1.shape[1], input_image_1.shape[0]
            )
            print(f"mask_json:\n{mask_json}")
            print('')

    process_image_1 = np.copy(input_image_1)
    process_image_2 = np.copy(input_image_2)
    # apply mask if exist
    if len(mask_json) > 0:
        # draw mask image
        mask_image = np.zeros(
            (
                input_image_1.shape[0],
                input_image_1.shape[1]
            ),
            np.uint8
        )
        mask_image, status = draw_mask_image(mask_image, mask_json)
        mask_image = cv.bitwise_not(mask_image)
        process_image_1 = cv.bitwise_and(process_image_1, process_image_1, mask=mask_image)
        process_image_2 = cv.bitwise_and(process_image_2, process_image_2, mask=mask_image)

    # check diff
    image_diff = np.abs(process_image_1 - process_image_2)
    image_diff_max = np.max(image_diff)
    print(f"Max Image diff: {image_diff_max}")
    print('')
    if image_diff_max > 0:
        print("Not Match!!")

    if flag_export_image:
        # create result image
        output_image = np.sum(image_diff, 2)
        output_image[output_image > 0] = 255
        output_image = output_image.astype(np.uint8)

        # draw the diff only
        output_image_file_path = os.path.join(output_image_path, file_name)
        cv.imwrite(output_image_file_path, output_image)

        # draw the outter bounding box
        contours, _ = cv.findContours(output_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        print(contours)
        for c in contours:
            area = cv.contourArea(c)
            if area < 10:
                continue
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(input_image_2, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv.imwrite(output_image_file_path, input_image_2)
