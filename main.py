def choose_practicum ():
    practicum = input("Please sign up for a practicum: ")
    if practicum == "Costumes" or practicum == "Scenery" or practicum == "Lighting" or practicum == "Sound":
        return practicum
    else:
        print("ERROR! Not a valid practicum. Please choose from costumes, scenery, lighting, or sound.")
        choose_practicum()
def main ():
    name = input("What is your name?: ")
    practicum_choice = choose_practicum()
    print(f"Congratulations {name} you are signed up for {practicum_choice}")
main()