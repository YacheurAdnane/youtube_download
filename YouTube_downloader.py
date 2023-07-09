
import subprocess
#SAVE THE VIDIO
# Define the URL variable
url =  input ("insert your youtube URL")

# Define the command with the URL variable

command = f'yt-dlp {url} -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4" -o "/content/video/%(title)s.%(ext)s"'#to download video 
subprocess.run(command, shell=True)

command = f'yt-dlp {url} --get-title'

# Run the command and capture the output
output = subprocess.check_output(command, shell=True, text=True)

# Extract the title from the output
video_title = output.strip()


#SAVE AUDIO FORMA OF THAT VEDIO

# Define the command with the URL variable to extract audio
command = f'yt-dlp {url} -x --audio-format mp3 -o "/content/AUDIO/%(title)s.%(ext)s"'#to download audio

subprocess.run(command, shell=True)
print ("secsusfely download mp3 audio and mp4 video :", video_title)

