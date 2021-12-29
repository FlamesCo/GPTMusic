## import gpt3 module
import openai
import os
import sys
import json
# open private openai api key
openai.api_key = open(os.path.expanduser('~/.openai_api_key'), 'r').read().strip()

## make a GAN that can generate mp3 files that make mashups of a dataset of a folder of mp3 files
## generate a mashup from a dataset of .jsonfiles from youtube url links using gpt3
generate_mp3_mashup = openai.OpenAI('generate_mp3_mashup.json')
## ask the user what song style they want to use
print("What song style would you like to use? (1) Pop, (2) Rock, (3) Rap, (4) Country, (5) Classical, (6) Jazz, (7) Hip Hop, (8) Metal, (9) Reggae, (10) R&B, (11) Techno, (12) Trance, (13) World")
song_style = input()
## ask the user what genre they want to use
print("What genre would you like to use? (1) Alternative, (2) Blues, (3) Classical, (4) Country, (5) Electronic, (6) Folk, (7) Funk, (8) Hip Hop, (9) Jazz, (10) Latin, (11) Metal, (12) Pop, (13) Reggae, (14) Rock")
genre = input()
## ask the user what mood they want to use
print("What mood would you like to use? (1) Angry, (2) Bored, (3) Calm, (4) Confident, (5) Depressed, (6) Excited, (7) Happy, (8) Sad, (9) Stressed")
mood = input()
## ask the user what instrument they want to use
print("What instrument would you like to use? (1) Acoustic Guitar, (2) Acoustic Piano, (3) Acoustic Strings, (4) Bass, (5) Electric Guitar, (6) Electric Piano, (7) Electric Strings, (8) Flute, (9) Guitar, (10) Piano, (11) Saxophone, (12) Strings, (13) Trumpet, (14) Violin")
instrument = input()
## ask the user what instrument they want to use
## ask the user to point to a json files of instruments from youtube url links samples from videos and then mash it up with the required
## instrument on the input file
instrumentgenerator=openai.OpenAI('instrumentgenerator.json')
## in the instrumentgenetaor.json file, change the instrument to the instrument the user wants to use
print("Syncing to instrument.")
instrumentgenerator.set_inputs({"instrument": instrument})
## prompt the output song with the instrument, tone of the song, and the style of the song
print("Generating song.")
## get the genre, song style and prompt those parametrs to thea .sjon file called "musicmood.json"
generate_mp3_mashup.set_inputs({"genre": genre, "style": song_style, "mood": mood})
## get the output song from the .json file called "musicmood.json"
## use the music mood to save the songs folder of dataset into instrumentgenerator.json
musicmood = generate_mp3_mashup.get_response()
output_song = generate_mp3_mashup.call()
generated_song = instrumentgenerator.generate()
## save the song to the desktop
print("Done! Saving song to desktop.")
with open("generated_song.mp3", "wb") as f:
    f.write(output_song)
print("Done! Saving song to desktop.")
## save to your folder of choice