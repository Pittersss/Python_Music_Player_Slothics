import PySimpleGUI as sg
import button
from playsound import playsound

sg.theme('Black')

layout = [[sg.Push(),sg.Image('images/capa_album.png'),sg.Push()],[sg.Text("Guns N' Roses - Sweet Child O' Mine"), sg.Push()],[sg.Push(),sg.Button('', image_data=button.button_left_next, key='-PREVIOUS-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=button.button_play, key='-PLAY-', button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0),sg.Button('', image_data=button.button_rigth_next, key='-NEXT-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Push()]]
window = sg.Window('Slothics', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    if event == '-PLAY-':
        playsound("Guns N' Roses - Sweet Child O' Mine.mp3", False)
window.close()
