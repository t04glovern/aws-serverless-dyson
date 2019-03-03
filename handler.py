from libpurecoollink.dyson import DysonAccount
import os
import json


def stats(event, context):
    # Log to Dyson account
    dyson_account = DysonAccount(os.environ['DYSON_EMAIL'], os.environ['DYSON_PASS'], os.environ['DYSON_LANG'])
    logged = dyson_account.login()

    if not logged:
        body = {
            "message": "Unable to login to Dyson account"
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    # List devices available on the Dyson account
    devices = dyson_account.devices()

    if os.environ['DYSON_ENDPOINT']:
        # Connect using discovery to the first device
        connected = devices[0].connect(os.environ['DYSON_ENDPOINT'])
    else:
        # Connect using discovery to the first device
        connected = devices[0].auto_connect()

    if connected:
        body = {
            "state": devices[0].state.fan_mode,
            "fan_state": devices[0].state.fan_state,
            "night_mode": devices[0].state.night_mode,
            "speed": devices[0].state.speed,
            "oscillation": devices[0].state.oscillation,
            "filter_life": devices[0].state.filter_life,
            "quality_target": devices[0].state.quality_target,
            "standby_monitoring": devices[0].state.standby_monitoring,
            "tilt": devices[0].state.tilt,
            "focus_mode": devices[0].state.focus_mode,
            "heat_mode": devices[0].state.heat_mode,
            "heat_target": devices[0].state.heat_target,
            "heat_state": devices[0].state.heat_state
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        # Disconnect
        devices[0].disconnect()

        return response


def sleep_timer(event, context):
    # Log to Dyson account
    dyson_account = DysonAccount(os.environ['DYSON_EMAIL'], os.environ['DYSON_PASS'], os.environ['DYSON_LANG'])
    logged = dyson_account.login()

    if not logged:
        body = {
            "message": "Unable to login to Dyson account"
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    # List devices available on the Dyson account
    devices = dyson_account.devices()

    if os.environ['DYSON_ENDPOINT']:
        # Connect using discovery to the first device
        connected = devices[0].connect(os.environ['DYSON_ENDPOINT'])
    else:
        # Connect using discovery to the first device
        connected = devices[0].auto_connect()

    if connected:
        timer = event['sleep_timer']
        devices[0].set_configuration(sleep_timer=timer)

        body = {
            "sleep_timer": timer
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        # Disconnect
        devices[0].disconnect()

        return response
