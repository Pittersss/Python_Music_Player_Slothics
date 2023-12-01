import PySimpleGUI as sg
import button
import pygame
import os

sg.theme('Black')
musics = []
for _, _, arquivo in os.walk('musics/'):
    musics = arquivo
def extract_autor(music_path_name):
    autor_name = ""
    for i in range(len(music_path_name)):
        if music_path_name[i] == "-":
            for j in range(0, i-1):
                autor_name += music_path_name[j]
            break
    return autor_name

def extract_music_title(music_path_name):
    music_name = ""
    def extract_initial_index():
        for i in range(len(music_path_name)):
            if music_path_name[i] == "-":
                return i + 2
    for j in range(extract_initial_index(), len(music_path_name)):
        if music_path_name[j] != "-":
            if music_path_name[j] == ".":
                break
            music_name += music_path_name[j]
    return music_name


layout = [
    [sg.Image('images/capa_album.png'),sg.Push()],
    [sg.Text(extract_music_title(musics[0])+f"\n{extract_autor(musics[0])}", key="-TITLE-", font="Negrito"), sg.Push()],
    [sg.Push(),sg.Button('', image_data=button.button_left_next, key='-PREVIOUS-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
    sg.Button('', image_data=button.button_pause, key='-PLAY-', button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0),
    sg.Button('', image_data=button.button_rigth_next, key='-NEXT-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Push()]
    ]

window = sg.Window('Slothics', layout,size=(320, 550))


i = 0
click_play, is_pause, is_move = False, False, False
pygame.mixer.init()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    if event == '-NEXT-':
        is_move = True
        if i == (len(musics)-1):
            i = 0
            window.Element("-TITLE-").update(extract_music_title(musics[i])+f"\n{extract_autor(musics[i])}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            if click_play:
                pygame.mixer.music.play(-1)
        else:
            i += 1
            window.Element("-TITLE-").update(extract_music_title(musics[i])+f"\n{extract_autor(musics[i])}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            if click_play:
                pygame.mixer.music.play(-1)
    if event == '-PREVIOUS-':
        is_move = True
        if i == 0:
            i = len(musics)-1          
            window.Element("-TITLE-").update(extract_music_title(musics[i])+f"\n{extract_autor(musics[i])}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            if click_play:
                pygame.mixer.music.play(-1)
        else:
            i -= 1
            window.Element("-TITLE-").update(extract_music_title(musics[i])+f"\n{extract_autor(musics[i])}")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'musics/{musics[i]}')
            if click_play:
                pygame.mixer.music.play(-1)
    if event == '-PLAY-':
        if not click_play:
            window.Element("-PLAY-").update(image_data=button.button_play)
            click_play = True
            if not is_pause:
                pygame.mixer.music.load(f'musics/{musics[i]}')
                pygame.mixer.music.play(-1)
            else:
                if is_move:
                    pygame.mixer.music.play(-1)
                    is_move = False
                else:
                    pygame.mixer.music.unpause()
                    is_pause = False
        else:
            window.Element("-PLAY-").Update(image_data=button.button_pause)
            click_play = False
            pygame.mixer.music.pause()
            is_pause = True

window.close()
