==========================================================================================
					README
==========================================================================================

* In ~2-3 sentences, what does your project do?

This project gets 50 posts from a public group named 'Spurs Nation' and finds the most common word that is not a "stop word" among all of these posts. Then, the project makes a search on that word in the iTunes Search API and stores relevant information in a csv file.

* What files (by name) are included in your submission? List them all! MAKE SURE YOU INCLUDE EVERY SINGLE FILE YOUR PROGRAM NEEDS TO RUN, as well as a sample of its output file.

File list includes SI506_finalproject.py, SI506finalproject_cache.json, stopwords, README.txt, SAMPLE_Song.csv.

* What Python modules must be pip installed in order to run your submission? List them ALL (e.g. including requests, requests_oauthlib... anything someone running it will need!). Note that your project must run in Python 3.

Required modules: json, webbrowser, requests, and requests_oauthlib


* Explain SPECIFICALLY how to run your code. We should very easily know, after reading this:
    - What file to run (e.g. python SI506_finalproject.py). That's what we expect -- but tell us specifically, just in case.

You should run SI506_finalproject.py directly like "python SI506_finalproject.py"

    - Anything else (e.g. "There will be a prompt asking you to enter a word. You'll definitely get good data if you enter the word 'mountains', but you can try anything", or "You need to fill out secret_data.py with the Facebook key and secret" -- if you have to do something like this, you should include the FULL INSTRUCTIONS, just like we did. Not enough to say "just like PS9". Provide text or a link to tell someone exactly what to do to fill out a file they need to include.

No

    - Anything someone should know in order to understand what's happening in your program as it runs

No, it is plain and simple.

    - If your project requires secret data of YOUR OWN, and won't work with OURS (e.g. if you are analyzing data from a private group that is just yours and not ours), you must include the secret data we need in a file for us and explain that you are doing that. (We don't expect this to happen, but if it does, we still need to be able to run your program in order to grade it.)

* Where can we find all of the project technical requirements in your code? Fill in with the requirements list below.
-- NOTE: You should list (approximately) every single line on which you can find a requirement. If you have requirements written in different files, you should also specify which filename it is in! For example, ("Class definition: 26" -- if you begin a class definition on line 26 of your Python file)
It's ok to be off by a line or 2 but you do need to give us 100% of this information -- it makes grading much easier!

REQUIREMENTS LIST:
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):
Function in line 100~127
Invoking in line 122, 156, 160
    * If you relied upon FB data and did not cache it, say so here:
	I did not cache FB data.
* Define at least 2 classes, each of which fulfill the listed requirements:
Facebook: line 48~79
iTunes: line 163~177
* Create at least 1 instance of each class:
Facebook: Line 82, 83
iTunes: line 180, 181
* Invoke the methods of the classes on class instances:
Facebook: line 87
iTunes: line 185
* At least one sort with a key parameter:
Line 183
* Define at least 2 functions outside a class (list the lines where function definitions begin):
Line 17, 38, 105, 112, 124, 129
* Invocations of functions you define:
Line 39, 43, 122, 160, 130, 161
* Create a readable file:
Line 187~190
END REQUIREMENTS LIST

* Put any citations you need below. If you borrowed code from a 506 problem set directly, or from the textbook directly, note that. If you borrowed code from a friend/classmate or worked in depth with a friend/classmate, note that. If you borrowed code from someone else's examples on a website, note that.
1. Problem Set 8
2. Problem Set 9
3. https://requests-oauthlib.readthedocs.io/en/latest/examples/facebook.html
4. section_9_itunes_solution.py
5. https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
6. https://developers.facebook.com/docs/graph-api/reference

* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of how many lines, how many columns, which headers...?
The result of my code is that there will be a website popping up, showing the store page of longest song. And then, a csv file named Song.csv will be created to store the relevant information about the all the songs related to the most frequent word generated from Facebook.

* Make sure you include a SAMPLE version of the file this project outputs (this should be in your list of submitted files above!).

* Is there anything else we need to know or that you want us to know about your project? Include that here!
Note that there is a file named "stopwords" containing all the stop words, which is essential to the project.
