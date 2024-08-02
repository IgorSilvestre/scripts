import sys
import subprocess


def reduce_video_size(input_path: str, output_path: str, target_width: int = 640):
    # Command to resize the video using ffmpeg
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={target_width}:-2',
        '-c:v', 'libx264',
        '-preset', 'slow',
        '-b:v', '500k',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y',  # Overwrite output file if it exists
        output_path
    ]

    # Execute the command
    subprocess.run(command, check=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compress_video.py <input_path> <output_path>")
    else:
        input_video = sys.argv[1]
        output_video = sys.argv[2]
        reduce_video_size(input_video, output_video)
