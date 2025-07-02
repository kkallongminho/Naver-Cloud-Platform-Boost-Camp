⚙️ Auto Scaling Group (ASG)
	•	Name: hnu-20222016-kr1-prv-sub
	•	VPC: hnu20222016
	•	Subnet: 10.29.0.0/24 (Private)
	•	Server Count:
	•	Minimum: 0
	•	Maximum: 30
	•	Desired: 2
	•	Scaling Policy:
	•	Metric: avg_cpu_used_rto
	•	Condition: CPU > 30% for 1 minute
	•	Action: Scale out (add instances)
	•	Cooldown: 300 seconds
	•	Health Check: Load Balancer-based

⸻

🌐 Load Balancer
	•	Name: hnu-20222016
	•	Target Group: hnu-20222016-tg
	•	Protocol: HTTP
	•	Port: 80
	•	Target Type: VPC Server
	•	Health Check:
	•	Protocol: HTTP
	•	Path: /
	•	Response Code: 200 (OK)

⸻

🔔 Monitoring (Cloud Insight)
	•	Event Rule Created:
	•	Metric: avg_cpu_used_rto
	•	Threshold: >30% for 1 minute
	•	Notification: Email + SMS (to Hanbat University - Hwang Minho)
	•	Connected Action:
	•	Auto Scaling Policy Trigger (add server)

⸻

🗑 How to Delete ASG Cleanly

Auto Scaling Groups can’t be deleted while monitoring is active.

Steps:
	1.	Go to [Monitoring] → [Cloud Insight] → [Event Rule]
	2.	Delete the Event Rule connected to the ASG
	3.	Set Desired Capacity = 0 in ASG
	4.	Terminate all instances
	5.	Delete Auto Scaling Group
	6.	Optionally, remove Target Group and Load Balancer
	7.	Finally, delete the Subnet and related VPC resources

⸻

🗂 Technologies Used
	•	Naver Cloud Platform (NCP)
	•	Auto Scaling Group (ASG)
	•	Load Balancer (HTTP)
	•	Target Group
	•	Cloud Insight (Monitoring)
	•	Custom AMI
	•	Access Control Group (ACG)
	•	Private Subnet with internal instance orchestration
