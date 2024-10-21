def encoder(password):
    encoded_password = ""
    temp_list = list(password)
    for i in range(len(temp_list)):
        if temp_list[i] == "7":
            encoded_password += "0"
        if temp_list[i] == "8":
            encoded_password += "1"
        if temp_list[i] == "9":
            encoded_password += "2"
        else:
            encoded_password += str(int(temp_list[i]) + 3)
    return encoded_password

if __name__ == '__main__':
    while True:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")

