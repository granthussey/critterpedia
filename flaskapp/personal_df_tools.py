import pandas as pd
import numpy as np


def generate_row_list(df):

    compound_row_List = [each_row for each_row in df.iterrows()]
    row_list = [each_compound_row[1] for each_compound_row in compound_row_List]

    return row_list
