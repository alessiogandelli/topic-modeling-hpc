ml purge  # Ensure we don't have any conflicting modules loaded

# Load all your needed modules
ml TensorFlow/2.11.0-foss-2022a-CUDA-11.7.0 PyTorch/1.11.0-foss-2022a-CUDA-11.7.0 matplotlib/3.5.2-foss-2022a
ml JupyterLab/3.5.0-GCCcore-11.3.0 

# Activate your virtual environment if needed
# source path/to/your/venv/bin/activate

# You can launch jupyter notebook or lab, but you must specify the config file as below: 
jupyter lab --config="${CONFIG_FILE}"