import sys
import argparse
import xarray as xr


def fair_fit_temperature(param_file):
    # Load the AR6 calibrated parameters for the FAIR model
    pars = xr.load_dataset(param_file)

    # Save the fit data to a pickle
    output = {"pars": pars, "param_file": param_file}

    return output


if __name__ == "__main__":
    # Initialize the command-line argument parser
    parser = argparse.ArgumentParser(
        description="Run the fNumber of years to use as a smoothing window (default=19)it stage for the FAIR AR6 temperature module",
        epilog="Note: This is meant to be run as part of the Framework for the Assessment of Changes To Sea-level (FACTS)",
    )

    # Define the command line arguments to be expected
    parser.add_argument(
        "--pipeline_id",
        help="Unique identifier for this instance of the module",
        required=True,
    )
    parser.add_argument(
        "--param_file",
        help="Full path to FAIR parameter file",
        default="./parameters/fair_ar6_climate_params_v4.0.nc",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Run the code
    fair_fit_temperature(param_file=args.param_file, pipeline_id=args.pipeline_id)

    sys.exit()
