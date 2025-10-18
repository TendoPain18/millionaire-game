from pygame import mixer
import pyttsx3


class Audio:
    def __init__(self):
        mixer.init()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    @staticmethod
    def PlayTheme():
        mixer.music.stop()
        mixer.music.load('audios/theme.mp3')
        mixer.music.play(-1)

    @staticmethod
    def PlayThemeWin():
        mixer.music.stop()
        mixer.music.load('audios/theme_win.mp3')
        mixer.music.play(-1)

    @staticmethod
    def PlayPhoneSound():
        mixer.music.stop()
        mixer.music.load('audios/phone_sound.mp3')
        mixer.music.play()

    @staticmethod
    def Pause():
        mixer.music.pause()

    @staticmethod
    def Continue():
        mixer.music.play()

    def Say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

