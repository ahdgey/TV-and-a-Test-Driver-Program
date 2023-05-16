#Alexza Jean R. Catanoy
#BSCPE 1-4
#TV and a Test Driver Program named TestTV

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mClass named TV and a Test Driver program named TestTV".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

class TV:

    #Constructor
    def __init__(self):

        #channel: int (The current channel (1 to 120) of this TV.)
        self.channel = 1

        #volumelevel: int (The current volume (1 to 7) of this TV.)
        self.volumelevel = 1

        #on: bool (Indicates whether this TV is on/off)
        self.on = False

    
    
    

