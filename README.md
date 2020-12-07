# zipline-docker
configuration for zipline using github codespaces


On initialization run 
```
conda install -c Quantopian zipline
```


## New Instructions

After initializing docker file manually run

```
apt-get install libatlas-base-dev python-dev gfortran pkg-config libfreetype6-dev hdf5-tools
```

```
sudo pip install zipline
```

```
python /usr/local/bin/python3.6
```

 Click Python 3.6.12 as interpreted language


Install ipykernel
```
pip install -U ipykernel
```

```
python3.6 -m pip install -r requirements.txt
```

To register zipline bundles modify `~/.zipline/extension.py`

```bash
cat ~/.zipline/extension.py
```

See https://anaconda.org/Quantopian/zipline

Need to make file /opt/conda/pkgs/urls.txt

```bash
conda install python=3.6.9
conda install -c quantopian zipline
conda env export > environment.yml
```