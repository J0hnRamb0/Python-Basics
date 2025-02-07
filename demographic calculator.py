def get_voting_data():
    # Voting data from the 2024 election
    data = {
        "White": {"Trump": 58, "Harris": 40},
        "Black": {"Trump": 16, "Harris": 83},
        "Hispanic": {"Trump": 42, "Harris": 56},
        "Asian": {"Trump": 34, "Harris": 61},
        "Men": {"Trump": 53, "Harris": 45},
        "Women": {"Trump": 47, "Harris": 53},
        "18-29 years old": {"Trump": 36, "Harris": 60},
        "30-44 years old": {"Trump": 46, "Harris": 52},
        "45-64 years old": {"Trump": 50, "Harris": 49},
        "65+ years old": {"Trump": 52, "Harris": 45},
        "Income <$50,000": {"Trump": 55, "Harris": 35},
        "Income $50,000-$100,000": {"Trump": 49, "Harris": 39},
        "Income >$100,000": {"Trump": 54, "Harris": 26},
        "Union Household": {"Trump": 49, "Harris": 40},
        "Republican": {"Trump": 94, "Harris": 6},
        "Democrat": {"Trump": 5, "Harris": 94},
        "Independent": {"Trump": 41, "Harris": 54},
        "Conservative": {"Trump": 85, "Harris": 14},
        "Moderate": {"Trump": 34, "Harris": 38},
        "Liberal": {"Trump": 10, "Harris": 24},
    }
    return data

def calculate_votes(demographic, data):
    if demographic in data:
        trump_votes = data[demographic]["Trump"]
        harris_votes = data[demographic]["Harris"]
        return trump_votes, harris_votes
    else:
        return None

def main():
    data = get_voting_data()
    print("Demographic Groups:")
    for key in data.keys():
        print(f"- {key}")
    
    demographic = input("Enter the demographic group: ")
    result = calculate_votes(demographic, data)
    
    if result:
        trump_votes, harris_votes = result
        print(f"In the {demographic} demographic:")
        print(f"  - Trump received {trump_votes}% of the votes.")
        print(f"  - Harris received {harris_votes}% of the votes.")
    else:
        print("Invalid demographic group. Please try again.")
        
if __name__ == "__main__":
    main()
