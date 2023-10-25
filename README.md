# audio_to_text_sphinx

In October 2023, I was writing an article, and I wanted to pull some quotes from an approximately 41-minute-long podcast
episode. After reading about my audio-to-text Python module options, I went with CMU Sphinx after having some trouble with a few of the 
others.

First, because the full 41-minute-long wav file was about 440 mb, I had to break it up into many segments that were 25 mb max
for which I used the first python file **break_up_wav_file.py**.

Next, I used CMU Sphinx to transcribe the audio from the 19 wav files and print it all to one doc using the python file **transcribe_pocketsphinx.py**.

* In the future, I would like to use ML to train this model to transcribe more accurately. While my code worked well enough for what I needed, there's definitely room for improvement.
