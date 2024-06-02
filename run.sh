#!/bin/sh

#SBATCH --gpus-per-node=V100:1
#SBATCH -t 01:00:00
export APPTAINERENV_PATH="$PATH"
export APPTAINERENV_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"


apptainer run --nv ./container.sif  python3 src/arvis_tm.py ./../data/cop_merged_original.pkl