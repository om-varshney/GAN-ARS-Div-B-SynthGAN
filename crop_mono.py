import os
import glob
from pydub import AudioSegment
from tqdm import tqdm


def crop_audio(input_file, output_file, max_duration_ms=10000):
    # Load the audio file
    sound = AudioSegment.from_file(input_file)

    # If the duration is less than or equal to max_duration_ms, keep the audio as it is
    if len(sound) <= max_duration_ms:
        sound.export(output_file, format="wav")
    else:
        # Crop the audio to max_duration_ms
        cropped_sound = sound[:max_duration_ms]
        cropped_sound.export(output_file, format="wav")


# Get list of mono WAV files using glob
wav_files = glob.glob("./mono/**/*.wav", recursive=True)

# Process each WAV file with tqdm progress bar
for file_path in tqdm(wav_files, desc="Cropping WAV files", unit="files"):
    # Construct output directory path in the cropped directory
    output_dir = os.path.join(
        "./cropped", os.path.relpath(os.path.dirname(file_path), "./mono")
    )

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Construct output file path
    output_file = os.path.join(output_dir, os.path.basename(file_path))

    # Crop audio to a maximum duration of 4 seconds
    crop_audio(file_path, output_file, max_duration_ms=4000)
