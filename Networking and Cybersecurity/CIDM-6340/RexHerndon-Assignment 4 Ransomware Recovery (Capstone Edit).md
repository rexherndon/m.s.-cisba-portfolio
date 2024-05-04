# Assignment 4: Ransomware Recovery (Capstone Edit)

# Disclaimer:

This assignment was originally intended as the final project for my “Network Management and Information Security” class (CIDM-6340) taught by Dr. Murray Jennex at West Texas A&M University in the Summer II 2023 semester. Since then, this assignment has been published to this GitHub repository as a part of developing my portfolio for my M.S. Computer Information Systems and Business Analytics Capstone Course (CIDM-6395) taught by Dr. Jeffry Babb. 

Any individuals/entities that may have been reviewed in this assignment have no identifiable information listed here in order to protect their privacy and right to confidentiality.

# What did you do?

For this report, I will be designing a ransomware/disaster recovery plan, going through each step of the design and processes used to come up with the plan along the way. 

Throughout the assignments in this network security class, I have been working with a local store, and I have been trying to gather detailed information about their network and attack surface. Along the way, I’ve also gathered a general understanding of their operations as a business too. I made an agreement to not disclose any sort of identifiable information in the reports I have made, but I will still do my best to give relevant and essential information needed for the context of this assignment. At the end of this report, I will provide the business with my recovery plan, recommendations to be proactive/prepared before a disaster would occur, and my scan results from previous assignments.

However, before doing all of this, I had to gather a list of components about the business, including:

1. An overview of the businesses operations
2. A full list of devices on their network, and devices that are in their inventory
3. A list of services/passwords/data that they need for their business
4. A list of backups that need to be prepared and maintained

Once I have this information (acquired by either directly asking the business or retrieving information from previous assignments), I will then come up with a plan and recommendations for the business to mitigate the overall impact of a cyber attack or assist with disaster recovery. If proper precautions are taken beforehand, such as backing up data and having a restoration plan, disaster recovery will become exponentially easier for the business.

For the mitigation and proactive procedures, here’s what I will walk through and work with the business on: 

1. We will identify all known assets and define “mission-critical” or high priority assets (including hardware, software and data), and identify vulnerabilities or ways that the business could lose access to these assets.
    1. This was done first by directly asking the business about their day-to-day operations. Some of the operations involve interacting with their customers (such as making transactions) and other’s don’t. 
    2. I also asked about the assets they used, and if any operational data was stored locally (or “on-prem”). I also asked them to identify their most important assets to recover if they were in a disaster scenario.
    3. Also, since I have been working with them on previous assignments in this class, I have the advantage of already having some understanding with this business and their network. I would also compare their answers with the scans from my previous assignments (ie. - scans involving host discovery in Nmap and Nessus) to get a more complete picture of their full inventory and critical assets.
2. We will remediate any vulnerabilities found and ensure that any “mission-critical” data (including passwords and license keys) are properly backed up. A copy of the data should be able to be restored or recovered if “mission-critical” assets are inaccessible.
    1. The vulnerabilities will be identified in the previous step with Nessus and ShieldsUP, and then from there, we will take action to remediate them through reconfiguring and updating devices.
    2. Passwords that are meant to access sensitive data and operational services are planning to be strengthened in order to avoid them needing to be changed at frequent intervals. Ideally, if their passwords are strong enough, then they can be set to change once every 2 years.
    3. Backups of critical data and endpoint agents will be created and automated to back up at regular intervals (ie. - daily or any time transactional data is entered).
3. We will maintain their assets through regularly scheduled patches and updates. This could also potentially involve dry-runs of disaster recovery scenarios, which simulate cases like ransomware attacks.
    1. Automated vulnerability detection could be done through scheduled Nessus scans or anti-virus software, which might be a more cost-effective and “user-friendly” solution for smaller businesses like the one I am working with. Dr. Jennex also mentioned using the paid version of ShieldsUP to create monthly reports for businesses, so that could also be an effective alternative or supplement. 
    2. Wireshark scans could be performed at scheduled intervals also to perform a granular network analysis. However, using Wireshark would require assistance from someone with an information technology background, since the program is more advanced.

