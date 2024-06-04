ml purge  # Ensure we don't have any conflicting modules loaded

# this fixes the issue with the libstdc++ version
export LD_LIBRARY_PATH=/apps/Arch/software/Python/3.11.5-GCCcore-13.2.0/lib:$LD_LIBRARY_PATH

# Load all your needed modules
ml SciPy-bundle/2023.07-gfbf-2023a
ml JupyterLab/4.0.5-GCCcore-12.3.0

# Activate your virtual environment if needed
# source path/to/your/venv/bin/activate

# You can launch jupyter notebook or lab, but you must specify the config file as below: 
jupyter lab --config="${CONFIG_FILE}"