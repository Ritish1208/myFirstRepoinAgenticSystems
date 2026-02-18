def calculate_averages(users):
    averages=[]
    for user in users:
        scores = user["scores"]
        average = sum(scores)/ len(scores) if scores else 0
        averages.append((user["name"], average))
        return averages 
    
def has_admin_access(roles):
    return "admin" in roles

def main():
    users=[
        {
            "name": "Alice",
            "scores": [80, 85, 82],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 68],
            "roles": {"viewer"}

        },
        {
            "name": "Charlie",
            "scores": [90, 88, 92],
            "roles": {"editor", "viewer"}
        }

    ]

    average_data = calculate_averages(users)

    for user in users:
        name = user["name"]
        average = sum(user["scores"])/len(user["scores"])
        admin_status= has_admin_access(user["roles"])
        print("Name :", name)
        print("Average Score :", round(average, 2))
        print("Admin Access :", admin_status)
        print()

main()
