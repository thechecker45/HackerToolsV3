import requests
import json
import os
import socket
import hashlib
import random
import string
import base64
import ipaddress
import platform
import subprocess
import re
from collections import Counter
from colorama import Fore

def clear_screen():
    # os.system("clear") # Kullanıcı isteğine göre aktif edilebilir
    pass

def print_menu():
    print("-" * 60)
    print(f"{Fore.RED}*** HACKER TOOLS v3.0 ***{Fore.RESET}")
    print("-" * 60)
    
    menu_items = [
        "1. IP Adresi", "2. Site Raporu",
        "3. Whois Sorgusu", "4. HTTP Header Analizi",
        "5. Port Tarama", "6. Hash Oluşturucu",
        "7. Güçlü Şifre Oluşturucu", "8. DNS Kayıtları Sorgula",
        "9. IP Konum Haritası", "10. Kaynak Kod Çekici",
        "11. IP/Subnet Hesaplayıcı", "12. Base64 Çevirici",
        "13. Gelişmiş Link Çözücü", "14. MAC Adresi Sorgula",
        "15. Detaylı Sistem Bilgisi", "16. JSON Güzelleştirici",
        "17. Robots.txt Analizi", "18. Ping Aracı",
        "19. Admin Paneli Bulucu", "20. Subdomain Tarayıcı",
        "21. Sahte Kimlik Oluşturucu", "22. Basit SQLi Tarayıcı",
        "23. Basit XSS Tarayıcı", "24. Sezar Şifreleme",
        "25. Şifre Gücü Kontrolü", "26. User-Agent Oluşturucu",
        "27. Banner Grabbing", "28. Email Doğrulama",
        "29. Mors Alfabesi Çevirici", "30. Metin İstatistikleri"
    ]
    
    # 2 Sütunlu Yazdırma Mantığı
    for i in range(0, len(menu_items), 2):
        if i + 1 < len(menu_items):
            print(f"{menu_items[i]:<35} | {menu_items[i+1]:<35}")
        else:
            print(f"{menu_items[i]:<35} |")
            
    print("-" * 60)
    print("Q. Çıkış")

