# Anki-Distraction-Free

Ever get lost in thought or distracted while doing your flashcards? This add-on is a simple solution to a common problem, helping you maintain focus and efficiency during your review sessions.

## Motivation

I often found myself getting distracted while doing my flashcards in the morning. I built this add-on to act as a wake-up call; if I didn't answer a card quickly enough, an alarm sound would play alongside a red backdrop, prompting me to get back on track and stay focused on my study session.

---

## Features

-   **Auto-Advance:** After **3 minutes** on a single card, a sound will play, the background will turn red, and you will automatically be advanced to the next flashcard.
-   **Visual Feedback:** A **green background** briefly appears on cards that you answer within the time limit, serving as a positive reinforcement. The background returns to white when you advance.
-   **Configurable:** The time limit (currently 3 minutes) can be adjusted in the add-on's configuration file.

---

## Technologies Used

* **Programming Language:** Python 3.9.6
* **Framework:** Anki Add-on API

---

## How it Works

This add-on functions by running a simple timer in the background of your Anki session. It monitors the time spent on each flashcard. If the timer exceeds the set limit, it triggers an event that changes the background color, plays a sound, and simulates a keypress to advance to the next card. This process is designed to be lightweight and non-intrusive, ensuring a seamless user experience.

---

## Future Work

I have several ideas for improving and expanding this add-on:

* **GUI for Customization:** Adding a graphical user interface within Anki to easily change the time limit, sound, and colors without having to edit the code.
* **Customizable Alerts:** Allowing users to select from different sounds and color schemes for both the negative and positive feedback alerts.
* **Difficulty-Based Timers:** Implementing different time limits based on a card's difficulty or the number of times it has been reviewed.
