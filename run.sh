#!/bin/sh

#SBATCH --gpus-per-node=V100:1
#SBATCH -t 01:00:00

module load GCC/11.2.0

export APPTAINERENV_PATH="$PATH"
export APPTAINERENV_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"


apptainer run --nv ./container.sif gcc python3 src/arvis_tm.py ./../data/cop_merged_original.pkl