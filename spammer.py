#!/usr/bin/python

# - Spammer v9.9
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: RecordStudio
# | Date: 25/04/2018
# | Disclaimer: Editing author will not make you the real coder
# | What's New?
# | - Fixed 403 forbidden
# | - Use less CPU

import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "RecordStduiio
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC+"\n"
    exit()
