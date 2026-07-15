from flask import Flask, render_template_string
import os
import platform
import datetime

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to GitHub</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            padding: 50px;
            max-width: 600px;
            width: 90%;
            text-align: center;
        }
        .logo {
            font-size: 80px;
            margin-bottom: 20px;
        }
        h1 {
            color: #24292e;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #586069;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        .info-box {
            background: #f6f8fa;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            text-align: left;
        }
        .info-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #e1e4e8;
        }
        .info-item:last-child {
            border-bottom: none;
        }
        .label {
            color: #586069;
            font-weight: 600;
        }
        .value {
            color: #24292e;
            font-family: 'Courier New', monospace;
        }
        .footer {
            margin-top: 30px;
            color: #586069;
            font-size: 0.9rem;
        }
        .github-icon {
            display: inline-block;
            margin-top: 10px;
        }
        .badge {
            display: inline-block;
            background: #2ea44f;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🐙</div>
        <h1>Welcome to GitHub</h1>
        <p class="subtitle">Your code, your community, your platform</p>
        
        <div class="info-box">
            <div class="info-item">
                <span class="label">🐳 Docker Container</span>
                <span class="value">{{ container_id[:12] }}</span>
            </div>
            <div class="info-item">
                <span class="label">🖥️ Hostname</span>
                <span class="value">{{ hostname }}</span>
            </div>
            <div class="info-item">
                <span class="label">🐍 Python Version</span>
                <span class="value">{{ python_version }}</span>
            </div>
            <div class="info-item">
                <span class="label">📅 Server Time</span>
                <span class="value">{{ server_time }}</span>
            </div>
            <div class="info-item">
                <span class="label">🌍 Platform</span>
                <span class="value">{{ platform }}</span>
            </div>
            <div class="info-item">
                <span class="label">📦 Environment</span>
                <span class="value">{{ environment }}</span>
            </div>
        </div>
        
        <div class="badge">🚀 Deployed with Docker</div>
        
        <div class="footer">
            <p>Powered by Flask & Docker • Made with ❤️</p>
            <p class="github-icon">
                <a href="https://github.com" target="_blank" style="text-decoration: none; color: #24292e;">
                    ⭐ Star on GitHub
                </a>
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def welcome():
    """Main welcome page"""
    return render_template_string(
        HTML_TEMPLATE,
        container_id=os.environ.get('HOSTNAME', 'local'),
        hostname=platform.node(),
        python_version=platform.python_version(),
        server_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        platform=platform.system() + ' ' + platform.release(),
        environment=os.environ.get('ENV', 'development')
    )

@app.route('/health')
def health():
    """Health check endpoint for Docker"""
    return {
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'service': 'welcome-to-github'
    }, 200

@app.route('/info')
def info():
    """System information endpoint"""
    return {
        'container_id': os.environ.get('HOSTNAME', 'unknown'),
        'hostname': platform.node(),
        'python_version': platform.python_version(),
        'platform': platform.platform(),
        'environment': os.environ.get('ENV', 'development')
    }

if __name__ == '__main__':
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    app.run(
        host='0.0.0.0',  # Listen on all interfaces
        port=port,
        debug=os.environ.get('DEBUG', 'False').lower() == 'true'
    )