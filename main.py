from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# 1. Morning Greetings & Islamic Reminders
def get_islamic_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Assalam-o-Alaikum! Alhamdulillah parhein aur Allah ka shukar ada karein."
    return "Allah Behtar Karega, Mayos Na Hon."

# 2. Main Execution Logic
@app.route('/execute/<feature>')
def execute_feature(feature):
    if feature == 'gdrive_lock':
        # Agar user subscription expire ho jaye
        return jsonify({"message": "G-Drive Locked! Data access revoked for non-premium users."})
    
    elif feature == 'capcut':
        return jsonify({"message": "CapCut Dubbing & Auto-Subtitles are now ACTIVE."})
    
    elif feature == 'quran':
        return jsonify({"message": "Opening Quran with Tajweed (Taj Company). Raat ko soney ki duayein zaroor parhein."})
    
    elif feature == 'surveillance':
        return jsonify({"message": "Ghost Mode Active. Privacy level set to Ultra-Strict."})

    return jsonify({"message": "Feature not found."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
