# Script for ArcGIS Pro (ArcPy 3.x) to perform Hot Spot Analysis (Getis-Ord Gi*)
# Author: (Your Name)
# Date: (Today's Date)

# Import arcpy to access ArcGIS geoprocessing tools
import arcpy
import os

# Allow overwriting of existing outputs
arcpy.env.overwriteOutput = True

# Provide simple user feedback
print("Starting Hot Spot Analysis (Getis-Ord Gi*)...")

# Define the input and output file paths
input_directory = r"C:\temp"
input_shapefile = os.path.join(input_directory, "robbery_census.shp")
output_shapefile = os.path.join(input_directory, "robbery_hotspots.shp")

# Define parameters exactly as specified
Input_Feature_Class = input_shapefile
Input_Field = "Join_Count"
Output_Feature_Class = output_shapefile
Conceptualization_of_Spatial_Relationships = "FIXED_DISTANCE_BAND"
Distance_Band_or_Threshold_Distance = "1817.2120"   # Distance as string or float
Standardization = "NONE"
Distance_Method = "EUCLIDEAN_DISTANCE"

try:
    # Check if the input shapefile exists
    if not arcpy.Exists(Input_Feature_Class):
        raise FileNotFoundError(f"Input shapefile not found at {Input_Feature_Class}")

    print(f"Input shapefile found: {Input_Feature_Class}")
    print("Running Hot Spot Analysis (Getis-Ord Gi*)...")

    # Run the Hot Spot Analysis using **named arguments**
    arcpy.stats.HotSpots(
        Input_Feature_Class=Input_Feature_Class,
        Input_Field=Input_Field,
        Output_Feature_Class=Output_Feature_Class,
        Conceptualization_of_Spatial_Relationships=Conceptualization_of_Spatial_Relationships,
        Distance_Band_or_Threshold_Distance=Distance_Band_or_Threshold_Distance,
        Standardization=Standardization,
        Distance_Method=Distance_Method
    )

    print(f"Hot Spot Analysis completed successfully.")
    print(f"Output shapefile created at: {Output_Feature_Class}")

except FileNotFoundError as fnf_error:
    # Handle missing input shapefile
    print(f"File error: {fnf_error}")
except arcpy.ExecuteError:
    # Handle errors raised by ArcGIS tools
    print("ArcPy execution error:")
    print(arcpy.GetMessages(2))
except Exception as e:
    # Handle any other unexpected Python errors
    print(f"An unexpected error occurred: {e}")
finally:
    # Final message to indicate script completion
    print("Script execution completed.")
