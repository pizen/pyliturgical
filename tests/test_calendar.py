from datetime import date
import pytest

from pyliturgical import calendar


CAL_2017 = {
    calendar.ADVENT: date(2017, 12, 3),
    calendar.CHRISTMAS_DAY: date(2017, 12, 25),
    calendar.EPIPHANY: date(2017, 1, 6),
    calendar.BAPTISM_OF_THE_LORD: date(2017, 1, 8),
    calendar.TRANSFIGURATION: date(2017, 2, 26),
    calendar.ASH_WEDNESDAY: date(2017, 3, 1),
    calendar.LENT: date(2017, 3, 2),
    calendar.MAUNDAY_THURSDAY: date(2017, 4, 13),
    calendar.GOOD_FRIDAY: date(2017, 4, 14),
    calendar.HOLY_SATURDAY: date(2017, 4, 15),
    calendar.EASTER_SUNDAY: date(2017, 4, 16),
    calendar.EASTER: date(2017, 4, 17),
    calendar.EASTER: date(2017, 6, 3),
    calendar.PENTECOST: date(2017, 6, 4),
    calendar.TRINITY_SUNDAY: date(2017, 6, 11),
    calendar.CHRIST_THE_KING: date(2017, 11, 26),
    calendar.ORDINARY_TIME: date(2017, 7, 11)
}

CAL_2018 = {
    calendar.ADVENT: date(2018, 12, 2),
    calendar.CHRISTMAS_DAY: date(2018, 12, 25),
    calendar.EPIPHANY: date(2018, 1, 6),
    calendar.BAPTISM_OF_THE_LORD: date(2018, 1, 7),
    calendar.TRANSFIGURATION: date(2018, 2, 11),
    calendar.ASH_WEDNESDAY: date(2018, 2, 14),
    calendar.LENT: date(2018, 2, 15),
    calendar.MAUNDAY_THURSDAY: date(2018, 3, 29),
    calendar.GOOD_FRIDAY: date(2018, 3, 30),
    calendar.HOLY_SATURDAY: date(2018, 3, 31),
    calendar.EASTER_SUNDAY: date(2018, 4, 1),
    calendar.EASTER: date(2018, 4, 2),
    calendar.EASTER: date(2018, 5, 19),
    calendar.PENTECOST: date(2018, 5, 20),
    calendar.TRINITY_SUNDAY: date(2018, 5, 27),
    calendar.CHRIST_THE_KING: date(2018, 11, 25),
    calendar.ORDINARY_TIME: date(2018, 7, 11)
}

CAL_2019 = {
    calendar.ADVENT: date(2019, 12, 2),
    calendar.CHRISTMAS_DAY: date(2019, 12, 25),
    calendar.EPIPHANY: date(2019, 1, 6),
    calendar.BAPTISM_OF_THE_LORD: date(2019, 1, 13),
    calendar.TRANSFIGURATION: date(2019, 3, 3),
    calendar.ASH_WEDNESDAY: date(2019, 3, 6),
    calendar.LENT: date(2019, 3, 7),
    calendar.MAUNDAY_THURSDAY: date(2019, 4, 18),
    calendar.GOOD_FRIDAY: date(2019, 4, 19),
    calendar.HOLY_SATURDAY: date(2019, 4, 20),
    calendar.EASTER_SUNDAY: date(2019, 4, 21),
    calendar.EASTER: date(2019, 4, 22),
    calendar.EASTER: date(2019, 6, 8),
    calendar.PENTECOST: date(2019, 6, 9),
    calendar.TRINITY_SUNDAY: date(2019, 6, 16),
    calendar.CHRIST_THE_KING: date(2019, 11, 24),
    calendar.ORDINARY_TIME: date(2019, 7, 11)
}


@pytest.mark.parametrize('cal', [CAL_2017, CAL_2018, CAL_2019])
def test_seasons(cal):
    for expected in cal:
        actual, color = calendar.lookup(cal[expected])
        assert actual == expected


def test_default_calendar_year():
    cal = calendar.Calendar()
    assert cal.cal[calendar.LENT][0]['start'].year == date.today().year
