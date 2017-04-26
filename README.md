# neubias_segment_clustered_nuclei

Github repository:
https://github.com/carlosym/neubias_segment_clustered_nuclei

The volume mounted within the docker should have two folders called in and out, within in we will put all the input images to process and the out folder will contain the output of the algorithm.

Example: Volume (File system folder)
Data
 |__in
 |__out

Run command:
docker run -v $(pwd):/home/data -t -i carlosym1/nuclei_segmentation_python data/in data/out 1.3 5 