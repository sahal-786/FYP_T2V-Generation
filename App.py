from flask import Flask, request, render_template, send_file
from Vid_gen_script import generate_video

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_video', methods=['POST'])
def process_text_prompt():
    text_prompt = request.form['text_prompt']
    video_path = generate_video(text_prompt)
    return video_path

@app.route('/download_video')
def download_video():
    video_path = request.args.get('video_path')
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
