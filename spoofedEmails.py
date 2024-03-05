import re
import dns.resolver

def get_domain(email):
    return re.findall("@[\w.]+", email)[0][1:]

def check_mx(domain):
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.Timeout:
        return False

def detect_email_spoofing(email):
    sender_domain = get_domain(email)
    if check_mx(sender_domain):
        print("Email is not spoofed.")
    else:
        print("Email might be spoofed.")

email = "email"
detect_email_spoofing(email)
