import webbrowser
import pytube
def YouTube(search):
    s = pytube.Search(search)
    rvideo = s.results[0].video_id
    video_url = "https://www.youtube.com/watch?v="+rvideo
    webbrowser.open_new_tab(video_url)
query = input("What you want to search in YouTube : ")
YouTube(query)