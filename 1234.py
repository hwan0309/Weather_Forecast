import numpy as np
import pandas as pd
import os
import math
from glob import glob
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

data_day_path = os.listdir('../project')
data_hour_path = os.listdir('../project')
data_day_path[0], data_hour_path[0]

('속초_day.csv', '속초_time.csv')

def get_columns (word):
    summary = pd.read_excel('속초_day.xls')
    avg_day = summary[summary['방법'] == word] ['일_컬럼'].values
    avg_tm= summary[summary['방법']== word]['시간_컬럼'].values
    avg_dict = dict(zip(avg_day, avg_tm))
    return avg_dict