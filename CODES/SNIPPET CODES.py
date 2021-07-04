# SET THE X AND Y POSITION AND THE SIZE OF THE WINDOW
MainSystemWindow.setGeometry(50, 60, 1824, 954)

# ----------------------------------------------------------------------------------------------------------------------

# GETTING DATE TODAY (MONTH, DAY, YEAR, TIME, AM/PM)
today = datetime.today()
date_today = today.strftime("%B %d, %Y") + " " + datetime.today().strftime("%I:%M %p")
print("Date Today =", date_today)

# ----------------------------------------------------------------------------------------------------------------------