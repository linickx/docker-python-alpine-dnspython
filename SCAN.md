# Security vulnerability scanner (for container) report.

This docker image and packages are not pinned to any version, as such the repository doesn't change and the vulnerabilities present are based on the build time.

To help give users and idea of what the latest dockerhub build/images looks like, this report is produced.

The scanner uses [Grype](https://github.com/anchore/grype/) within a [Github Scan Action](https://github.com/anchore/scan-action) 

---
05-21-2026 14:48:47
---
````
NAME           INSTALLED   FIXED IN  TYPE    VULNERABILITY   SEVERITY  EPSS           RISK   
python         3.14.5                binary  CVE-2026-6100   Critical  0.2% (36th)    0.1    
python         3.14.5                binary  CVE-2026-3298   High      < 0.1% (20th)  < 0.1  
python         3.14.5                binary  CVE-2026-7210   Critical  < 0.1% (19th)  < 0.1  
python         3.14.5      3.15.0a6  binary  CVE-2025-15366  Medium    < 0.1% (23rd)  < 0.1  
python         3.14.5      3.15.0a6  binary  CVE-2025-15367  Medium    < 0.1% (23rd)  < 0.1  
python         3.14.5                binary  CVE-2026-1502   Medium    < 0.1% (22nd)  < 0.1  
busybox        1.37.0-r30            apk     CVE-2025-60876  Medium    < 0.1% (15th)  < 0.1  
busybox-binsh  1.37.0-r30            apk     CVE-2025-60876  Medium    < 0.1% (15th)  < 0.1  
ssl_client     1.37.0-r30            apk     CVE-2025-60876  Medium    < 0.1% (15th)  < 0.1  
python         3.14.5                binary  CVE-2025-12781  Medium    < 0.1% (13th)  < 0.1  
python         3.14.5                binary  CVE-2026-4786   High      < 0.1% (6th)   < 0.1  
python         3.14.5                binary  CVE-2026-6019   Medium    < 0.1% (8th)   < 0.1  
````
