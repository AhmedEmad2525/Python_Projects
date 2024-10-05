# World Cup 2022 Simulator

- This is a Python-based simulation for the World Cup 2022 group stages. It uses a graphical user interface (GUI) built with Tkinter to simulate group formations, matches, and rankings of the teams involved. 
- This project simulates the creation of the groups for the group stage (random) and simulates the matches played with the score of each team in each match. Then, it displays the ranking of each team with the points each team earned throughout this stage, and finally, the ranking of the groups regarding the points. In case of a tie, the ranking is based on Goals.

## Features

- **Group Draw Simulation**: Teams are drawn from different pots to form the 8 groups (A-H), with each group consisting of 4 teams.
- **Match Simulation**: The teams within each group play matches against each other, with scores generated randomly.
- **Points Calculation**: The points for each team are calculated based on match results:
  - Win: 3 points
  - Draw: 1 point
  - Loss: 0 points
- **Goals Scored**: Displays the total goals scored by each team after all the matches in a group are completed.
- **User-friendly GUI**: Users can navigate through different screens using buttons, view match results, and see rankings in a straightforward manner.

## Concepts Implemented

- **Graphical User Interface (GUI)**: Built using Tkinter, with buttons, labels, frames, and images for user interaction.
- **Randomization**: Used to create random match outcomes and to generate group compositions from predefined pots of teams.
- **Tkinter Frames Management**: Utilizes a function (`clear_frame`) to manage the transition between different screens by clearing the content and loading the required frames dynamically.
- **Image Display**: Uses PIL (Python Imaging Library) to display an image on the welcome screen.

## Requirements

- Python 3
- Tkinter (included in standard Python library)
- Pillow (`pip install Pillow`)

## Project Structure
- Welcome screen with a brief introduction to the simulator.
  
  ![Screenshot 2024-10-05 122156](https://github.com/user-attachments/assets/5885cd2b-4c6b-48cd-a9e8-7d8dab256a73) 
 
- Display of pots used to create groups.

  ![Screenshot 2024-10-05 122239](https://github.com/user-attachments/assets/8e62a0ee-0636-4d86-b3a7-5a3b73c0b764)
  
- Display of the group stage draw with each group containing four teams.
  
 ![Screenshot 2024-10-05 122247](https://github.com/user-attachments/assets/2be3fe39-7303-4768-ae9d-93f937c69418)
  
-  Simulation of matches within each group and display of results.
  
  ![Screenshot 2024-10-05 122255](https://github.com/user-attachments/assets/8f4a187e-aff7-42b5-836a-f1015e9c868d)

-  Final ranking of teams in each group based on points and goals scored
  
 ![Screenshot 2024-10-05 122300](https://github.com/user-attachments/assets/a5ac7762-00ed-4542-b601-088cb9d0823b)

  


