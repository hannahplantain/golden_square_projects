## 1. Describe the Problem

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2. Design the Function Signature

#name: reading_estimate

#Parameters: the number of words the user has to read, an integer 

#Returns: a string with the appropriate message for the minutes:
    # under 200 words = "This text will take you less than 1 minute ro read"
    # 200-299 words or more = "This text will take you 1 minute to read"
    #300+ words = "This text will take you 2 minutes to read"


## EXAMPLE

#given 150 words, the outpur should be:
    #reading_estimate(150) => "This text will take you less than 1 minute to read"

#given 200 words, the output should be:
    #reading_estimate(200) => "This text will take you 1 minute to read"

#given 500 words, the output should be:
    #reading_estimate(500) => "This text will take you 2.5 minutes to read"


def reading_estimate(int):
    minutes = int // 200
    if minutes == 0:
        return f"This text will take you less than 1 minute to read"
    elif minutes == 1:
        return f"This text will take you approximately {minutes} minute to read"
    else:
        return f"This text will take you approximately {minutes} minutes to read"
    
print(reading_estimate(1200))
print(reading_estimate(5000))
print(reading_estimate(300))