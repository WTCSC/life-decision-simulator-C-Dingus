def read_msg(message):
    with open("messages.ook", "r") as file:
        return file.read().split(f"%msg{message}%")[1].strip()

choice = input(f"{read_msg(0)}\n")

if choice == "1":
    choice = input(f"{read_msg(1)}\n")

    choice = input(f"{read_msg(3)}\n")
    if choice == "1":
        choice = input(f"{read_msg(6)}\n")
        choice = input(f"{read_msg(7)}\n")
        choice = input(f"{read_msg(10)}\n")
        choice = input(f"{read_msg(14)}\n")
        choice = input(f"{read_msg(16)}\n")
        #END
    else:
        choice = input(f"{read_msg(7)}\n")
        choice = input(f"{read_msg(10)}\n")
        choice = input(f"{read_msg(14)}\n")
        choice = input(f"{read_msg(16)}\n")
        #END

else:
    choice = input(f"{read_msg(2)}\n")
    if choice == "1":
        while True:
            choice = input(f"{read_msg(4)}\n")
            if choice != "1":
                choice = input(f"{read_msg(5)}\n")
                if choice == "1":
                    choice = input(f"{read_msg(9)}\n")
                    if choice == "1":
                        choice = input(f"{read_msg(12)}\n")
                        if choice == "1":
                            choice = input(f"{read_msg(13)}\n")
                            if choice == "1":
                                choice = input(f"{read_msg(15)}\n")
                                choice = input(f"{read_msg(14)}\n")
                                choice = input(f"{read_msg(16)}\n")

                                break
                    else:
                        choice = input(f"{read_msg(13)}\n")
                        if choice == "1":
                            choice = input(f"{read_msg(15)}\n")
                            choice = input(f"{read_msg(14)}\n")
                            choice = input(f"{read_msg(16)}\n")
                            break
            else:
                choice = input(f"{read_msg(8)}\n")
                if choice == "1":
                    choice = input(f"{read_msg(5)}\n")
                    if choice == "1":
                        choice = input(f"{read_msg(9)}\n")
                        if choice == "1":
                            choice = input(f"{read_msg(12)}\n")
                            if choice == "1":
                                choice = input(f"{read_msg(13)}\n")
                                if choice == "1":
                                    choice = input(f"{read_msg(15)}\n")
                                    choice = input(f"{read_msg(14)}\n")
                                    choice = input(f"{read_msg(16)}\n")
                                    break
                        else:
                            choice = input(f"{read_msg(13)}\n")
                            if choice == "1":
                                choice = input(f"{read_msg(15)}\n")
                                choice = input(f"{read_msg(14)}\n")
                                choice = input(f"{read_msg(16)}\n")
                                break
    else:
        while True:
            choice = input(f"{read_msg(5)}\n")
            if choice == "1"
                if choice == "1":
                    choice = input(f"{read_msg(9)}\n")
                    if choice == "1":
                        choice = input(f"{read_msg(12)}\n")
                        if choice == "1":
                            choice = input(f"{read_msg(13)}\n")
                            if choice == "1":
                                choice = input(f"{read_msg(15)}\n")
                                choice = input(f"{read_msg(14)}\n")
                                choice = input(f"{read_msg(16)}\n")
                                break
                        else:
                            choice = input(f"{read_msg(13)}\n")
                            if choice == "1":
                                choice = input(f"{read_msg(15)}\n")
                                choice = input(f"{read_msg(14)}\n")
                                choice = input(f"{read_msg(16)}\n")
                                break
            else:
                choice = input(f"{read_msg(4)}\n")
                if choice != "1":
                    choice = input(f"{read_msg(8)}\n")
                    if choice == "1":







