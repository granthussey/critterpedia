import flaskapp.ac_df_tools as ac_tls
import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY_ACNH")


class FishDatabase:
    BACKEND_FISH_DF = ac_tls.get_backend_fish_df()
    ENDUSER_FISH_DF = ac_tls.filter_backend_table(BACKEND_FISH_DF)

    AVAIL_FISH = BACKEND_FISH_DF[BACKEND_FISH_DF.columns[0]].sort_values().unique()

    AVAIL_MONTHS = (
        BACKEND_FISH_DF.loc[:, "January":"December"].columns.unique().tolist()
    )


class BugDatabase:
    BACKEND_BUG_DF = ac_tls.get_backend_bug_df()
    ENDUSER_BUG_DF = ac_tls.filter_backend_table(BACKEND_BUG_DF)

    AVAIL_BUGS = BACKEND_BUG_DF[BACKEND_BUG_DF.columns[0]].sort_values().unique()

    AVAIL_MONTHS = BACKEND_BUG_DF.loc[:, "January":"December"].columns.unique().tolist()
