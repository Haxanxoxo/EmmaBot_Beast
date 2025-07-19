from flask import Flask, render_template_string
import threading
import time

app = Flask(__name__)
lead_count = 0

# 👑 Your Discord ID
discord_id = "emma_austin102"

@app.route('/')
def dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>EmmaBot Beast Dashboard</title>
        <meta http-equiv="refresh" content="2">
        <style>
            body {
                background: #000000;
                color: #39FF14;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            h1 {
                font-size: 36px;
                color: #FF00FF;
                text-shadow: 0px 0px 10px #FF00FF;
            }
            p {
                font-size: 24px;
            }
            .discord {
                font-size: 26px;
                color: #00FFFF;
                text-shadow: 0px 0px 10px #00FFFF;
            }
        </style>
    </head>
    <body>
        <h1>👑 EmmaBot Beast Version</h1>
        <p>📥 Leads Collected: {{lead_count}}</p>
        <p class="discord">🎯 Discord: {{discord_id}}</p>
    </body>
    </html>
    """, lead_count=lead_count, discord_id=discord_id)

# Flask app thread
def run_dashboard():
    app.run(host="0.0.0.0", port=5000)

# EmmaBot loop
def emma_bot():
    global lead_count
    print("👑 EmmaBot Beast is running...")
    while True:
        lead_count += 1
        print(f"📥 Lead Collected: {lead_count}")
        time.sleep(3)

# Start dashboard in thread
threading.Thread(target=run_dashboard).start()
# Start bot
emma_bot()
