## 📘 Naver Cloud Platform - Auto Scaling & Load Balancer Setup

### 🚀 Overview
This documentation covers the configuration of **Auto Scaling Groups (ASG)** and **Load Balancers (LB)** in **Naver Cloud Platform (NCP)**. The goal is to automatically manage server instances based on CPU usage and ensure high availability via health-checked load balancing.

---

### 🧱 Infrastructure Summary

| Component             | Description                                      |
|-----------------------|--------------------------------------------------|
| **VPC**               | `hnu20222016` - Custom Virtual Private Cloud     |
| **Subnet**            | `hnu-20222016-kr1-prv-sub` (`10.29.0.0/24`) - Private Subnet |
| **Server Spec**       | `c2-g2-s50` (2 vCPU, 4GB RAM, 50GB SSD)          |
| **AMI**               | Custom server image: `hnu-20222016`             |
| **Access Control Group** | `hnu20222016-default-acg` (port rules applied) |

---

### ⚙️ Auto Scaling Group (ASG)

- **Name**: `hnu-20222016-kr1-prv-sub`
- **VPC**: `hnu20222016`
- **Subnet**: `10.29.0.0/24` (Private)
- **Server Count**:
  - Minimum: `0`
  - Maximum: `30`
  - Desired: `2`
- **Scaling Policy**:
  - Metric: `avg_cpu_used_rto`
  - Condition: CPU > 30% for 1 minute
  - Action: Scale out (add instances)
- **Cooldown**: 300 seconds
- **Health Check**: Load Balancer-based

---

### 🌐 Load Balancer

| Item            | Details                         |
|-----------------|----------------------------------|
| **Name**        | `hnu-20222016`                   |
| **Target Group**| `hnu-20222016-tg`                |
| **Protocol**    | HTTP                             |
| **Port**        | 80                               |
| **Target Type** | VPC Server                       |
| **Health Check**| Protocol: HTTP / Path: `/` / Expect: HTTP 200 |

---

### 🔔 Monitoring (Cloud Insight)

| Setting     | Value                                           |
|-------------|-------------------------------------------------|
| **Metric**  | `avg_cpu_used_rto`                              |
| **Condition** | CPU > 30% for 1 minute                        |
| **Action**  | Send Email + SMS alert (Hanbat Univ - Hwang Minho) |
| **Linked Policy** | Auto Scaling Group: Add instance        |

---

### 🗑 How to Delete ASG Cleanly

> Auto Scaling Groups can't be deleted while monitoring is active.

Steps:

1. Go to **Monitoring → Cloud Insight → Event Rule**
2. **Delete the Event Rule** connected to the ASG
3. Set **Desired Capacity = 0** in ASG
4. Terminate all instances
5. Delete Auto Scaling Group
6. Optionally, remove Target Group and Load Balancer
7. Finally, delete the Subnet and related VPC resources

---

### 🗂 Technologies Used

- Naver Cloud Platform (NCP)
- Auto Scaling Group (ASG)
- Load Balancer (HTTP)
- Target Group
- Cloud Insight (Monitoring)
- Custom AMI
- Access Control Group (ACG)
- Private Subnet with internal instance orchestration
