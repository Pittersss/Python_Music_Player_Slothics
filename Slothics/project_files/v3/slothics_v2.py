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
    [sg.Text(musics[0][:-4], key="-TEXT-"), sg.Push()],
    [sg.Push(),sg.Button('', image_data=button.button_left_next, key='-PREVIOUS-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
    sg.Button('', image_data=button.button_pause, key='-PLAY-', button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0),
    sg.Button('', image_data=button.button_rigth_next, key='-NEXT-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Push()]
    ]

window = sg.Window('Slothics', layout)

#os.path.getsize() -- > tamanho da pasta
# percorrer pela pasta
# extrair nome dos arquivos
i = 0
click_play, is_pause = False, False
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
        if not click_play:
            window.Element("-PLAY-").Update(image_data=button.button_play)
            click_play = True
            if not is_pause:
                pygame.mixer.music.load(f'musics/{musics[i]}')
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.unpause()
                is_pause = False
        else:
            window.Element("-PLAY-").Update(image_data=button.button_pause)
            click_play = False
            pygame.mixer.music.pause()
            is_pause = True

window.close()
