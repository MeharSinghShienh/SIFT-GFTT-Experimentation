'''
Largely referencing following video https://www.youtube.com/watch?v=DKkDVHhJ8_M&t=20s
'''

import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Function to perform feature matching and homography using SIFT on a series of frames within a certain interval
def featureMatchingHomographySIFT(video_path, start_time, time_interval, frames_count):
    # Load the video and retrieve frames per second
    cap = cv.VideoCapture(video_path)
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_interval = int(fps * time_interval / frames_count)  # Calculate interval to get 'frames_count' frames within 'time_interval' seconds
    start_frame = start_time * fps # Determine start frame based on start time

    frames = []
    frame_indices = [start_frame, start_frame + frame_interval, start_frame + (2 * frame_interval)] # Define indices for frames to capture

    # Capture and convert frames to grayscale
    for idx in frame_indices:
        cap.set(cv.CAP_PROP_POS_FRAMES, idx)  # Set the position of the video to the frame index
        ret, frame = cap.read()
        if ret:
            frames.append(cv.cvtColor(frame, cv.COLOR_BGR2GRAY))  # Convert to grayscale

    # Initialize the plot with subplots
    #fig, axs = plt.subplots(1, frames_count - 1, figsize=(15, 5))
    #fig.suptitle('Feature Matching and Homography (SIFT)')

    # Process each pair of consecutive frames
    for i in range(frames_count-1):
        img1, img2 = frames[i], frames[i + 1] # Select consecutive frames

        # Initialize SIFT and detect keypoints and descriptors
        sift = cv.SIFT_create()
        keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
        keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

        # Set up FLANN-based matcher with KD-Tree for SIFT
        FLANN_INDEX_KDTREE = 1
        indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        searchParams = dict(checks=50)
        flann = cv.FlannBasedMatcher(indexParams, searchParams)
        nNeighbours = 2
        matches = flann.knnMatch(descriptors1, descriptors2, nNeighbours) # Find matches using k-nearest neighbors

        # Filter good matches based on Lowe's ratio test
        goodMatches = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                goodMatches.append(m)

        # Extract matched points
        srcPoints = np.float32([keypoints1[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        dstPoints = np.float32([keypoints2[m.trainIdx].pt for m in goodMatches]).reshape(-1, 1, 2)

        # Calculate homography using RANSAC
        errorThreshold = 5
        M,mask = cv.findHomography(srcPoints, dstPoints, cv.RANSAC, errorThreshold)
        matchesMask = mask.ravel().tolist() # Mask for visualizing inlier matches

        # Draw projected border on img2 for alignment visualization
        h,w = img1.shape
        imgBorder = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]]).reshape(-1,1,2)
        warpedImgBorder = cv.perspectiveTransform(imgBorder, M)
        img2 = cv.polylines(img2, [np.int32(warpedImgBorder)], True, 255, 3, cv.LINE_AA)

        # Draw matches with matched points highlighted in green
        green = (0, 255, 0)
        drawParams = dict(matchColor=green, singlePointColor=None, matchesMask=matchesMask, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
        imgMatch = cv.drawMatches(img1, keypoints1, img2, keypoints2, goodMatches, None, **drawParams)

        
        plt.figure()
        plt.imshow(imgMatch, 'gray')
        plt.show()
        '''

        # Plot each result in a separate subplot
        axs[i].imshow(imgMatch, 'gray')
        axs[i].set_title(f'Frames {i} and {i+1}')
        axs[i].axis('off')

    # Show the combined plot
    plt.show()
    '''

# Function to perform feature matching and homography using GFTT for keypoint detection and SIFT for descriptors
def featureMatchingHomographySIFTandGFTT(video_path, start_time, time_interval, frames_count):
    # Load the video
    cap = cv.VideoCapture(video_path)
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_interval = int(fps * time_interval / frames_count)  # Calculate interval to get 'frames_count' frames within 'time_interval' seconds
    start_frame = start_time * fps

    frames = []
    frame_indices = [start_frame, start_frame + frame_interval, start_frame + (2 * frame_interval)]

    for idx in frame_indices:
        cap.set(cv.CAP_PROP_POS_FRAMES, idx)  # Set the position of the video to the frame index
        ret, frame = cap.read()
        if ret:
            frames.append(cv.cvtColor(frame, cv.COLOR_BGR2GRAY))  # Convert to grayscale

    # Initialize the plot with subplots
    #fig, axs = plt.subplots(1, frames_count - 1, figsize=(15, 5))
    #fig.suptitle('Feature Matching and Homography (SIFT)')

    # Process each pair of consecutive frames
    for i in range(frames_count-1):
        img1, img2 = frames[i], frames[i + 1]

        # Initialize GFTT for corner detection and SIFT for descriptor computation
        gftt = cv.GFTTDetector_create(maxCorners=1000, qualityLevel=0.01, minDistance=5)
        sift = cv.SIFT_create()
        # Detect corners with GFTT
        keypoints1 = gftt.detect(img1)
        keypoints2 = gftt.detect(img2)
        # Compute SIFT descriptors at the GFTT keypoints
        keypoints1, descriptors1 = sift.compute(img1, keypoints1)
        keypoints2, descriptors2 = sift.compute(img2, keypoints2)

        FLANN_INDEX_KDTREE = 1
        indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        searchParams = dict(checks=50)
        flann = cv.FlannBasedMatcher(indexParams, searchParams)
        nNeighbours = 2
        matches = flann.knnMatch(descriptors1, descriptors2, nNeighbours)

        goodMatches = []
        for m, n in matches:
            if m.distance < 0.8 * n.distance:
                goodMatches.append(m)

        srcPoints = np.float32([keypoints1[m.queryIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        dstPoints = np.float32([keypoints2[m.trainIdx].pt for m in goodMatches]).reshape(-1, 1, 2)
        errorThreshold = 5
        M,mask = cv.findHomography(srcPoints, dstPoints, cv.RANSAC, errorThreshold)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        imgBorder = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]]).reshape(-1,1,2)
        warpedImgBorder = cv.perspectiveTransform(imgBorder, M)
        img2 = cv.polylines(img2, [np.int32(warpedImgBorder)], True, 255, 3, cv.LINE_AA)

        green = (0, 255, 0)
        drawParams = dict(matchColor=green, singlePointColor=None, matchesMask=matchesMask, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
        imgMatch = cv.drawMatches(img1, keypoints1, img2, keypoints2, goodMatches, None, **drawParams)

        
        plt.figure()
        plt.imshow(imgMatch, 'gray')
        plt.show()
        '''
        
        # Plot each result in a separate subplot
        axs[i].imshow(imgMatch, 'gray')
        axs[i].set_title(f'Frames {i} and {i+1}')
        axs[i].axis('off')

    # Show the combined plot
    plt.show()
    '''

if __name__ == '__main__':
    #add local paths to videos
    root = os.getcwd()
    #vid1path = os.path.join(root, 'videos', 'laurier_field.MTS')
    #featureMatchingHomographySIFTandGFTT(vid1path, 30, 3, 3)
    vid2path = os.path.join(root, 'videos', 'basic_field.MTS')
    featureMatchingHomographySIFTandGFTT(vid2path, 38, 3, 3)