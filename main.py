import yt_dlp
import os

os.makedirs('./yt_dlp_cache', exist_ok=True)

custom_dir = input('\033[1mSet directory name where we should save your downloads: \033[0m').lower()
if custom_dir:
    os.makedirs(f'./{custom_dir}', exist_ok=True)
else:
    os.makedirs('downloaded', exist_ok=True)


ydl_opts = {
        # CRITICAL PERFORMANCE FIXES
        'extractor_args': {
            'youtube': {
                'skip': ['configs', 'webpage'] # Additional optimization
            }
        },
        'youtube_include_dash_manifest': False,
        'youtube_include_hls_manifest': False,
        'referer': 'https://m.youtube.com/',
        'user_agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        
        # CONNECTION OPTIMIZATIONS
        'socket_timeout': 5,
        'extractor_timeout': 15,
        'retries': 3,
        'skip_unavailable_fragments': True,
        
        'format': 'bestvideo+bestaudio/best',
        'throttledratelimit': 0,  
        'merge_output_format': 'mp4',
        'outtmpl': f'downloaded/%(title)s.%(ext)s',
        'cachedir': './yt_dlp_cache',
        'verbose': False, #Enable for debugging
        'quiet': False,
    }

video_list = []


while True:
    print('''\t\t####################################################################
\n\t\t\033[1;4;31mYouTube downloader created By: \033[1;4;32mDardan Ternava !!!\033[0m\n
\t\t#################################################################### \n
\t\t\033[1;33mThis app makes it possible to download whole YouTube video lists, single videos or multiple videos.
\t\tJust follow the prompts and answer accordingly. \033[0m\n
''')
    list_or_single = input('\t\033[1;4;32mAre you downloading a whole list of YouTube videos ? \033[44;30m(Y/N):\033[0m ').lower()
    if list_or_single == 'y':
        user_input = input('\t\033[1;4;31mPaste your link here:\033[0m ')
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print('\033[1;33mDownloading...\n This may take a while depending on the connection!\033[0m')
                ydl.download([user_input])
                print(f'\033[1;32mVideo downloaded successfully to "downloaded" folder.\033[0m')
        except Exception as error:
            print(f'\033[1;31mAn error occurred: {error}!\033[0m')
        break
    elif list_or_single == 'n':
        print('''\t\t\033[1;33mIf you are downloading only one video answer N when asked if you want to add more links,\n
              If you want to download more than one video, add the links one by 
              one and answer Y each time you want to add a link to download.\033[0m''')
        user_input = input('\t\033[1;4;31mPaste your link here:\033[0m ')
        confirmation = input('\t\033[1;4;32mDo you want to add more links ? \033[44;30m(Y/N):\033[0m  ').lower()
        if confirmation == 'y':
            video_list.append(user_input)
        elif confirmation == 'n':
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    print('\033[1;33mDownloading...\n This may take a while depending on the connection!\033[0m')
                    ydl.download([user_input])
                    print(f'\033[1;32mVideo downloaded successfully to "downloaded" folder.\033[0m')
            except Exception as error:
                print(f'\033[1;31mAn error occurred: {error}!\033[0m')
            break
        else:
            print('\033[1;31mInvalid input !\033[0m')
    else:
        print('\033[1;31mInvalid input !\033[0m')