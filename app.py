from flask import Flask, jsonify, request
from itertools import islice
from youtube_comment_downloader import *

app = Flask(__name__)


@app.route('/comments/<video_id>')
def get_comments(video_id):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(
        f'https://www.youtube.com/watch?v={video_id}', sort_by=SORT_BY_POPULAR)
    top_comments = list(islice(comments, 20))
    return jsonify(top_comments)


if __name__ == '__main__':
    app.run(debug=True)
