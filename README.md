# fair-temperature

Application wrapping the FAIR climate model emulator to generate samples of global mean surface air temperature and ocean heat content under prescribed emissions trajectories.

> [!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example

First, create a new directory, download required input data and prepare for the run, like

```shell

# Input data we will pass to the container
mkdir -p ./data/input
curl -sL https://zenodo.org/record/7478192/files/fair_temperature_fit_data.tgz | tar -zx -C ./data/input
curl -sL https://zenodo.org/record/7478192/files/fair_temperature_preprocess_data.tgz | tar -zx -C ./data/input

# Output projections will appear here
mkdir -p ./data/output
```
Now run the container, for example with Docker, like

```shell
docker run --rm \
  -v ./data:/data \
  fair-temperature:dev \
  --pipeline-id=1234 \
  --output-oceantemp-file="/data/output/oceantemp.nc" \
  --output-ohc-file="/data/output/ohc.nc" \
  --output-gsat-file="/data/output/gsat.nc" \
  --output-climate-file="/data/output/climate.nc" \
  --rcmip-file="/data/input/rcmip/rcmip-emissions-annual-means-v5-1-0.csv" \
  --param-file="/data/input/parameters/fair_ar6_climate_params_v4.0.nc"
```

## Features

Several options and configurations are available when running the container.

```
Usage: fair-temperature [OPTIONS]

Options:
  --pipeline-id TEXT            Unique identifier for this instance of the
                                module  [required]
  --output-oceantemp-file TEXT  Path to write output ocean temperature file
                                [required]
  --output-ohc-file TEXT        Path to write output ocean heat content file
                                [required]
  --output-gsat-file TEXT       Path to write output global mean surface air
                                temperature file  [required]
  --output-climate-file TEXT    Path to write output climate file  [required]
  --rcmip-file TEXT             Full path to RCMIP emissions file  [required]
  --param-file TEXT             Full path to FAIR parameter file  [required]
  --scenario TEXT               SSP Emissions scenario
  --nsamps INTEGER              Number of samples to create (uses replacement
                                if nsamps > n parameters) (default=10)
  --seed INTEGER                Seed value for random number generator.
  --cyear-start INTEGER         Start year of temporal range for centering
                                (default=1850)
  --cyear-end INTEGER           End year of temporal range for centering
                                (default=1900)
  --smooth-win INTEGER          Number of years to use as a smoothing window
                                (default=19)
  --help                        Show this message and exit.
```

See this help documentation by running:

```shell
docker run --rm ghcr.io/stcaf-org/fair-temperature:0.1.0 --help
```

These options and configurations can also be set with environment variables prefixed by `FAIR_TEMPERATURE_*`. For example, set `--rcmip-file` with as an environment variable with `FAIR_TEMPERATURE_RCMIP_FILE`.

## Building the container locally

You can build the container with Docker by cloning the repository locally and then running

```shell
docker build -t fair-temperature:dev .
```
from the repository root.

## Support

Source code is available online at https://github.com/stcaf-org/fair-temperature. This software is open source and available under the MIT license.

Please file issues in the issue tracker at https://github.com/stcaf-org/fair-temperature/issues.