# Ana döngü
while True:
    clear_screen()
    print_menu()
    
    secim = input("\nSeçiminiz: ")

    if secim.lower() == 'q':
        print("Çıkış yapılıyor...")
        break

    print("-" * 60)

    if secim == "1":
        ip = input("IP adresini giriniz: ")
        banner = r"""
        .________________________.___ _______  ________  _____________________ 
        |   \______   \_   _____/|   |\      \ \______ \ \_   _____/\______   \
        |   ||     ___/|    __)  |   |/   |   \ |    |  \ |    __)_  |       _/
        |   ||    |    |     \   |   /    |    \|    `   \|        \ |    |   \
        |___||____|    \___  /   |___\____|__  /_______  /_______  / |____|_  /
        
        """
        print(Fore.RED + banner)
        try:
            url = f"https://ipinfo.io/{ip}"
            response = requests.get(url)
            json_data = response.json()
            
            print(f"IP Adresi: {ip}")
            print(f"İl: {json_data.get('city')}")
            print(f"İlçe: {json_data.get('region')}")
            print(f"Ülke: {json_data.get('country')}")
            print(f"Konum: {json_data.get('loc')}")
            print(f"Organizasyon: {json_data.get('org')}")
            print(f"Posta Kodu: {json_data.get('postal')}")
            print(f"Zaman Dilim: {json_data.get('timezone')}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "2":
        site = input("Site adresini giriniz: ")
        try:
            response = requests.get(f"https://www.usom.gov.tr/api/incident/index?url={site}")
            json_data = response.json()
            print("-" * 60)
            for model in json_data.get('models', []):
                print(f"ID: {model.get('id')}")
                print(f"Başlık: {model.get('title')}")
                print(f"Tarih: {model.get('date')}")
                print("-" * 60)
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "3":
        site = input("Site adresini giriniz: ")
        API_KEY = "caf715a79f5a490e811d185f2990b7dd"
        try:
            response = requests.get(f"https://api.whoisfreaks.com/v1.0/whois?apiKey={API_KEY}&whois=live&domainName={site}")
            whois_data = response.json()
            
            if whois_data.get("status"):
                print("-" * 60)
                print(f"Domain: {whois_data.get('domain_name')}")
                print(f"Kayıt Durumu: {whois_data.get('domain_registered')}")
                print(f"Oluşturulma Tarihi: {whois_data.get('create_date')}")
                print(f"Güncelleme Tarihi: {whois_data.get('update_date')}")
                print(f"Bitiş Tarihi: {whois_data.get('expiry_date')}")
                
                print("\nDomain Durum Kodları:")
                for status in whois_data.get('domain_status', []):
                    print(f"- {status}")
                
                registrar = whois_data.get('domain_registrar', {})
                print(f"\nKayıt Firması: {registrar.get('registrar_name', 'Bilinmiyor')}")
                print(f"Web Sitesi: {registrar.get('website_url', '-')}")
                print(f"E-posta: {registrar.get('email_address', '-')}")
                print(f"Telefon: {registrar.get('phone_number', '-')}")
                
                registrant = whois_data.get('registrant_contact', {})
                print(f"\nSahibi: {registrant.get('company', registrant.get('name', 'Gizli'))}")
                print(f"Ülke: {registrant.get('country_name', '-')}")
                print(f"E-posta: {registrant.get('email_address', '-')}")
                
                ns = ", ".join(whois_data.get('name_servers', []))
                print(f"\nName Serverlar: {ns}")
                print("-" * 60)
            else:
                print("Whois bilgisi alınamadı!")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "4":
        site = input("Site adresini giriniz (http/https olmadan): ")
        if not site.startswith("http"):
            site = "http://" + site
        try:
            response = requests.get(site)
            headers = response.headers
            
            print("-" * 60)
            print(f"Hedef Site: {site}")
            print(f"Sunucu (Server): {headers.get('Server', 'Gizli/Bilinmiyor')}")
            print(f"X-Powered-By: {headers.get('X-Powered-By', 'Bulunamadı')}")
            
            security_headers = [
                "Strict-Transport-Security", "X-Frame-Options", "X-XSS-Protection",
                "Content-Security-Policy", "X-Content-Type-Options"
            ]
            
            print("\nGüvenlik Başlıkları:")
            for header in security_headers:
                if header in headers:
                    print(f"[+] {header}: {headers[header]}")
                else:
                    print(f"[-] {header} eksik!")
            print("-" * 60)
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "5":
        host = input("Hedef IP veya Domain giriniz: ")
        try:
            target_ip = socket.gethostbyname(host)
            print(f"\n{host} ({target_ip}) taranıyor...\n")
            print("-" * 60)
            
            common_ports = [
                21, 22, 23, 25, 53, 80, 110, 123, 139, 443, 445, 
                465, 587, 993, 995, # Email
                1433, 3306, 5432, 6379, 27017, # Database
                3389, 5900, 8080 
            ]
            
            for port in common_ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"[+] Port {port} AÇIK")
                else:
                    pass
                sock.close()
            print("-" * 60)
            print("Tarama tamamlandı.")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "6":
        text = input("Hashlenecek metni giriniz: ")
        encoded_text = text.encode('utf-8')
        print("-" * 60)
        print(f"MD5: {hashlib.md5(encoded_text).hexdigest()}")
        print(f"SHA-1: {hashlib.sha1(encoded_text).hexdigest()}")
        print(f"SHA-256: {hashlib.sha256(encoded_text).hexdigest()}")
        print(f"SHA-512: {hashlib.sha512(encoded_text).hexdigest()}")
        print("-" * 60)

    elif secim == "7":
        try:
            length = int(input("Şifre uzunluğu (örn: 16): "))
            use_upper = input("Büyük harf olsun mu? (E/H): ").lower() == 'e'
            use_digits = input("Rakam olsun mu? (E/H): ").lower() == 'e'
            use_symbols = input("Sembol olsun mu? (E/H): ").lower() == 'e'
            
            chars = string.ascii_lowercase
            if use_upper: chars += string.ascii_uppercase
            if use_digits: chars += string.digits
            if use_symbols: chars += string.punctuation
            
            password = ''.join(random.choice(chars) for _ in range(length))
            print("-" * 60)
            print(f"Oluşturulan Şifre: {password}")
            print("-" * 60)
        except Exception:
            print("Hata oluştu.")

    elif secim == "8":
        domain = input("Domain giriniz: ")
        try:
            response = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}")
            data = response.json()
            if data.get('status') == 'OK':
                records = data.get('records', {})
                print("-" * 60)
                if records.get('A'):
                    print("A Kayıtları:")
                    for r in records['A']: print(f"- {r['address']}")
                if records.get('MX'):
                    print("\nMX Kayıtları:")
                    for r in records['MX']: print(f"- {r['exchange']}")
                if records.get('NS'):
                    print("\nNS Kayıtları:")
                    for r in records['NS']: print(f"- {r['nameserver']}")
                if records.get('TXT'):
                    print("\nTXT Kayıtları:")
                    for r in records['TXT']: print(f"- {r}")
                print("-" * 60)
            else:
                print("DNS bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "9":
        ip = input("IP adresini giriniz: ")
        try:
            response = requests.get(f"https://ipinfo.io/{ip}")
            data = response.json()
            loc = data.get('loc')
            if loc:
                print(f"Konum: {loc}")
                print(f"Maps: https://www.google.com/maps/search/?api=1&query={loc}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "10":
        url = input("URL giriniz: ")
        if not url.startswith("http"): url = "http://" + url
        try:
            response = requests.get(url)
            action = input("Yazdır (Y) / Kaydet (K): ").lower()
            if action == 'k':
                with open("source.html", "w") as f: f.write(response.text)
                print("Kaydedildi: source.html")
            else:
                print(response.text[:1000] + "...")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "11":
        cidr = input("IP/CIDR (192.168.1.1/24): ")
        try:
            net = ipaddress.ip_network(cidr, strict=False)
            print(f"Network: {net.network_address}")
            print(f"Broadcast: {net.broadcast_address}")
            print(f"Netmask: {net.netmask}")
            print(f"Host Sayısı: {net.num_addresses}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "12":
        action = input("1.Encode 2.Decode: ")
        text = input("Metin: ")
        try:
            if action == "1":
                print(base64.b64encode(text.encode()).decode())
            else:
                print(base64.b64decode(text).decode())
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "13":
        url = input("Kısa Link: ")
        if not url.startswith("http"): url = "http://" + url
        try:
            res = requests.get(url, allow_redirects=True)
            for h in res.history:
                print(f"{h.status_code} -> {h.url}")
            print(f"{res.status_code} -> {res.url}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "14":
        mac = input("MAC: ")
        try:
            r = requests.get(f"https://api.macvendors.com/{mac}")
            print(f"Vendor: {r.text}")
        except Exception:
            print("Bulunamadı.")

    elif secim == "15":
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Node: {platform.node()}")
        print(f"CPU: {platform.processor()}")
        try:
            print(f"Local IP: {socket.gethostbyname(socket.gethostname())}")
            print(f"Public IP: {requests.get('https://ifconfig.me/ip', timeout=2).text}")
        except: pass

    elif secim == "16":
        raw = input("JSON: ")
        try:
            print(json.dumps(json.loads(raw), indent=4))
        except: print("Geçersiz JSON")

    elif secim == "17":
        url = input("URL: ")
        if not url.startswith("http"): url = "http://" + url
        try:
            r = requests.get(f"{url}/robots.txt")
            if r.status_code == 200:
                for l in r.text.splitlines():
                    if "disallow" in l.lower(): print(Fore.RED + l + Fore.RESET)
                    elif "allow" in l.lower(): print(Fore.GREEN + l + Fore.RESET)
                    else: print(l)
            else: print("robots.txt yok")
        except: print("Hata")

    elif secim == "18":
        host = input("Ping Adresi: ")
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.call(['ping', param, '4', host])

    elif secim == "19":
        url = input("Site Adresi (örn: example.com): ")
        if not url.startswith("http"): url = "http://" + url
        paths = ["admin", "login", "wp-admin", "cpanel", "dashboard", "panel", "user", "yonetim", "giris"]
        print("Taranıyor...")
        for p in paths:
            target = f"{url}/{p}"
            try:
                r = requests.get(target, timeout=2)
                if r.status_code == 200:
                    print(f"{Fore.GREEN}[BULUNDU] {target} (200 OK){Fore.RESET}")
                else:
                    print(f"{Fore.RED}[404] {target}{Fore.RESET}")
            except: pass

    elif secim == "20":
        domain = input("Domain (örn: google.com): ")
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                subs = set()
                for item in r.json():
                    subs.add(item['name_value'])
                print(f"\nBulunan Subdomainler ({len(subs)}):")
                for s in sorted(subs):
                    print(f"- {s}")
            else:
                print("Hata veya Subdomain bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "21":
        names = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "John", "Alice", "Veli", "Zeynep"]
        surnames = ["Yılmaz", "Kaya", "Demir", "Smith", "Doe", "Öztürk", "Çelik"]
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
        
        n = random.choice(names)
        s = random.choice(surnames)
        print("-" * 60)
        print(f"İsim: {n} {s}")
        print(f"Email: {n.lower()}.{s.lower()}@{random.choice(domains)}")
        print(f"Adres: {random.randint(1,99)} Sokak, No:{random.randint(1,50)}, PK:{random.randint(10000,99999)}")
        print("-" * 60)

    elif secim == "22":
        url = input("Test edilecek URL (parametre içeren): ")
        if not url.startswith("http"): url = "http://" + url
        payload = "'"
        target = url + payload
        try:
            r = requests.get(target, timeout=3)
            errors = ["SQL syntax", "mysql", "syntax error", "ORA-", "PostgreSQL", "SQLite"]
            if any(e in r.text for e in errors):
                print(f"{Fore.GREEN}[!] Olası SQL Injection Açığı Tespit Edildi!{Fore.RESET}")
            else:
                print(f"{Fore.YELLOW}[-] Belirgin bir SQL hatası dönmedi.{Fore.RESET}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "23":
        url = input("Test edilecek URL: ")
        if not url.startswith("http"): url = "http://" + url
        payload = "<script>alert('XSS')</script>"
        if "?" not in url: url += "?q=" + payload
        else: url += payload
        
        try:
            r = requests.get(url, timeout=3)
            if payload in r.text:
                print(f"{Fore.GREEN}[!] XSS Payloadi sayfada yansıdı (Reflected XSS ihtimali)!{Fore.RESET}")
            else:
                print(f"{Fore.YELLOW}[-] Payload yansımadı.{Fore.RESET}")
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "24":
        text = input("Metin: ")
        try:
            shift = int(input("Kaydırma Sayısı (Shift): "))
            result = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    result += char
            print(f"Sonuç: {result}")
        except: print("Hata.")

    elif secim == "25":
        pwd = input("Şifrenizi girin: ")
        score = 0
        if len(pwd) >= 8: score += 20
        if len(pwd) >= 12: score += 20
        if any(c.isupper() for c in pwd): score += 15
        if any(c.islower() for c in pwd): score += 15
        if any(c.isdigit() for c in pwd): score += 15
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd): score += 15
        
        print(f"Şifre Puanı: {score}/100")
        if score < 50: print(f"{Fore.RED}ZAYIF{Fore.RESET}")
        elif score < 80: print(f"{Fore.YELLOW}ORTA{Fore.RESET}")
        else: print(f"{Fore.GREEN}GÜÇLÜ{Fore.RESET}")

    elif secim == "26":
        uas = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
        ]
        print(f"Random User-Agent:\n{random.choice(uas)}")

    elif secim == "27":
        ip = input("Hedef IP: ")
        port = int(input("Port (örn 22, 80): "))
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, port))
            # Bazı servisler bağlantı anında banner gönderir
            # Bazısı için veri göndermek gerekir, örneğin HTTP
            if port == 80 or port == 8080 or port == 443:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            
            banner = s.recv(1024)
            print(f"Banner: {banner.decode().strip()}")
            s.close()
        except Exception as e:
            print(f"Hata: {e}")

    elif secim == "28":
        email = input("Email adresi: ")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            print(f"{Fore.GREEN}[+] Format Geçerli.{Fore.RESET}")
            domain = email.split('@')[1]
            try:
                # MX kontrolü için DNS API kullanıyoruz tekrar
                r = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}")
                if r.json().get('records', {}).get('MX'):
                    print(f"{Fore.GREEN}[+] Domain MX kaydı mevcut (Mail sunucusu var).{Fore.RESET}")
                else:
                    print(f"{Fore.YELLOW}[-] Domain MX kaydı bulunamadı.{Fore.RESET}")
            except: pass
        else:
            print(f"{Fore.RED}[-] Geçersiz Email Formatı.{Fore.RESET}")

    elif secim == "29":
        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            ' ': '/'
        }
        reverse_dict = {v: k for k, v in morse_code_dict.items()}
        
        choice = input("1. Metin -> Mors\n2. Mors -> Metin\nSeçim: ")
        text = input("Veri: ").upper()
        
        if choice == "1":
            try:
                print(" ".join(morse_code_dict.get(c, c) for c in text))
            except: print("Hata")
        elif choice == "2":
            try:
                print("".join(reverse_dict.get(c, "?") for c in text.split()))
            except: print("Hata")

    elif secim == "30":
        text = input("Metni giriniz: ")
        print("-" * 60)
        print(f"Karakter Sayısı (boşluklu): {len(text)}")
        print(f"Karakter Sayısı (boşluksuz): {len(text.replace(' ', ''))}")
        print(f"Kelime Sayısı: {len(text.split())}")
        
        # En çok tekrar eden öğeler
        letters = Counter(c for c in text if c.isalpha())
        if letters:
            most_common = letters.most_common(1)[0]
            print(f"En çok geçen harf: '{most_common[0]}' ({most_common[1]} kez)")
        print("-" * 60)

    else:
        print("Geçersiz Seçim! Tekrar deneyin.")
    
    input("\nDevam etmek için Enter'a basın...")