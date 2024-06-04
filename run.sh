#!/usr/bin/env bash
#SBATCH -A NAISS2024-22-128 -p alvis
#SBATCH --gpus-per-node=V100:1
#SBATCH -t 01:00:00

export LD_LIBRARY_PATH=/apps/Arch/software/Python/3.11.5-GCCcore-13.2.0/lib:"$LD_LIBRARY_PATH"

# Load all your needed modules
ml SciPy-bundle/2023.07-gfbf-2023a

source /mimer/NOBACKUP/groups/it-gov-data/alessio/my_venv/bin/activate



python src/arvis_tm.py ./../data/cop_merged_original.pkl