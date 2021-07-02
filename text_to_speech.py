# # Import the Gtts module for text  
# # to speech conversion 
# from gtts import gTTS 
  
# # import Os module to start the audio file
# import os 
  
# mytext = 'Convert this Text to Speech in Python'
  
# # Language we want to use 
# language = 'en'
  

# myobj = gTTS(text=mytext, lang=language, slow=False) 
  

# myobj.save("output.mp3") 
  
# # Play the converted file 
# os.system("start output.mp3") 



#  ----------------------------------- Text File to Speech -----------------------------------------------

# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 

fh = open("Text.txt", "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()

# Play the converted file 
os.system("start output.mp3")