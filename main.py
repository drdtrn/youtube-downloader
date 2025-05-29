import yt_dlp

ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4', 
    }

video_list = []


while True:
    user_input = input('Paste your link here: ')
    confirmation = input('Do you want to add more links ? (Y/N): ').lower()
    if confirmation == 'y':
        video_list.append(user_input)
    elif confirmation == 'n':
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_list.append(user_input)
            ydl.download(video_list)
        break
    else:
        print('Invalid input !')
        break