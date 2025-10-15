from pygame import mixer
import pyttsx3

class Audio:
    def __init__(self):
        mixer.init()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)  # 1 for male 0 for female

    def PlayTheme(self):
        mixer.music.stop()
        mixer.music.load('audios/theme.mp3')
        mixer.music.play(-1)

    def PlayThemeWin(self):
        mixer.music.stop()
        mixer.music.load('audios/theme_win.mp3')
        mixer.music.play(-1)

    def PlayPhoneSound(self):
        mixer.music.stop()
        mixer.music.load('audios/phone_sound.mp3')
        mixer.music.play()

    def Pause(self):
        mixer.music.pause()

    def Continue(self):
        mixer.music.play()

    def Say(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
