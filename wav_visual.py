import wave
import numpy as np
import matplotlib.pyplot as plt


def plot_waveform(filename):
    # Open the WAV file
    with wave.open(filename, "rb") as wf:
        # Get the number of frames, sample width (in bytes), frame rate, and number of channels
        num_frames = wf.getnframes()
        sample_width = wf.getsampwidth()
        frame_rate = wf.getframerate()
        num_channels = wf.getnchannels()

        # Read all frames from the WAV file
        frames = wf.readframes(num_frames)

    # Convert the raw byte string to a NumPy array
    if sample_width == 1:
        # 8-bit samples are unsigned, so offset by 128 to center them
        samples = np.frombuffer(frames, dtype=np.uint8) - 128
    elif sample_width == 2:
        # 16-bit samples are signed, so just interpret them as such
        samples = np.frombuffer(frames, dtype=np.int16)
    else:
        raise ValueError("Unsupported sample width")

    # Reshape the array to have one column per channel
    samples = samples.reshape(-1, num_channels)

    print(samples.shape)

    # Create a time axis in seconds
    time_axis = np.arange(len(samples)) / frame_rate

    # Plot each channel
    for i in range(num_channels):
        plt.plot(time_axis, samples[:, i], label=f"Channel {i + 1}")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Waveform")
    plt.legend(loc=2)
    plt.grid(True)
    plt.show()


# Usage example
filename = "./wav/2_Brothers_on_the_4th_Floor/Never_Alone.1.wav"
plot_waveform(filename)
filename = "./mono/2_Brothers_on_the_4th_Floor/Never_Alone.1.wav"
plot_waveform(filename)
filename = "./cropped/2_Brothers_on_the_4th_Floor/Never_Alone.1.wav"
plot_waveform(filename)
filename = "./resampled/2_Brothers_on_the_4th_Floor/Never_Alone.1.wav"
plot_waveform(filename)
