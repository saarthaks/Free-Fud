# Free Fu'd

The proper operation of this code relies on the UEM (University Event Management) website and their listings of all reservable, on-campus event booking. When student groups plan an event with food, UEM lists the event on their website with a Food Policy notice. Our web scraping takes advantage of this and filters by events from the current day which have this notice. 

The output from this search is then stored in a file 'list of food.txt'.

