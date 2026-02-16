import runpod

from rp_handler import run


def handler(event):
    return run(event)


runpod.serverless.start({"handler": handler})
