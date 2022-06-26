from os import link
from scipy.fftpack import tilbert


class Video():
    def __init__(self,title,link):
        self.title = title
        self.link = link

def read_video():
    title = input("Video title: ")
    link = input("Video link: ")
    video = Video(title,link)
    return video

def print_video(video):
    print("Video title : ",video.title,end='')
    print("Video link : ",video.link,end='')

def read_videos():
    videos = []
    total = int(input("Enter bumber video : "))
    for i in range(total):
        print("Enter video " ,i + 1)
        video = read_video()
        videos.append(video)
    return videos

def print_videos(videos):
    total = len(videos)
    print("-----")
    for i in range(total):
        print_video(videos[i])

def write_video_to_txt(file,video):
    file.write(video.title + "\n")
    file.write(video.link + "\n")

def write_videos_to_txt(videos):
    total = len(videos)
    with open("data.txt",'w') as file:
        file.write(str(len(videos)) + "\n")
        for i in range(total):
            write_video_to_txt(file,videos[i])

def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

def read_videos_from_txt():
    videos = []
    with open('data.txt','r') as file:
        total = file.readline()
        for i in range(int(total)):
            video = read_video_from_txt(file)
            videos.append(video)
    return videos

def main():
    videos = read_videos()
    write_videos_to_txt(videos)
    videos = read_videos_from_txt()
    print_videos(videos)

main()