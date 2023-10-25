def spawn_enemies(coordinates):
    enemies = []

    for coord in coordinates:
        x, y = coord

       
        nearby_enemies = [enemy for enemy in enemies if abs(enemy[0] - x) <= 2 and abs(enemy[1] - y) <= 2]

        if nearby_enemies:
            print("Character died!")
            return


        enemies.append((x, y))

    print("Character survived!")


N = int(input("Enter the number of coordinates: "))

coordinates = []
for i in range(N):
    x = int(input(f"Enter x-coordinate for drop {i+1}: "))
    y = int(input(f"Enter y-coordinate for drop {i+1}: "))
    coordinates.append((x, y))

spawn_enemies(coordinates)
