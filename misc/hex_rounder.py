

def round_up_to_zero_ending_hexidecimal(number):
    try:
        num = int(number)
        while str(hex(num))[-1] <> "0":
            print(hex(num))
            num +=1

        return num
    except:
        print("can't convert the provided parameter")
        quit

i = 17
h = round_to_zero_ending_hexidecimal(i)
print("i rounded up "  + str((h-i)) \
      + " to get from " +str(i) + " to " \
      + str(h) + " to get a round hex " + str(hex(h)))
