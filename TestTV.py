class TestTV:

    #Import file TV Program.py
    from TV import TV

    #Methods of TestTV
    def main():

        #tv1's channel is 30 and volume level is 3

        #Object 1 of the TV class
        tv1 = TV()

        #Turn on TV 1
        tv1.turn_on()

        #Set TV 1's channel and volume level
        tv1.set_channel(30)
        tv1.set_volume(3)

        #Print the channel and volume level that is set for TV 1
        print("tv1's channel", tv1.get_channel(), "and volume level is", tv1.get_volume())


        #tv2's channel is 3 and volume level is 2
