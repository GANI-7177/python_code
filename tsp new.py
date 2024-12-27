monkey = int(input("Enter Monkey's starting position: "))
chair = int(input("Enter Chair's starting position: "))
banana = int(input("Enter Banana's position: "))
climbed = False

while True:
    print(f"Monkey: {monkey}, Chair: {chair}, Banana: {banana}")
    action = input("Action (move/push/climb/grab): ").strip().lower()
    
    if action == "move":
        monkey = int(input("Move to position: "))
    elif action == "push" and monkey == chair:
        chair = int(input("Push chair to position: "))
    elif action == "climb" and monkey == chair:
        climbed = True
    elif action == "grab" and climbed and chair == banana:
        print("Monkey got the banana!")
        break
    else:
        print("Invalid action or condition.")
