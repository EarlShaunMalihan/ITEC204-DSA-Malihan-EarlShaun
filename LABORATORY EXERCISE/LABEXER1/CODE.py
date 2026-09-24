ticket_data = [
    ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
    ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
    ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
    ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
    ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
    ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
    ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
    ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
    ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
    ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
]

tickets = [
    {"incident_id": inc_id, "bot": bot, "description": desc}
    for inc_id, bot, desc in ticket_data
]


def find(inc_id):
    return next((t for t in tickets if t["incident_id"].lower() == inc_id.lower()), None)
 
def add():
    inc_id = input("Incident ID: ").strip()
    if find(inc_id):
        print("ID already existing >:D."); return
    bot = input("Bot: ").strip()
    desc = input("Description: ").strip()
    tickets.append({"incident_id": inc_id, "bot": bot, "description": desc})
    print("Ticket has been added to what is basically a digital jail cell, wonderful.")
 
def display():
    if not tickets:
        print("No active tickets. Must be on vacation."); return
    for t in tickets:
        print(f"{t['incident_id']:<15}{t['bot']:<20}{t['description']}")
 
def search():
    t = find(input("Incident ID: ").strip())
    print(t if t else "Weird, no ID found at all. Wait... look behind you...")
 
def remove():
    t = find(input("Incident ID: ").strip())
    if t:
        tickets.remove(t); print("Ticket eradicated, disintergrated, annihilated.")
    else:
        print("Not found mate. If you wanna assassinate a ticket, be efficient. - Sniper from TF2")
 
def count():
    print(f"Total active tickets: {len(tickets)}")
 
menu = {"1": add, "2": display, "3": search, "4": remove, "5": count}
 
while True:
    choice = input("\n1)Add 2)Display 3)Search 4)Remove 5)Count 0)Exit\n> ").strip()
    if choice == "0":
        break
    menu.get(choice, lambda: print("Invalid choice mi compadre >:l."))()

    
