import os
from flask import Flask
from extensions import init_extensions
from routes.auth_routes import auth_bp
from routes.job_routes import job_bp

app = Flask(__name__)

# Set Supabase environment variables
os.environ.setdefault('SUPABASE_URL', 'https://mmwaubrgkbcjhazsjjpm.supabase.co')
if 'SUPABASE_KEY' not in os.environ:
    # Default key for development only - use environment variables in production
    os.environ.setdefault('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1td2F1YnJna2JjamhhenNqanBtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5NDc3NzMsImV4cCI6MjA1NzUyMzc3M30.MgIGlzy8NRtIDkVaGsf3Z21PnRii3UoK_f-s_RHFTOU')

# Initialize extensions (e.g., database, auth, etc.)
init_extensions(app)

# Register Blueprints (Routes)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(job_bp, url_prefix='/api')

# Root route
@app.route('/')
def home():
    return "Welcome to the Job Backend!"

# No need for db.create_all() as we're using Supabase directly

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)