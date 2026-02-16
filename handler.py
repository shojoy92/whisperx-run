import runpod

from rp_handler import run


runpod.serverless.start({"handler": run})
