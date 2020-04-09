from flask import render_template
from flask import request
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import url_for

from flaskapp.config import FishDatabase
from flaskapp.config import BugDatabase


import flaskapp.personal_df_tools as tls
import flaskapp.ac_df_tools as ac_tls

main = Blueprint("main", __name__)

from .forms import (
    FishNameForm,
    FishMonthForm,
    FishLeavingForm,
    FishArrivingForm,
    ResetFishForm,
)


from .forms import (
    BugNameForm,
    BugMonthForm,
    BugLeavingForm,
    BugArrivingForm,
    ResetBugForm,
)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html", title="About")


@main.route("/fish", methods=["GET", "POST"])
def fish():
    fish_name_form = FishNameForm()
    fish_month_form = FishMonthForm()
    fish_leaving_form = FishLeavingForm()
    fish_arriving_form = FishArrivingForm()
    reset_fish_form = ResetFishForm()

    if fish_name_form.validate_on_submit():
        # print("DONE FISH NAME")
        # print(fish_name_form.errors)
        # print(fish_name_form.fish_name.data)
        # print(type(fish_name_form.fish_name.data))

        # filtered_df = FishDatabase.ENDUSER_FISH_DF.sort_values("Location")
        filtered_df = ac_tls.filter_df_by_critter_name(
            FishDatabase.BACKEND_FISH_DF,
            FishDatabase.ENDUSER_FISH_DF,
            fish_name_form.fish_name.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "fish.html",
            fish_name_form=fish_name_form,
            fish_month_form=fish_month_form,
            fish_arriving_form=fish_arriving_form,
            fish_leaving_form=fish_leaving_form,
            reset_fish_form=reset_fish_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Fish",
        )

    if fish_month_form.validate_on_submit():
        # print("DONE FISH MONTH")
        # print(fish_month_form.errors)
        # print(fish_month_form.month_name.data)
        # print(type(fish_month_form.month_name.data))

        filtered_df = ac_tls.filter_df_by_month_name(
            FishDatabase.BACKEND_FISH_DF,
            FishDatabase.ENDUSER_FISH_DF,
            fish_month_form.month_name.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "fish.html",
            fish_name_form=fish_name_form,
            fish_month_form=fish_month_form,
            fish_arriving_form=fish_arriving_form,
            fish_leaving_form=fish_leaving_form,
            reset_fish_form=reset_fish_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Fish",
        )

    if fish_leaving_form.validate_on_submit():
        # print("DONE FISH LEAVING")
        # print(fish_leaving_form.errors)
        # print(fish_leaving_form.month_leaving.data)
        # print(type(fish_leaving_form.month_leaving.data))

        filtered_df = ac_tls.filter_df_by_species_leaving(
            FishDatabase.BACKEND_FISH_DF,
            FishDatabase.ENDUSER_FISH_DF,
            FishDatabase.AVAIL_MONTHS,
            fish_leaving_form.month_leaving.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "fish.html",
            fish_name_form=fish_name_form,
            fish_month_form=fish_month_form,
            fish_arriving_form=fish_arriving_form,
            fish_leaving_form=fish_leaving_form,
            reset_fish_form=reset_fish_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Fish",
        )

    if fish_arriving_form.validate_on_submit():
        # print("DONE FISH ARRIVING")
        # print(fish_arriving_form.errors)
        # print(fish_arriving_form.month_arriving.data)
        # print(type(fish_arriving_form.month_arriving.data))

        filtered_df = ac_tls.filter_df_by_species_arriving(
            FishDatabase.BACKEND_FISH_DF,
            FishDatabase.ENDUSER_FISH_DF,
            FishDatabase.AVAIL_MONTHS,
            fish_arriving_form.month_arriving.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "fish.html",
            fish_name_form=fish_name_form,
            fish_month_form=fish_month_form,
            fish_arriving_form=fish_arriving_form,
            fish_leaving_form=fish_leaving_form,
            reset_fish_form=reset_fish_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Fish",
        )

    if reset_fish_form.validate_on_submit():

        return render_template(
            "fish.html",
            fish_name_form=fish_name_form,
            fish_month_form=fish_month_form,
            fish_arriving_form=fish_arriving_form,
            fish_leaving_form=fish_leaving_form,
            reset_fish_form=reset_fish_form,
            table_exists=True,
            selected_df=FishDatabase.ENDUSER_FISH_DF,
            row_list=tls.generate_row_list(FishDatabase.ENDUSER_FISH_DF),
            title="Fish",
        )

    return render_template(
        "fish.html",
        fish_name_form=fish_name_form,
        fish_month_form=fish_month_form,
        fish_arriving_form=fish_arriving_form,
        fish_leaving_form=fish_leaving_form,
        reset_fish_form=reset_fish_form,
        table_exists=False,
        selected_df=None,
        row_list=None,
        title="Fish",
    )


