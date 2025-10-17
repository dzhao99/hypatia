# MIT License
#
# Copyright (c) 2020 Debopam Bhattacherjee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from astropy import units as u
# from poliastro.bodies import Earth
# from poliastro.twobody import Orbit
# from astropy.time import Time
# from extractor import CZMLExtractor
import math
try:
    from . import util
except (ImportError, SystemError):
    import util

# Generate static visualizations for entire constellation (multiple shells).

EARTH_RADIUS = 6378135.0 # WGS72 value; taken from https://geographiclib.sourceforge.io/html/NET/NETGeographicLib_8h_source.html

# CONSTELLATION GENERATION GENERAL CONSTANTS
ECCENTRICITY = 0.0000001  # Circular orbits are zero, but pyephem does not permit 0, so lowest possible value
ARG_OF_PERIGEE_DEGREE = 0.0
PHASE_DIFF = True
EPOCH = "2000-01-01 00:00:00"

# Shell wise color codes
# COLOR = [[255, 0, 0, 200], [32, 128, 46, 200], [0, 0, 255, 200], [245, 66, 242, 200], [245, 126, 66, 200]]
COLOR = ['CRIMSON', 'FORESTGREEN', 'DODGERBLUE', 'PERU', 'BLUEVIOLET', 'DARKMAGENTA', 'ORANGE', 'GOLD', 'YELLOWGREEN']
# CONSTELLATION SPECIFIC PARAMETERS


# STARLINK
# NAME = "Starlink"

# SHELL_CNTR = 5

# MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
# ALTITUDE_M = [None]*SHELL_CNTR
# NUM_ORBS = [None]*SHELL_CNTR
# NUM_SATS_PER_ORB = [None]*SHELL_CNTR
# INCLINATION_DEGREE = [None]*SHELL_CNTR
# BASE_ID = [None]*SHELL_CNTR
# ORB_WISE_IDS = [None]*SHELL_CNTR

# MEAN_MOTION_REV_PER_DAY[0] = 15.19  # Altitude ~550000 km
# ALTITUDE_M[0] = 550000  # Altitude ~550000 km
# NUM_ORBS[0] = 72
# NUM_SATS_PER_ORB[0] = 22
# INCLINATION_DEGREE[0] = 53
# BASE_ID[0] = 0
# ORB_WISE_IDS[0] = []

# MEAN_MOTION_REV_PER_DAY[1] = 15.19  # Altitude ~1110 km
# ALTITUDE_M[1] = 540000  # Altitude ~1110 km
# NUM_ORBS[1] = 72
# NUM_SATS_PER_ORB[1] = 22
# INCLINATION_DEGREE[1] = 53.2
# BASE_ID[1] = 1584
# ORB_WISE_IDS[1] = []

# MEAN_MOTION_REV_PER_DAY[2] = 15.19  # Altitude ~1130 km
# ALTITUDE_M[2] = 570000  # Altitude ~1130 km
# NUM_ORBS[2] = 36
# NUM_SATS_PER_ORB[2] = 20
# INCLINATION_DEGREE[2] = 70
# BASE_ID[2] = 3168
# ORB_WISE_IDS[2] = []

# MEAN_MOTION_REV_PER_DAY[3] = 15.19  # Altitude ~1275 km
# ALTITUDE_M[3] = 560000  # Altitude ~1275 km
# NUM_ORBS[3] = 6
# NUM_SATS_PER_ORB[3] = 58
# INCLINATION_DEGREE[3] = 97.6
# BASE_ID[3] = 3888
# ORB_WISE_IDS[3] = []

# MEAN_MOTION_REV_PER_DAY[4] = 15.19  # Altitude ~1325 km
# ALTITUDE_M[4] = 560000  # Altitude ~1325 km
# NUM_ORBS[4] = 4
# NUM_SATS_PER_ORB[4] = 43
# INCLINATION_DEGREE[4] = 97.6
# BASE_ID[4] = 4236
# ORB_WISE_IDS[4] = []
NAME = "Starlink-gen2"

SHELL_CNTR = 9

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 15.19  # Altitude ~550000 km
ALTITUDE_M[0] = 340  # Altitude ~550000 km
NUM_ORBS[0] = 48
NUM_SATS_PER_ORB[0] = 110
INCLINATION_DEGREE[0] = 53
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

