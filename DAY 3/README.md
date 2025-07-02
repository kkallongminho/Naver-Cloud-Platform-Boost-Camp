## 📘 Naver Cloud Platform - Auto Scaling Behavior Verification

### 🚀 Overview
This document verifies the actual behavior of the Auto Scaling Group (ASG) in Naver Cloud Platform (NCP), from instance creation to deletion, triggered by CPU metrics. It also confirms that the load balancer health checks work as expected.

---

### 📌 Triggering the Scaling Policy

| Item                  | Value                            |
|-----------------------|----------------------------------|
| **Monitoring Metric** | `avg_cpu_used_rto`               |
| **Condition**         | CPU Usage > 30% for 1 minute     |
| **Scaling Action**    | Add instance (scale-out)         |
| **Monitoring Tool**   | Cloud Insight (Event Rule active) |

Command used to simulate CPU load:

```bash
stress --cpu 2
```

> ✅ Result: Scaling policy was triggered successfully.

---

### 🖥️ Instance Creation & Target Group Status

After the trigger, a new instance was created automatically by the ASG.

| Component         | Status                     |
|-------------------|----------------------------|
| **Instance**      | Created via Auto Scaling   |
| **Network**       | IP: `10.29.1.100` (eth0)   |
| **Target Group**  | Status: `UP` / Response: `HTTP 200` |
| **Health Check**  | Passed via Load Balancer   |

✅ Server responded to HTTP check on `/` and remained healthy.

---

### 🔄 Auto Termination Behavior

If the health check fails (e.g., web server not running), the instance is automatically **terminated** by Auto Scaling:

| Log Entry             | Timestamp               | Status   |
|------------------------|--------------------------|----------|
| `Server Termination`   | `2025-07-01 15:47:50`    | SUCCESS  |
| `Block Storage Deleted`| `2025-07-01 15:47:50`    | SUCCESS  |
| `ASG Update`           | multiple timestamps      | SUCCESS  |

> ⚠️ Auto Scaling terminated the instance after failed health check.

---

### 🧼 Deletion Workflow

To clean up all related resources:

1. Stop monitoring: delete related **Event Rule** from Cloud Insight
2. Set Auto Scaling **desired capacity = 0**
3. Wait for all instances to terminate
4. Delete **Auto Scaling Group**
5. Delete **Target Group**, **Load Balancer**
6. Delete Subnets and VPC (if not in use)

---

### ✅ Key Takeaways

- Auto Scaling with Cloud Insight and CPU metrics works reliably in NCP
- Health checks must be configured properly (e.g., nginx running on port 80)
- Instances are created and terminated based on health and policy
- Manual cleanup requires deleting Event Rules first to unlock ASG

---

### 🛠️ Technologies Involved

- Naver Cloud Platform (NCP)
- Auto Scaling Group (ASG)
- Cloud Insight (Monitoring & Event Rule)
- Load Balancer (HTTP)
- Target Group & Health Check
- Stress Test Utility (`stress`)
- Custom AMI with nginx