The final disaster/ransomware recovery plan for the business is similar to what we will also see for the proactive procedures, and it will broken up into four different steps/categories (based on the steps provided by Dzimiela and Jennex regarding ransomware recovery for small municipalities in 2019).

1. Identify and restore “mission-critical” assets (including hardware, software and data).
2. Patch or remediate vulnerabilities, starting with ones directly related to the attack or disaster.
3. Clean up remaining damage and restore remaining network components.
4. Reflect and investigate why the disaster happened, and assess what can be done to stay proactive and prevent the disaster from happening in the future.

During this process of creating the procedures for defending their network and being proactive, it was important to clearly convey what I would set up for the business and what they would need to do to maintain their security with minimal interference to their current business operations. I tried my best to make sure what I was doing for them wasn’t an unnecessarily inconvenience for the end-users, but I also made sure to emphasize the importance of information security along the way so they could understand why I was working with them on a project like this.

---

# What are the results?

In this section, I start by providing a description/overview on the business and their operations. From there, I will provide their full known inventory list and identify the “mission-critical” endpoints that need to be protected or recovered first. Afterwards, I will provide information on other important assets that need to be protected or backed up (such as software, credentials, license keys/information, and other related business data). 

Then, I will identify vulnerabilities that the organization can already remediate. Finally, I will summarize all the needed information from these previous deliverables in a disaster/ransomware recovery plan for the business.

The next few sections will be organized in the following format:

| Section Name | Deliverables |
| --- | --- |
| Business Overview and Operations | N/A |
| Inventory and Vital Endpoints | Complete inventory list (categorized by importance) |
| Software and Business Data | Complete list of essential data, software, credentials, license keys/info needed for business operations |
| Current Vulnerabilities | Summarized list of initial vulnerabilities that need to be remediated |
| Maintenance and Recovery Plan | Final recovery/maintenance plan |

## *Business Overview and Operations:*

At first glance, here’s what I was able to understand about the business I have been working with.

