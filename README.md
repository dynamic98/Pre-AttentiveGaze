# Pre-AttentiveGaze

### Index 
- [1. Project Introduction](#1-project-introduction)
- [2. Task and Gaze Stimuli](#2-task-and-gaze-stimuli)
- [3. Data Collection Envs](#3-data-collection-envs)
- [4. Collected Gaze Features](#4-collected-gaze-features)
- [5. Dev Envs](#5-dev-envs)
- [6. Understandig Github Structure](#6-understandig-github-structure)


---
### 1. Project Introduction 
- Category: `Security and Privacy` `Authentication` `Human-centered computing`
- Keywords: `Gaze` `Authentication` `Person Identification` `Pre-attentive processing` 
- Data: To be released
---
### 2. Task and Gaze Stimuli
<img width="800" alt="Task_and_Gaze_Stimuli" src="https://github-production-user-asset-6210df.s3.amazonaws.com/98831107/340265856-75048462-8a36-42fd-9f8c-a87e1b49dea9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240721%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240721T142509Z&X-Amz-Expires=300&X-Amz-Signature=cda2e9f65c85cd4d8662bcbe5067ae5369b00796ec067e8aa4bd155196c2f987&X-Amz-SignedHeaders=host&actor_id=43838273&key_id=0&repo_id=813592648">


- **A visual search task** where targets (black circles) and distractors (dashed circles) are arranged in a circular pattern. 
- Each level has a specific arrangement of targets and distractors.

---
### 3. Data Collection Envs
<img width="800" alt="Data_Collection_Envs" src="https://github.com/user-attachments/assets/321bf858-0af9-4cc6-b315-ea5152ee567a">


---
### 4. Collected Gaze Features
**(1) Raw Gaze**
 - Coordinate of gaze point (x1, y1, …, x84, y84), (120 Hz × 0.7 s = 84 samples)

   
**(2) Eye Movement**
 - Path length: Length of path traveled in screen
 - Gaze velocity: Velocity of path traveled in screen
 - Gaze angle: Angle with centroid of previous fixation

   
**(3) Eye Movement**
 - Path length: Length of path traveled in screen
 - Gaze velocity: Velocity of path traveled in screen
 - Gaze angle: Angle with centroid of prev

   
**(4) Fixation**
 - Reaction time: Time until the first fixation is made outside the cross point (equal to the first fixation time)
 - Fixation duration: Duration per fixation
 - Fixation dispersion: Spatial spread during a fixation
 - Fixation count: Number of fixations
   
   
**(5) Saccade**
 - Saccade duration: Duration per saccade
 - Saccade velocity: Angular velocity per saccade
 - Saccade amplitude: Angular distance per saccade
 - Saccade dispersion: Spatial spread during a saccade
 - Saccade count: Numbers of saccades
   
**(6) MFCC**
 - 12 Mel-frequency ceptral coefficients for overall stimuli


**(7) Pupil**
 - Left pupil diameter: Pupil diameter of left eye
 - Right pupil diameter: Pupil diameter of right eye
 - Average pupil diameter: Average of left and right pupil diameter


**Additional Explanation for fixation and saccade**
<img width="800" alt="스크린샷 2024-06-17 오후 5 09 11" src="https://github-production-user-asset-6210df.s3.amazonaws.com/98831107/340228668-980e21ce-ebd8-4474-a09e-08e201e09a07.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240721%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240721T142557Z&X-Amz-Expires=300&X-Amz-Signature=64f1e721458559ced9aed289d4341244ac62e5cdbfc3a960d0d2811d601b84cb&X-Amz-SignedHeaders=host&actor_id=43838273&key_id=0&repo_id=813592648">


In fixation section, 'duration' and 'dispersion' value is extracted. 
In saccade section, 'duration', 'velocity', 'amplitude', and 'dispersion' value is extracted. 
The number of each section is a 'count' value

---
### 5. Dev Envs
##### python version <img src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=Python&logoColor=white"/>
    python version = 3.10
##### install package
    pip install -r requirements.txt
---

### 6. Understandig Github Structure
##### Directory
```bash
Pre-AttentiveGazeAuth/
├── data/
│   ├── PreAttentiveGaze/
│   ├── MultipleVC.tsv
│   └── SingleVC.tsv
├── Figure3.ipynb
├── Figure4.ipynb
├── main.ipynb
├── README.md
├── requirements.txt
└── src/
    ├── feature_extraction.py
    ├── gazeheatplot.py
    ├── load_data.py
    ├── ML_util.py
    ├── model.py
    ├── preprocessing.py
    └── stimuli/
        ├── LevelDictionary_MultipleVC.json
        ├── LevelDictionary_SingleVC.json
        ├── stimuli.py
        └── util.py
```
##### JSON Files
The repository contains two JSON files, `LevelDictionary_MultipleVC.json` and `LevelDictionary_SingleVC.json`, which define different levels for the visual search task.

##### LevelDictionary_MultipleVC.json
- **`level`**: Specifies the shape, size, hue, and brightness of the targets.
  - The array contains four elements representing:
    - Shape (e.g., 3)
    - Size (e.g., 50)
    - Hue (e.g., 3)
    - Brightness (e.g., 2)
- **`target_list`**: Lists the positions (0 to 15) where the targets are located.

Example:
```json
"0": {
    "level": [3, 50, 3, 2],
    "target_list": [6, 5, 1, 10]
}
```
This means for stimuli index number 0, the targets are at positions 6, 5, 1, and 10 with shape 3, size 50, hue 3, and brightness 2.

##### LevelDictionary_SingleVC.json

- **`visual_component`**: Describes the visual feature used in the level (e.g., "brightness", "hue", "shape", "size").
- **`level`**: Specifies the configuration for the visual component.
- **`target_list`**: Lists the positions where the targets are located.

Example:
```json
"0": {
    "visual_component": "brightness",
    "level": [1, 1, 1, 1],
    "target_list": [9, 10, 14, 5]
}
```
This means for stimuli index number 0, the targets are at positions 9, 10, 14, and 5, and the task focuses on the brightness visual component with the specified configuration.

##### Example Explanation

For level 0 in `LevelDictionary_MultipleVC.json`:
- **`level`**: `[3, 50, 3, 2]` (shape, size, hue, brightness)
- **`target_list`**: `[6, 5, 1, 10]` (positions of targets)
  - Targets are at positions 6, 5, 1, and 10 with shape 3, size 50, hue 3, and brightness 2.

For level 0 in `LevelDictionary_SingleVC.json`:
- **`visual_component`**: `"brightness"`
- **`level`**: `[1, 1, 1, 1]` (configuration for brightness)
- **`target_list`**: `[9, 10, 14, 5]`
  - Targets are at positions 9, 10, 14, and 5 focusing on the brightness visual component with the specified configuration.

---





