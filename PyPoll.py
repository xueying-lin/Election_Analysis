#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


##How to read the csv file
#Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
#file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file.
#election_data = open(file_to_load, "r")

#To do: peform analysis.

#Close file
#election_data.close()

     #Alternative one, using with() function to replace open() and close()
with open(file_to_load) as election_data: 
    
    #To do: read and analyze the data here.
   file_reader = csv.reader(election_data)
   
   #print the header row.
   headers = next(file_reader)
   print(headers)
   #print each row in the CSV file.
   #for row in file_reader:
       #print(row)


##How to write a file
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

#Using the with statement open the file as a text file.
#with open(file_to_save, "w") as outfile:            
#Write some data to the file.
    #Write the header
    #outfile.write("Counties in the Election\n-------------------------\n")
    
    #write three counties to the file.
      #outfile.write("Arapahoe, ")
      #outfile.write("Denver, ")
      #outfile.write("Jefferson")
      #outfile.write("Arapahoe, Denver, Jefferson")
      #Put the county in each line
    #outfile.write("Arapahoe\nDenver\nJefferson")

#Close the file
#outfile.close()