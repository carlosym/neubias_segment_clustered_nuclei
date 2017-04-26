#!/usr/bin/python

# Author: Sebastien Tosi (IRB Barcelona)
# Version: 1.0
# Date: 24/04/2017
import sys
import glob
import os
import numpy as np
from skimage import io
from skimage import filters
from skimage import morphology
from skimage import img_as_uint
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.morphology import watershed



def main(argv):

    InputFolderPath = argv[0]  # "./../Annotated images/Normal/"
    OutputFolderPath = argv[1]  # "./../Annotated images/Normal/out/"

    IntensityBlurRad = argv[2]  # 1.5
    DistanceBlurRad = argv[3]  # 3

    for img in glob.glob(InputFolderPath+"/*.tif"):
        InputPath = img
        print "Processing "+img

        OutputPath = OutputFolderPath +"/OUT_"+os.path.basename(InputPath)

        # Read image
        I = io.imread(InputPath)

        # Processing
        If = filters.gaussian(I, sigma=IntensityBlurRad)
        val = filters.threshold_otsu(If)
        mask = If >= val
        distance = ndimage.distance_transform_edt(mask)
        distance = filters.gaussian(distance, sigma=DistanceBlurRad)
        local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=mask)
        markers = morphology.label(local_maxi)
        nuclei_labels = watershed(-distance, markers, mask=mask)
        nuclei_labels = img_as_uint(nuclei_labels)

        print "Saving..."
        # Export label mask
        io.imsave(OutputPath, nuclei_labels)

        # Display label mask
        #import matplotlib.pyplot as plt
        #plt.figure(figsize=(4, 4))
        #plt.imshow(nuclei_labels%9 , cmap='jet', interpolation='nearest')
        #plt.axis('off')
        #plt.tight_layout()
        #plt.show()


if __name__ == "__main__":
   main(sys.argv[1:])