@main.route("/bugs", methods=["GET", "POST"])
def bugs():
    bug_name_form = BugNameForm()
    bug_month_form = BugMonthForm()
    bug_leaving_form = BugLeavingForm()
    bug_arriving_form = BugArrivingForm()
    reset_bug_form = ResetBugForm()

    if bug_name_form.validate_on_submit():
        # print("DONE bug NAME")
        # print(bug_name_form.errors)
        # print(bug_name_form.bug_name.data)
        # print(type(bug_name_form.bug_name.data))

        # filtered_df = BugDatabase.ENDUSER_BUG_DF.sort_values("Location")
        filtered_df = ac_tls.filter_df_by_critter_name(
            BugDatabase.BACKEND_BUG_DF,
            BugDatabase.ENDUSER_BUG_DF,
            bug_name_form.bug_name.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "bugs.html",
            bug_name_form=bug_name_form,
            bug_month_form=bug_month_form,
            bug_arriving_form=bug_arriving_form,
            bug_leaving_form=bug_leaving_form,
            reset_bug_form=reset_bug_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Bugs",
        )

    if bug_month_form.validate_on_submit():
        # print("DONE bug MONTH")
        # print(bug_month_form.errors)
        # print(bug_month_form.month_name.data)
        # print(type(bug_month_form.month_name.data))

        filtered_df = ac_tls.filter_df_by_month_name(
            BugDatabase.BACKEND_BUG_DF,
            BugDatabase.ENDUSER_BUG_DF,
            bug_month_form.month_name.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "bugs.html",
            bug_name_form=bug_name_form,
            bug_month_form=bug_month_form,
            bug_arriving_form=bug_arriving_form,
            bug_leaving_form=bug_leaving_form,
            reset_bug_form=reset_bug_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Bugs",
        )

    if bug_leaving_form.validate_on_submit():
        # print("DONE bug LEAVING")
        # print(bug_leaving_form.errors)
        # print(bug_leaving_form.month_leaving.data)
        # print(type(bug_leaving_form.month_leaving.data))

        filtered_df = ac_tls.filter_df_by_species_leaving(
            BugDatabase.BACKEND_BUG_DF,
            BugDatabase.ENDUSER_BUG_DF,
            BugDatabase.AVAIL_MONTHS,
            bug_leaving_form.month_leaving.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "bugs.html",
            bug_name_form=bug_name_form,
            bug_month_form=bug_month_form,
            bug_arriving_form=bug_arriving_form,
            bug_leaving_form=bug_leaving_form,
            reset_bug_form=reset_bug_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Bugs",
        )

    if bug_arriving_form.validate_on_submit():
        # print("DONE bug ARRIVING")
        # print(bug_arriving_form.errors)
        # print(bug_arriving_form.month_arriving.data)
        # print(type(bug_arriving_form.month_arriving.data))

        filtered_df = ac_tls.filter_df_by_species_arriving(
            BugDatabase.BACKEND_BUG_DF,
            BugDatabase.ENDUSER_BUG_DF,
            BugDatabase.AVAIL_MONTHS,
            bug_arriving_form.month_arriving.data,
        )

        selected_df = filtered_df.sort_values("Location")

        return render_template(
            "bugs.html",
            bug_name_form=bug_name_form,
            bug_month_form=bug_month_form,
            bug_arriving_form=bug_arriving_form,
            bug_leaving_form=bug_leaving_form,
            reset_bug_form=reset_bug_form,
            table_exists=True,
            selected_df=selected_df,
            row_list=tls.generate_row_list(selected_df),
            title="Bugs",
        )

    if reset_bug_form.validate_on_submit():

        return render_template(
            "bugs.html",
            bug_name_form=bug_name_form,
            bug_month_form=bug_month_form,
            bug_arriving_form=bug_arriving_form,
            bug_leaving_form=bug_leaving_form,
            reset_bug_form=reset_bug_form,
            table_exists=True,
            selected_df=BugDatabase.ENDUSER_BUG_DF,
            row_list=tls.generate_row_list(BugDatabase.ENDUSER_BUG_DF),
            title="Bugs",
        )

    return render_template(
        "bugs.html",
        bug_name_form=bug_name_form,
        bug_month_form=bug_month_form,
        bug_arriving_form=bug_arriving_form,
        bug_leaving_form=bug_leaving_form,
        reset_bug_form=reset_bug_form,
        table_exists=False,
        selected_df=None,
        row_list=None,
        title="Bugs",
    )
