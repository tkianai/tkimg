"""This visualize the keypoints, including pose, face, hand and so on
"""


import os
import cv2
import numpy as np


def show_keypoints_over_image(
    img, 
    points, 
    skeletons=None,
    radius=3,
    color=(0, 255, 0),
):
    """Plot keypoints on image
    
    Arguments:
        img {str | np img | pil img} -- input image
        points {list of list} -- point set
    
    Keyword Arguments:
        skeletons {list of list} -- point collection (default: {None})
        radius {int} -- radius of keypoint (default: {3})
        color {tuple} -- keypoint color to show (default: {(0, 255, 0)})
    
    Returns:
        img -- numpy image[opencv]
    """

    if isinstance(img, str):
        img = cv2.imread(img)

    if isinstance(img, np.ndarray):
        img = np.array(img)   # Handle PIL object

    # plot isolate keypoints
    for point in points:
        # point: [width(x), height(y)]
        img = cv2.circle(img, (int(point[0], int(point[1]))), radius, color, -1)
    
    
    # plot skeletons
    if skeletons is not None:
        for skeleton in skeletons:
            line_color = np.random.randint(256, size=3).tolist()
            p1 = points[skeleton[0]]
            p2 = points[skeleton[1]]
            img = cv2.line(img, p1, p2, line_color, 2)


    return img