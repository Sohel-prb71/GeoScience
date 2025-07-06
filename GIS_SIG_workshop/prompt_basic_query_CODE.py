# Import the arcpy module which gives access to ArcGIS tools
import arcpy

# Always good practice to set environment settings
# This will overwrite any existing outputs if needed
arcpy.env.overwriteOutput = True

try:
    # Provide basic user feedback
    print("Starting selection process...")

    # Reference the current ArcGIS Pro project (.aprx file)
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    print("Successfully accessed current ArcGIS Project.")

    # Reference the first map in the project (you can change 'Map' to your map's name if needed)
    map_obj = aprx.listMaps()[0]
    print(f"Accessed the map: {map_obj.name}")

    # Find the layer called 'world_country_boundaries'
    layer_name = 'world_country_boundaries'
    layer = map_obj.listLayers(layer_name)[0]
    print(f"Layer '{layer_name}' found.")

    # Define the selection query
    # This SQL expression selects features where the POP_RANK field is >= 15
    selection_query = "POP_RANK >= 15"
    print(f"Using selection query: {selection_query}")

    # Make the selection on the layer
    arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=layer,        # The layer to select from
        selection_type="NEW_SELECTION",# Create a new selection
        where_clause=selection_query   # The SQL expression
    )
    print("Feature selection complete.")

    # Optional: Count selected features and report
    count_result = arcpy.management.GetCount(layer)
    selected_count = int(count_result.getOutput(0))
    print(f"Number of features selected: {selected_count}")

except IndexError:
    # This happens if the layer or map is not found
    print(f"Error: Could not find the map or layer '{layer_name}'. Please check the names.")
except arcpy.ExecuteError:
    # Catch errors specific to ArcPy tools
    print("ArcPy execution error:")
    print(arcpy.GetMessages(2))
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")

finally:
    print("Script execution completed.")