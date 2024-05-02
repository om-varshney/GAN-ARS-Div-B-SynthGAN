import numpy as np
import tensorflow as tf
from pydub import AudioSegment
import uuid

# Load the generator model
generator = tf.keras.models.load_model('generator_model')

# Define latent dimension
latent_dim = 100

# Number of inference passes
num_passes = 5

# Generate audio for multiple passes
for i in range(num_passes):
    # Generate latent noise vector
    z = np.random.normal(0, 1, (1, latent_dim))

    # Generate audio
    generated_audio = generator.predict(z) * 10e4

    # Convert audio to appropriate format
    audio_segment = AudioSegment(
        generated_audio[0].astype(np.int16).tobytes(),
        frame_rate=1600,
        sample_width=2,  # 16-bit encoding
        channels=1  # Mono audio
    )

    # Export the audio segment as a WAV file
    audio_segment.export(f'./out/generated_audio-{uuid.uuid4()}.wav', format='wav')
