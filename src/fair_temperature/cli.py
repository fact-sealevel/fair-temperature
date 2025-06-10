import click

from fair_temperature.fair_temperature_preprocess import fair_preprocess_temperature
from fair_temperature.fair_temperature_fit import fair_fit_temperature
from fair_temperature.fair_temperature_project import fair_project_temperature


@click.command()
@click.option(
    "--pipeline-id",
    envvar="FAIR_TEMPERATURE_PIPELINE_ID",
    help="Unique identifier for this instance of the module",
    required=True,
)
@click.option(
    "--rcmip-file",
    envvar="FAIR_TEMPERATURE_RCMIP_FILE",
    help="Full path to RCMIP emissions file",
    type=str,
    required=True,
)
@click.option(
    "--param-file",
    envvar="FAIR_TEMPERATURE_PARAM_FILE",
    help="Full path to FAIR parameter file",
    type=str,
    required=True,
)
@click.option(
    "--scenario",
    envvar="FAIR_TEMPERATURE_SCENARIO",
    help="SSP Emissions scenario",
    default="ssp585",
)
@click.option(
    "--nsamps",
    envvar="FAIR_TEMPERATURE_NSAMPS",
    help="Number of samples to create (uses replacement if nsamps > n parameters) (default=10)",
    default=10,
)
@click.option(
    "--seed",
    envvar="FAIR_TEMPERATURE_SEED",
    help="Seed value for random number generator.",
    default=1234,
)
@click.option(
    "--cyear-start",
    envvar="FAIR_TEMPERATURE_CYEAR_START",
    help="Start year of temporal range for centering (default=1850)",
    default=1850,
)
@click.option(
    "--cyear-end",
    envvar="FAIR_TEMPERATURE_CYEAR_END",
    help="End year of temporal range for centering (default=1900)",
    default=1900,
)
@click.option(
    "--smooth-win",
    envvar="FAIR_TEMPERATURE_SMOOTH_WIN",
    help="Number of years to use as a smoothing window (default=19)",
    default=19,
)
def main(
    pipeline_id,
    rcmip_file,
    param_file,
    scenario,
    nsamps,
    seed,
    cyear_start,
    cyear_end,
    smooth_win,
) -> None:
    click.echo("Hello from fair-temperature!")

    fair_preprocess_temperature(pipeline_id, rcmip_file, scenario)
    fair_fit_temperature(param_file, pipeline_id)
    fair_project_temperature(
        nsamps, seed, cyear_start, cyear_end, smooth_win, pipeline_id
    )
