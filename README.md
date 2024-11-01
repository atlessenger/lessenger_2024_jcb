# Code for Lessenger et al., 2024, JCB

We provide here the custom code used for our RNA-seq and ChIP-seq experiments as well as the custom 3D StarDist (https://stardist.net/) model used to segment C. elegans nuclei.

## Sequencing
The python scripts for ChIP-seq were originally written by Georgi Marinov, so please credit him if you use these scripts. The R markdown files included were used to produce all figures in the manuscript as well as some additional, unpublished analyses.

## 3D StarDist model
This model performs extremely well on germline nuclei, and somewhat well on other nuclei. The model was trained on DAPI-stained nuclei, but also performed well on endogenously tagged RNA polymerase II. It performed poorly on NLS-mScarlet.

While this model may perform well for your images, it is more likely that it will serve only as a starting point for labeling your own training images. Your images may need to be rescaled so that nuclei are isometric in z and approximately the same size (in pixels) as ours: nuclei are segmented best when 20-50 pixels in diameter, with ok segmentation from 16-60 pixels. Our model could then provide a preliminary segmentation which can be corrected, instead of starting from scratch.
