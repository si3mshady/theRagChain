import requests, os

file_list = [
  {
    "Filename": "10_Considerations_for_a_Cloud_Procurement.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/10-considerations-for-a-cloud-procurement.pdf"
  },
  {
    "Filename": "5_Ways_the_Cloud_Can_Drive_Economic_Development.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/5_ways_the_cloud_can-drive_economic_development.pdf"
  },
  {
    "Filename": "A_Platform_for_Computing_at_the_Mobile_Edge_Joint_Solution_with_HPE_Saguna_and_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/platform-for-computing-at-the-mobile-edge-hpe-saguna-aws.pdf"
  },
  {
    "Filename": "A_Practical_Guide_to_Cloud_Migration_Migrating_Services_to_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/the-path-to-the-cloud-dec2015.pdf"
  },
  {
    "Filename": "Active_Directory_Domain_Services_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/adds-on-aws.pdf"
  },
  {
    "Filename": "Amazon_Aurora_Migration_Handbook.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Migration/amazon-aurora-migration-handbook.pdf"
  },
  {
    "Filename": "Amazon_Aurora_MySQL_Database_Administrators_Handbook_Connection_Management.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/amazon-aurora-connection-management-handbook.pdf"
  },
  {
    "Filename": "Amazon_EC2_Reserved_Instances_and_Other_Reservation_Models.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-reservation-models.pdf"
  },
  {
    "Filename": "Amazon_Elastic_File_System_Choosing_Between_Different_Throughput_and_Performance_Mode.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Storage/amazon_efs_choosing_between_different_performance_and_throughput.pdf"
  },
  {
    "Filename": "Amazon_Virtual_Private_Cloud_Network_Connectivity_Options.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-amazon-vpc-connectivity-options.pdf"
  },
  {
    "Filename": "Amdocs_Optima_Digital_Customer_Management_and_Commerce_Platform_in_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/amdocs-optima-digital-customer-management-and-commerce-platform-on-aws.pdf"
  },
  {
    "Filename": "An_Introduction_to_High_Performance_Computing_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf"
  },
  {
    "Filename": "An_Overview_of_AWS_Cloud_Data_Migration_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Storage/An_Overview_of_AWS_Cloud_Data_Migration_Services.pdf"
  },
  {
    "Filename": "An_Overview_of_the_AWS_Cloud_Adoption_Framework.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf"
  },
  {
    "Filename": "Architecting_for_Genomic_Data_Security_and_Compliance_in_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_dBGaP_Genomics_on_AWS_Best_Practices.pdf"
  },
  {
    "Filename": "Architecting_for_HIPAASecurity_and_Compliance_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf"
  },
  {
    "Filename": "Automating_Elasticity.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-automating-elasticity.pdf"
  },
  {
    "Filename": "Automating_Governance_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Automating_Governance_on_AWS.pdf"
  },
  {
    "Filename": "AWS_Answers_to_Key_Compliance_Questions.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Answers_to_Key_Compliance_Questions.pdf"
  },
  {
    "Filename": "AWS_Best_Practices_for_DDoS_Resiliency.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf"
  },
  {
    "Filename": "AWS_Best_Practices_for_Oracle_PeopleSoft.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-best-practices-for-oracle-peoplesoft.pdf"
  },
  {
    "Filename": "AWS_Certifications_Programs_Reports_and_ThirdParty_Attestations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Certifications_Programs_Reports_Third-Party_Attestations.pdf"
  },
  {
    "Filename": "AWS_Cloud_Adoption_Framework_Security_Perspective.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_CAF_Security_Perspective.pdf"
  },
  {
    "Filename": "AWS_Cloud_Transformation_Maturity_Model.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS-Cloud-Transformation-Maturity-Model.pdf"
  },
  {
    "Filename": "AWS_Database_Migration_Service_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf"
  },
  {
    "Filename": "AWS_Governance_at_Scale.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/AWS_Governance_at_Scale.pdf"
  },
  {
    "Filename": "AWS_Key_Management_Service_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-kms-best-practices.pdf"
  },
  {
    "Filename": "AWS_Key_Management_Service_Cryptographic_Details.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf"
  },
  {
    "Filename": "AWS_Migration_Whitepaper.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Migration/aws-migration-whitepaper.pdf"
  },
  {
    "Filename": "AWS_Operational_Resilience.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Operational_Resilience.pdf"
  },
  {
    "Filename": "AWS_Overview_of_Security_Processes.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf"
  },
  {
    "Filename": "AWS_Response_to_CACP_Information_and_Communication_Technology_SubCommittee.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Response_to_CACP_Information_Storage_Requirements.pdf"
  },
  {
    "Filename": "AWS_Risk__Compliance.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Whitepaper.pdf"
  },
  {
    "Filename": "AWS_Risk_and_Compliance_Overview.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Overview.pdf"
  },
  {
    "Filename": "AWS_Security_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf"
  },
  {
    "Filename": "AWS_Security_Checklist.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Checklist.pdf"
  },
  {
    "Filename": "AWS_Serverless_MultiTier_Architectures_Using_Amazon_API_Gateway_and_AWS_Lambda.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf"
  },
  {
    "Filename": "AWS_Storage_Optimization.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-storage-optimization.pdf"
  },
  {
    "Filename": "AWS_Storage_Services_Overview.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS%20Storage%20Services%20Whitepaper-v9.pdf"
  },
  {
    "Filename": "AWS_User_Guide_to_Financial_Services_Regulations__Guidelines_in_Hong_Kong__Insurance_Authority.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/hong-kong-insurance-authority-financial-regulations-guidelines.pdf"
  },
  {
    "Filename": "AWS_User_Guide_to_Financial_Services_Regulations__Guidelines_in_Hong_Kong__Monetary_Authority.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/HKMA_User_Guide.pdf"
  },
  {
    "Filename": "AWS_User_Guide_to_Financial_Services_Regulations__Guidelines_in_Singapore.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Financial_Services_Regulations_Guidelines_in_Singapore.pdf"
  },
  {
    "Filename": "AWS_User_Guide_to_Financial_Services_Regulations_and_Guidelines_in_Hong_Kong.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/hong-kong-insurance-authority-financial-regulations-guidelines.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Cost_Optimization_Pillar.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__HPC_Lens.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-HPC-Lens.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__IoT_Lens.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-IoT-Lens.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Operational_Excellence_Pillar.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Operational-Excellence-Pillar.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Performance_Efficiency_Pillar.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Performance-Efficiency-Pillar.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Reliability_Pillar.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Security_Pillar.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework__Serverless_Applications_Lens.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS-Serverless-Applications-Lens.pdf"
  },
  {
    "Filename": "AWS_WellArchitected_Framework.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf"
  },
  {
    "Filename": "Backup_and_Recovery_Approaches_Using_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Storage/Backup_and_Recovery_Approaches_Using_AWS.pdf"
  },
  {
    "Filename": "Best_Practices_for_Deploying_Alteryx_Server_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/best-practices-for-deploying-alteryx-server-on-aws.pdf"
  },
  {
    "Filename": "Best_Practices_for_Deploying_Amazon_WorkSpaces.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/workspaces/Best_Practices_for_Deploying_Amazon_WorkSpaces.pdf"
  },
  {
    "Filename": "Best_Practices_for_Deploying_Microsoft_SQL_Server_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/best-practices-for-deploying-microsoft-sql-server-on-aws.pdf"
  },
  {
    "Filename": "Best_Practices_for_Migrating_from_RDBMS_to_Amazon_DynamoDB.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/migration-best-practices-rdbms-to-dynamodb.pdf"
  },
  {
    "Filename": "Best_Practices_for_Migrating_MySQL_Databases_to_Amazon_Aurora.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/Best-Practices-for-Migrating-MySQL-Databases-to-Amazon-Aurora.pdf"
  },
  {
    "Filename": "Best_Practices_for_Running_Oracle_Database_on_AWS.pdf",
    "Link": "https://docs.aws.amazon.com/aws-technical-content/latest/oracle-database-aws-best-practices/oracle-database-aws-best-practices.pdf?icmpid=link_from_whitepapers_page"
  },
  {
    "Filename": "Best_Practices_for_Running_Oracle_Siebel_CRM_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/best-practices-for-running-oracle-siebel-crm-on-aws.pdf"
  },
  {
    "Filename": "Big_Data_Analytics_Options_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Big_Data_Analytics_Options_on_AWS.pdf"
  },
  {
    "Filename": "BlueGreen_Deployments_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_Blue_Green_Deployments.pdf"
  },
  {
    "Filename": "Breaking_Intrusion_Kill_Chains_with_AWS_Reference_Material.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Break-Intrusion-Kill-Chains-with-AWS_Reference-Material.pdf"
  },
  {
    "Filename": "Breaking_Intrusion_Kill_Chains_with_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Break-Intrusion-Kill-Chains-with-AWS.pdf"
  },
  {
    "Filename": "Building_a_RealTime_Bidding_Platform_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Building_a_Real_Time_Bidding_Platform_on_AWS_v1_Final.pdf"
  },
  {
    "Filename": "Building_a_Secure_Approved_AMI_Factory_Process_Using_Amazon_EC2_Systems_Manager_SSM_AWS_Marketplace_and_AWS_Service_Catalog.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-building-ami-factory-process-using-ec2-ssm-marketplace-and-service-catalog.pdf"
  },
  {
    "Filename": "Building_Big_Data_Storage_Solutions_Data_Lakes_for_Maximum_Flexibility.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Storage/data-lake-on-aws.pdf"
  },
  {
    "Filename": "Building_FaultTolerant_Applications_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-building-fault-tolerant-applications.pdf"
  },
  {
    "Filename": "Building_Media__Entertainment_Predictive_Analytics_Solutions_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Analytics/ME%20Advanced%20Analytics%20on%20AWS.pdf"
  },
  {
    "Filename": "Choosing_the_Operating_System_for_Oracle_Workloads_on_Amazon_EC2.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/choosing-os-for-oracle-workloads-on-ec2.pdf"
  },
  {
    "Filename": "Comparing_the_Use_of_Amazon_DynamoDB_and_Apache_HBase_for_NoSQL.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_Comparing_the_Use_of_DynamoDB_and_HBase_for_NoSQL.pdf"
  },
  {
    "Filename": "Configuring_Amazon_RDS_as_an_Oracle_PeopleSoft_Database.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/configuring-amazon-rds-as-peoplesoft-database.pdf"
  },
  {
    "Filename": "Considerations_for_Using_AWS_Products_in_GxP_Systems.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf"
  },
  {
    "Filename": "Core_Tenets_of_IoT.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/core-tenets-of-iot1.pdf"
  },
  {
    "Filename": "Cost_Management_in_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-tco-2-cost-management.pdf"
  },
  {
    "Filename": "Creating_a_Culture_of_Cost_Transparency_and_Accountability.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-transparency-accountability.pdf"
  },
  {
    "Filename": "Criminal_Justice_Information_Service_Compliance_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_CJIS_Whitepaper.pdf"
  },
  {
    "Filename": "CrossDomain_Solutions_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/cross-domain-solutions-on-aws.pdf"
  },
  {
    "Filename": "CSA_Consensus_Assessments_Initiative_Questionnaire.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/CSA_Consensus_Assessments_Initiative_Questionnaire.pdf"
  },
  {
    "Filename": "Data_Warehousing_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/enterprise-data-warehousing-on-aws.pdf"
  },
  {
    "Filename": "Database_Caching_Strategies_Using_Redis.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Database/database-caching-strategies-using-redis.pdf"
  },
  {
    "Filename": "Demystifying_the_Number_of_vCPUs_for_Optimal_Workload_Performance.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Demystifying_vCPUs.pdf"
  },
  {
    "Filename": "Deploying_Microsoft_SQL_Server_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/Deploying_SQLServer_on_AWS.pdf"
  },
  {
    "Filename": "Designing_MQTT_Topics_for_AWS_IoT_Core.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Designing_MQTT_Topics_for_AWS_IoT_Core.pdf"
  },
  {
    "Filename": "Determining_the_IOPS_Needs_for_Oracle_Database_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/determining-iops-needs-for-oracle-database-on-aws.pdf"
  },
  {
    "Filename": "Development_and_Test_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-development-test-environments.pdf"
  },
  {
    "Filename": "Digital_Transformation_Checklist_Using_Technology_to_Break_Down_Innovation_Barriers_in_Government.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/digital-transformation-checklist.pdf"
  },
  {
    "Filename": "Docker_on_AWS_Running_Containers_in_the_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/docker-on-aws.pdf"
  },
  {
    "Filename": "DoDCompliant_Implementations_in_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_DOD_CSM_Reference_Architecture.pdf"
  },
  {
    "Filename": "Encrypting_Data_at_Rest.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_Securing_Data_at_Rest_with_Encryption.pdf"
  },
  {
    "Filename": "Encrypting_File_Data_with_Amazon_Elastic_File_System.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/amazon-efs-encrypted-filesystems.pdf"
  },
  {
    "Filename": "Establishing_Enterprise_Architecture_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/establishing-enterprise-architecture.pdf"
  },
  {
    "Filename": "Estimating_AWS_Deployment_Costs_for_Microsoft_SharePoint_Server.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/estimating-aws-deployment-costs-for-sharepoint.pdf"
  },
  {
    "Filename": "Extend_Your_IT_Infrastructure_with_Amazon_Virtual_Private_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/extend-your-it-infrastructure-with-amazon-vpc.pdf"
  },
  {
    "Filename": "Federal_Financial_Institutions_Examination_Council_FFIEC_Audit_Guide.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/FFIEC_Audit_Guide.pdf"
  },
  {
    "Filename": "File_Gateway_for_Hybrid_Cloud_Storage_Architectures.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-storage-gateway-file-gateway-for-hybrid-architectures.pdf"
  },
  {
    "Filename": "Financial_Services_Grid_Computing_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-financial-services-grid-computing.pdf"
  },
  {
    "Filename": "Guidance_for_Trusted_Internet_Connection_TIC_Readiness_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Guidance_for_Trusted_Internet_Connection_TIC_Readiness_on_AWS.pdf"
  },
  {
    "Filename": "Homelessness_and_Technology.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/homelessness-technology.pdf"
  },
  {
    "Filename": "Hosting_Static_Websites_on_AWS_Prescriptive_Guidance.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Building%20Static%20Websites%20on%20AWS.pdf"
  },
  {
    "Filename": "How_AWS_Pricing_Works.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf"
  },
  {
    "Filename": "How_Cities_Can_Stop_Wasting_Money_Move_Faster_and_Innovate.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/how-cities-can-stop-wasting-money-move-faster-and-innovate.pdf"
  },
  {
    "Filename": "Hybrid_Cloud_DNS_Solutions_for_Amazon_VPC.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/hybrid-cloud-dns-options-for-vpc.pdf"
  },
  {
    "Filename": "Import_Windows_Server_to_Amazon_EC2_with_PowerShell.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/DevOps/import-windows-server-to-amazon-ec2.pdf"
  },
  {
    "Filename": "Infrastructure_as_Code.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/DevOps/infrastructure-as-code.pdf"
  },
  {
    "Filename": "Infrastructure_Event_Readiness.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-infrastructure-event-readiness.pdf"
  },
  {
    "Filename": "Installing_JD_Edwards_EnterpriseOne_on_Amazon_RDS_for_Oracle.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Database/jd-edwards-on-rds-oracle.pdf"
  },
  {
    "Filename": "Integrating_AWS_with_Multiprotocol_Label_Switching.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Networking/integrating-aws-with-multiprotocol-label-switching.pdf"
  },
  {
    "Filename": "Introduction_to_Auditing_the_Use_of_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Auditing_Security_Checklist.pdf"
  },
  {
    "Filename": "Introduction_to_AWS_Security_by_Design.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Intro_to_Security_by_Design.pdf"
  },
  {
    "Filename": "Introduction_to_AWS_Security_Processes.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Intro_Security_Practices.pdf"
  },
  {
    "Filename": "Introduction_to_AWS_Security.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Intro_to_AWS_Security.pdf"
  },
  {
    "Filename": "Introduction_to_DevOps_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_DevOps.pdf"
  },
  {
    "Filename": "Introduction_to_Scalable_Gaming_Patterns_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-scalable-gaming-patterns.pdf"
  },
  {
    "Filename": "ITIL_Asset_and_Configuration_Management_in_the_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/AWS_Asset_Config_Management.pdf"
  },
  {
    "Filename": "ITIL_Event_Management_in_the_Cloud_An_AWS_Cloud_Adoption_Framework_Addendum.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/itil-event-management-in-the-cloud.pdf"
  },
  {
    "Filename": "Jenkins_on_AWS.pdf",
    "Link": "https://docs.aws.amazon.com/aws-technical-content/latest/jenkins-on-aws/jenkins-on-aws.pdf#jenkins-on-aws"
  },
  {
    "Filename": "Lambda_Architecture_for_Batch_and_RealTime_Processing_on_AWS_with_Spark_Streaming_and_Spark_SQL.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/lambda-architecure-on-for-batch-aws.pdf"
  },
  {
    "Filename": "Lambda_Architecture_for_Batch_and_Stream_Processing.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/lambda-architecure-on-for-batch-aws.pdf"
  },
  {
    "Filename": "Laying_the_Foundation_Setting_Up_Your_Environment_for_Cost_Optimization.pdf",
    "Link": "https://docs.aws.amazon.com/aws-technical-content/latest/cost-optimization-laying-the-foundation/cost-optimization-laying-the-foundation.pdf#introduction"
  },
  {
    "Filename": "Leveraging_Amazon_Chime_Voice_Connector_for_SIP_Trunking.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/leveraging_chime_voice_connector_for_sip_trunking.pdf"
  },
  {
    "Filename": "Leveraging_Amazon_EC2_Spot_Instances_at_Scale.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-leveraging-ec2-spot-instances.pdf"
  },
  {
    "Filename": "Leveraging_AWS_Marketplace_Storage_Solutions_for_Microsoft_SharePoint.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/marketplace-storage-softnas-sharepoint.pdf"
  },
  {
    "Filename": "Machine_Learning_Foundations_Evolution_of_Machine_Learning_and_Artificial_Intelligence.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/machine-learning-foundations.pdf"
  },
  {
    "Filename": "Managing_Machine_Learning_Projects.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-managing-ml-projects.pdf"
  },
  {
    "Filename": "Managing_User_Logins_for_Amazon_EC2_Linux_Instances.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Managing-user-login_ec2-linux.pdf"
  },
  {
    "Filename": "Managing_Your_AWS_Infrastructure_at_Scale.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/managing-your-aws-infrastructure-at-scale.pdf"
  },
  {
    "Filename": "Maximizing_Value_with_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/total-cost-of-operation-benefits-using-aws.pdf"
  },
  {
    "Filename": "Microservices_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/microservices-on-aws.pdf"
  },
  {
    "Filename": "Migrating_Applications_to_AWS_Guide_and_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Migration/migrating-applications-to-aws.pdf"
  },
  {
    "Filename": "Migrating_AWS_Resources_to_a_New_Region.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-migrate-resources-to-new-region.pdf"
  },
  {
    "Filename": "Migrating_Microsoft_Azure_SQL_Databases_to_Amazon_Aurora.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Migration/migrating-microsoft-azure-sql-databases-to-amazon-aurora.pdf"
  },
  {
    "Filename": "Migrating_Oracle_Database_Workloads_to_Oracle_Linux_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/migrating-oracle-database-workloads-to-oracle-linux-on-aws.pdf"
  },
  {
    "Filename": "Migrating_to_Apache_HBase_on_Amazon_S3_on_Amazon_EMR.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Migrating_to_Apache_Hbase_on_Amazon_S3_on_Amazon_EMR.pdf"
  },
  {
    "Filename": "Migrating_Your_Databases_to_Amazon_Aurora.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/Migrating your databases to Amazon Aurora.pdf"
  },
  {
    "Filename": "Migrating_Your_Existing_Applications_to_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cloud-migration-main.pdf"
  },
  {
    "Filename": "Modernize_Your_Microsoft_Applications_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/modernize-your-microsoft-applications-whitepaper.pdf"
  },
  {
    "Filename": "Move_Amazon_RDS_MySQL_Databases_to_Amazon_VPC_using_Amazon_EC2_ClassicLink_and_Read_Replicas.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/RDS/Moving_RDS_MySQL_DB_to_VPC.pdf"
  },
  {
    "Filename": "NIST_Cybersecurity_Framework_CSF.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/NIST_Cybersecurity_Framework_CSF.pdf"
  },
  {
    "Filename": "Optimizing_ASP.NET_with_C_AMP_on_the_GPU.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/optimizing-asp-net-with-cpp-amp-on-the-gpu.pdf"
  },
  {
    "Filename": "Optimizing_Electronic_Design_Automation_EDA_Workflows_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/optimizing-electronic-design-automation-eda-workflows-on-aws.pdf"
  },
  {
    "Filename": "Optimizing_Enterprise_Economics_with_Serverless_Architectures.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/optimizing-enterprise-economics-serverless-architectures.pdf"
  },
  {
    "Filename": "Optimizing_Multiplayer_Game_Server_Performance_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/optimizing-multiplayer-game-server-performance-on-aws.pdf"
  },
  {
    "Filename": "Optimizing_MySQL_Running_on_Amazon_EC2_Using_Amazon_EBS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Database/optimizing-mysql-running-on-amazon-ec2-using-amazon-ebs.pdf"
  },
  {
    "Filename": "Oracle_WebLogic_Server_12c_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Oracle-WebLogic-12c-on-AWS.pdf"
  },
  {
    "Filename": "Overview_of_Amazon_Web_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-overview.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Analytics_Mobile_and_Application_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Security_Analytics_Mobile_Services_Applications_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Application_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Security_Application_Services_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Compute_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Security_Compute_Services_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Database_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Security_Database_Services_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Network_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Networking_Security_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_AWS_Security__Storage_Services.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Security_Storage_Services_Whitepaper.pdf"
  },
  {
    "Filename": "Overview_of_Deployment_Options_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/overview-of-deployment-options-on-aws.pdf"
  },
  {
    "Filename": "Overview_of_Oracle_EBusiness_Suite_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Database/overview-oracle-e-business-suite-aws.pdf"
  },
  {
    "Filename": "Overview_of_the_Samsung_Push_to_Talk_PTT_Solution_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/samsung-push-to-talk-solution-aws.pdf"
  },
  {
    "Filename": "Performance_at_Scale_with_Amazon_ElastiCache.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf"
  },
  {
    "Filename": "Practicing_Continuous_Integration_and_Continuous_Delivery_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/DevOps/practicing-continuous-integration-continuous-delivery-on-AWS.pdf"
  },
  {
    "Filename": "Provisioning_Oracle_Wallets_and_Accessing_SSLTLSBased_Endpoints_on_Amazon_RDS_for_Oracle.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/provisioning-oracle-wallets-on-amazon-rds.pdf"
  },
  {
    "Filename": "RealTime_Communication_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Industries/Telco/real-time_communication_aws.pdf"
  },
  {
    "Filename": "Regulation_Systems_Compliance_and_Integrity_Considerations_for_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Regulation_Systems_Compliance_and_Integrity_Considerations.pdf"
  },
  {
    "Filename": "Right_Sizing_Provisioning_Instances_to_Match_Workloads.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/cost-optimization-right-sizing.pdf"
  },
  {
    "Filename": "Robust_Random_Cut_Forest_Based_Anomaly_Detection_on_Streams.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/kinesis-anomaly-detection-on-streaming-data.pdf"
  },
  {
    "Filename": "Running_Adobe_Experience_Manager_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Adobe AEM on AWS.pdf"
  },
  {
    "Filename": "Running_Containerized_Microservices_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/DevOps/running-containerized-microservices-on-aws.pdf"
  },
  {
    "Filename": "Running_Neo4j_Graph_Databases_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Database/neo4j-graph-databases-aws.pdf"
  },
  {
    "Filename": "SaaS_Solutions_on_AWS_Tenant_Isolation_Architectures.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/saas-solutions-on-aws-final.pdf"
  },
  {
    "Filename": "SaaS_Storage_Strategies_Building_a_Multitenant_Storage_Model_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Multi_Tenant_SaaS_Storage_Strategies.pdf"
  },
  {
    "Filename": "SAP_HANA_on_AWS_Operations_Overview_Guide.pdf",
    "Link": "https://d1.awsstatic.com/enterprise-marketing/SAP/SAP_HANA_on_AWS_Implementation_and_Operations_Guide.pdf"
  },
  {
    "Filename": "Secure_Content_Delivery_with_CloudFront.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/Secure_content_delivery_with_CloudFront_whitepaper.pdf"
  },
  {
    "Filename": "Securely_Access_Services_Over_AWS_PrivateLink.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-privatelink.pdf"
  },
  {
    "Filename": "Security_at_Scale_Governance_in_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Security_at_Scale_Governance_in_AWS_Whitepaper.pdf"
  },
  {
    "Filename": "Security_at_Scale_Logging_in_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_Security_at_Scale_Logging_in_AWS_Whitepaper.pdf"
  },
  {
    "Filename": "Security_of_AWS_CloudHSM_Backups.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/security-of-aws-cloudhsm-backups.pdf"
  },
  {
    "Filename": "Security_Overview_of_AWS_Lambda.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Overview-AWS-Lambda-Security.pdf"
  },
  {
    "Filename": "Serverless_Architectures_with_AWS_Lambda.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/serverless-architectures-with-aws-lambda.pdf"
  },
  {
    "Filename": "Serverless_Streaming_Architectures_and_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Serverless_Streaming_Architecture_Best_Practices.pdf"
  },
  {
    "Filename": "Setting_Up_Multiuser_Environments_for_Classroom_Training_and_Research.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-setting-up-multiuser-environments-education.pdf"
  },
  {
    "Filename": "Single_SignOn_Integrating_AWS_OpenLDAP_and_Shibboleth.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-whitepaper-single-sign-on-integrating-aws-open-ldap-and-shibboleth.pdf"
  },
  {
    "Filename": "Sizing_Cloud_Data_Warehouses.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Size-Cloud-Data-Warehouse-on-AWS.pdf"
  },
  {
    "Filename": "SoftNAS_Architecture_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/softnas-architecture-on-aws.pdf"
  },
  {
    "Filename": "Strategies_for_Managing_Access_to_AWS_Resources_in_AWS_Marketplace.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/strategies-for-managing-access-to-aws-resources-in-aws-marketplace.pdf"
  },
  {
    "Filename": "Strategies_for_Migrating_Oracle_Databases_to_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/strategies-for-migrating-oracle-database-to-aws.pdf"
  },
  {
    "Filename": "Streaming_Data_Solutions_on_AWS_with_Amazon_Kinesis.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/whitepaper-streaming-data-solutions-on-aws-with-amazon-kinesis.pdf"
  },
  {
    "Filename": "Tagging_Best_Practices_Implement_an_Effective_AWS_Resource_Tagging_Strategy.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf"
  },
  {
    "Filename": "The_Total_Cost_of_Non_Ownership_of_a_NoSQL_Database_Cloud_Service.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-tco-dynamodb.pdf"
  },
  {
    "Filename": "The_Total_Cost_of_Non_Ownership_of_Web_Applications_in_the_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-tco-web-applications.pdf"
  },
  {
    "Filename": "U.S._Securities_and_Exchange_Commissions_SEC_Office_of_Compliance_Inspections_and_Examinations_OCIE_Cybersecurity_Initiative_Audit_Guide.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_SEC_Cybersecurity_Guide.pdf"
  },
  {
    "Filename": "Understanding_T2_Standard_Instance_CPU_Credits.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/t2-std-cpu-credits.pdf"
  },
  {
    "Filename": "Understanding_the_ASDs_Cloud_Computing_Security_for_Tenants_in_the_Context_of_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Understanding_the_ASDs_Cloud_Computing_Security_for_Tenants_in_the_Context_of_AWS.pdf"
  },
  {
    "Filename": "Use_Amazon_Elasticsearch_Service_to_Log_and_Monitor_Almost_Everything.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/whitepaper-use-amazon-elasticsearch-to-log-and-monitor-almost-everything.pdf"
  },
  {
    "Filename": "Use_AWS_Config_to_Monitor_License_Compliance_on_Amazon_EC2_Dedicated_Hosts.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws_config_dh_whitepaper_v1_editcb_editsm_final.pdf"
  },
  {
    "Filename": "Use_AWS_WAF_to_Mitigate_OWASPs_Top_10_Web_Application_Vulnerabilities.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Security/aws-waf-owasp.pdf"
  },
  {
    "Filename": "Using_AWS_for_Disaster_Recovery.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-disaster-recovery.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Australian_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Australian_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Common_Privacy__Data_Protection_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Common_Privacy_and_Data_Protection_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Hong_Kong_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Hong_Kong_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Japan_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Japanese_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Malaysian_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Malaysian_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_NCSC_UKs_Cloud_Security_Principles.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/AWS_NCSC_UK_Cloud_Security_Principles.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_New_Zealand_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_New_Zealand_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_PhilippinesPrivacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Philippines_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_Singapore_Privacy_Considerations.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_Singapore_Privacy_Considerations.pdf"
  },
  {
    "Filename": "Using_AWS_in_the_Context_of_UK_Healthcare_IG_SoC_Process.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_UK_Healthcare_IG_SoC_process.pdf"
  },
  {
    "Filename": "Using_Windows_Active_Directory_Federation_Services_ADFS_for_Single_SignOn_to_EC2.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/ec2-adfs-howto.pdf"
  },
  {
    "Filename": "Web_Application_Hosting_in_the_AWS_Cloud_Best_Practices.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/aws-web-hosting-best-practices.pdf"
  },
  {
    "Filename": "WeDo_Telecom_RAID_Risk_Management_Solution_in_the_AWS_Cloud.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/Industries/Telco/WeDo_RAID_Risk_Management_Solution_AWS_Cloud.pdf"
  },
  {
    "Filename": "WordPress_Best_Practices_on_AWS.pdf",
    "Link": "https://d1.awsstatic.com/whitepapers/wordpress-best-practices-on-aws.pdf"
  }
]

download_dir = "./papers"

# Check if the "papers" directory exists, create it if not
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    print(f"Created directory: {download_dir}")

for file_info in file_list:
    filename = file_info["Filename"]
    url = file_info["Link"]
    file_path = os.path.join(download_dir, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

print("Download completed.")