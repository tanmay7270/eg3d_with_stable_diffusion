import random
from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import shutil


def prep_dataset_analysis(src_dir, dst_dir, real_imgs_dir):
    # Set the directories
    src_dir = '/Users/christina/Downloads/sd_stylized/comic/'
    real_imgs_dir = '/Users/christina/Downloads/faces_dataset_small'
    dst_dir = '/Users/christina/Downloads/sd_stylized/real_imgs/'

    # Get the filenames in the source directory
    filenames = os.listdir(src_dir)

    # Loop through the filenames
    for filename in filenames:
        # Construct the full path to the file in the source directory
        src_path = os.path.join(src_dir, filename)
        # Construct the full path to the file in the destination directory
        dst_path = os.path.join(dst_dir, filename)

        real_path = os.path.join(real_imgs_dir, filename)
        # Check if the file exists in the destination directory
        if os.path.exists(real_path):
            # If it doesn't exist, copy it from the source directory to the destination directory
            shutil.copy(real_path, dst_path)


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


def plot_images(dir1, dir2, dir3, dir4):

    # Get the filenames in the first directory
    filenames = os.listdir(dir1)
    random_filenames = random.sample(filenames, 10)

    # Loop through the filenames
    for filename in random_filenames:

        # Construct the full paths to the images in all four directories
        path1 = os.path.join(dir1, filename)
        path2 = os.path.join(dir2, filename)
        path3 = os.path.join(dir3, filename)
        path4 = os.path.join(dir4, filename)

        # Read the images from the file paths
        image1 = imread(path1)
        print(path1)
        image2 = imread(path2)
        print(path2)
        image3 = imread(path3)
        print(path3)
        image4 = imread(path4)
        print(path4)

        # Create a subplot with four images
        plt.subplot(1, 4, 1)
        plt.imshow(image1)
        plt.title(os.path.dirname(dir1))
        plt.axis('off')
        plt.subplot(1, 4, 2)
        plt.imshow(image2)
        plt.title(os.path.dirname(dir2))
        plt.axis('off')
        plt.subplot(1, 4, 3)
        plt.imshow(image3)
        plt.title(os.path.dirname(dir3))
        plt.axis('off')
        plt.subplot(1, 4, 4)
        plt.imshow(image4)
        plt.title(os.path.dirname(dir4))
        plt.axis('off')

        # Show the plot
        plt.show()


comic = '/Users/christina/Downloads/sd_stylized/comic/'
pixar = '/Users/christina/Downloads/sd_stylized/pixar/'
sculpture = '/Users/christina/Downloads/sd_stylized/sculpture/'
real_imgs_dir = '/Users/christina/Downloads/sd_stylized/real_imgs/'

plot_images(real_imgs_dir, comic, pixar, sculpture)
