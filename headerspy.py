import requests

SEC_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    try:
        print(f"\n[+] Checking security headers for: {url}")
        response = requests.get(url, timeout=10)
        headers = response.headers

        print("\n--- Security Header Check ---")
        for header in SEC_HEADERS:
            if header in headers:
                print(f"[+] {header}: FOUND")
            else:
                print(f"[-] {header}: MISSING")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    target = input("Enter website URL (e.g. https://example.com): ")
    check_headers(target)