# python speech-to-text.py /path/to/file.wav --api_key <API_KEY>
import argparse
from openai import OpenAI


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using OpenAI's Whisper model."
    )
    parser.add_argument(
        'file_path', type=str, help='Path to the audio file'
    )
    parser.add_argument(
        '--api_key', type=str, required=True, help='OpenAI API key'
    )

    # Parse arguments
    args = parser.parse_args()

    # Initialize OpenAI client with the provided API key
    client = OpenAI(api_key=args.api_key)

    # Open the audio file
    try:
        with open(args.file_path, "rb") as audio_file:
            # Create the transcription
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        # Print the transcription
        print(transcription.text)
    except Exception as e:
        print(f"Error during transcription: {e}")


if __name__ == "__main__":
    main()

