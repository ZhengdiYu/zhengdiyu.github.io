import os
import subprocess
import json

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

def get_video_info(video_path):
    """Get video dimensions and other info"""
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        video_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        video_stream = next((s for s in data['streams'] if s['codec_type'] == 'video'), None)
        if video_stream:
            return {
                'width': int(video_stream['width']),
                'height': int(video_stream['height'])
            }
    except:
        pass
    return None

def detect_crop_parameters(video_path):
    """Detect crop parameters to remove black borders"""
    # Use cropdetect filter to find the optimal crop area
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", "cropdetect=mode=mvedges:round=1",
        "-f", "null",
        "-"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Parse the output to find crop parameters
        lines = result.stderr.split('\n')
        for line in lines:
            if 'crop=' in line:
                # Extract crop parameters from the line
                crop_part = line.split('crop=')[1].split()[0]
                return crop_part
    except:
        pass
    
    # Fallback: return a conservative crop
    return "iw-100:ih-100:50:50"

for video in video_files:
    input_path = os.path.join(video_dir, video)
    output_path = os.path.join(video_dir, fixed_name(video))
    
    # Detect crop parameters
    crop_params = detect_crop_parameters(input_path)
    print(f"Detected crop parameters for {video}: {crop_params}")

    command = [
        "ffmpeg",
        "-y",  # overwrite output file if exists
        "-i", input_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-vf", f"crop={crop_params}",
        "-an",  # remove audio, or replace with "-c:a aac -b:a 128k" to keep/add audio
        output_path
    ]

    print(f"Processing {video}...")
    try:
        subprocess.run(command, check=True)
        print(f"✅ Successfully processed {video}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error processing {video}: {e}")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install FFmpeg first.")

print("✅ All videos processed for HTML5 embedding.")
