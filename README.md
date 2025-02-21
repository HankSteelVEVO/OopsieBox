Oopsie Box Documentation
Kaleb Kruse


0 - Introduction


	Congratulations on purchasing your very own Oopsie Box! Not that I’d sell it or anything, it’d be way too expensive for what you’re really getting. This guide should not only get your Oopsie Box set up, but also show you how to properly use and maintain it. 


1 - Setting Up


I made the box in a way (conceptually, not physically) so that it could last a long time and be reused with any group of people or for any purpose really. To start, all you need is your Oopsie Box, a USB type B cable and a computer to connect to that can run Python scripts. Below is a list of dependencies required for the Python script to run properly:

pyserial - This library is what allows the serial communication between the arduino and your computer.
gspread - This library allows the script to read and write to the Google Sheet. 
oauth2client - Allows interaction with resources that require authentication, especially those related to Google APIs.
desktop-notifier - Take a wild guess what this one does.

With all of these libraries installed on your computer, you’re ready to get the box up and running. Since the Arduino you’re being given already has code written to it, you won’t need to worry about uploading anything to it. However, if you do need to upload code to the Arduino, this can be done by connecting it to your computer, opening the oopsieBox.ino file and selecting the “Upload” button from the toolbar. The final step is to ensure oopsieBoxScript.py is running at all times. I recommend having it run on start-up for your computer.



2 - General Usage


	The Oopsie Box is fairly simple to use, but just in case, here’s a little run through. Someone says a bad word, someone who’s name is on the box, in a place they shouldn’t. While the script is running, push the button with their name on it. Boom. That’s it. You should receive a desktop notification saying who you selected and what their count is. If you’d like to decrement the count, hold the decrement button marked with an arrow in the bottom right corner of the box and press someone’s button. This will decrease their count by one and you will receive another desktop notification. If you are not receiving the desktop notifications, it is likely because your computer blocks notifications from Python. This can be changed in your notification settings.

	People come and go, but the Oopsie Box is eternal. If you need to swap out the names of the people in the box, it’s as easy as going to the shared Google Sheets and editing the names column. There will be a column dedicated to that person’s pin number, which matches up with the numbers next to the buttons on the box. I recommend labeling the box with something removable to make the process of switching out people easier. Other than that, the only other edit that needs to be made to the Google Sheet is resetting the Oopsie Count at whatever interval you’d like. Messing with the pin number column, moving the cells around, or otherwise adjusting the Google Sheet can cause the script to cease functioning properly. The script is looking for certain types of information in specific cells, and messing around too much with the Google Sheet can ruin that. So don’t do that I guess.

3 - Common Issues


	Oh my gosh, it stopped working, now what do I do? While I’d be more than happy to help repair the Oopsie Box if you need, if it’s a problem you can fix yourself I’d like to keep it that way. I’ll be going over a list of common foreseeable issues and their possible causes.

The box isn’t giving me desktop notifications.
	
	Like I mentioned earlier, the likely cause of this is that you have Python desktop notifications muted. Go into your notification settings and change this. Otherwise, it’s possible your desktop-notifications library isn’t installed, which would be really bad because if the script tries to use it and it’s not there the whole thing will throw an error and stop running. Ensure all the proper libraries are installed.

I got a desktop notification saying the value wasn’t updated correctly.

	This one is likely caused by a faulty connection to the Google Sheets. The fact that you got a desktop notification means that the serial connection between the Arduino and the computer is still going good, so the most likely issue is with the Google Sheets. This error is thrown when the script checks to see if the value was increased by one or decreased by one based on the last action and discovers it isn’t what it should be. This would likely be due to faulty permissions of the service account. If you see this one, go ahead and give me a call.

None of the buttons are working.

	This one could be for a myriad of different reasons. First, check to see if it’s plugged in. Next, make sure oopsieBoxScript.py is up and running. If both of these are good, it would likely be an issue with the serial communication between the computer and the Arduino. If this is the case, go ahead and give me a call. It might be as simple as the script listening to the wrong serial communication port, or it could be a larger issue such as the Arduino not getting any power from the computer.

A select few buttons are not working, or pushing a button is adding to the wrong person’s count.

	This would be the biggest pain to resolve, as these would likely mean an issue with the internal hardware. Unless you feel like busting out a soldering iron and poking through the rat’s nest that is the Oopsie Box internals, go ahead and give me a call and I can take a look around in there to see what’s going on.

	On a separate note, this would likely be caused by someone dropping the Oopsie Box. While it’s not fragile, it was still made by me, which means it’s probably just itching for the chance to break itself. So pretty please don’t drop it.

I don’t really like how the box looks.

	Unless you’d like to make another model and print it, you’re gonna just have to live with this one unfortunately.



4 - Conclusion


	That’s about all I’ve got in terms of how to use this. I’m really hopeful already seeing the reactions to it and I hope it helps. We’ve got a really great staff this year, and a lack of professionalism behind the front desk because they’re all friends and work well together is probably the best problem we could have, especially considering how it can be resolved like this. If you have any questions, let me know!

-Kaleb
