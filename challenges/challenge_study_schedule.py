def study_schedule(permanence_period, target_time):
    if (target_time is None or permanence_period is None):
        return None

    count = 0

    for student in permanence_period:

        if (type(student[0]) != int or type(student[1]) != int):
            return None
        if (student[0] <= target_time <= student[1]):
            count += 1

    return count
