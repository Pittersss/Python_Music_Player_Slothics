import PySimpleGUI as sg
import button
import pygame
import os

sg.theme('Black')
musics = []
for _, _, arquivo in os.walk('musics/'):
    musics = arquivo




layout = [
    [sg.Push(),sg.Image('images/capa_album.png'),sg.Push()],
    [sg.Text("a", key="-TEXT-"), sg.Push()],
    [sg.Push(),sg.Button('', image_data=button.button_left_next, key='-PREVIOUS-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
    sg.Button('', image_data=button.button_play, key='-PLAY-', button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0),
    sg.Button('', image_data=button.button_rigth_next, key='-NEXT-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Push()]
    ]

window = sg.Window('Slothics', layout)

#os.path.getsize() -- > tamanho da pasta
# percorrer pela pasta
# extrair nome dos arquivos
i = 0
pygame.mixer.init()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    if event == '-NEXT-':
        if i == (len(musics)-1):
            i = 0
            window.Element("-TEXT-").update(f'{musics[i][:-4]}')
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            pygame.mixer.music.play(-1)
        else:
            i += 1
            window.Element("-TEXT-").update(f'{musics[i][:-4]}')
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            pygame.mixer.music.play(-1)
    if event == '-PREVIOUS-':
        if i == 0:
            i = len(musics)-1          
            window.Element("-TEXT-").update(f'{musics[i][:-4]}')
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            pygame.mixer.music.play(-1)
        else:
            i -= 1
            window.Element("-TEXT-").update(f'{musics[i][:-4]}')
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            pygame.mixer.music.play(-1)
    if event == '-PLAY-':
        pygame.mixer.music.load(f'musics/{musics[i]}')
        pygame.mixer.music.play(-1)
window.close()
