class Bullets(object):
    def match(self, guns, bullet):
        for i, gun in enumerate(guns):
            if gun == bullet:
                return i
            else:
                for j in range(1, len(gun)):
                    bullet = bullet[j:] + bullet[:j]
                    if bullet == gun:
                        return i
        else: 
            return -1

my = Bullets()
print my.match(("||| |","| | || "), "|||| ") 
            