import os
import glob
from tqdm import tqdm
from pydub import AudioSegment


def convert_midi_to_wav(midi_file, output_dir):
    # Construct output directory based on input directory structure
    rel_path = os.path.relpath(os.path.dirname(midi_file), start='data')
    output_subdir = os.path.join(output_dir, rel_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_subdir, exist_ok=True)

    # Construct output WAV filename
    wav_file = os.path.join(output_subdir, os.path.basename(midi_file).replace('.mid', '.wav'))

    ffmpeg_command = f'ffmpeg -y -i "{midi_file}" -vn -acodec pcm_s16le "{wav_file}" 2>NUL'  # use ffmpeg -y means
    # override any files -i means input file -vn means ignore video data use the pcm_s16le audio codec for the
    # conversion and save the output to specified file and 2>NUL means redirect standard error to NUL essentially
    # silencing the error output which comes with using ffmpeg. 2>NUL ensures that my tqdm bar is visible.

    # Convert MIDI to WAV using ffmpeg
    os.system(ffmpeg_command)


# Define glob pattern for MIDI files
pattern = './data/**/*.mid'

# Get list of MIDI files matching the pattern
midi_files = glob.glob(pattern, recursive=True)

# Define output directory for WAV files
output_dir = './wav/'

# Iterate through MIDI files and convert to WAV
for midi_file in tqdm(midi_files, desc='Converting MIDI to WAV', unit='file'):
    convert_midi_to_wav(midi_file, output_dir)
