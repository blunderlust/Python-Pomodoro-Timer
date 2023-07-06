import tkinter as tk
import pygame
from datetime import timedelta
import time

# Initialize the mixer for playing sounds
pygame.mixer.init()

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Pomodoro Timer')
        self.time_left = tk.StringVar()
        self.time_left.set("00:00:00")

        # Load sounds
        self.sound_start = pygame.mixer.Sound("start.wav")  # start sound file
        self.sound_end = pygame.mixer.Sound("end.wav")  # end sound file

        # UI setup
        self.label = tk.Label(root, textvariable=self.time_left, font=('Courier', 48))
        self.label.pack()

        self.buttons = []
        for i, time in enumerate([30, 20, 10, 5]):
            button = tk.Button(root, text=f'{time} Minutes', command=lambda time=time: self.start_timer(time))
            button.pack()
            self.buttons.append(button)

    def start_timer(self, minutes):
        self.sound_start.play()
        end_time = time.time() + minutes * 60

        while time.time() < end_time:
            remaining = int(end_time - time.time())
            self.time_left.set(str(timedelta(seconds=remaining)))
            self.root.update()

        self.sound_end.play()
        self.time_left.set("00:00:00")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('333x233')  # Set the window size
    app = PomodoroApp(root)
    root.mainloop()
