class Iditarod (object):
    
    def avgMinutes(self, list_string):
        total = 0
        for string_ in list_string:
            hh = int(string_[:2])
            mm = int(string_[3:5])
            xM = string_[6:8]
            n = int(string_[14:])
            

            if hh >= 8 and xM == "AM":
                time = 24*60*(n-1) + (hh-8)*60 + mm
                total += time
                
            elif xM == "PM":
                time = 24*60*(n-1) + (hh+4)*60 + mm
                total += time
                
            else:
                time = 24*60*(n-2) + (16+hh)*60 + mm
                total += time
        avg = total/len(list_string)
        return avg