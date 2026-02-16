import runpod

def handler(job):
    job_input = job["input"]
    normalized_job = {"id": job.get("id", "local-test-job"), "input": job_input}

    try:
        from src.rp_handler import run
    except ImportError:
        # In container images using `COPY src .`, rp_handler is top-level.
        from rp_handler import run

    return run(normalized_job)


runpod.serverless.start({"handler": handler})
