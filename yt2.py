import PySimpleGUI as sg
import youtube_dl

layout = [
    [sg.Text('YOUTUBE VIDEO DOWNLOADER',
             font='Franklin 16',
             justification='center',
             expand_x=True,
             pad=(10, 20),
             key='-TEXT-')],
    [sg.Text('VIDEO URL :'),sg.Input(expand_x=True, key='-URL-')],
    [sg.Button('DOWNLOAD',expand_x=True)]
]

window = sg.Window('YT Downloader', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'DOWNLOAD':
        url = values['-URL-']
        ydl_opts = {}
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download([url])


window.close()