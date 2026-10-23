def show_open_tickets(tickets):
    for current_ticket in tickets:
        if current_ticket["status"] == "Open":
            print("Ticket ID:", current_ticket["ticket_id"])
            print("Title:", current_ticket["title"])
            print()



def resolve_ticket(tickets, ticket_id):
    found = False
    
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            found = True
            if ticket["status"] == "Resolved":
                print(f"Ticket {ticket_id} is already resolved")
            else:
                ticket["status"] = "Resolved"
                print(f"Ticket {ticket_id} has been resolved")

    if found == False:
        print(f"Ticket {ticket_id} does not exist")
        
        
        
        
        
def create_ticket(tickets):
    ticket_title = input("Enter the title of your issue: ")
    description = input("Please describe your issue: ")
    
    # Calculate the ID before putting it in the dictionary
    # If the tickets list is empty, start at 1001. Otherwise, take the last ID and add 1.
    
    if not tickets:
        next_id = 1001
    else:
        highest = 0
        for ticket in tickets:
            if ticket["ticket_id"] > highest:
                highest = ticket["ticket_id"]
        next_id = highest + 1
    
    new_ticket = {
        "ticket_id" : next_id, 
        "title" : ticket_title, 
        "description" : description,
        "priority" : "Medium",
        "status" : "Open"
    }
    tickets.append(new_ticket)

tickets = []

while True:
    print("1 = Create Ticket")
    print("2 = View Open Tickets")
    print("3 = Resolve Ticket")
    print("4 = Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You have selected Choice 1")
        create_ticket(tickets)
    elif choice == "2":
        print("You have selected Choice 2")
        show_open_tickets(tickets)
    elif choice == "3":
        print("You have selected Choice 3")
        ticket_id = input("Enter a ticket ID you wish to resolve: ")
        try:
            ticket_id = int(ticket_id)
            resolve_ticket(tickets, ticket_id)
        except ValueError:
            print("Invalid number")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")