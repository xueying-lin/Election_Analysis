# Election_Analysis

## Overview of Election_Audit Analysis
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of counties that participated in the votes.
7. Get the percentage of votes from each county out of the total count.
8. Conclude the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election_Audit Results
With the analysis of the election_results.csv:
- **369,711** votes were cast in this congressional election
- The counties participated in the votes were: 
     - *Jefferson*: put **38,855** votes, accounting for **10.5%** of total votes.
     - *Denver*: put **306,055** votes, accounting for **82.8%** of total votes.
     - *Arapahoe*: put **24,801** votes, accounting for **6.7%** of total votes.
- The county with the largest number of votes was:
   - *Denver*, that contributed **82.8%** of the vote and **306,055** of total votes.
- The candidates results were:
    - *Charles Casper Stockham* received **23.0%** of the vote and **85,213** number of votes.
    - *Diana DeGette* received **73.8%** of the vote and **272,892** number of votes.
    - *Raymon Anthony Doane* received **3.1%** of the vote and **11,606** number of votes.
- The winner of the election was:
    - *Diana DeGette*, who received **73.8%** of the vote and **272,892** number of votes.

## Election-Audit Summary
There are two modification could be applied to this scrip, in order to be used for any election.
1. Ignore the invalid vote
- Since the election may be voted through multiple ways. 
- There are many potential reasons can lead to the incomplete or invalid data in the dataset of election results.
- This modification will ignore the data with any invalid ID name, to improve the validity of the analysis. The script will ask the analyst to enter all of the invalid ID names first. This portion of code will be add **before read the data.**
- This is how the script will look like:
```
#Initialize a invalid ID list
ID_invalid = []
#Ask analyst to enter the invalid ID name
invalid = input("Please enter all the invalid ID name(one name at once, enter'end'to close the file):")
#Store the input invalid ID name into the list
while invalid != "end":
    ID_invalid.append(invalid)
    invalid = input("Please enter all the invalid ID name(one name at once, enter'end'to close the file):")
#Print the invalid ID list to double check
print(ID_invalid)
```
And then, after read the file, we need to add a script within the for loop, before we count the name of counties and candidates as follows:
```
...
....
  # For each row in the CSV file.
    for row in reader:
        #Check if the ID is valid
        if row[0] not in ID_invalid:
            # Add to the total vote count
            total_votes = total_votes + 1

            # Get the candidate name from each row.
            candidate_name = row[2]

            # 3: Extract the county name from each row.
            county_name = row[1]


            # If the candidate does not match any existing candidate add it to
            # the candidate list
            if candidate_name not in candidate_options:

                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
......
......
```

2. Do the data analysis for selected variable
- The original script use the index number of county and candidate variables manually.
- But with the large dataset, there will be more variables need to be analyzed, so we can let the code help us to find the index location of the selected variable.
- For example, if we are looking for the variable of **county and candidate**, the script will be modified like this:
```
.....
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Read the header
        header = next(reader)
        for num in range(len(header)):
            if header[num] == "County":
                county_index = num
            elif header[num] == "Candidate":
                candidate_index = num
        print(county_index)
        print(candidate_index)
        
        for row in reader:
     # Add to the total vote count
            total_votes = total_votes + 1

            # Get the candidate name from each row.
            candidate_name = row[candidate_index]

            # 3: Extract the county name from each row.
            county_name = row[county_index]

.....
.....
```


