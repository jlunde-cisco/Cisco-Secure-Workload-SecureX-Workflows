# Cisco Secure Workload - Secure-X Workflows	

These workflows can be downloaded as JSON files, and imported into Cisco Secure-X orchestrator. The value of these is that you can quickly push malicious IP addresses, or malicious hashes from a Secure-X incident or casebook into Cisco Secure Workload as an inventory filter. These inventory filters can be used within Secure Workload policies in order to quickly block possible malicious traffic within your organization, and/or group workloads that may be running processes with known malicious hashes in order to segement them off from the rest of the infrastructure until the processes are dealt with.

![Quick Video!](Secure-X-ReadMe.mp4)

The pre-requisites are that you already have an inventory filter created (one malicious IP addresses, and one for malicious hashes) that you wish to push either the 1) Malicious IP addresses, or 2) Malicious hashes into, and you must have an API Key generated for your Cisco Secure Workload instance.

# After Importing...

 - Open the Workflow and click on the 'start' circle
 - On the right-hand side (you may need to scroll down) fill in the variables with your information (see picture below)
 - If you dont know your inventory filter id, simply open the CSW UI, and open that inventory filter. It will be the value in the URL after '?filter_id='


![See how here!](https://github.com/jlunde-cisco/SecureX/blob/main/workflow_edits.png)

