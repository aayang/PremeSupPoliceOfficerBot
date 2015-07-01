# PremeSupPoliceOfficerBot


# Getting Started
1. Say this out loud: "I am the pinnacle fuq boi for using this bot"
1. Install Python
1. Install selenium for python 
1. Confirm that it works by making a new [FILE_NAME].py and try importing 
   selenium by typing "from selenium import webdriver"

1. Download this and configue with your information on the Checkout part of
   Store: https://addons.mozilla.org/en-US/firefox/addon/autofill-262804/
   (Or use the coded in autofil but its slow by about 3 seconds)

1. After you configue autofill, find the address of the firefox profile on your
   computer (look at the code for example path (on my computer))

1. TEST IT WITH BAD INFO FIRST BECAUSE IT WILL BUY SHIT IF YOU RUN IT

1. Go into code and edit items under "PARTS YOU SHOULD EDIT"

1. Delete the specififed lines at around 103 or so if you want to use it for
real (I put that there for testing purposes, basically it refreshes 3 times
      only and then selects the item, if you delete the specified line, then it
      will continue to refresh the new page until the item with the specified
      keywords pop up)

1. execute by typing "python supremeCopBot.py" (or "python supremeCopBotMac.py)
1. Enjoy how much of a fuq boi you are
1. Tip Aaron if you copped something (jk but it would be nice, at least let me
      know if it worked for you)


# High level description of how it works
1. Goes to the shop and adds an item to cart and go to the checkout page to
buffer the checkout page, then removes the item
1. Then goes to the new section and refreshes, compiling all the links of the
items into an array
1. Checks if the first item is the same as the old item when we first started
program
1. If so, refresh the page again and repeat until first item changes (means
      shop was updated)
1. If first item changes start searching the array of links for keywords
1. The first result that contains both keywords is clicked
1. The item is added to cart and then checked out

