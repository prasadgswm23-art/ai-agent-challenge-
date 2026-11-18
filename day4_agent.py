# Day 4: Sorting Client Leads using Dictionaries, Lists, and Loops

# A list of client dictionaries (just like real API data!)
leads = [
    {"name": "TechCorp", "budget": 5000},
    {"name": "Local Bakery", "budget": 400},
    {"name": "FinTech Startup", "budget": 3500},
    {"name": "Solo Blogger", "budget": 150}
]

print("--- AI Lead Sorter Starting ---\n")

for client in leads:
    client_name = client["name"]
    client_budget = client["budget"]

    if client_budget >= 2000:
        print(f"✅ PRIORITY: Contact {client_name} (Budget: ${client_budget})")
    else:
        print(f"📩 AUTO-REPLY: Send free guide to {client_name} (Budget: ${client_budget})")
