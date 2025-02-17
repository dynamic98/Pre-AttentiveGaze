# Pre-AttentiveGaze: gaze-based authentication dataset with momentary visual interactions

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)


### Index 
- [1. Project Introduction](#1-project-introduction)
- [2. Task and Gaze Stimuli](#2-task-and-gaze-stimuli)
- [3. Data Collection Envs](#3-data-collection-envs)
- [4. Pre-processed Gaze Features](#4-pre-processed-gaze-features)
- [5. Dev Envs](#5-dev-envs)
- [6. Understandig Github Structure](#6-understandig-github-structure)


---
### 1. Project Introduction 
- Category: `Security and Privacy` `Authentication` `Human-centered computing`
- Keywords: `Gaze` `Authentication` `Person Identification` `Pre-attentive processing` 
- Data: To be released
---
### 2. Task and Gaze Stimuli
<img width="800" alt="Task_and_Gaze_Stimuli" src="https://github.com/user-attachments/assets/9c7afe0e-df04-465f-a9f1-cdb212cd4193">


- **A visual search task** where targets (black circles) and distractors (dashed circles) are arranged in a circular pattern. 
- Each level has a specific arrangement of targets and distractors.

---
### 3. Data Collection Envs
<img width="800" alt="Data_Collection_Envs" src="https://github.com/user-attachments/assets/cbc7cba2-2302-45ae-a6c2-4ea0301abe85">


---
### 4. Pre-processed Gaze Features
**(1) Raw Gaze**
 - X: Corresponding to Gaze point X (x1, …, x84) 
 - Y: Corresponding to Gaze point Y (y1, …, y84) 

   
**(2) Eye Movement**
 - Path length: Length of path traveled in screen
 - Gaze velocity: Velocity of path traveled in screen
 - Gaze angle: Angle with centroid of previous fixation

   
**(3) Eye Movement**
 - Path length: Length of path traveled in screen
 - Gaze velocity: Velocity of path traveled in screen
 - Gaze angle: Angle with centroid of prev
 - Eye movement type: Type of eye movement event classified by the I-VT filter; Fixation: 1, Saccade: 2, else: 0
   
**(4) Fixation**
 - Reaction time: Time until the first fixation is made outside the cross point (equal to the first fixation time)
 - Fixation duration: Duration per fixation
 - Fixation dispersion: Spatial spread during a fixation
 - Fixation count: Number of fixation intervals identified within 84 sampled gaze points
   
   
**(5) Saccade**
 - Saccade duration: Duration per saccade
 - Saccade velocity: Angular velocity per saccade
 - Saccade amplitude: Angular distance per saccade
 - Saccade dispersion: Spatial spread during a saccade
 - Saccade count: Number of saccade intervals identified within 84 sampled gaze points
   
**(6) MFCC**
 - 12 Mel-frequency ceptral coefficients for overall stimuli


**(7) Pupil**
 - Left pupil diameter: Pupil diameter of left eye
 - Right pupil diameter: Pupil diameter of right eye
 - Filtered pupil diameter: Pupil diameter after applying pupil diameter filter (noise reduction by moving median)


**Additional Explanation for fixation and saccade**
<img width="800" alt="Fixation and Saccade" src="https://github.com/user-attachments/assets/36d50e71-019d-4ee3-a880-750fa114f639">


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
Pre-AttentiveGaze/
├── data/
│   ├── Raw Dataset/
│   │   ├── Trial data/
│   │   └── Validation data.tsv
│   └── Gaze Feature Dataset/
│       ├── MultipleVC.tsv
│       └── SingleVC.tsv
├── Figure4.ipynb
├── Figure5.ipynb
├── Figure8.ipynb
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


## Citation

If you use this dataset, please cite:

**Jeon, J., Noh, YG., Kim, J. et al.**  
Pre-AttentiveGaze: gaze-based authentication dataset with momentary visual interactions.  
*Scientific Data*, **12**, 263 (2025).  
[DOI: 10.1038/s41597-025-04538-3](https://doi.org/10.1038/s41597-025-04538-3)

#### Subjects
- Electrical and Electronic Engineering
- Research Data


