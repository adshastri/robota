# Robota

Built at TechCrunch Disrupt New York 2017

## Brief description
The robot's camera recognizes looks for and recognizes a face, prompts for speech, transcribes, analyzes for sentiment, and notifies the teacher.

It is not properly configured for movement around a classroom, identifying individuals, or determining facial expressions due to time constraints at the hackathon.

### Notes:
* The API keys and Auth tokens are hidden.
* The server side code was written with Pubnub Blocks, which offers a different than traditional RESTful services. For this reason, the format of the callback function is different from a standard express.js function.
