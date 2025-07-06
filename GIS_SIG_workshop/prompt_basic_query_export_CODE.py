# Import the arcpy module to access ArcGIS functions
import arcpy
import os

# Allow overwriting of outputs
arcpy.env.overwriteOutput = True

# Define key variables
layer_name = 'world_country_boundaries'              # Name of the layer to select from
output_directory = r"C:\temp"                         # Directory to save the new shapefile
output_shapefile = os.path.join(output_directory, "populated_world_countries.shp")  # Full path for new shapefile
selection_query = "POP_RANK >= 15"                    # SQL query for selection

try:
    print("Starting the feature selection and export process...")

    # Access the current ArcGIS Pro project
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    print("Accessed the current ArcGIS Project.")

    # Access the first map in the project (modify if you have multiple maps)
    map_obj = aprx.listMaps()[0]
    print(f"Using map: {map_obj.name}")

    # Access the specified layer by name
    layer = map_obj.listLayers(layer_name)[0]
    print(f"Found layer: {layer.name}")

    # Apply the selection based on the SQL query
    arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=layer,
        selection_type="NEW_SELECTION",
        where_clause=selection_query
    )
    print(f"Selected features where {selection_query}.")

    # Count the number of selected features and report
    count_result = arcpy.management.GetCount(layer)
    selected_count = int(count_result.getOutput(0))
    print(f"Number of features selected: {selected_count}")

    # Check if any features were selected before exporting
    if selected_count > 0:
        # Export selected features to a new shapefile
        arcpy.management.CopyFeatures(
            in_features=layer,
            out_feature_class=output_shapefile
        )
        print(f"Selected features exported successfully to: {output_shapefile}")
    else:
        print("No features matched the selection criteria. No shapefile was created.")

except IndexError:
    # Handle the case where the layer or map is not found
    print(f"Error: Could not find the map or layer named '{layer_name}'. Please check the name.")
except arcpy.ExecuteError:
    # Handle any ArcGIS-specific execution errors
    print("ArcPy execution error:")
    print(arcpy.GetMessages(2))
except Exception as e:
    # Catch any other unexpected Python errors
    print(f"An unexpected error occurred: {e}")
finally:
    print("Script execution completed.")
