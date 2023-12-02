# Python_Music_Player_Slothics
![logo_slothics](https://github.com/Pittersss/Python_Music_Player_Slothics/assets/70235190/9d19ff0e-d5a0-478f-ba46-9f2527e01ef4)

A small project to work on my python skills developed in my first period at college
## Introduction
Firstly, this project was developed to expand my knowledge of Python. After my first semester at college, a great curiosity arose. I wanted to know what I could do with this language beyond what I saw in college, so I discovered the possibility of creating a music player and here I am.

## Development
I divided the application development into 3 parts, that is, three versions. I decided to do it this way to control the evolution of the project and keep track of the evolution of my knowledge and the project
### Version 1
My goal was to set up the visual structure of the program and make music play when pressing the PLAY button. The libraries used to develop this part were: PysimpleGUI and playsound. After reading the documentation of both libraries I started to structure the program. An auxiliary class was created to extract the images in the form of buttons located below the song name. PysimpleGUI only reads images in base64 button format, which is very long, so I put the base64 codes in another file. After an hour of study and coding, the first version was ready.

https://github.com/Pittersss/Python_Music_Player_Slothics/assets/70235190/e500817a-75e3-409c-9ec4-052046d5be12

### Version 2
In this version I wanted to add the song change mechanic and with each change the name of the song would also change. How I did this? First, I created a folder with the desired songs for testing, after that I extracted the names of all the songs from the folder using the library and stored them in a list. Messing with this type of activity showed me how merging libraries is very important. Furthermore, I realized how managing folders via terminal helped me understand the features of the OS library. After having the name of the songs, it was necessary to change the list index if it was changed to the previous or next song. However, the Playsound library did not have a functionality to stop the current song, so I had to test other libraries to create such systems. Therefore, the library that best fit my idea was Pygame, as it has several simple tools for manipulating audio. After 4 hours of a lot of research and testing I got the expected result.

https://github.com/Pittersss/Python_Music_Player_Slothics/assets/70235190/b14444d2-31f0-4795-bc17-036a919b416f

### Version 3
In this final stage, my objective was to polish mechanics already applied. One of them was the separation of the song title and its author, which helped me learn about string manipulation. This way, in a database that receives real songs, a standardization in the song title would be requested to adapt to the algorithm. A bug has been recognized. In version two, if my current song was paused and the user went to the next one, the song would start automatically, but this wasn't right and caused a bottleneck in the Play and Pause logic also allocated in this current version. The image was updated through the use of conditionals linked to possible events on the pages. I personally wouldn't like to have an extra button just to pause the music and I put it that way.

https://github.com/Pittersss/Python_Music_Player_Slothics/assets/70235190/c709d51e-40c8-4a43-9147-018708a5d34d

## Conclusion

This project was very useful for learning about new development tools with Python. It also gave me good practice in basic language concepts.




