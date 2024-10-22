# Original file: Christian Domingo
def encoder(password):
    encoded_password = ""
    temp_list = list(password)
    for i in range(len(temp_list)):
        if temp_list[i] == "7":
            encoded_password += "0"
        elif temp_list[i] == "8":
            encoded_password += "1"
        elif temp_list[i] == "9":
            encoded_password += "2"
        else:
            encoded_password += str(int(temp_list[i]) + 3)
    return encoded_password

#Added by Yiqiao (Emily) Huang
def decoder(password_to_decode):
    decoded_pass_list = []
    for letter in password_to_decode:
        decoded_pass_list.append(str((int(letter) - 3 + 10) % 10))
    return "".join(decoded_pass_list)

def main():
    is_running = True
    while is_running:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        # Option 2 added by Yiqiao (Emily) Huang
        if menu_option == 2:
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
            print()
        # Option 3 added by Yiqiao (Emily Huang
        if menu_option == 3:
            is_running = False


if __name__ == '__main__':
    main()