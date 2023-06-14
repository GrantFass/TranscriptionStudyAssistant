"""
The code in this file is based on a tutorial from
https://debuggercafe.com/moving-object-detection-using-frame-differencing-with-opencv/

The steps for moving object detection are as follows:
    1. grab 8 consecutive frames from video feed
    2. convert each of the frames to grayscale
    3. get background model by taking median of x frames
    4. subtract each frame from background model
    5. add the 8 frames
    6. fill gaps inside the objects
    7. convert to binary image by applying thresholding
    8. remove noise with things like dilation and erosion
    9. draw contours around detected objects
"""

# Imports
import cv2 as cv
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time

##################################
#        GLOBAL VARIABLES        #
##################################
# The number of frames to include in the buffer. The median of these
# frames is then taken and converted into grayscale to get the background.
BACKGROUND_FRAME_BUF_SIZE = 4
# The number of frames of interval between when the background should be recalculated.
BACKGROUND_RECALCULATION_INTERVAL = 8
# The number of frames per second to record at. Note that higher values may not be supported.
FPS = 7
# number of passes of dilation to run. This should reduce the number of separate objects
# but it will also make objects bigger.
DILATION_PASSES = 3
# Specifies the number of frames that should be averaged when looking
# for moving targets. Lower numbers result in smoother video but more
# inaccuracy.
CONSECUTIVE_FRAMES = 2
# Where to read the video feed from. filepaths work with prerecorded video.
# can also specify ip addresses of cameras. Integers specify the camera number
# on the system itself. On a laptop 0 would usually be the internal camera.
# 1 would then be the first external webcam and so on.
VIDEO_FEED_PATH = 1
# Specifies if the resulting video should be saved
SAVE_RESULT = False
# Specifies where the resulting video should be saved to
SAVE_NAME = "temp_save_file.mp4"


def setup_video_writer(capture_feed):
    # get the video frame height and width
    width = int(capture_feed.get(3))
    height = int(capture_feed.get(4))
    # define codec and create VideoWriter object
    return cv.VideoWriter(
        SAVE_NAME,
        cv.VideoWriter_fourcc(*'mp4v'),
        FPS,
        (width, height)
    )


def sublist_operations(frame, background):
    # grayscale each frame in the sublist
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate the difference from the background for each frame in sublist
    frame_diff = cv.absdiff(gray, background)
    # threshold each frame in sublist
    ret, thresh = cv.threshold(frame_diff, 50, 255, cv.THRESH_BINARY)
    # dilate each frame in sublist
    dilate_frame = cv.dilate(thresh, None, iterations=DILATION_PASSES)
    return dilate_frame


def calculate_background(buffer):
    background_median = np.median(buffer, axis=0).astype(np.uint8)
    background = cv.cvtColor(background_median, cv.COLOR_BGR2GRAY)
    return background


def draw_contours(frame, sum_frames):
    # find the contours
    contours, hierarchy = cv.findContours(sum_frames, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # continue through the loop if contour area is less than 500...
        # ... helps in removing noise detection
        if cv.contourArea(contour) < 500:
            continue
        # get the xmin, ymin, width, and height coordinates from the contours
        (x, y, w, h) = cv.boundingRect(contour)
        # draw the bounding boxes
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_connected_components(frame, sum_frames):
    connectivity = 4
    connected = cv.connectedComponentsWithStats(sum_frames, connectivity, cv.CV_32S)
    (numLabels, labels, stats, centroids) = connected

    df = pd.DataFrame(columns=['area', 'x', 'y', 'w', 'h', 'cX', 'cY'])
    for i in range(0, numLabels):
        x = stats[i, cv.CC_STAT_LEFT]
        y = stats[i, cv.CC_STAT_TOP]
        w = stats[i, cv.CC_STAT_WIDTH]
        h = stats[i, cv.CC_STAT_HEIGHT]
        area = stats[i, cv.CC_STAT_AREA]
        (cX, cY) = centroids[i]
        temp = pd.DataFrame([{'area': area, 'x': x, 'y': y, 'w': w, 'h': h, 'cX': cX, 'cY': cY}])
        df = pd.concat([df, temp])

    df = df.sort_values(by='area', ascending=False, ignore_index=True)
    df = df[df['area'] > 100]
    if len(df) > 1:
        df = df.iloc[[1]].reset_index(drop=True)  # grab the second element because the first is the window as a whole.
    for i in range(len(df)):
        x = int(df.at[i, 'x'])
        y = int(df.at[i, 'y'])
        w = int(df.at[i, 'w'])
        h = int(df.at[i, 'h'])
        cX = int(df.at[i, 'cX'])
        cY = int(df.at[i, 'cY'])
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv.circle(frame, (int(cX), int(cY)), 4, (0, 0, 255), -1)


# def wait_for_fps(start_time):
#     while datetime.now() - timedelta(seconds=(1/FPS)) < start_time:
#         time.sleep(1/1000.)


def moving_object():
    cap = cv.VideoCapture(VIDEO_FEED_PATH)
    out = None
    if SAVE_RESULT:
        out = setup_video_writer(cap)

    # Populate the initial background
    background_frame_buf = []
    for i in range(BACKGROUND_FRAME_BUF_SIZE):
        ret, frame = cap.read()
        background_frame_buf.append(frame)  # adds to end of list

    background = calculate_background(background_frame_buf)
    # Begin the computation loop
    background_count = 0
    frame_count = 0
    frame_diff_list = []
    # start_time = datetime.now()
    while cap.isOpened():
        # wait_for_fps(start_time)
        # start_time = datetime.now()
        ret, frame = cap.read()  # grab the latest frame
        if ret:
            # remove the oldest frame in the buffer (front of list)
            background_frame_buf.pop(0)
            # add the current frame at the most recent spot (end of list)
            background_frame_buf.append(frame)
            # recalculate the background once per interval
            if background_count >= BACKGROUND_RECALCULATION_INTERVAL:
                background = calculate_background(background_frame_buf)
                background_count = 0
            else:
                background_count += 1

            frame_count += 1
            if frame_count % CONSECUTIVE_FRAMES == 0 or frame_count == 1:
                frame_diff_list = []
            frame_diff_list.append(sublist_operations(frame, background))
            # if we have reached `consecutive_frame` number of frames
            if len(frame_diff_list) == CONSECUTIVE_FRAMES:
                # add all the frames in the `frame_diff_list`
                sum_frames = sum(frame_diff_list)
                # draw_contours(frame, sum_frames)
                draw_connected_components(frame, sum_frames)
                cv.imshow('Detected Objects', frame)
                if out is not None:
                    out.write(frame)
                if cv.waitKey(100) & 0xFF == ord('q'):
                    break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    moving_object()
