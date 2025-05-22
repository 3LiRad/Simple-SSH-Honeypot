# 🐍 Simple SSH Honeypot

A lightweight SSH honeypot written in Python. It simulates a real SSH server to capture unauthorized login attempts and log attacker commands for educational and monitoring purposes.

---

## 🚀 Features

- Listens on port `2222` and mimics an SSH service.
- Logs:
  - Source IP and timestamp of connection
  - Username and password input
  - All shell-like commands typed by the attacker
- Sends fake SSH banner to appear legitimate.
- Fully written in Python (no third-party libraries).

---

## 📂 Log Sample

```
=== Connection from <your IP>:54012 at 2025-05-22 01:08:34 ===
[<your IP>] Username attempt: admin
[<your IP>] Password attempt: hunter2
[<your IP>] Command: whoami
[<your IP>] Command: uname -a
```

---

## 🛠️ How to Run

```bash
git clone https://github.com/3LiRad/simple-ssh-honeypot.git
cd simple-ssh-honeypot
sudo python3 honeypot.py
```

🧪 From another terminal or machine:

```bash
nc <your IP> 2222
```

Then type some fake SSH commands and check `log.txt`.

---

## 🧠 Educational Use Only

This project is intended for educational use, local testing, and safe internal lab environments. Do **not** expose it directly to the internet without proper hardening.

---

## 📎 Author

Ali Abobaker Ali Radman  
Cybersecurity Enthusiast | eJPT Certified  
[LinkedIn](https://www.linkedin.com/in/ali-radman-46706430b) • [GitHub](https://github.com/3LiRad)

---

## 🔒 Disclaimer

This project is for **educational and demonstration purposes** only. Running a honeypot publicly without proper authorization may violate laws and terms of service.

