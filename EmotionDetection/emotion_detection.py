import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    if response.status_code == 200:

        emotion_predictions=formatted_response['emotionPredictions'][0]['emotion']

        anger_score=formatted_response['emotionPredictions'][0]['emotion']['anger']

        disgust_score=formatted_response['emotionPredictions'][0]['emotion']['disgust']
        
        fear_score=formatted_response['emotionPredictions'][0]['emotion']['fear']

        joy_score=formatted_response['emotionPredictions'][0]['emotion']['joy']

        sadness_score=formatted_response['emotionPredictions'][0]['emotion']['sadness']

        dominant_emotion=max(emotion_predictions,key=emotion_predictions.get)
    
    elif response.status_code == 400:

        anger_score=None

        disgust_score=None
        
        fear_score=None

        joy_score=None

        sadness_score=None 

        dominant_emotion=None


    # Returning a dictionary containing sentiment analysis results
    return {'anger':anger_score,
    'disgust':disgust_score,
    'fear': fear_score,
    'joy':joy_score,
    'sadness':sadness_score,
    'dominant_emotion':dominant_emotion
    }


