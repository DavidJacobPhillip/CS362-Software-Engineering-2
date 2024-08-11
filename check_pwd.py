def check_pwd(string):
    # if password is greater than or equal to 8 digits or less than or equal to 20 digits
    if len(string) >= 8 and len(string) <= 20:

        # if password has lowercase digits
        for letter in string:
            if letter.islower() == True:

                # if password has uppercase digits
                for letter in string:
                    if letter.isupper() == True:

                        # if password has digits
                        for letter in string:
                            if letter.isdigit() == True:

                                # if password has symbols
                                symbols = "~`!@#$%^&*()_+-="
                                for letter in string:
                                    if letter in symbols:
                                        return True

    return False
