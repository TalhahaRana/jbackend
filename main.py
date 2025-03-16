from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for specific origins
CORS(app, origins=[
    "http://localhost:3000",  # Local development
    "https://job-frontend-blond.vercel.app"  # Vercel frontend
])

# Temporary in-memory storage for jobs
jobs = []

# Root route
@app.route('/')
def home():
    return "Welcome to the Job Backend!"

# Get all jobs
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

# Create a new job
@app.route('/api/jobs', methods=['POST'])
def create_job():
    new_job = request.json
    new_job['id'] = len(jobs) + 1  # Assign a unique ID
    jobs.append(new_job)
    return jsonify(new_job), 201

# Update an existing job
@app.route('/api/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    updated_data = request.json
    job.update(updated_data)
    return jsonify(job)

# Delete a job
@app.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    global jobs
    jobs = [job for job in jobs if job['id'] != job_id]
    return jsonify({"message": "Job deleted"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)