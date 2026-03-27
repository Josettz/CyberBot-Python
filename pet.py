class CyberBot:
    def __init__(self, name, model):
        self.name = name 
        self.model = model 
        self.battery = 100 
        self.memory_space = 0
        self.is_alive = True
    
    def status_report(self):
        print(f"\n--- {self.name.upper()} STATUS ---")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery}%")
        print(f"Memory Space: {self.memory_space} GB")
        print(f"System Status: {'Online' if self.is_alive else 'Offline'}")
    
    def charge_battery(self):
        self.battery = 100
        print(f"[*] {self.name} is charging... Battery at 100%!")
    
    def run_program(self):
        print(f"[*] Running software update on {self.name}...")
        # We subtract 20 from the current battery
        self.battery -= 20
        # We add 10 to memory space
        self.memory_space += 10
        print(f"[!] System updated. Battery consumed: {self.battery}%")