import ffmpeg
import tempfile
import random
import os

def random_file(folder_path):
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    return os.path.join(folder_path, random_file)

def random_time(timeStr, delta):
    timeArray = timeStr.split(":")
    h = int(timeArray[0])
    m = int(timeArray[1])
    s = int(timeArray[2].split(".")[0])
    us = int(timeArray[2].split(".")[1])
    us += ((h*60+m)*60+s)*1000000-delta
    us = random.randint(0, us)
    h = us // (1000000 * 60 * 60)
    us %= 1000000 * 60 * 60
    m = us // (1000000 * 60)
    us %= 1000000 * 60
    s = us // 1000000
    us %= 1000000
    return str(h)+':'+str(m)+':'+str(s)+'.'+str(us)

#ffprobe -i .\video\Mygo04.mp4 -show_entries format=duration -v quiet -of csv="p=0" -sexagesimal 
def get_video_duration(video_path):
    probe = ffmpeg.probe(video_path, cmd='ffprobe', v='error', sexagesimal=None, show_entries='format=duration')
    return probe['format']['duration']

def random_frame(video_path, output_file):
    (
        ffmpeg
        .input(video_path, ss=random_time(get_video_duration(video_path), 5000), hide_banner=None, loglevel='error')
        .output(output_file, vframes=1, y=None)
        .run()
    )

# duration count in second
def random_gif(video_path, output_file, duration=3):
    tmpDir = tempfile.TemporaryDirectory()
    
    (
    ffmpeg
    .input(video_path, ss=random_time(get_video_duration(video_path), 5000+int(duration*25*100000)), hide_banner=None, loglevel='error')
    .output(os.path.join(tmpDir.name,"output.mp4"), vf="fps=25,scale=448:-1:flags=lanczos", t=duration, an=None, y=None)
    .run()
    )

    (
    ffmpeg
    .input(os.path.join(tmpDir.name,"output.mp4"))
    .output(os.path.join(tmpDir.name,"palette.png"),hide_banner=None, loglevel='error', vf="palettegen", update=True, y=None)
    .run()
    )

    inV = ffmpeg.input(os.path.join(tmpDir.name,"output.mp4"))
    inP = ffmpeg.input(os.path.join(tmpDir.name,"palette.png"))
    (
        ffmpeg
        .filter([inV, inP], "paletteuse")
        .output(output_file, hide_banner=None, loglevel='error')
        .overwrite_output()
        .run()
    )