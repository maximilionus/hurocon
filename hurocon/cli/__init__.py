def run_cli():
    from .__cli_base__ import cli

    # Initialize CLI modules
    from . import auth, config, device, sms, lte, net

    cli()
