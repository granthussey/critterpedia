import pandas as pd
import numpy as np


def filter_backend_table(backend_df):

    # Bug doesn't have "Shadow size" column
    if backend_df.columns[0] == "Bug":
        return backend_df.filter(
            items=[backend_df.columns[0], "Location", "Price", "From", "To",]
        )

    # Fish does have "Shadow size" column
    elif backend_df.columns[0] == "Fish":
        return backend_df.filter(
            items=[
                backend_df.columns[0],
                "Location",
                "Shadow size",
                "Price",
                "From",
                "To",
            ]
        )


def filter_df_by_critter_name(backend_df, enduser_df, selected_critter):

    if isinstance(selected_critter, str):
        selected = backend_df[backend_df.columns[0]] == selected_critter
    else:
        selected = [True] * len(backend_df)

    return enduser_df.loc[selected]


def filter_df_by_month_name(backend_df, enduser_df, selected_months):

    if isinstance(selected_months, str):
        selected = backend_df[selected_months]
    else:
        selected = [True] * len(backend_df)

    return enduser_df.loc[selected]


def filter_df_by_species_arriving(BACKEND_DF, enduser_df, AVAIL_MONTHS, selected_month):
    """"can be used for bugs & fish I think"""

    # Explaination
    # Get "Arriving in March" -> GIVES YOU "MARCH" value (3)
    # But fish arriving in march (3) are fish NOT in feb (2)
    # So I need fish that are in APRIL but NOT in March

    # print(AVAIL_MONTHS)
    # print(selected_month)

    # find index of selected month
    cur_month = AVAIL_MONTHS.index(selected_month)

    # wrap around if December
    prev_month = cur_month - 1

    cur_vector = BACKEND_DF[AVAIL_MONTHS[cur_month]]
    prev_vector = BACKEND_DF[AVAIL_MONTHS[prev_month]]
    selected = cur_vector & ~prev_vector

    # creatures NOT in this month but DEFINITELY next month
    return enduser_df.loc[selected]


def filter_df_by_species_leaving(BACKEND_DF, enduser_df, AVAIL_MONTHS, selected_month):
    """"can be used for bugs & fish I think"""

    # find index of selected month
    cur_month = AVAIL_MONTHS.index(selected_month)

    # wrap around if December
    if cur_month == 11:
        next_month = 0
    else:
        next_month = cur_month + 1

    cur_vector = BACKEND_DF[AVAIL_MONTHS[cur_month]]
    next_vector = BACKEND_DF[AVAIL_MONTHS[next_month]]
    selected = cur_vector & ~next_vector

    # creatures NOT in this month but DEFINITELY next month
    return enduser_df.loc[selected]


# to read in from a public Google Sheet
def get_backend_fish_df():
    return download_creature_data("fish")


def get_backend_bug_df():
    return download_creature_data("bugs")


def download_creature_data(creature_type):
    """creature_type is the worksheet name in the Google Sheet, either fish or bugs"""

    google_sheet_id = "1YXGasmPBqnTw1B5gIfWA-ci7NiO-EdtS-PsxjNrYUls"
    #     worksheet_name = creature_type
    URL = "https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(
        google_sheet_id, creature_type
    )

    df = pd.read_csv(URL)
    df = df.drop(columns=["Unnamed: 0",])
    return df
