import os
import subprocess

# Path to your video folder
video_dir = "/data/home/zy3023/code/zhengdiyu.github.io/NRMF/static/videos"

# List of video filenames to fix
video_files = [
    "noisy.mp4",
    "part.mp4",
    # Add more if needed
]

# Output filenames (you can change this to overwrite originals)
def fixed_name(name): return name.replace(".mp4", "_fixed.mp4")

for video in video_files:
    input_path = os.path.join(video_dir, video)
    output_path = os.path.join(video_dir, fixed_name(video))

    command = [
        "ffmpeg",
        "-y",  # overwrite output file if exists
        "-i", input_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-vf", "scale=iw:ih",
        "-an",  # remove audio, or replace with "-c:a aac -b:a 128k" to keep/add audio
        output_path
    ]

    print(f"Processing {video}...")
    subprocess.run(command, check=True)

print("✅ All videos fixed for HTML5 embedding.")
