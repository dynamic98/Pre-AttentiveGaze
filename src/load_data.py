import os
import pandas as pd
import numpy as np

this_file_path = os.path.dirname(__file__)
data_file_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'data', 'Gaze Feature Dataset')

def load_data(file_name: str):
    data = pd.read_csv(os.path.join(data_file_path, file_name), sep='\t')
    serial_columns = ['x', 'y', 'gaze_velocity', 'gaze_angle', 'mfcc', 'left_pupil_diameter', 'right_pupil_diameter',
        'filtered_pupil_diameter', 'eye_movement_type', 'fixation_duration', 'fixation_dispersion',
        'saccade_duration', 'saccade_dispersion', 'saccade_velocity',
        'saccade_amplitude']
    for column in serial_columns:
        data[column] = data[column].apply(lambda x: x[1:-1].split(','))     
    return data


if __name__ == "__main__":
    pass