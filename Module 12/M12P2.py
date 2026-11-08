#Iana Vasileva  CIS160 B65   M112P2 11/8/26
# Add another array to problem M12P1.
# This array should contain exam score for the respective students. That is, the first name goes with the first score etc.
# Modify the display functions to include exam score array in addition to the last name array.

last_names=["John","Smith","Malone","Barrington","King","Anderson","Townsend","Lee","Miller","Robinson"]
exam_scores=[100,95,98,94,92,93,88,99,78,80]

#Define functions
def display_names(last_names,exam_scores):
    for i in range(len(last_names)):
        print("Last name: ",last_names[i],", exam score is: ",exam_scores[i])

#Call function
display_names(last_names,exam_scores)
