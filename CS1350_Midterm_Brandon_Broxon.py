class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies
        self.books[isbn] = {"title": str(title), "author": str(author), "copies": int(copies)}
        return self.books[isbn]
    
    def checkout(self, isbn):
        if isbn in self.books and self.books[isbn]["copies"] > 0:
            self.books[isbn]["copies"] -= 1
            return True
        return False
    
    def by_author(self, author):
        return {info["title"] for isbn, info in self.books.items() if info["author"] == author}
    
    def inventory_value(self, prices):
        total_value = 0
        for isbn, price in prices.items():
            if isbn in self.books:
                total_value += self.books[isbn]["copies"] * price
        return total_value
    
    def low_stock(self, threshold):
        return {isbn: info for isbn, info in self.books.items() if info["copies"] <= threshold}
    
lib = Library()
lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)
lib.add_book("111", "Python Basics", "Jane Doe", 2)

print(lib.checkout("222"))
print(lib.checkout("222"))
print(lib.checkout("999"))
print(lib.by_author("Jane Doe"))
print(lib.inventory_value({"111": 10, "222": 15, "333": 20}))
print(lib.low_stock(2))

class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()
    
    def register(self, name):
        self.attendees.add(name)
    
    def unregister(self, name):
        self.attendees.remove(name) if name in self.attendees else None
    
    def attendee_count(self):
        return len(self.attendees)

def attended_all(sessions):
    if not sessions:
        return set()
    all_attended = set(sessions[0].attendees)
    for session in sessions[1:]:
        all_attended &= session.attendees
    return all_attended

def attended_exactly_one(sessions):
    exactly_one = set()
    for session in sessions:
        for attendee in session.attendees:
            if sum(attendee in s.attendees for s in sessions) == 1:
                exactly_one.add(attendee)
    return exactly_one

def no__shows(registered, sessions):
    no_shows = set(registered)
    for session in sessions:
        no_shows -= session.attendees
    return no_shows

def summary(sessions):
    for session in sessions:
        print(f"{session.title}: {len(session.attendees)} attendees")
    print(f"Distinct attendees: {len(set(attendee for session in sessions for attendee in session.attendees))}")

keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)
workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)
panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed") 
print(workshop.attendee_count())

sessions = [keynote, workshop, panel]
print(attended_all(sessions))
print(attended_exactly_one(sessions))
print(no__shows({"Ana", "Ben", "Fay", "Gus"}, sessions))

summary(sessions)