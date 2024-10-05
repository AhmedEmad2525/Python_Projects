# World Cup 2022 Simulator

This is a Python-based simulation for the World Cup 2022 group stages. It uses a graphical user interface (GUI) built with Tkinter to simulate group formations, matches, and rankings of the teams involved.
This projects simulates the creation of the Groups for the Groups stage(Random) and Simulates the matches played with the score of each team in each match then displayes the ranking of each team with the
points each team earned throught this stage and finally the ranking of the groups regarding the points in case of a Tie the ranking is regarding to the goals.

## Features

Group Draw Simulation: Teams are drawn from different pots to form the 8 groups (A-H), with each group consisting of 4 teams.
Match Simulation: The teams within each group play matches against each other, with scores generated randomly.
Points Calculation: The points for each team are calculated based on match results, where:
Win: 3 points
Draw: 1 point
Loss: 0 points
Goals Scored: Displays the total goals scored by each team after all the matches in a group are completed.
User-friendly GUI: Users can navigate through different screens using buttons, view match results, and see rankings in a straightforward manner.
Concepts Implemented
Graphical User Interface (GUI): Built using Tkinter, with buttons, labels, frames, and images for user interaction.
Randomization: Used to create random match outcomes and to generate group compositions from predefined pots of teams.
Tkinter Frames Management: Utilizes a function (clear_frame) to manage the transition between different screens by clearing the content and loading the required frames dynamically.
Image Display: Uses PIL (Python Imaging Library) to display an image on the welcome screen.

## Requirements
Python 3
Tkinter (included in standard Python library)
Pillow (pip install Pillow)
