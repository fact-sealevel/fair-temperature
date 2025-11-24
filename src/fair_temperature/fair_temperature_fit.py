import xarray as xr


def fair_fit_temperature(param_file):
    # Load the AR6 calibrated parameters for the FAIR model
    pars = xr.load_dataset(param_file)

    # Save the fit data to a pickle
    output = {"pars": pars, "param_file": param_file}

    return output