MEAN_MOTION_REV_PER_DAY[1] = 15.19  # Altitude ~550000 km
ALTITUDE_M[1] = 345  # Altitude ~550000 km
NUM_ORBS[1] = 48
NUM_SATS_PER_ORB[1] = 110
INCLINATION_DEGREE[1] = 46
BASE_ID[1] = 0
ORB_WISE_IDS[1] = []

MEAN_MOTION_REV_PER_DAY[2] = 15.19  # Altitude ~550000 km
ALTITUDE_M[2] = 350  # Altitude ~550000 km
NUM_ORBS[2] = 48
NUM_SATS_PER_ORB[2] = 110
INCLINATION_DEGREE[2] = 38
BASE_ID[2] = 0
ORB_WISE_IDS[2] = []

MEAN_MOTION_REV_PER_DAY[3] = 15.19  # Altitude ~550000 km
ALTITUDE_M[3] = 360  # Altitude ~550000 km
NUM_ORBS[3] = 30
NUM_SATS_PER_ORB[3] = 120
INCLINATION_DEGREE[3] = 96.9
BASE_ID[3] = 0
ORB_WISE_IDS[3] = []

MEAN_MOTION_REV_PER_DAY[4] = 15.19  # Altitude ~550000 km
ALTITUDE_M[4] = 525  # Altitude ~550000 km
NUM_ORBS[4] = 28
NUM_SATS_PER_ORB[4] = 120
INCLINATION_DEGREE[4] = 53
BASE_ID[4] = 0
ORB_WISE_IDS[4] = []

MEAN_MOTION_REV_PER_DAY[5] = 15.19  # Altitude ~550000 km
ALTITUDE_M[5] = 530  # Altitude ~550000 km
NUM_ORBS[5] = 23
NUM_SATS_PER_ORB[5] = 20
INCLINATION_DEGREE[5] = 43
BASE_ID[5] = 0
ORB_WISE_IDS[5] = []

MEAN_MOTION_REV_PER_DAY[6] = 15.19  # Altitude ~550000 km
ALTITUDE_M[6] = 614  # Altitude ~550000 km
NUM_ORBS[6] = 18
NUM_SATS_PER_ORB[6] = 18
INCLINATION_DEGREE[6] = 115.7
BASE_ID[6] = 0
ORB_WISE_IDS[6] = []

MEAN_MOTION_REV_PER_DAY[7] = 15.19  # Altitude ~550000 km
ALTITUDE_M[7] = 604  # Altitude ~550000 km
NUM_ORBS[7] = 18
NUM_SATS_PER_ORB[7] = 18
INCLINATION_DEGREE[7] = 148
BASE_ID[7] = 0
ORB_WISE_IDS[7] = []

MEAN_MOTION_REV_PER_DAY[8] = 15.19  # Altitude ~550000 km
ALTITUDE_M[8] = 535  # Altitude ~550000 km
NUM_ORBS[8] = 28
NUM_SATS_PER_ORB[8] = 120
INCLINATION_DEGREE[8] = 53
BASE_ID[8] = 0
ORB_WISE_IDS[8] = []

"""
# TELESAT
NAME = "Telesat"
SHELL_CNTR = 2

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 13.66  # Altitude ~1015 km
ALTITUDE_M[0] = 1015000  # Altitude ~1015 km
NUM_ORBS[0] = 27
NUM_SATS_PER_ORB[0] = 13
INCLINATION_DEGREE[0] = 98.98
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

MEAN_MOTION_REV_PER_DAY[1] = 12.84  # Altitude ~1325 km
ALTITUDE_M[1] = 1325000  # Altitude ~1325 km
NUM_ORBS[1] = 40
NUM_SATS_PER_ORB[1] = 33
INCLINATION_DEGREE[1] = 50.88
BASE_ID[1] = 351
ORB_WISE_IDS[1] = []
"""

