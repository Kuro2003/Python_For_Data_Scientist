from platform import platform

class Playlist():
	def __init__(self,name,description,rating,videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class Video():
	def __init__(self,title,link):
		self.title = title
		self.link = link

def read_video():
	title = input("Video title: ") + '\n'
	link = input("Video link: ") +'\n'
	video = Video(title,link)
	return video

def print_video(video):
	print("Video title: ",video.title,end='')
	print("Video link: ",video.link,end='')

def read_videos():
	videos = []
	total = int(input("How many videos : "))
	for i in range(total):
		print("Enter video:" ,i + 1)
		video = read_video()
		videos.append(video)
	return videos

def print_videos(videos):
	total = len(videos)
	for i in range(total):
		print_video(videos[i])

def write_video_to_txt(file,video):
	file.write(video.title)
	file.write(video.link)

def write_videos_to_txt(file,videos):
	total = len(videos)
	file.write(str(len(videos)) + "\n")
	for i in range(total):
		write_video_to_txt(file,videos[i])

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name : ") + '\n'
	playlist_description = input("Enter playlist description : ") + '\n'
	playlist_rating = input("Enter playlist rating(1-5) : ") +'\n'
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt",'w') as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_to_txt(file,playlist.videos)

def read_playlist_txt():
	with open('data.txt','r') as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline() 
		playlist_videos = read_videos_from_txt(file)
		playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_videos)
	return playlist

def print_playlist(playlist):
	print("-----")
	print("Playlist name: " + playlist.name , end='')
	print("Playlist description: " + playlist.description , end= '')
	print("Playlist rating: " + playlist.rating , end ='')
	print_videos(playlist.videos)

def show_menu():
	print("-----------")
	print("Option 1: Create playlist")
	print("Option 2: Show playlist")
	print("Option 3: Play a video")
	print("Option 7: Save and Exit")
	print("-----------")

def main():
	try:
		playlist = read_playlist_txt()
		print("Load data Succesfully !!!")
	except:
		print("Welcome to first user !!!")
	while True:
		show_menu()
		choice = int(input("Select an option(1-7): "))
		if choice == 1:
			playlist = read_playlist()
		elif choice == 2:
			print_playlist(playlist)
		elif choice == 7:
			write_playlist_txt(playlist)
			print("Save data Successfully")
			break

main()