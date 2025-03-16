from flask import Blueprint

job_bp = Blueprint('job', __name__)

@job_bp.route('/', methods=['GET'])
def get_jobs():
    return "Get all jobs"

@job_bp.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
    return f"Get job with ID {job_id}"