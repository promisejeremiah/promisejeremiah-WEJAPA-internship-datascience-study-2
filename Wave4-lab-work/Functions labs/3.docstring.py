def readable_timedelta(days):
    # insert your docstring here
    
    """
    This function returns a string of the number of weeks and days included in days.

    Input:
    days = This is number of days to be converted to (int)

    Output:
    The string of the number of weeks and days included in days
    
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
