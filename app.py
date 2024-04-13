from flask import Flask, render_template, request, redirect, url_for
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_link = request.form['video_link']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output template for the downloaded file
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_link, download=False)
        title = info_dict.get('title', 'Video')
    return render_template('download.html', title=title)

@app.route('/download_video', methods=['POST'])
def download_video():
    video_link = request.form['video_link']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output template for the downloaded file
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
