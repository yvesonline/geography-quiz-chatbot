#!/usr/bin/env python3
# encoding: utf-8

import boto3
from botocore.exceptions import ClientError
import cartopy
import cartopy.io.shapereader as shpreader
import json
import matplotlib.pyplot as plt
import shapely.wkt as wkt
from shapely.geometry import MultiPolygon


boto3.setup_default_session(profile_name='yvesweissig')
s3_client = boto3.client('s3')
bucket = 'geography-quiz-bot-images'

shpfilename = shpreader.natural_earth(
    resolution='10m',
    category='cultural',
    name='admin_0_countries'
)
reader = shpreader.Reader(shpfilename)
countries = reader.records()

color = '#9CCC9C'

allowed_types = ['Sovereign country', 'Country', 'Dependency']
filtered_countries = [country for country in countries if country.attributes['TYPE'] in allowed_types]
print('Number of countries:', len(filtered_countries))

for country in filtered_countries:
    name_long = country.attributes['NAME_LONG']
    iso = country.attributes['ADM0_A3']
    filename = f"{name_long.replace(' ', '_')}-{iso}.png"
    print(filename)
    # print(country.attributes['SOVEREIGNT'], country.attributes['TYPE'], country.attributes['MIN_ZOOM'])
    ax = plt.axes(projection=cartopy.crs.PlateCarree())
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=.25)
    # ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    # ax.add_feature(cartopy.feature.RIVERS)
    ax.outline_patch.set_edgecolor('grey')
    diff_x = abs(country.geometry.bounds[0]-country.geometry.bounds[2])
    diff_y = abs(country.geometry.bounds[1]-country.geometry.bounds[3])
    bounds = [coord for coord in country.geometry.bounds]
    # print(bounds)
    # print('diff_x', diff_x)
    # print('diff_y', diff_y)
    bounds[0] -= diff_x  # Lower left x
    if bounds[0] < -180.0:
        bounds[0] = -180.0
    if bounds[0] > 180.0:
        bounds[0] = 180.0
    bounds[1] -= diff_y  # Lower left y
    if bounds[1] < -90.0:
        bounds[1] = -90.0
    if bounds[1] > 90.0:
        bounds[1] = 90.0
    bounds[2] += diff_x  # Upper right x
    if bounds[2] < -180.0:
        bounds[2] = -180.0
    if bounds[2] > 180.0:
        bounds[2] = 180.0
    bounds[3] += diff_y  # Upper right y
    if bounds[3] < -90.0:
        bounds[3] = -90.0
    if bounds[3] > 90.0:
        bounds[3] = 90.0
    # print(bounds)
    ax.set_global()
    ax.set_extent([bounds[0], bounds[2], bounds[1], bounds[3]], cartopy.crs.PlateCarree())
    try:
        ax.add_geometries(
            country.geometry,
            cartopy.crs.PlateCarree(),
            facecolor=(color),
            label=iso,
            edgecolor='grey',
            linewidth=.25
        )
    except Exception:
        list_str_polygons = [str(country.geometry)]
        c = MultiPolygon(map(wkt.loads, list_str_polygons))
        ax.add_geometries(
            c,
            cartopy.crs.PlateCarree(),
            facecolor=(color),
            label=iso,
            edgecolor='grey',
            linewidth=.25
        )
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.0, dpi=300)
    plt.clf()
    try:
        s3_client.upload_file(filename, bucket, filename, ExtraArgs={'ContentType': 'image/png'})
    except ClientError as e:
        print(e)
