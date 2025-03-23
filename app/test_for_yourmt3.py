import requests
'''torch.cuda.empty_cache()
print(transformers.__version__)
mp3_file_path = "test_files/late-night-big-band-swing-jazz-instrumental-236168.mp3"
midi = transcribe.transcribe(mp3_file_path)
print(midi)'''

if __name__ == "__main__":

    # Define the file path of the MP3 file you want to send
    mp3_file_path = "test_files/late-night-big-band-swing-jazz-instrumental-236168.mp3"  # Ensure the correct path format

    # Define the endpoint URL
    url = "http://localhost:8000/transcribe"  # Ensure this matches where your FastAPI app is hosted

    # Open the MP3 file in binary mode and send it in a POST request
    with open(mp3_file_path, 'rb') as mp3_file:
        files = {'mp3_file': (mp3_file_path, mp3_file, 'audio/mpeg')}
        response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print("Transcription successful!")
        
        # Check the content type to handle different responses
        content_type = response.headers.get('Content-Type')

        if 'application/json' in content_type:
            # Handle JSON response
            print(response.json())  # Example of processing a JSON response
        elif 'audio/midi' in content_type:
            # Handle MIDI file response
            midi_filename = "output.midi"
            with open(midi_filename, "wb") as midi_file:
                midi_file.write(response.content)
            print(f"MIDI file saved as '{midi_filename}'")
        else:
            print("Unknown content type:", content_type)
            
    else:
        print("Request failed with status code:", response.status_code)
        print(response.text)  # Details of the failure