import whisper
import config
import os, glob
import time
import sys
sys.path.insert(0, '/Users/astridpedersen/Desktop/python-test/MiniProject/sentiment.py')

import sentiment # Import the sentiment analysis script
import hue_controller # Import the Philips Hue controller script

# Define color coordinates in the CIE   1931 color space
RED = [0.675,   0.322]  # Red color
GREEN = [0.409,   0.518]  # Green color
NEUTRAL = [0.3127,   0.3290]  # Neutral white color

# Function to map sentiment to color and brightness
def map_sentiment_to_color_and_brightness(sentiment_score):
    max_brightness =  254  # Maximum brightness level
    min_brightness =  100  # Minimum brightness level (adjust as needed)

    # Calculate the brightness based on the sentiment score
    if sentiment_score <  0:  # Negative sentiment
        # Assuming a higher absolute value of sentiment_score indicates stronger negative sentiment
        # We map the absolute value of sentiment_score to the range between min_brightness and max_brightness
        brightness = int((abs(sentiment_score) * (max_brightness - min_brightness)) + min_brightness)
        return RED, brightness
    elif sentiment_score >  0:  # Positive sentiment
        # Similarly, we map the positive sentiment_score to the range between min_brightness and max_brightness
        brightness = int((sentiment_score * (max_brightness - min_brightness)) + min_brightness)
        return GREEN, brightness
    else:  # Neutral sentiment
        return NEUTRAL, min_brightness  # Use minimum brightness for neutral sentiment

# find all files in a directory
recordings_dir = os.path.join('recordings', '*')

# Use the base model ~1 GB ~16x
model = whisper.load_model("tiny.en")

# list to store which wav files have been transcribed
transcribed = []

while True:
    # get all wav recordings in the recordings directory
    files = sorted(glob.iglob(recordings_dir), key=os.path.getctime, reverse=True)
    for file in files:
        if os.path.exists(file) and not file in transcribed:
            audio = whisper.load_audio(file)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(model.device)
            options = whisper.DecodingOptions(language= 'en', fp16=False)

            result = whisper.decode(model, mel, options)

            if result.no_speech_prob < 0.5:
                print(result.text)

                # Analyze sentiment of the transcribed text
                sentiment_scores = sentiment.analyze_sentiment(result.text)
                print(sentiment_scores)

                 # Map sentiment to color and brightness
                color, brightness = map_sentiment_to_color_and_brightness(sentiment_scores['compound'])
                print(f"Color: {color}, Brightness: {brightness}")  # Corrected print statement

                 # Set light color and brightness based on sentiment
                light_id =   1  # Replace with your light ID
                hue_controller.set_all_lights_color_and_brightness(*color, brightness)

                # append text to transcript file
                with open(config.TRANSCRIPT_FILE, 'a') as f:
                    f.write(result.text + '\n')
                    f.write(str(sentiment_scores) + '\n')
                
                # save list of transcribed recordings so that we don't transcribe the same one again
                transcribed.append(file) 

                # delete the file after transcription (Havent been tested!)
                os.remove(file)

  
