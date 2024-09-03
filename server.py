'''Initiate the app to be executed over the Flask channel 
and deployed on localhost:5000'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    '''Run emotion detection on text from html request'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    split_response = str(response).replace('{','').replace('}','').split(",")
    str_out = "For the given statement, the system response is "
    str_out = str_out + ','.join(split_response[:-2])
    str_out = str_out + ' and ' + split_response[-2]
    str_out = str_out + '. The dominant emotion is '
    str_out = str_out + f"<b>{response['dominant_emotion']}.</b>"
    return str_out

@app.route("/")
def render_index_page():
    '''Render the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
