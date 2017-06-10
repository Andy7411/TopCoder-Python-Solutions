class WidgetRepairs(object):
    def days(self, tuples, max_repair):
        new = 0
        day_count = 0
        for num in tuples:
            num += new
            if num == 0:
                pass
            elif (num < max_repair):
                new = 0
                day_count += 1
            else:
                new = num - max_repair
                day_count += 1
        day_count += new/float(max_repair)
        return int(day_count)
