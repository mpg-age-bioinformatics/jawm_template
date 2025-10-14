# jawm_template

This is a jawm template module.

Installing jawm:
```
pip install git+ssh://git@github.com/mpg-age-bioinformatics/jawm.git --user
```
For more information on jawm please visit jawm's repo on [GitHub.com](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# download test data
jawm-test -r download

# docker
jawm template.py template -p ./yaml/docker.yaml

# slrum and apptainer
jawm template.py template -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Testing this module on your system's python and jawm installation:
```
jawm-test --python_versions system --jawm_versions local
```
More information on running and developing tests can be found in `./test/README.md`.