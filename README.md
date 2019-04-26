# Batch geocode dataframe

This is a Python script that can be used as a module for simple geocoding of pandas dataframes, using the Google Geocoding API.

## Why

There are many geocoding solutions out there, including for dataframes (see [geopandas](http://geopandas.org/geocoding.html)), but none were exactly what I needed.

This script attempts solve the following:

- provide a simple way for geocoding a dataframe;
- save the results of each geocoded address into jsons that get reloaded, **to avoid multiple calls to the Google API for the same address**.

## Requirements

- `pandas`
- `geopy`

I recommend using this with Conda.

## Usage

1. Copy the `geocoder.py` into your project.
2. `import geocoder` into your script.
3. Run it with `geocoder.geocode(df, address_col, data_folder, GOOGLE_MAPS_API_KEY)`. Example `geocoder.geocode(my_df, 'formatted_address', 'geocoded_output/', 'YOUR_GOOGLE_API_KEY')`.
4. If you want to use it with slugs for address IDs instead of SHA hashes, pass `use_slugify=True` to the `geocode` method.
