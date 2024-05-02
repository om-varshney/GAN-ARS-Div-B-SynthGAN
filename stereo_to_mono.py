import os
import glob
from pydub import AudioSegment
from tqdm import tqdm


def stereo_to_mono(input_file, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the stereo audio file
    sound = AudioSegment.from_file(input_file)

    # Convert stereo to mono
    mono_sound = sound.set_channels(1)

    # Construct output file path
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    # Export the mono audio to a file
    mono_sound.export(output_file, format="wav")


# Get list of stereo WAV files using glob
wav_files = glob.glob('./wav/**/*.wav', recursive=True)

# Process each WAV file with tqdm progress bar
for file_path in tqdm(wav_files, desc="Processing WAV files", unit="file"):
    # Construct output directory path
    output_dir = os.path.join('./mono', os.path.dirname(os.path.relpath(file_path, './wav')))
    # Split channels and save as mono WAV files
    stereo_to_mono(file_path, output_dir)
