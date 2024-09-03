import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    # extract the emotions to the (still incomplete) output dictionary
    out_dict = formatted_response['emotionPredictions'][0]['emotion']
    # the key of the max score is the value we need to append to the output dictionary
    out_dict['dominant_emotion'] = max(out_dict, key=out_dict.get)
    return out_dict