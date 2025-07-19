from flask import Flask
import threading

app = Flask(__name__)
lead_count = 0

@app.route('/')
def dashboard():
    return f"""
    <html>
      <head>
        <title>EmmaBot Admin Dashboard</title>
        <meta http-equiv="refresh" content="2">
        <style>
          body {{
            background: #1e1e1e;
            color: #00ff00;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
          }}
          h1 {{
            font-size: 36px;
          }}
          p {{
            font-size: 24px;
          }}
        </style>
      </head>
      <body>
        <h1>👑 EmmaBot Admin Dashboard</h1>
        <p>📥 Leads Collected: {lead_count}</p>
      </body>
    </html>
    """

@app.route('/update_leads')
def update_leads():
    global lead_count
    lead_count += 1
    print(f"Lead Collected: {lead_count}")
    return "Lead Added"

def run_dashboard():
    app.run(host="0.0.0.0", port=5000)

# Start Flask server in a separate thread
threading.Thread(target=run_dashboard).start()
