import os
from music21 import *
from midi2audio import FluidSynth

# Define the song in ABC notation
abc_string = '''
X:1
T:Warsaw Improv Night
M:4/4
L:1/4
K:C
| C D E F | G E D C |
| A B C B | A G F E |
| C D E F | G E D C |
| F G A G | F E F D |
| A B C B | A G F E |
| C D E F | G F E C |
'''

# Parse the ABC string into a music21 stream
abc_handler = converter.subConverters.ConverterABC()
stream = abc_handler.parseData(abc_string)

# Write the music21 stream to a MIDI file
mf = midi.translate.streamToMidiFile(stream)
midi_file = 'warsaw_improv_night.mid'
mf.open(midi_file, 'wb')
mf.write()
mf.close()

# Convert the MIDI file to MP3 using FluidSynth
fs = FluidSynth()
fs.midi_to_audio(midi_file, 'warsaw_improv_night.mp3')

# Clean up the temporary MIDI file
os.remove(midi_file)
