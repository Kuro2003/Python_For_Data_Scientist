from platform import platform
import webbrowser
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
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True
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
		print("Video ",i+1)
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
	playlist_rating = input("Enter playlist rating(1-5) : ") + '\n'
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
	print("Playlist rating: " + str(playlist.rating) , end ='')
	print_videos(playlist.videos)

def show_menu():
	print("Main Menu:")
	print("-----------------------------")
	print("| Option 1: Create playlist |")
	print("| Option 2: Show playlist   |")
	print("| Option 3: Play a video    |")
	print("| Option 4: Add a video     |")
	print("| Option 5: Update playlist |")
	print("| Option 6: Remove video    |")
	print("| Option 7: Save and Exit   |")
	print("-----------------------------")


def select_in_range(promp,min,max):
	choice = input(promp)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(promp)
	return int(choice)

def play_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Select video (1," + str(len(playlist.videos)) + "): ",1,len(playlist.videos))
	print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end ="")
	playlist.videos[choice-1].open()

def add_video(playlist):
	print("Enter new video information: ")
	new_video_title = input("Enter new video title: ") + '\n'
	new_video_link = input("Enter new video_link: ") + '\n'
	new_video = Video(new_video_title,new_video_link)
	playlist.videos.append(new_video)
	return playlist

def update_playlist(playlist):
	print("Update playlist: ")
	print("1.Name ")
	print("2.Description ")
	print("3.Rating ")

	choice = select_in_range("Enter what you want update(1,3): ",1,3)

	if choice == 1:
		new_playlist_name = input("Enter new name for playlist: ") + '\n'
		playlist.name = new_playlist_name
		print("Update Successfully")
		return playlist

	if choice == 2:
		new_playlist_desctiption = input("Enter new desctiption for playlist: ") + '\n'
		playlist.desctiption = new_playlist_desctiption
		print("Update Successfully")
		return playlist	
	if choice == 3:
		new_playlist_rating = input("Enter new rating for playlist: ") + '\n'
		playlist.rating = new_playlist_rating
		print("Update Successfully")
		return playlist

def remove_playlist(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Enter video you want to delete: ",1,len(playlist.videos))
	playlist.videos.pop(choice - 1)
	print("Delete Successfully !!!")
	return playlist
def main():
	try:
		playlist = read_playlist_txt()
		print("Load data Succesfully !!!")
	except:
		print("Welcome to first user !!!")
	while True:
		show_menu()
		choice = select_in_range("Select an option(1-7): ",1,7)
		if choice == 1:
			playlist = read_playlist()
			input("\nPress Enter to continue.\n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 3:
			play_video(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			playlist = remove_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 7:
			write_playlist_txt(playlist)
			print("Save data Successfully")
			break

main()