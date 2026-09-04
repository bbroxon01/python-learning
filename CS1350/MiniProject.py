#Start of Project
contact_book = {
    "Mom":{"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad":{"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister":{"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"}
}
call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}
#Created an empty dictionary quick_contacts and add five entries (name → phone string):
quick_contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000",
}
print("=== Phase 1: Quick Contacts ===")
#Printed Quick Contacts
print(quick_contacts,"\n")
print("--- Access and Modify ---")
#Printed Mom's number using bracket notation.
print("Mom's number is:", quick_contacts["Mom"])
#Updated Dad's number to "555-4321".
contact_book["Dad"]["phone"] = "555-4321"
#Added "Dentist": "555-2222".
quick_contacts["Dentist"] = "555-2222"
#Look up "Grandma" with get(), printing Contact not found when the key is missing. Do not let the program crash.
print("Grandma's number is:", quick_contacts.get("Grandma", "Not found"))
#Printed the updated dictionary.
print("The updated quick contact dictionary is:", quick_contacts,"\n")

print("--- Delete and Analyze ---")
#Removed "Pizza Place" with del
del quick_contacts["Pizza Place"]
#Remove "Work" with pop(), saving the old number in old_work, and print it.
old_work = quick_contacts.pop("Work")
print("Your old work number was:", old_work)
#Print the number of contacts left with len(), then the names with keys() and the numbers with values(), each wrapped in list().
print("The number of quick contacts left is:", len(quick_contacts))
#We lost the pizza place and replaced the work number
print("The names of those contacts are:", list(quick_contacts.keys()))
print("The numbers of those contacts are:", list(quick_contacts.values()),"\n")

print("=== Phase 2: Contact Activity ===")
total_minutes = {}
for contact, calltime in call_log.items():
    months_called = 0
    total_time = 0
    busiest_month, busiest_time = max(calltime.items(), key = lambda x: x[1])
    average = sum(calltime.values())/ len(calltime.values())
    for month, time in calltime.items():
        months_called+=1
        total_time += time
    print(f"{contact}: {months_called} month(s), {total_time} min total, avg: {average:.2f}, busiest: {busiest_month} ({busiest_time})")
    
    total_minutes[contact] = total_time
#sort by month instead of contact
month_stats = {
    "Jan": {"minutes": 0, "total": 0, "avg": 0, "contacts":0}, 
    "Feb": {"minutes": 0, "total": 0, "avg": 0, "contacts":0},
    "Mar": {"minutes": 0, "total": 0, "avg": 0, "contacts":0} 
}
for contact, calltime in call_log.items():
    for month, minutes in calltime.items():
        month_stats[month]["minutes"] = minutes
        month_stats[month]["total"] = sum(minutes.values())
        month_stats[month]["avg"] = month_stats[month]["total"] / len(minutes)
        month_stats[month]["contacts"] = len(minutes)


#call_log is organized by contact. Build a dictionary organized by month instead. Name it month_stats; each 
#month maps to a dictionary containing:
# "minutes" — a list of every minute-value recorded that month,
# "total" — the sum of those minutes,
# "avg" — the average, and
# "contacts" — how many contacts were called that month.
# Then print each month sorted by average, highest first, using sorted()
# -with a lambda key.    
print(calltime.items())
print("=== Phase 3: Aggregations ===")
#month_stats = {"Month"  {[minutes], [total](sum), [avg], [contacts](how many called that month)
minutes = total_minutes[month]
total = sum(minutes)
month_stats = dict(sorted(calltime.items))