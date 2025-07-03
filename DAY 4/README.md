# 📦 Day 4 - IaaS & PaaS PostgreSQL DB Integration

This guide explains how to configure a web server and database server using **Naver Cloud Platform**, comparing **IaaS-based PostgreSQL** and **PaaS-based RDS (PostgreSQL)** environments.

---

## 🧱 Architecture

```
Client ─▶ Web Server ─▶ DB Server (PostgreSQL)
                      └▶ RDS (PostgreSQL)
```

---

## 1️⃣ IaaS: Web + PostgreSQL on VPC

### Step 1: Launch Web Server
- Name: `web-server`
- Subnet: Public
- Open TCP 22 (SSH), 80 (HTTP) in ACG

### Step 2: Launch PostgreSQL Server
- Name: `db-server`
- Subnet: Private
- Open TCP 5432 (PostgreSQL) in ACG (from web-server only)

### Step 3: Install PostgreSQL on db-server
```bash
sudo yum install -y postgresql-server
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Step 4: Allow Remote Access
- Edit `postgresql.conf`:
  ```
  listen_addresses = '*'
  ```
- Edit `pg_hba.conf`:
  ```
  host    all             all             [web-server IP]/32         md5
  ```

### Step 5: Restart DB Server
```bash
sudo systemctl restart postgresql
```

### Step 6: Create DB and User
```bash
sudo -i -u postgres
psql
CREATE DATABASE testdb;
CREATE USER testuser WITH PASSWORD 'testpass';
GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;
```

### Step 7: Test from Web Server
```bash
psql -h [db-server private IP] -U testuser -d testdb
```

---

## 2️⃣ PaaS: RDS (PostgreSQL)

### Step 1: Create RDS Instance
- Type: PostgreSQL
- Version: 13+
- Subnet Group: Include public subnet
- Public Access: Yes
- Set username/password

### Step 2: Allow Connection in ACG
- Add rule: TCP 5432 from web-server public IP

### Step 3: Connect from Web Server
```bash
psql -h [RDS Endpoint] -U [username] -d [dbname]
```

---

## ✅ Comparison Table

| Feature         | IaaS PostgreSQL       | PaaS RDS PostgreSQL       |
|-----------------|-----------------------|----------------------------|
| Setup           | Manual installation   | One-click provisioning     |
| Scaling         | Manual                | Auto-scaling options       |
| Maintenance     | Manual patching       | Automatic by NCP           |
| Security        | Manual firewall setup | Built-in + ACG control     |
| Backup          | Manual (pg_dump)      | Auto backup support        |
| Cost            | Lower                 | Slightly higher (managed)  |

---

## 🔧 Useful Commands

```bash
# Install PostgreSQL
sudo yum install -y postgresql-server

# Initialize DB
sudo postgresql-setup initdb

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Connect to PostgreSQL
psql -h [host] -U [user] -d [database]
```

---

## 🔗 Reference
- 실습 노션: [Day 4 - IaaS & PaaS DB 실습](https://swift-talon-3c6.notion.site/4-IaaS-PaaS-DB-21a7143378678002a3fbfa428fea4811)
- Console: https://console.ncloud.com
