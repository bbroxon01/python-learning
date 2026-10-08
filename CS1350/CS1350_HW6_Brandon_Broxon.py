from abc import ABC, abstractmethod
    
class Employee(ABC):
    employees = []
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        Employee.employees.append(name)

    @abstractmethod
    def calculate_pay(self):
        pay = float(self.calculate_pay().strip('$'))
        return f"{pay:.2f}"
    
    @abstractmethod
    def description(self):
        return f"{self.name} (ID: {self.employee_id})"
    
    def pay_stub(self):
        return f"{self.name} (ID: {self.employee_id}): ${self.calculate_pay()}"

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return True

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.validate_positive(annual_salary, "Annual salary")
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return f"{self.annual_salary / 24:.2f}"

    def description(self):
        return f"Salaried: {self.name}"

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.validate_positive(hourly_rate, "Hourly rate")
        self.validate_positive(hours_worked, "Hours worked")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_pay(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)
        return f"{(regular_hours * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5):.2f}"

    def description(self):
        return f"Hourly: {self.name}"

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.validate_positive(base_salary, "Base salary")
        self.validate_positive(sales, "Sales")
        if commission_rate <= 0 or commission_rate > 1.0:
            raise ValueError("Commission rate must be positive and <= 1.0")
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate
    
    def calculate_pay(self):
        return f"{self.base_salary + (self.sales * self.commission_rate):.2f}"
    
    def description(self):
        return f"Commission: {self.name}"

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        total_pay = sum(float(emp.calculate_pay()) for emp in self.employees)
        return total_pay
    def print_all_stubs(self):
        for emp in self.employees:
            print(emp.pay_stub())

# Test your code
if __name__ == "__main__":

    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)

    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f" {emp.description()}")
    
    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f" {emp.pay_stub()}")

    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)

    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")

    print("\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f" Caught: {e}")
    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f" Caught: {e}")
        
class Song:
    total_songs = 0
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        Song.total_songs += 1
    def display(self):
        return f"{self.title} - {self.artist} ({self.format_duration(self.duration_seconds)})"
    
    @classmethod
    def from_string(cls, s):
        title, artist, duration_str = s.split(" | ")
        duration_seconds = cls.parse_duration(duration_str)
        return cls(title, artist, duration_seconds)
    
    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @staticmethod
    def format_duration(seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02}"

    @staticmethod
    def parse_duration(duration_str):
        minutes, secs = map(int, duration_str.split(":"))
        return minutes * 60 + secs

class Playlist:
    total_playlists = 0
    def __init__(self, name):
        Playlist.total_playlists += 1
        self.playlist_id = f"PL_{Playlist.total_playlists:03}"
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def total_duration(self):
        return sum(song.duration_seconds for song in self.songs)
    
    def display(self):
        count = len(self.songs)
        total_seconds = self.total_duration()
        return f"Playlist: {self.name} ({count} songs, {Song.format_duration(total_seconds)})"

    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists

class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name)
        for s in song_strings:
            song = Song.from_string(s)
            playlist.add_song(song)
        return playlist
    
    @staticmethod
    def format_library_report(playlists):
        report_lines = []
        print("\n=== LIBRARY REPORT ===")
        for pl in playlists:
            report_lines.append(pl.display())
            for song in (pl.songs):
                report_lines.append(f"  - {song.display()}")
        return "\n".join(report_lines) + "\n" + "\n" + f"Total Songs: {Song.get_total_songs()}" + "\n" + f"{'='*22}"
        
# Test your code
if __name__ == "__main__":
# Test Song creation
    s1 = Song("Bohemian Rhapsody", "Queen", 354)
    s2 = Song("Imagine", "John Lennon", 187)
    print("Individual Songs:")
    print(f" {s1.display()}")
    print(f" {s2.display()}")
# Test factory method
    s3 = Song.from_string("Hotel California | Eagles | 6:31")
    print(f" {s3.display()}")
# Test static methods
    print(f"\nFormat 245 seconds: {Song.format_duration(245)}")
    print(f"Parse '4:05': {Song.parse_duration('4:05')} seconds")
# Test Playlist
    playlist = Playlist("Classic Rock")
    playlist.add_song(s1)
    playlist.add_song(s2)
    playlist.add_song(s3)
    print(f"\n{playlist.display()}")
# Test LibraryManager
    chill_songs = [
    "Weightless | Marconi Union | 8:09",
    "Electra | Airstream | 5:51",
    "Mellomaniac | DJ Shah | 7:34"
]
    chill = LibraryManager.create_playlist_from_strings("Chill Vibes", chill_songs)
    print(f"{chill.display()}")
# Test report
    print(f"{LibraryManager.format_library_report([playlist, chill])}")
# Test counts
    print(f"Total songs created: {Song.get_total_songs()}")
    print(f"Total playlists created: {Playlist.get_total_playlists()}")

