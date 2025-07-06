# Lake Area Monitoring Using Sentinel 2 Imagery
This repository contains code for monitoring the change in lake area over time using Sentinel-2 satellite imagery(10m spatial resolution). The project analyzes the Normalized Difference Water Index (NDWI) from Sentinel-2 data to track the variation in lake area from 2015. The workflow includes the use of Google Earth Engine for satellite data processing, xarray for managing and visualizing data, and KMeans clustering for identifying water and non-water areas. The results are visualized through annual lake area maps and area calculations.



## Project Overview
The purpose of this project is to analyze the temporal changes in lake area, helping researchers and environmentalists understand the impact of climate change, human activity, and other factors on water bodies. By calculating NDWI over the years, the code extracts the water body and uses clustering to differentiate between water and non-water areas. The analysis then computes the lake area on an annual basis and visualizes these changes.



## Example Outputs

![image alt](https://github.com/SaeidDaliriSusefi/Lake-Change-Monitoring-Sentinel2/blob/9dfdb81a6229993020c2ed20d6841ae3591d0be2/Images/download%20(9).png)
