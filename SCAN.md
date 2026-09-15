# Security vulnerability scanner (for container) report.

This docker image and packages are not pinned to any version, as such the repository doesn't change and the vulnerabilities present are based on the build time.

To help give users and idea of what the latest dockerhub build/images looks like, this report is produced.

The scanner uses [Grype](https://github.com/anchore/grype/) within a [Github Scan Action](https://github.com/anchore/scan-action) 

---
09-15-2026 08:32:24
---
````
NAME           INSTALLED   FIXED IN   TYPE    VULNERABILITY   SEVERITY  EPSS          RISK   
python         3.14.7      3.15.0rc2  binary  CVE-2026-17084  Medium    0.6% (46th)   0.3    
python         3.14.7                 binary  CVE-2026-19672  Medium    0.4% (34th)   0.2    
python         3.14.7      3.15.0rc2  binary  CVE-2026-15806  Medium    0.4% (34th)   0.2    
python         3.14.7      3.15.0a6   binary  CVE-2025-15367  Medium    0.3% (26th)   0.2    
busybox        1.37.0-r31             apk     CVE-2025-60876  Medium    0.3% (21st)   0.2    
busybox-binsh  1.37.0-r31             apk     CVE-2025-60876  Medium    0.3% (21st)   0.2    
ssl_client     1.37.0-r31             apk     CVE-2025-60876  Medium    0.3% (21st)   0.2    
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-76642  High      0.2% (7th)    0.1    
python         3.14.7                 binary  CVE-2026-4360   Medium    0.3% (20th)   0.1    
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-78409  High      0.1% (2nd)    < 0.1  
libuuid        2.42.1-r0   2.42.3-r1  apk     CVE-2026-78408  High      0.1% (1st)    < 0.1  
python         3.14.7      3.15.0rc2  binary  CVE-2026-15310  Low       0.3% (26th)   < 0.1  
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-78410  High      < 0.1% (0th)  < 0.1  
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-53612  Unknown   N/A           N/A    
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-53613  Unknown   N/A           N/A    
libuuid        2.42.1-r0   2.42.3-r0  apk     CVE-2026-53614  Unknown   N/A           N/A    
````
