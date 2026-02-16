import runpod

try:
    from src.rp_handler import run
except ImportError:
    # In the container image, src files are copied to "/" so rp_handler is top-level.
    from rp_handler import run


def handler(job):
    job_input = job["input"]
    normalized_job = {
        "id": job.get("id", "local-test-job"),
        "input": job_input
    }
    return run(normalized_job)


runpod.serverless.start({"handler": handler})
