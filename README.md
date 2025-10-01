# jawm_template

This is a jawm template module.

For more information on jawm please visit [jawm's repo](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# docker
jawm template.py template -p ./yaml/docker.yaml

# slrum and apptainer
jawm template.py template -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Running tests:
```
jawm-dev test
```