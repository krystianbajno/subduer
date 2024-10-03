class Entry:
    def __init__(self):
        self.ips = []
        self.domains = []
        
    def add_domain(self, domain):
        if domain not in self.domains:
            self.domains.append(domain)
        
    def add_ip(self, ip):
        if ip not in self.ips:
            self.ips.append(ip)
        
    def __repr__(self):
        return f"{self.domains} = {self.ips}"
        