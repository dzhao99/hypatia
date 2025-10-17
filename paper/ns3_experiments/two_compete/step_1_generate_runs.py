# The MIT License (MIT)
#
# Copyright (c) 2020 ETH Zurich
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

import exputil
import networkload

local_shell = exputil.LocalShell()

# Clean-up for new a fresh run
local_shell.remove_force_recursive("runs")
local_shell.remove_force_recursive("pdf")
local_shell.remove_force_recursive("data")

for movement in ["static", "moving"]:

    # Prepare run directory
    run_dir = "runs/run_two_kuiper_isls_" + movement
    local_shell.remove_force_recursive(run_dir)
    local_shell.make_full_dir(run_dir)

    # config_ns3.properties
    local_shell.copy_file("templates/template_config_ns3.properties", run_dir + "/config_ns3.properties")
    local_shell.sed_replace_in_file_plain(
        run_dir + "/config_ns3.properties",
        "[SATELLITE-NETWORK-FORCE-STATIC]",
        "true" if movement == "static" else "false"
    )

    # Make logs_ns3 already for console.txt mapping
    local_shell.make_full_dir(run_dir + "/logs_ns3")

    # .gitignore (legacy reasons)
    local_shell.write_file(run_dir + "/.gitignore", "logs_ns3")

    # From-to list
    # list_from_to = [(1160, 1161), (1166, 1167), (1192, 1193), (1217, 1216)]
    # list_from_to = [(1166, 1167), (1160, 1161)]
    # list_from_to = [(1167,1166), (1161, 1160)]
    # list_from_to = [(1241, 1199), (1158, 1159)]
    # list_from_to = [(1217, 1216), (1166, 1167)]
    # list_from_to = [(1160, 1161), (1192, 1193), (1217, 1216), (1176, 1177), (1228, 1229)]
    # list_from_to = [(1244, 1245), (1196, 1197), (1218, 1219), (1232, 1233), (1214, 1215), (1238, 1239),
    #                 (1202, 1203), (1252, 1253), (1162, 1163), (1234, 1235), (1172, 1173), (1199, 1241),
    #                 (1221, 1220), (1178, 1179), (1226, 1227), (1182, 1183), (1176, 1177), (1248, 1249),
    #                 (1246, 1247), (1166, 1167), (1190, 1191), (1210, 1211), (1164, 1165), (1224, 1225),
    #                 (1230, 1231), (1180, 1254), (1208, 1209), (1170, 1171), (1204, 1205), (1156, 1157),
    #                 (1236, 1237), (1212, 1213), (1194, 1195)]
    # list_from_to = [(1160, 1161), (1192, 1193), (1217, 1216), (1223, 1222), (1158, 1159), (1251, 1250), (1174, 1175),
    #                 (1198, 1240), (1188, 1189), (1186, 1187), (1201, 1200), (1228, 1229)]
    # list_from_to = [(1160, 1161), (1192, 1193), (1217, 1216), (1223, 1222), (1158, 1159), (1251, 1250), (1174, 1175),
    #                 (1198, 1240), (1188, 1189)]

    list_from_to = [(1156, 1157)]

    list_from_to = list_from_to * 20

    # Log all flows
    local_shell.sed_replace_in_file_plain(
        run_dir + "/config_ns3.properties",
        "[FLOW-LOG-SET]",
        ",".join(list(map(lambda x: str(x), range(len(list_from_to)))))
    )

    # Write the schedule
    networkload.write_schedule(
        run_dir + "/schedule_kuiper_630.csv",
        len(list_from_to),
        list_from_to,
        [1000000000000] * len(list_from_to),
        [0] * len(list_from_to)
    )

# Finished successfully
print("Success")