"""
# KUIPER
NAME = "kuiper"
################################################################
# The below constants are taken from Kuiper's FCC filing as below:
# [1]: https://www.itu.int/ITU-R/space/asreceived/Publication/DisplayPublication/8716
################################################################

SHELL_CNTR = 3

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 14.80  # Altitude ~630 km
ALTITUDE_M[0] = 630000  # Altitude ~630 km
NUM_ORBS[0] = 34
NUM_SATS_PER_ORB[0] = 34
INCLINATION_DEGREE[0] = 51.9
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

MEAN_MOTION_REV_PER_DAY[1] = 14.86  # Altitude ~610 km
ALTITUDE_M[1] = 610000  # Altitude ~610 km
NUM_ORBS[1] = 36
NUM_SATS_PER_ORB[1] = 36
INCLINATION_DEGREE[1] = 42
BASE_ID[1] = 1156
ORB_WISE_IDS[1] = []

MEAN_MOTION_REV_PER_DAY[2] = 14.93  # Altitude ~590 km
ALTITUDE_M[2] = 590000  # Altitude ~590 km
NUM_ORBS[2] = 28
NUM_SATS_PER_ORB[2] = 28
INCLINATION_DEGREE[2] = 33
BASE_ID[2] = 2452
ORB_WISE_IDS[2] = []
"""


# General files needed to generate visualizations; Do not change for different simulations
topFile = "../static_html/top.html"
bottomFile = "../static_html/bottom.html"

# Output directory for creating visualization html files
OUT_DIR = "../viz_output/"
# JSON_NAME  = NAME+"_5shell.json"
# OUT_JSON_FILE = OUT_DIR + JSON_NAME
OUT_HTML_FILE = OUT_DIR + NAME + ".html"

# START = Time(EPOCH, scale="tdb")
# END = START + (10*60) * u.second
# sample_points = 10
# extractor = CZMLExtractor(START, END, sample_points)


def generate_satellite_trajectories():
    """
    Generates and adds satellite orbits to visualization.
    :return: viz_string
    """
    viz_string = ""
    for i in range(0, SHELL_CNTR):
        sat_objs = util.generate_sat_obj_list(
            NUM_ORBS[i],
            NUM_SATS_PER_ORB[i],
            EPOCH,
            PHASE_DIFF,
            INCLINATION_DEGREE[i],
            ECCENTRICITY,
            ARG_OF_PERIGEE_DEGREE,
            MEAN_MOTION_REV_PER_DAY[i],
            ALTITUDE_M[i]
        )
        for j in range(len(sat_objs)):
            sat_objs[j]["sat_obj"].compute(EPOCH)
            viz_string += "var redSphere = viewer.entities.add({name : '', position: Cesium.Cartesian3.fromDegrees(" \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublong)) + ", " \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublat)) + ", " + str(
                sat_objs[j]["alt_km"] * 1000) + "), " \
                          + "ellipsoid : {radii : new Cesium.Cartesian3(30000.0, 30000.0, 30000.0), " \
                          + "material : Cesium.Color.BLACK.withAlpha(1),}});\n"
        orbit_links = util.find_orbit_links(sat_objs, NUM_ORBS[i], NUM_SATS_PER_ORB[i])
        for key in orbit_links:
            sat1 = orbit_links[key]["sat1"]
            sat2 = orbit_links[key]["sat2"]
            viz_string += "viewer.entities.add({name : '', polyline: { positions: Cesium.Cartesian3.fromDegreesArrayHeights([" \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat1]["alt_km"] * 1000) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat2]["alt_km"] * 1000) + "]), " \
                          + "width: 0.5, arcType: Cesium.ArcType.NONE, " \
                          + "material: new Cesium.PolylineOutlineMaterialProperty({ " \
                          + "color: Cesium.Color."+COLOR[i]+".withAlpha(0.4), outlineWidth: 0, outlineColor: Cesium.Color.BLACK})}});"
    return viz_string


def write_viz_files():
    """
    Writes JSON and TML files to the output folder
    :return: None
    """
    writer_html = open(OUT_HTML_FILE, 'w')
    with open(topFile, 'r') as fi:
        writer_html.write(fi.read())
    writer_html.write(viz_string)
    with open(bottomFile, 'r') as fb:
        writer_html.write(fb.read())
    writer_html.close()


viz_string = generate_satellite_trajectories()
write_viz_files()