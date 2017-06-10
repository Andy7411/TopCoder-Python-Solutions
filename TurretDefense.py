class TurretDefense(object):
    def firstMiss(self, x, y, times):

        if times[0] < x[0] + y[0]:
            return 0
        else:
            for i in range(1, len(x)):
                time = times[i] - times[i - 1]
                x_ = abs(x[i] - x[i - 1])
                y_ = abs(y[i] - y[i - 1])
                if time >= (x_ + y_):
                    pass
                else:
                    return i

            else:
                return -1
