from flask import Flask, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/stream/<video_id>')
def stream_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        stream_url = info.get('url')
        return redirect(stream_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
