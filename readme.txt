Python usage:

python PythonSegmentClusteredNuclei.py data/in data/out 1.5 3

Buiding image:

1) Go to Dockerfile folder
2) Run next command:
docker build -t carlosym1/nuclei_segmentation_python .

Run nuclei_segementation_python within Docker

docker run -t -i nuclei_segmentation_python /bin/bash

Good one:
docker run -v $(pwd):/home/data -t -i carlosym1/nuclei_segmentation_python data/in data/out 1.3 5 