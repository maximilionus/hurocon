def run_cli():
    from .cli_base import cli

    # Initialize CLI modules
    from . import auth, config, device, sms, net, \
        lte  # Deprecated modules on this line

    cli()
