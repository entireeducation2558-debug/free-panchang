# app.py - Hindi Panchang Full-Stack Flask Server & REST API
from flask import Flask, send_from_directory, request, jsonify, Response
from datetime import datetime
import os

app = Flask(__name__, static_folder='.')

# Optional Swiss Ephemeris support (works even if pyswisseph is not installed on basic hosts)
try:
    import swisseph as swe
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    HAS_SWE = True
except ImportError:
    HAS_SWE = False

TITHIS_HI = [
    "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पंचमी", "षष्ठी", "सप्तमी", "अष्टमी",
    "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा",
    "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पंचमी", "षष्ठी", "सप्तमी", "अष्टमी",
    "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "अमावस्या"
]

NAKSHATRAS_HI = [
    "अश्विनी", "भरणी", "कृत्तिका", "रोहिणी", "मृगशिरा", "आर्द्रा", "पुनर्वसु", "पुष्य", "आश्लेषा",
    "मघा", "पूर्वाफाल्गुनी", "उत्तराफाल्गुनी", "हस्त", "चित्रा", "स्वाती", "विशाखा", "अनुराधा", "ज्येष्ठा",
    "मूल", "पूर्वाषाढ़ा", "उत्तराषाढ़ा", "श्रवण", "धनिष्ठा", "शतभिषा", "पूर्वभाद्रपद", "उत्तरभाद्रपद", "रेवती"
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return "File not found", 404

@app.route('/api/panchang', methods=['GET'])
def api_panchang():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    if not HAS_SWE:
        return jsonify({
            "status": "frontend_engine_active",
            "date": date_str,
            "message": "Install pyswisseph for server-side ephemeris API."
        })

    dt = datetime.strptime(date_str, '%Y-%m-%d')
    jd = swe.julday(dt.year, dt.month, dt.day, 0.5)
    sun_lon = swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)[0][0]
    moon_lon = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]

    diff = (moon_lon - sun_lon) % 360
    tithi_idx = int(diff // 12)
    paksha = "शुक्ल पक्ष" if tithi_idx < 15 else "कृष्ण पक्ष"
    nak_idx = int(moon_lon // (360 / 27))

    return jsonify({
        "date": date_str,
        "paksha": paksha,
        "tithi": TITHIS_HI[tithi_idx],
        "nakshatra": NAKSHATRAS_HI[nak_idx],
        "ayanamsa": "Lahiri"
    })

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)