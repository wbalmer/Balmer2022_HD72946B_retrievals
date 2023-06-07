# Atmospheric retrieval scripts for Balmer et al. 2022a (in prep.)

This code will reproduce the ```petitRADTRANS``` spectral retrievals presented in the paper, and the repository hosts the necessary data (the observations) used in the paper. The code requires the ```species``` package, and the retrievals are computationally intensive.

The scripts must be run in order, first ```HD72946B_init_species.py```, then ```HD72946B_final_retrieval_comparison.py```, and then ```HD72946B_final_retrieval_figures.py```. 
