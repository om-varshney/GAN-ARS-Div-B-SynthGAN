import os
import glob
from pydub import AudioSegment
from tqdm import tqdm

# Define the target sampling rate
target_sr = 16000  # 16 kHz

# Define the input directory using glob pattern
input_pattern = "./cropped/**/*.wav"

# Define the output directory for resampled files
output_dir = "./resampled"

# Make sure the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all WAV files matching the input pattern
input_files = glob.glob(input_pattern, recursive=True)

# Iterate through each WAV file
for input_file in tqdm(input_files, desc="Resampling", unit="files"):
    # Construct the output file path by replacing the input directory with the output directory
    output_file = os.path.join(output_dir, os.path.relpath(input_file, start="./cropped"))

    # Make sure the directory structure exists in the output directory
    output_file_dir = os.path.dirname(output_file)
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)

    # Load audio with pydub
    audio = AudioSegment.from_file(input_file)

    # Resample audio
    audio = audio.set_frame_rate(target_sr)

    # Save resampled audio
    audio.export(output_file, format="wav")
