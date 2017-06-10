tup = []
class InterestingDigits(object):
    
    def digits(self, base):
        for i in range(2,base):
            x = 1
            count = 0
            while i*x < base**3:
                mul = i*x
                sum_of = InterestingDigits.sum_(self, mul, base)
                
                if (sum_of%i) != 0:
                    count += 1
                    x += 1
            if count == 0:
                tup.append(i)
        return tuple(tup)

    def sum_(self, item, base):

        pol = 0
        while item != 0:
            pol += item%base 
            item /= base
        return pol

