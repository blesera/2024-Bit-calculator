# ask users for file type (integer/ image / text/ xxx)

def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"

        # check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text...
        elif response in ["text", 'txt' 't']:
            return "text"

    # if the response is invalid output an error
        else:
            print ("please enter a valid file type")


#Main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i' ask if they qant an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an imagine . ")
        if want_image == "":
            file_type = "integer"
        else
            file_type = "image"

        print(f"You choose {file_type}")

        if file_type == "xxx":
            break
