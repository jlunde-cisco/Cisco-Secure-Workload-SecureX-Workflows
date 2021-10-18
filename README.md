# Cisco Secure Workload aka Tetration - SecureX Workflows	

These workflows can be downloaded as JSON files, and imported into Cisco Secure-X orchestrator. The value of these is that you can quickly push malicious IP addresses, or malicious hashes from a Secure-X incident or casebook into Cisco Secure Workload as an inventory filter. These inventory filters can be used within Secure Workload policies in order to quickly block possible malicious traffic within your organization, and/or group workloads that may be running processes with known malicious hashes in order to segement them off from the rest of the infrastructure until the processes are dealt with.

![Quick Video!](Secure-X-ReadMe.gif)

# Pre-Requisites:
- Create an inventory filter within Secure Workload for Malicious IP addresses, and note the filter-ID
- Create an inventory filter within SEcure Workload for Malicious hashes, and note the filter-ID
- Create an API key from within Cisco Secure Workload for use within the workflow(s)

# In Cisco SecureX

 - Click into the 'orchestration' tab within the SecureX header (if you have not already, you may have to request this feature)
 - Import the workflow by clicking 'import' within the orchestration splash screen
 - Open the Workflow and click on the 'start' circle
 - On the right-hand side (you may need to scroll down) fill in the variables with your information (see picture below)
 - If you dont know your inventory filter id, simply open the CSW UI, and open that inventory filter. It will be the value in the URL after '?filter_id='

After importing, and filling in your variable information, you should be able to run these from UI's like SecureX, Cisco Cloud Analytics, Threat Response, and any webpage that you have running with the SecureX ribbon! See the video in this readme for an example!

![See how here!](https://github.com/jlunde-cisco/SecureX/blob/main/workflow_edits.png)

