# jawm Template

This is a jawm template module.

Installing jawm:
```
pip install git+ssh://git@github.com/mpg-age-bioinformatics/jawm.git
```
For more information on jawm please visit jawm's repo on [GitHub.com](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# download test data
jawm-test -r download

# docker
jawm template.py _template -p ./yaml/docker.yaml

# slrum and apptainer
jawm template.py _template -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Additional jawm workflows are available [here (GitHub.com)](https://github.com/mpg-age-bioinformatics?q=jawm_&type=all&language=&sort=).
