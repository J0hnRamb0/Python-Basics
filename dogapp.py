print("Hello dog lovers. Here is the menu. Select a dog to learn more about it: ")

while True:

    print("1 is Labrador Retriever")
    print("2 is German Shepard ")
    print("3 is Bulldog")
    print("4 is Beagle")
    print("5 is Poodle")
    print("0 to Exit")

# print(intro)

    user = input("Please enter your name: ")

    breed = int(input("Select the dog breed from options 1 - 5: "))

#Labrador Retriever

    if breed == 1:
        print("Here are some interesting facts about Labrador Retrievers: \nOrigin: Labrador Retrievers originated in Newfoundland, Canada, not Labrador as their name suggests. \nPopularity: They are one of the most popular dog breeds in the world, known for their friendly and outgoing nature.")

    elif breed == 2:
        print("Here are 10 interesting facts about German Shepherds: \nOrigin: German Shepherds were originally bred in Germany in the late 19th century by Captain Max von Stephanitz. \nIntelligence: They are known for their high intelligence and are often ranked among the smartest dog breeds.")

    elif breed == 3:
        print("Bulldogs are charming and distinctive dogs! Here are some interesting facts about them: \nOrigin: Bulldogs were originally bred in England for bull-baiting, a cruel sport that was eventually banned. \nAppearance: They have a distinctive wrinkled face, pushed-in nose, and a muscular, stocky build.")

    elif breed == 4:
        print("Beagles are adorable and energetic dogs! Here are some interesting facts about them: \nOrigin: Beagles were originally bred in England for hunting small game like rabbits and hares. \nSize: They are a small to medium-sized breed, typically weighing between 20-30 pounds.")

    elif breed == 5:
        print("Poodles are elegant and intelligent dogs! Here are some interesting facts about them: \nOrigin: Poodles were originally bred in Germany as water retrievers, but they became popular in France, where they are now considered the national dog. \nSizes: Poodles come in three sizes: Standard, Miniature, and Toy.")

    elif breed == 0:
        print("Thank you for using the program. Goodbye!")
        break

    else:
        print("Invalid Choice, Please try again!")

