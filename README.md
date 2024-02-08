# Sentiment Analysis and Light Control System

![Example Image](images/lightcontrol.png)

## Overview

This project is a sentiment analysis and light control system that uses speech recognition to analyze the sentiment of spoken words and adjust the color and brightness of lights accordingly. It leverages advanced speech recognition technology and natural language processing techniques to provide somewhat real-time feedback through lighting effects.

## Features

- Somewhat real-time sentiment analysis of spoken words.
- Automatic adjustment of light color and brightness based on sentiment.
- Integrated voice activity detection for efficient speech processing.
- Transcription and sentiment scoring of recorded audio files.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python  3.x
- An API key for the Whisper ASR service
- Philips Hue Bridge and compatible lights

### Installation

Follow these steps to install the project and its dependencies:

1. Clone the repository: `git clone https://github.com/Aekp/MiniProject`
2. Change into the project directory: `cd yourrepository`
3. Install the required Python packages: `pip install -r requirements.txt`

## Usage

To use the system, follow these steps:

1. Run the main script: `python main.py`
2. Speak into the microphone connected to your device.
3. Observe the lights change color and brightness based on the sentiment of your speech.

## Models

### Whisper ASR Model

[Whisper](https://openai.com/research/whisper/) is an automatic speech recognition (ASR) model developed by OpenAI. It's used in this project to convert spoken language into written text.

- **Model Details**: The Whisper model used in this project is the "tiny.en" variant, which is optimized for English speech and is suitable for real-time applications.
- **Usage**: The Whisper ASR model is utilized to transcribe spoken words into text. This text is then analyzed for sentiment using the VADAR NLTK model.

### VADAR NLTK Model

[VADAR](https://www.nltk.org/) is a voice activity detection algorithm implemented in the Natural Language Toolkit (NLTK) library. It's used in conjunction with the Whisper ASR model to identify segments of speech and filter out non-speech sounds.

- **Model Details**: VADAR is a pre-trained model available in the NLTK library. It's used to segment the audio stream into speech and non-speech segments, improving the accuracy of the Whisper ASR model.
- **Usage**: VADAR is applied to the raw audio input before it's processed by the Whisper ASR model. This helps to focus the ASR model on the most relevant parts of the audio stream.



