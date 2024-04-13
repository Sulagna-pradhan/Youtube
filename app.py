# app.py

from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_link = request.form['video_link']
    
    try:
        yt = YouTube(video_link)
        streams = yt.streams.filter(progressive=True)
        return render_template('download.html', streams=streams)
    except VideoUnavailable:
        return "Video is unavailable. Please try another video link."

@app.route('/download_video', methods=['POST'])
def download_video():
    video_link = request.form['video_link']
    selected_stream = request.form['selected_stream']
    
    try:
        yt = YouTube(video_link)
        stream = yt.streams.get_by_itag(selected_stream)
        stream.download()
        return redirect(url_for('index'))
    except VideoUnavailable:
        return "Video is unavailable. Please try another video link."

if __name__ == '__main__':
    app.run(debug=True)
