import random
def get_choice(options, prompt):
    while True:
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def display_text(text):
    print(text)
    input("Press Enter to continue...")
def encounter_scenario():
    display_text("You are on a quest to find a hidden treasure deep within a dark forest.")
    
    choice = get_choice(["Explore deeper into the forest", "Try to find a way out"], "What do you do?")
    
    if choice == 1:
        display_text("You venture deeper into the forest...")
        outcome = random.choice(["You find a treasure chest!", "You get lost and can't find your way back."])
        display_text(outcome)
    else:
        display_text("You decide to find a way out of the forest.")
        display_text("You reach a river. What do you do?")
        
        choice = get_choice(["Swim across", "Look for a bridge"], "What's your next move?")
        
        if choice == 1:
            display_text("You swim across the river and continue your journey.")
        else:
            display_text("You find a bridge and cross it safely.")
            display_text("You reach a village. What's your next move?")
            
            choice = get_choice(["Ask for directions", "Keep walking"], "What do you do?")
            
            if choice == 1:
                display_text("You ask for directions and get closer to the treasure's location.")
            else:
                you_died()
                
        display_text("You're getting closer to the treasure's location...")
        display_text("Suddenly, a dragon appears! What do you do?")
        
        choice = get_choice(["Fight the dragon", "Run away"], "What's your decision?")
        
        if choice == 1:
            you_died()
        else:
            display_text("You run away and escape the dragon.")
            display_text("After a long journey, you finally find the hidden treasure!")
            display_text("Congratulations, you win!")
def you_died():
    display_text("You made the wrong choice and lost your life.")
    display_text("Game Over!")
while True:
    print("\nWelcome to the Treasure Hunt Adventure Game!")
    play = input("Are you ready to begin your adventure? (yes/no): ").lower()
    
    if play != "yes":
        break

    encounter_scenario()

print("Thank you for playing!")
