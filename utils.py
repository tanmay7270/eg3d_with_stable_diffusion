import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import shutil

def prep_dataset_analysis(src_dir, dst_dir, real_imgs_dir):
    # Set the directories
    # src_dir = '/Users/christina/Downloads/sd_stylized/comic/'
    # dst_dir = '/Users/christina/Downloads/faces_dataset_small'
    # real_imgs_dir = '/Users/christina/Downloads/sd_stylized/real_imgs/'

    # Get the filenames in the source directory
    filenames = os.listdir(src_dir)

    # Loop through the filenames
    for filename in filenames:
        # Construct the full path to the file in the source directory
        src_path = os.path.join(src_dir, filename)
        # Construct the full path to the file in the destination directory
        dst_path = os.path.join(dst_dir, filename)
        # Check if the file exists in the destination directory
        if os.path.exists(dst_path):
        # If it doesn't exist, copy it from the source directory to the destination directory
            shutil.copy(src_path, real_imgs_dir)




def pose_estimation(filename):
  # Use EG3D pose detector
  pass

def check_poses_mismatch(dir1, dir2):
    # Set the directories
    dir1 = '/path/to/first/directory'
    dir2 = '/path/to/second/directory'

    # Initialize a list to store the poses that don't match
    mismatch_poses = []

    # Get the filenames in both directories
    filenames1 = os.listdir(dir1)
    filenames2 = os.listdir(dir2)

    # Make sure the filenames are the same in both directories
    assert filenames1 == filenames2, 'The directories have different filenames'

    # Loop through the filenames
    for filename in filenames1:
    # Construct the full paths to the files in both directories
    path1 = os.path.join(dir1, filename)
    path2 = os.path.join(dir2, filename)

    # Get the poses for both files
    pose1 = pose_estimation(path1)
    pose2 = pose_estimation(path2)

    # Check if the poses match
    if pose1 != pose2:
        # If they don't match, add the pose to the list of mismatch poses
        mismatch_poses.append(pose1)

    # Draw a histogram of the mismatch poses
    plt.hist(mismatch_poses)
    plt.show()