Our business is a fairly new local antique shop, selling different goods such as records, posters, and other vintage and collectible items. As of right now, they also only have one location. They only have one POS (point of sale) through a Square POS ([https://squareup.com/us/en/point-of-sale](https://squareup.com/us/en/point-of-sale)), and they also don’t have any CCTV (this is currently being worked on by the business). They do also have a website (hosted and set up through Squarespace), business email, and store phone.

As of right now, a majority of the vendors that they get their items from are regular people around the area looking to sell products directly to the business (combined with a few larger distributors/suppliers for certain products like posters). This essentially makes our business the “middle man” instead of a direct supplier, since they coordinate with different vendors to assess the value of the items, buy them from their vendors, and then generate profit by selling those items back to their customers. Those vendors/sellers reach out via email or phone, and their contact information is stored in a Google Sheet. Their business email has access to the Google Suite, so those products are used for a majority of their operations as well, especially Google Sheets for storing contact information, or Google Drive for file and document storage.

## *Inventory and Vital Endpoints:*

With the devices they have, let’s reveal the full inventory list for the business:

— *Note: This list was made based the results of the host discovery scan in Nessus (Assignment 3), Nmap (more specifically, the Zenmap GUI from assignment 1), and by asking the business directly about their inventory. The results from each of these scans are posted below, but the IPs had the potential to fluctuate because some devices on the network were mobile, and were not always present or connected to the network during one or more scans.*

*[image omitted to maintain privacy]*

*— excerpt of initial host discovery scan w/ Zenmap*

*[image omitted to maintain privacy]*

*— graphical map of endpoints/connections after host discovery and intense scans w/ Zenmap*

*[image omitted to maintain privacy]*

*— overview of host discovery scan results w/ Nessus*

I’ve compiled the full inventory list of devices in the following table:

| Device Name | Device Type | Mobile | Importance |
| --- | --- | --- | --- |
| [omitted to maintain privacy] | Router | No | Critical |
| [omitted to maintain privacy] | POS | No | Critical |
| [omitted to maintain privacy] | Phone | No | Critical |
| [omitted to maintain privacy] | Desktop | No | High/Critical |
| [omitted to maintain privacy] | Desktop | No | High/Critical |
| [omitted to maintain privacy] | Desktop | No | High/Critical |
| [omitted to maintain privacy] | Laptop | Yes | Medium |
| [omitted to maintain privacy] | Printer | No | Low |
| [omitted to maintain privacy] | Phone | Yes | Low |
| [omitted to maintain privacy] | Phone | Yes | Low |
| [omitted to maintain privacy] | TV | No | Low |
| [omitted to maintain privacy] | TV | No | Low |
| [omitted to maintain privacy] | IoT | No | Low |
| [omitted to maintain privacy] | IoT | No | Low |

— *Note: There were other IP addresses that responded to our scans in Nessus and Zenmap, but I was unable to identify or determine what devices were, which is a deficiency in this deliverable. These are most likely personal devices of other employees (or possibly some customers?) but ideally, these should be further investigated.* 

*For now, the unknown devices will not be accounted for for this report, but resolving this deficiency depends on what the business wants on their network. For example, if they want customers to access their wi-fi, they may consider having a separate employee network and a guest network, both of which could be reconfigured with different levels of access.*

I’ve classified their importance to the business based on the following criteria:

- Critical - business can not operate if lost more than a day
- High - business can not operate if lost for at least 2-5 business days
- Medium - notable disruptions if lost for more than 2 weeks
- Low - minimal impact to business operations, even if asset loss is long-term

With this aggregated information, I believe the three most important “on-prem” endpoints to protect or recover are the router, POS, and business phone (in that order by default, but can also vary with each specific scenario and its context). The desktops are also important to protect as well because they are primarily used to access business data (such as contacts for suppliers, ordering products or reviewing financial information), but I marked them as “High/Critical” because a majority of this information can still be accessed from another device, since their main services like Google Drive or Google Sheets are cloud-hosted (which will be discussed more in the next section). However, having the business access an operational service on an alternate device if their critical hardware is lost is not ideal for them, but it is better than not having access to the data entirely.

With the IoTs, like the Google Home or Google Nest for their employee areas, I also made them aware of the security and privacy risks tied with having these devices in the store (and especially in the more sensitive/restricted areas of their business). Particularly, I made them aware of the risk of having an attacker get control of an IoT and being able to listen in on private conversations (similar to people intercepting baby monitor audio, which was covered in previous lectures). At the time of this report, they are still keeping their IoT’s connected to their network, but they may adjust where they will be set up.

— *Note: If the router has an option to back up or export its configuration to an external storage (either cloud-based or on-prem), that should also be done as soon as possible if the router needs to be repaired or replaced. Also, it would be ideal to get multiple different ways to contact vendors (such as Square, Squarespace/their web development company, or other technical/emergency services tied with the business’s products) in case of an emergency breach or if immediate assistance is needed. Both of these will help speed up the recovery process exponentially.*

## *Software and Business Data:*

Since this business is on the smaller end, they don’t have very much data that they depend on, which is good for minimizing their attack surface. With their operations, they attempt to opt-in to bundled or free software whenever applicable (such as the Google Suite), and they currently have a majority of their data tied to cloud-hosted services. Here’s what I was able to find out after speaking with the business.

*— Note: All of the services here are essential to the business, and should be marked as critical to their operations.*

### Square POS:

![Untitled](Assignment%204%20Ransomware%20Recovery%20(Capstone%20Edit)%207dd825d1adcc44bab484cb45089a0e59/Untitled.png)

One of their primary functions in this business (and every business in general) is making transactions. For smaller business, like this one, a Square POS is a popular choice. This is mainly because of the minimal setup and maintenance required for each business. It can even be integrated to accept credit/debit card payments on-the-go through seamless integration with any mobile device or other related services, making POS systems accessible for anyone wanting to start a business.

This business has a single Square register and reader, and all transactions are stored in Square’s cloud hosted database. Transactions would then be deposited and recorded into the business’s bank account in a few business days (or minutes if the business wishes to pay a fee, similar to PayPal).

A backup copy of transactions could be generated if needed as well, which I would recommend for the business to do or automate at regular intervals (such as daily, weekly, or monthly).

### Google Suite:

Our business relies on the Google Suite as much as possible, particularly using services like Google Sheets for storing contact information for suppliers and vendors, Google Drive for storing files like photos of inventory or contracts, their Google account for registering with their IoT’s like their Google Home or Google Nest. They also use their business account to register with YouTube or related media services for playing music or even video on their Roku TVs. 

Google is great for affordable, accessible, and robust services (for both business and personal use), but they are also notorious for discontinuing several of their own services, sometimes seemingly out of nowhere as well (see [https://killedbygoogle.com/](https://killedbygoogle.com/) for more info). I don’t anticipate some of their most popular services (like Google Sheets, Docs and Drive) to go away anytime soon, but there is always that possibility when it comes to Google products. 

Because of this, I would also advise the business to have local backup copies of important and essential data, such as a local spreadsheet of their suppliers contact information, in a daily/weekly interval.

### QuickBooks:

QuickBooks is a popular choice for accounting, expense manage, and invoicing software. QuickBooks can be used “on-prem”, but newer versions of the software are being web-based and cloud-hosted, which is what our business is working with. This is good news for us, but if applicable, local backup copies should also be generated at frequent intervals (ideally, this could be weekly or monthly).

### Website:

With their website, they reached out to an external web development company for building this. According to the business, everything is run with Squarespace, including the hosting and acquisition of their domain name. This website also has a form for customers to contact the business as well for any questions, and those get directed through their Squarespace admin web console and the business email address can respond to form submissions. Additionally, they also post blogs, which are edited and created through the admin web console, and posted on the website.

All of the security configurations, such as setting up HTTPS, were verified and set up by the development company, and our business can reach out to them or Squarespace via technical support if they have issues with the website.

### Passwords/License Keys:

Learning about their passwords was slightly shocking to me, because I found out that they don’t store or write down (which, for the most part, isn’t recommended in the first place) any of their passwords to services like the Google Suite, Square, QuickBooks or access to their website’s admin console. They have one unified password for all of these services, which is accessible, but not ideal.

One of the most important recommendations I made to them was to change this setup. I did recommend to have them set up a password manager (such as 1Password, Dashlane, Bitwarden, etc) and change their passwords to have a unique one generated by the password manager for each service. If they wanted to increase their security, they could also change these passwords in a yearly internal or so, but I did advise them to at least change/strengthen their passwords for each service, and change them if their accounts/passwords were compromised in a data breach (they can easily check this through services like [https://haveibeenpwned.com/](https://haveibeenpwned.com/)).

As for license keys, the main ones that could potentially be backed up are the Windows keys for activating the OS on their desktops (in case these devices needed to be reimaged), and this could also be stored in the password manager (since most of them have places to store secure notes as well). Keys or activation licenses for other softwares are not needed, because that information is tied with their business accounts used for these services.

### Deficiencies:

For this section, I unfortunately wasn’t able to get an exhaustive list of their software without further investigation, but this was one of the areas that I did not want to overstep my boundaries on as a student doing an impromptu audit and analysis of their business. If more time and permission were given, I would be able to investigate further to develop a more complete list of software and data on their attack surface. However, the software’s and data listed here are important and vital to the business and their operations.

## *Current Vulnerabilities:*

The list of vulnerabilities in this report are also not an entirely exhaustive list, which is another deficiency in our report, but it is instead a summarized list compiled from the results in our previous report (Research Report 3) over vulnerability scanning with ShieldsUP and Nessus. More detailed information will be provided there, but this is a comprehensive summary of the scan results provided by that previous report. 

*— Note: In order to resolve this deficiency, more tools, like anti-virus software or other vulnerability detection scans/software, would need to be implemented into the business and constantly monitored to detect, report, and potentially even resolve vulnerabilities on this network. This is an ongoing challenge that every single business, regardless of size or industry, is working towards.*

To start off, doing individual scans with ShieldsUP on my endpoint on the business’s network came back with great results.

*[omitted to maintain privacy]*

*— graphical output from the GRC ShieldsUP “All Service Ports” scan*

```
----------------------------------------------------------------------

GRC Port Authority Report created on UTC: 2023-07-30 at 15:05:17

Results from scan of ports: 0-1055

    0 Ports Open
    0 Ports Closed
 1056 Ports Stealth
---------------------
 1056 Ports Tested

ALL PORTS tested were found to be: STEALTH.

TruStealth: PASSED - ALL tested ports were STEALTH,
                   - NO unsolicited packets were received,
                   - NO Ping reply (ICMP Echo) was received.

----------------------------------------------------------------------
```

*— text output from the GRC ShieldsUP “All Service Ports” scan*

An “All Service Ports” scan, which includes the first 1056 common ports (including important ones like 443 for HTTPS, 53 for DNS, 25 for SMTP, and others), came back with a passing result. All of the ports scanned on my device did not respond GRC’s ICMP/echo pings, which made my device undetectable in the eyes of an attacker trying to scan this network. 

Ports on each endpoint should ideally be set as stealth (where they are undetectable) or closed, but a closed port still lets an attacker know this device exists, which could lead the attacker to investigate this further and find another way to breach your network. However, ports should not be open unless *absolutely necessary*, since this can give an attacker an easy way to infiltrate your network.

With Nessus, I performed several different scans, which look for vulnerabilities or other specific attributes and compare them with Nessus’s database. These can range from general scans looking for misconfigurations on a network, vulnerabilities identified from recent breaches, or more specific scans that look for malware or ransomware.

![Untitled.png](Assignment%204%20Ransomware%20Recovery%20(Capstone%20Edit)%207dd825d1adcc44bab484cb45089a0e59/Untitled%201.png)

*— list of scans available in the free version of Nessus*

Here are the following scans I performed:

- Host Discovery
- Advanced Scan
- WannaCry Ransomware
- Solarigate
- CISA
- ContiLeaks
- Ransomware Ecosystem
- 2022 TLR

Another specific deficiency that I wished to resolve for this report was that Nessus also includes a general “Malware Scan” that you can use, however, it requires you to have access to a set of credentials for each live endpoint scanned. I was not able to obtain this information, but I did let them know about this scan in case they wished to revisit it in the future. To resolve this deficiency, I would need these credentials, but they would also most likely be different for each endpoint on the network.

Besides that though, here is the summary of my findings consolidated from each of these scans, which will be broken up into two parts - general misconfigurations and open ports.

**General Misconfigurations:**

For these, we mainly looked into the “Advanced Scan” results, because this scan was mainly designed for identifying general (and often easy to fix) misconfigurations on this network.

*[omitted to maintain privacy]*

*— excerpt of “Advanced Scan 1 / 192.168.1-254” on Nessus*

Among this output, our most important misconfiguration is the fact that our router is still using default credentials. This is an easy one to change, but it’s a very easy setting to miss as well. This is marked as critical just because of how easy it is to access if it is using the default credentials and how much control an attacker would have if they were able to get into the router’s interface. They could easily shut down their internet or leverage this for other attacks, all with a simple dictionary/brute force attack (which could be done manually in this case, and most likely without a script, code, or other resources).

If the business could remediate one of these vulnerabilities, it should optimally be this one.

With our high/medium/mixed risk vulnerabilities, most of them are also easy to disable or reconfigure. Some of them involve using an outdated version of a protocol like TLS or using outdated encryption methods, like 3DES. Most of these settings can be reconfigured or disabled using the router’s interface. 

A good portion of these alerts also allow us to mainly see services that are on, but are not being used by the business. For example, let’s look at SMB for creating network storage. This scan shows that the protocol is running, but from learning about the business, they don’t use a SMB network storage at all. This service should be disabled also if the business is not using it.

*[omitted to maintain privacy]*

*— excerpt of “Advanced Scan 1 / SMB information”  on Nessus*

Another important alert was that IP forwarding was enabled, but Nessus provides us with this description for that.

> The remote host has IP forwarding enabled. An attacker can exploit this to route packets through the host and potentially bypass some firewalls / routers / NAC filtering. Unless the remote host is a router, it is recommended that you disable IP forwarding.
> 

In our case, I believe it’s okay to keep IP forwarding on, but further investigation is needed to identify if this service should be enabled or disabled for the company.

With each of these scans, we detected no malware, ransomware, or any other type of virus/breach in our attack surface, which is very good for the company.

**Open Ports:**

Because there were several open ports on the live endpoints scanned (reported by nearly every scan I ran in Nessus), I’m providing the full list of open ports found for each IP address below. 

This list is also available in my previous vulnerability detection report.

192.168.1.1

```
Port 53/tcp was found to be open
Port 80/tcp was found to be open
Port 139/tcp was found to be open
Port 443/tcp was found to be open
Port 445/tcp was found to be open
Port 1883/tcp was found to be open
Port 5003/tcp was found to be open
Port 6060/tcp was found to be open
Port 8080/tcp was found to be open
Port 10000/tcp was found to be open
```

192.168.1.73

```
Port 8008/tcp was found to be open
Port 8009/tcp was found to be open
Port 8443/tcp was found to be open
Port 9000/tcp was found to be open
Port 10001/tcp was found to be open
Port 10005/tcp was found to be open
Port 10007/tcp was found to be open
Port 10101/tcp was found to be open
```

192.168.1.110

```
Port 62078/tcp was found to be open
```

192.168.1.139

```
Port 8008/tcp was found to be open
Port 8009/tcp was found to be open
Port 8443/tcp was found to be open
Port 9000/tcp was found to be open
Port 10001/tcp was found to be open
Port 10005/tcp was found to be open
Port 10007/tcp was found to be open
Port 10101/tcp was found to be open
```

192.168.1.174

```
Port 8008/tcp was found to be open
Port 8009/tcp was found to be open
Port 8443/tcp was found to be open
Port 9000/tcp was found to be open
Port 10001/tcp was found to be open
Port 10005/tcp was found to be open
Port 10007/tcp was found to be open
Port 10101/tcp was found to be open
```

192.168.1.175

```
Port 80/tcp was found to be open
Port 443/tcp was found to be open
Port 631/tcp was found to be open
Port 5355/tcp was found to be open
Port 8080/tcp was found to be open
Port 9100/tcp was found to be open
```

192.168.1.179

```
Port 5000/tcp was found to be open
Port 7000/tcp was found to be open
```

192.168.1.212

```
Port 62078/tcp was found to be open
```

192.168.1.215

```
Port 135/tcp was found to be open
Port 139/tcp was found to be open
Port 445/tcp was found to be open
```

With each of these ports, it can be tedious to ultimately sit down (most likely with a IT consultant or someone with IT related experience) and decide which ports need to be left open (if any), but it will greatly help the business reduce their attack surface as well.

Also, as another note that isn’t directly tied with the assignment, the business should also consider physical vulnerabilities and finding ways to remediate them, such as locking down equipment, locking doors when needed, and installing CCTV to help monitor and prevent theft. This is also an often overlooked step in the world of network security and cybersecurity, but physical security is also an important aspect of both of these. The easiest way for an attacker to breach a device is always by having physical access to it.

## *Maintenance and Recovery Plan:*

Maintenance is an often overlooked part, but ultimately, this is where a majority of the business’s efforts will go to after the initial vulnerabilities are identified and patched to the best of their ability. Even though this part could potentially be the most directly involved step for the employees of the business, it is still very crucial for network security and protecting their assets.

However, most businesses turn to automation to offset the physical labor they would take to monitoring and maintaining their internet security. Automated scanning and reporting could be done with some of the tools that we already have (ie. - Nessus or the paid version of ShieldsUP). Additionally, they could also invest in a dedicated anti-virus software (as opposed to the default Windows Defender on a good portion of their devices) that could constantly scan, monitor, and report any unwanted detections. They could also have occasional audits (similar to a check-up at the doctor’s office) for more in-depth scans and results.

Finally, after everything we found - here is the final ransomware/disaster recovery plan for our business (assuming that they have taken our recommendations so far, including recommendations to back up their data, update their software, and remediate our currently found vulnerabilities):

*— Note: This plan was based on the steps provided by the Dzimiela and Jennex security report regarding ransomware recovery for small municipalities in 2019.*

1. Identify and restore “mission-critical” assets (including hardware, software and data).
    1. If the assets are offline, efforts should be made to repair or replace any hardware damaged, starting with our essential hardware (router, POS, and business phone (in that order by default, but can also vary with each specific scenario and its context)). Afterwards, desktops should be checked if hardware needs to be repaired or replaced.
    2. If the hardware is encrypted or inaccessible otherwise, backup snapshots or images should be loaded onto the current hardware if applicable. Otherwise, the inaccessible assets would most likely need to be reset/reimaged or replaced entirely (worst-case scenario).
    3. In either case, depending on what hardware assets are down, the business should also contact any vendors or technical/emergency support tied with their products to accelerate the recovery process.
    4. With software and data, backup copies should also be retrieved and loaded if the software or initial data is inaccessible.
2. Patch or remediate vulnerabilities.
    1. Ideally, if automated intrusion detection and reporting are set up, reports should be investigated to see if this breach came from a new vulnerability or an existing one. In either case, if the vulnerability is identified, efforts should be made to patch it as soon as possible.
    2. If no vulnerabilities were found, further investigation is required (which should be done in step 4).
3. Clean up remaining damage and restore remaining network components.
    1. All remaining assets (hardware, software, data) that aren’t seen as critical or essential from the previous steps should currently be in the restoration process.
4. Reflect and investigate why the disaster happened. Assess what can be done to stay proactive and prevent the disaster from happening in the future.
    1. This may involve switching to different operational or security software, upgrading outdated software, reconfiguring network structures, additional network security training, new policies/rules to be formed, or a deeper investigation to potentially identify other potential reasons for a breach.
    2. The business should also work to identify if this attack was targeted specifically for this business, or if it targeted multiple business as a blanket attack (similar to the ransomware attack related to the Dzimiela and Jennex security report).

---

# What did you learn?

I am really grateful for the opportunities I had in this class to work with a small business and I learned more about several different aspects of network security, along with some new tools, and how I am able to apply them in a real-world scenario.

For context, I currently work within the division of information security at West Texas A&M University, and one of my primary responsibilities is to work with a team that maintains network security across campus. From my experience, I’ve been primarily working with enterprise-level networks for the past few years, and working with small businesses has been really interesting to compare with. Smaller businesses and organizations still have access to some useful tools needed for network security inspection and analysis, but often, they lack the expertise and experience of ensuring their network and assets are properly secured. This is similar to the findings in the Dzimiela and Jennex security report.

From the perspective of an attacker using ransomware, these businesses make an ideal target for a network breach and for a likely payout from the business, since small businesses wouldn’t know what to do or how to prevent that from happening. Fortunately, smaller businesses can still seek help from others to ultimately recover and avoid paying a fee for the possibility of having their data decrypted.

With this assignment, I cumulated all of my knowledge from the previous reports and previous experiences to identify a business’s operations, what their critical assets were, how to protect them by finding and remediating vulnerabilities, and inform a business about how to prevent and recover from a ransomware attack. Essentially, I acted as an IT consultant for this business, and it helped provide me with more experience to both be more aware/confident about my own network security risk and how I can help others feel more safe and secure on their network.

As for the business I helped, even though I personally can’t help them every step of the way, they are also very grateful that I was able to help them become more aware of their network security and more aware of how their assets can be compromised. I know they might not be able to remediate every vulnerability and defend every angle of their attack surface, but I was able to work with them on fixing the extremely crucial vulnerabilities, such as turning off old encryption policies like 3DES, changing their router password, and helping them get started with a password manager. I hope they continue to be more mindful of the network security aspect of their business, and continue to take more steps in securing their network in the future!
