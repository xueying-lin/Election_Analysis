counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print((counties[i]))

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, voters)

#Get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
    #print(county_dict)
#for num in range(len(voting_data)):
    #print(voting_data[num])


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]} registered voters.')