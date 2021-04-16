#!/usr/bin/env python3
# encoding: utf-8

import json
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection


def calculate_area(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


with open('0.geojson', 'r') as f:
    j = json.load(f)
    for feature in j['features']:
        admin = feature['properties']['ADMIN']
        iso = feature['properties']['ISO_A3']
        if feature['properties']['ISO_A3'] != '-99':
            coords = feature['geometry']['coordinates']
            num_subplots = len(coords)
            print(f"{admin.replace(' ', '_')}-{iso}.png")
            fig, ax = plt.subplots()
            try:
                if num_subplots == 1:
                    coll = PolyCollection(coords)
                else:
                    if iso == 'KGZ':
                        coll = PolyCollection(coords)
                    else:
                        areas = [calculate_area(sub_l[0]) for sub_l in coords]
                        max_area = max(areas)
                        print(areas)
                        coll = PolyCollection(
                            [sub_l[0] for sub_l in coords if max_area/calculate_area(sub_l[0]) < 100]
                        )
                ax.add_collection(coll)
            except ValueError as e:
                print('coords', coords)
                print('num_subplots', num_subplots)
                print(f"{admin.replace(' ', '_')}-{iso}.png")
                print(e)
            ax.autoscale_view()
            plt.axis('off')
            plt.tick_params(
                axis='both', left='off', top='off', right='off', bottom='off',
                labelleft='off', labeltop='off', labelright='off', labelbottom='off'
            )
            plt.savefig(
                f"{admin.replace(' ', '_')}-{iso}.png",
                dpi=100, bbox_inches='tight', pad_inches=0.0
            )
