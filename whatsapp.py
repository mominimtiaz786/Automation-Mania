import pywhatkit

group_id = "" # get from whatsapp group invite link

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+92xxxxxxxxxx", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+92xxxxxxxxxx", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image(f"{group_id}", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+92xxxxxxxxxx", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group(f"{group_id}", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")