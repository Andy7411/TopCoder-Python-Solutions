class Whisper(object):
    def toWhom(self, usernames, typed):
        whisper = []
        whisper_to = ""
        typed = typed.lower()
        whisper = typed.split()
        n = len(whisper)
        
        usernames = list(usernames)
        count = 0
        if len(usernames) == 1:
            if ' ' in usernames[0]:
                count += 1
            count += 1
            if count >= 2:
                name = ""

                for i in range(1, 1 + count):
                    name += whisper[i] + " "

                if name == usernames[0].lower():
                    return usernames[0]
                else:
                    return "user not logged in"
            elif whisper[1] == usernames[0].lower() and count == 1:
                return usernames[0]
            else:
                return "user not logged in"


        
        if "msg" in usernames and whisper[0] == "/msg":
            return "not a whisper"
            
        if (whisper[0] != "/msg"):
            return "not a whisper"

        i = 1
        while i < n:
            count = 0
            for name in usernames:
                if len(name) == 1:
                    username = tuple(usernames)
                    #print usernames
                #print name.lower()
                if whisper[i] == name.lower():
                    whisper_to = name
                    count = 1
                    break

            if count == 0 and len(whisper_to) == 0:
                return "user not logged in"
            elif count == 0:
                return whisper_to           
            elif count == 1 and i+1 < n:
                whisper[i+1] = whisper[i] + " " + whisper[i+1]

            i += 1

