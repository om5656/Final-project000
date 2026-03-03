def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 400 or not text_to_analyze.strip():
        return {'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None}

    result = json.loads(response.text)
    emotions = {k: v for k, v in result['document']['emotion'].items()
                if k in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
    dominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant
    return emotions
