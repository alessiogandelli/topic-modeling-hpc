# topic-modeling-hpc
files required to run the topic modeling on the gpu cluster alvis, using apptainer



``` bash
apptainer build container.sif recipe.def
```


``` bash
module load virtualenv/20.23.1-GCCcore-12.3.0 matplotlib/3.7.2-gfbf-2023a SciPy-bundle/2023.07-gfbf-2023a h5py/3.9.0-foss-2023a

virtualenv --system-site-packages my_venv

source my_venv/bin/activate

pip install quel che devi 

# you need this for jupyter
pip install ipykernel
pip install jupyter


python -m ipykernel install --user --name=my_venv --display-name="il mio pitonone"

``` 
