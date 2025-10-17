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

# Usage help
if [ "$1" == "--help" ] || [ "$#" != "2" ]; then
  echo "Usage: bash generate_for_paper.sh [id: 0 - 14] [number of threads]"
  exit 0
fi

# Fetch arguments
id="$1"
num_threads=$2

# Check validity of arguments
if [ "${id}" -lt "0" ] || [ "${id}" -gt "14" ]; then
  echo "Invalid workload id: ${id}"
  exit 1
fi
if [ "${num_threads}" -lt "0" ] || [ "${num_threads}" -gt "128" ]; then
  echo "Invalid number of threads: ${num_threads}"
  exit 1
fi

# Print what is being run
echo "Running workload ${id} with ${num_threads} threads"

# Kuiper-610 without ISLS, only ground station relays
if [ "${id}" = "2" ]; then
  python3 deflection_starlink_340_25deg.py 50 100 isls_plus_grid ground_stations_top_100 algorithm_free_gs_one_sat_uplink_downlink_only_over_isls_lasthop_splitting ${num_threads}
fi
# if [ "${id}" = "5" ]; then
#   python3 deflection_kuiper_630.py 200 100 isls_plus_grid ground_stations_top_100 algorithm_free_gs_one_sat_uplink_downlink_only_over_isls_lasthop_splitting ${num_threads}
# fi
# if [ "${id}" = "8" ]; then
#   python3 deflection_telesat_1015.py 200 100 isls_plus_grid ground_stations_top_100 algorithm_free_gs_one_sat_uplink_downlink_only_over_isls_lasthop_splitting ${num_threads}
# fi