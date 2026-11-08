#Iana Vasileva  CIS160 B65   M112P3 11/8/26
#The data to load is lastname and score. You can do this from a file as done in M12P1-P2
# Add a function to the program to display the last name and highest score, last name and lowest score.

last_names=["John","Smith","Malone","Barrington","King","Anderson","Townsend","Lee","Miller","Robinson"]
exam_scores=[100,95,98,94,92,93,88,99,78,80]
high_var=0
low_var=999

#Define function
def high_low_var(last_names,exam_scores):
    high_score=high_var
    low_score=low_var
    for i in range(len(exam_scores)):
        if exam_scores[i]>high_score:
            high_score=exam_scores[i]
            high_name=last_names[i]

        if exam_scores[i]<low_score:
            low_score=exam_scores[i]
            low_name=last_names[i]

    #display results
    print("Highest score:",high_name,"-",high_score)
    print("Lowest score:",low_name,"-",low_score)

#Call function
high_low_var(last_names,exam_scores)


