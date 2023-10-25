import os
import wave

# Define the source WAV file and the directory for the split files
source_file = "file"
output_dir = "filepath"
max_file_size = 23 * 1024 * 1024  # 25 MB in bytes

# Create the output directory and subfolder if they don't exist
os.makedirs(output_dir, exist_ok=True)

def split_wav_file(source_file, output_dir, max_file_size):
    input_audio = wave.open(source_file, 'rb')

    # Get the audio parameters from the source file
    params = input_audio.getparams()
    sample_width = input_audio.getsampwidth()

    # Initialize variables for the split files
    current_file_size = 0
    file_num = 1
    output_file = None

    while True:
        frame_data = input_audio.readframes(1024)  # Adjust the frame size as needed
        if not frame_data:
            break

        if output_file is None or current_file_size >= max_file_size:
            # Close the current split file and open a new one
            if output_file:
                output_file.close()
            output_file = wave.open(os.path.join(output_dir, f"split_{file_num}.wav"), 'wb')
            output_file.setparams(params)
            file_num += 1
            current_file_size = 0

        output_file.writeframes(frame_data)
        current_file_size += len(frame_data)

    # Close the last split file
    if output_file:
        output_file.close()

    input_audio.close()

# Call the function to split the WAV file
split_wav_file(source_file, output_dir, max_file_size)
