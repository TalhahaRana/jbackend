from flask import Blueprint, request, jsonify

job_bp = Blueprint('job', __name__)

# Temporary in-memory storage for jobs (replace with a database later)
jobs = []

# Get all jobs
@job_bp.route('/', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

# Get a specific job by ID
@job_bp.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        return jsonify(job)
    return jsonify({"error": "Job not found"}), 404

# Create a new job
@job_bp.route('/', methods=['POST'])
def create_job():
    new_job = request.json
    new_job['id'] = len(jobs) + 1  # Assign a unique ID
    jobs.append(new_job)
    return jsonify(new_job), 201

# Update an existing job
@job_bp.route('/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    updated_data = request.json
    job.update(updated_data)
    return jsonify(job)

# Delete a job
@job_bp.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    global jobs
    jobs = [job for job in jobs if job['id'] != job_id]
    return jsonify({"message": "Job deleted"}), 200