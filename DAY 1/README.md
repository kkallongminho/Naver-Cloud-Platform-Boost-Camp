📘 Naver Cloud Platform (NCP) Server & Auto Scaling Setup - Summary

🚀 Overview

This project demonstrates how to configure a scalable and secure infrastructure using Naver Cloud Platform (NCP). It covers VPC creation, public/private subnet setup, server deployment, and Auto Scaling with Load Balancer integration.

⸻

🔧 Infrastructure Configuration

✅ 1. VPC & Subnet
	•	Created a custom VPC named hnu20222016
	•	Configured two subnets:
	•	hnu-20222016-kr1-prv-sub (Private, 10.29.0.0/24)
	•	hnu-20222016-kr1-pub-sub (Public, 10.29.1.0/24)
	•	Internet Gateway linked to the public subnet for external access

✅ 2. Server Deployment
	•	Server type: c2-g2-s50 (2 vCPU, 4GB RAM, 50GB SSD)
	•	OS image: Custom image hnu-20222016
	•	Servers deployed in private subnet with Load Balancer handling external traffic

✅ 3. Load Balancer
	•	Protocol: HTTP (Port 80)
	•	Target Group created and connected to Auto Scaling Group
	•	Health check enabled via / endpoint (HTTP 200 expected)

✅ 4. Auto Scaling Group
	•	Name: hnu-20222016-kr1-prv-sub
	•	VPC: hnu20222016
	•	Desired Capacity: 2 (initially)
	•	Health Check: Load Balancer-based
	•	Scaling Policy: CPU utilization > 30% triggers scale-out
	•	Cooldown: 300 seconds

⸻

📡 Monitoring & Alerts
	•	Connected to Cloud Insight for real-time monitoring
	•	Event Rule configured:
	•	Metric: avg_cpu_used_rto
	•	Threshold: CPU usage > 30% for 1 minute
	•	Action: Send alert via SMS/Email and trigger Auto Scaling

⸻

🧹 Resource Cleanup

To properly delete all resources:
	1.	Stop Cloud Insight Monitoring (delete Event Rule)
	2.	Set desired capacity to 0 in Auto Scaling Group
	3.	Delete Auto Scaling Group
	4.	Terminate all related servers
	5.	Delete associated Load Balancer, Target Group, NAT Gateway
	6.	Finally, delete the Subnet and VPC

⸻

🗂 Technologies Used
	•	Naver Cloud Platform (NCP)
	•	Auto Scaling Group (ASG)
	•	Load Balancer (LB)
	•	Cloud Insight
	•	Custom AMI (image)
	•	Private/Public Subnet with Internet Gateway

