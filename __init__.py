from aqt import mw
from aqt.reviewer import Reviewer
from aqt.qt import QTimer
import os

yellow_persistent = False  # Tracks if the yellow background should persist

class AutoAdvance:
    def __init__(self, reviewer):
        self.reviewer = reviewer
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_out_action)

    def start(self):
        # Check if the yellow background is persistent
        global yellow_persistent
        if yellow_persistent:
            self.reviewer.web.eval("document.body.style.backgroundColor = 'yellow';")  # Keep yellow if set
        else:
            self.reviewer.web.eval("document.body.style.backgroundColor = '';")  # Reset to original color

        # Start the main timer (default: 180 seconds for testing)
        card_timer = mw.col.conf.get("timeLimit", 180) * 1000
        self.timer.start(card_timer)

    def stop(self):
        # Stop the timer
        self.timer.stop()

    def reset_background(self):
        # Reset the background to the default color
        self.reviewer.web.eval("document.body.style.backgroundColor = '';")

    def time_out_action(self):
        global yellow_persistent
        # Timer runs out: Flip card, choose "Again," and set yellow persistence
        if self.reviewer.state == "question":
            # self.reviewer._showAnswer()

            # Set the background to red for a brief moment
            self.reviewer.web.eval("document.body.style.backgroundColor = 'red';")
            yellow_persistent = True  # Persist yellow background
            
            # Replace the path below with the full path to your sound file
            sound_file = "/Users/arcSmith/Library/Application Support/Anki2/addons21/auto-advance/alarm.wav"

            # Check if the file exists
            if os.path.exists(sound_file):
                QTimer.singleShot(1 * 1000, lambda: [os.system(f'afplay \"{sound_file}\"'), self.reviewer._showAnswer(), self.reviewer._answerCard(0)])
        
        self.timer.stop()


# Wrapping Reviewer methods
original_showQuestion = Reviewer._showQuestion
original_showAnswer = Reviewer._showAnswer
original_answerCard = Reviewer._answerCard


def wrapped_showQuestion(self):
    # Start the timer and display the card as normal
    if not hasattr(self, "auto_advance"):
        self.auto_advance = AutoAdvance(self)
    self.auto_advance.start()
    original_showQuestion(self)  # Call the original method to show the card

def wrapped_showAnswer(self):
    global yellow_persistent

    # Stop the timer when manually flipping the card
    if hasattr(self, "auto_advance"):
        self.auto_advance.stop()

    # Automatically select "Good" after 10 seconds and reset background
    # QTimer.singleShot(10 * 1000, lambda: [
    #     self._answerCard(2),
    #     self.auto_advance.reset_background(),
    #     reset_persistence_on_success()  # Clear yellow persistence on success
    # ])
    self._answerCard(2)
    self.auto_advance.reset_background()
    reset_persistence_on_success()

    # Set the background to green for the "happy path"
    self.web.eval("document.body.style.backgroundColor = 'green';")

    original_showAnswer(self)  # Call the original method to show the answer

def reset_persistence_on_success():
    global yellow_persistent
    yellow_persistent = False  # Reset yellow persistence only on "happy path"

def wrapped_answerCard(self, ease):
    # Handle manual selection of "Good" or any other ease
    if hasattr(self, "auto_advance"):
        self.auto_advance.reset_background()

    # Call the original method to handle card advancement
    original_answerCard(self, ease)


# Attach the hooks
Reviewer._showQuestion = wrapped_showQuestion
Reviewer._showAnswer = wrapped_showAnswer
Reviewer._answerCard = wrapped_answerCard
