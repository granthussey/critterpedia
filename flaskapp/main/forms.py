from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, SelectField
from wtforms.validators import DataRequired

from flaskapp.config import FishDatabase
from flaskapp.config import BugDatabase


class BaseFish(FlaskForm):
    pass


class FishNameForm(FlaskForm):

    fish_name = SelectField(
        "Filter fish by name",
        choices=[
            (value, label)
            for value, label in zip(FishDatabase.AVAIL_FISH, FishDatabase.AVAIL_FISH)
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class FishMonthForm(FlaskForm):
    month_name = SelectField(
        "Filter fish by month active",
        choices=[
            (value, label)
            for value, label in zip(
                FishDatabase.AVAIL_MONTHS, FishDatabase.AVAIL_MONTHS
            )
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class FishArrivingForm(FlaskForm):
    month_arriving = SelectField(
        "Find fish coming to your island",
        choices=[
            (month, "Arriving in {}".format(month))
            for month in FishDatabase.AVAIL_MONTHS
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class FishLeavingForm(FlaskForm):
    month_leaving = SelectField(
        "Find fish leaving your island",
        choices=[
            (month, "Leaving after {}".format(month))
            for month in FishDatabase.AVAIL_MONTHS
        ],
        # validators=[DataRequired()],
    )

    submit = SubmitField("Go")


class ResetFishForm(FlaskForm):
    submit = SubmitField("See full table")


class BugNameForm(FlaskForm):

    bug_name = SelectField(
        "Filter bug by name",
        choices=[
            (value, label)
            for value, label in zip(BugDatabase.AVAIL_BUGS, BugDatabase.AVAIL_BUGS)
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class BugMonthForm(FlaskForm):
    month_name = SelectField(
        "Filter bug by month active",
        choices=[
            (value, label)
            for value, label in zip(BugDatabase.AVAIL_MONTHS, BugDatabase.AVAIL_MONTHS)
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class BugArrivingForm(FlaskForm):
    month_arriving = SelectField(
        "Find bug coming to your island",
        choices=[
            (month, "Arriving in {}".format(month))
            for month in BugDatabase.AVAIL_MONTHS
        ],
        # validators=[DataRequired()],
    )
    submit = SubmitField("Go")


class BugLeavingForm(FlaskForm):
    month_leaving = SelectField(
        "Find bug leaving your island",
        choices=[
            (month, "Leaving after {}".format(month))
            for month in BugDatabase.AVAIL_MONTHS
        ],
        # validators=[DataRequired()],
    )

    submit = SubmitField("Go")


class ResetBugForm(FlaskForm):
    submit = SubmitField("See full table")
