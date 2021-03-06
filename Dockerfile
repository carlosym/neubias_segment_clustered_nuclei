# Copyright (C) 2017 - Universitat Pompeu Fabra
# Author - Carlos Yagüe Méndez <carlos.yague@upf.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


FROM ubuntu:16.10

MAINTAINER Carlos Yagüe Méndez <carlos.yague@upf.edu>

################################## APT-GET #####################################
RUN apt-get -qq update && apt-get -qq install -y       \
                            python-setuptools \
                            python                                   \
                            python-pip                      \
                            python-numpy                    \
                            python-scipy                            \
                            python-matplotlib                \
                            python-pillow                    \
                            git                              \
                            wget       
#                            && rm -rf /var/lib/apt/lists/*

# 731MB

# RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends       \

RUN pip install --no-cache-dir scikit-image
RUN wget https://raw.githubusercontent.com/carlosym/neubias_segment_clustered_nuclei/master/PythonSegmentClusteredNuclei.py
RUN mv PythonSegmentClusteredNuclei.py /home/nucleisegmentation.py
#COPY  PythonSegmentClusteredNuclei.py /home/nucleisegmentation.py
RUN groupadd -r host && useradd -r -g host host && usermod -u 1000 host
USER host

WORKDIR "/home"

ENTRYPOINT ["python", "/home/nucleisegmentation.py"]
