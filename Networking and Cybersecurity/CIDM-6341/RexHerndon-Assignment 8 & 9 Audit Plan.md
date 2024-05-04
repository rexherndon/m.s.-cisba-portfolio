# Assignment 8 & 9: Audit Plan

# Disclaimer:

This assignment was originally intended as the final project for my “Current Issues in Cybersecurity” class (CIDM-6341) taught by Dr. Murray Jennex at West Texas A&M University in the Spring 2023 semester. Since then, this assignment has been published to this GitHub repository as a part of developing my portfolio for my M.S. Computer Information Systems and Business Analytics Capstone Course (CIDM-6395) taught by Dr. Jeffry Babb. 

The business (along with other individuals/entities that may have been reviewed in this audit) have no identifiable information listed here in order to protect their privacy and right to confidentiality.

# **What we did:**

For this assignment, I performed an audit on a local coffee shop in order to review the overall physical and internet security of the business. In order to do this, I met with one of the co-owners of the business at their primary location to initially start the audit. Since they were also tending to their customers at this time, I had to be brief with my time directly spent with them. This meant that I had to start by asking the co-owner all of the questions I needed for the audit, which included the following:

1. What is your (public) wi-fi password?
2. How often do you change the password for this?
3. What kind of equipment do you use to connect to the network? Is it just a router or do you have any other network equipment that you use?
4. Does your business take any other special precautions to make sure the router is secure?
5. Do you store any data over time on your cash register (tablet)? If so, what?
6. Is the cash register password-protected or locked in any way?
7. Is there CCTV or cameras in/around the building? If so, do you have access to review the footage if needed?
8. With the data on your cash register/CCTV’s, are there back-up copies made in case any data goes missing? If so, do you test the backups on them from time to time?
9. Are front/back doors locked outside of business hours?
10. Are there surge protectors plugged into your devices? If so, do you know how old they might be?
11. Have you had any previous experiences where your internet security was at risk or breached as a business?
12. Finally, do I have permission to continue looking for vulnerabilities or weak spots in your network? 

I additionally mentioned that I will not do an extreme “deep dive” on their entire network architecture, but I would be doing surface-level observations without breaching their privacy or security (ie. - from the perspective of a normal customer). Any and all findings and assessments will be made to the business as recommendations for them in order to keep the audit as casual and respectable as possible.

For the remainder of my time, I completed a port scan via ShieldsUp ([https://www.grc.com/shieldsup](https://www.grc.com/shieldsup)) to assess the common port status and went to HaveIBeenPwned (https://haveibeenpwned.com) to see if their wi-fi password was detected in any previous data breaches. After I gathered all of my information, I provided them with my findings and recommendations for the internet security of the business.

---

# What are the results:

**Finding 1:**

One of the most significant findings I found was with the strength of their wi-fi password. The password I used to login at the time of this assignment is shown below.

```markdown
SSID: ********
PASSWORD: wehavewifi
```

On the contrary, I found out that they change their passwords once every month, but with my experience at this particular coffee shop, the previous passwords I have used were in similar strength (I vaguely remember one of the passwords being “darkknight” for reference”). I understand why they would keep the public wi-fi password simple for ease of access, but having a password this weak can only make their network more vulnerable. The fact that they rotate their passwords very often does make for a decent counter to this vulnerability though.

I was very surprised to find out that their current password was not found in any data breach though according to HaveIBeenPwned (which is good news for them):

![Untitled](Assignment%208%20&%209%20Audit%20Plan%20535ad2dff6d74fffae408bd3775a30ac/Untitled.png)

**Finding 2:**

From previous experience, any time I would connect to this SSID, I would also get a “weak security” notification, similar to the screenshot attached to the side.

However, at the time of this write-up (03/24/2023), I was able to connect without any of those notifications. I was not able to identify which type of wi-fi security protocol they are using, but I’m very glad that they have updated their security type on these routers.

The owner did mention that they did not take any other security measures to ensure that the router is protected. This meant that any person was able to go into the coffee shop and have physical access to the parent router, which is most likely one of their biggest security vulnerabilities.

![Untitled](Assignment%208%20&%209%20Audit%20Plan%20535ad2dff6d74fffae408bd3775a30ac/Untitled%201.png)

**Finding 3:**

Regarding ShieldsUp, here’s the results of the common port scan:

```
----------------------------------------------------------------------

GRC Port Authority Report created on UTC: 2023-03-24 at 16:59:10

Results from scan of ports: 0, 21-23, 25, 79, 80, 110, 113,
                            119, 135, 139, 143, 389, 443, 445,
                            1002, 1024-1030, 1720, 5000

    0 Ports Open
   12 Ports Closed
   14 Ports Stealth
---------------------
   26 Ports Tested

NO PORTS were found to be OPEN.

Ports found to be CLOSED were: 0, 21, 1002, 1024, 1025, 1026,
                               1027, 1028, 1029, 1030, 1720,
                               5000

Other than what is listed above, all ports are STEALTH.

TruStealth: FAILED - NOT all tested ports were STEALTH,
                   - NO unsolicited packets were received,
                   - A PING REPLY (ICMP Echo) WAS RECEIVED.

----------------------------------------------------------------------
```

and I have also attached the results of the full service ports scan:

```
----------------------------------------------------------------------

GRC Port Authority Report created on UTC: 2023-03-24 at 17:10:56

Results from scan of ports: 0-1055

    0 Ports Open
   72 Ports Closed
  984 Ports Stealth
---------------------
 1056 Ports Tested

NO PORTS were found to be OPEN.

Ports found to be CLOSED were: 0, 1, 2, 3, 4, 5, 6, 30, 60,
                               61, 91, 92, 121, 122, 151, 152,
                               181, 182, 212, 213, 242, 243,
                               272, 273, 302, 303, 332, 333,
                               363, 364, 393, 394, 423, 424,
                               453, 454, 483, 484, 514, 515,
                               544, 545, 606, 607, 636, 637,
                               666, 667, 697, 698, 727, 728,
                               757, 758, 787, 788, 817, 818,
                               848, 849, 878, 879, 908, 909,
                               938, 939, 969, 970, 999, 1000,
                               1029, 1030

Other than what is listed above, all ports are STEALTH.

TruStealth: FAILED - NOT all tested ports were STEALTH,
                   - NO unsolicited packets were received,
                   - A PING REPLY (ICMP Echo) WAS RECEIVED.

----------------------------------------------------------------------
```

It looks like we were able to find several closed ports, but the majority of their ports were set in stealth. This may be because of their ISP or their router configuration, but I was unable to determine the root cause of this. I also noticed that port 60 was closed, which is the port used for TCP/UDP, a significant protocol in the world of internet security.

**Finding 4:**

I also tried to log in to the router I was connected to at the IP address 192.168.10.1, and I was unsuccessful, which is a good thing.

![Untitled](Assignment%208%20&%209%20Audit%20Plan%20535ad2dff6d74fffae408bd3775a30ac/Untitled%202.png)

I tried to see if I could reach 192.168.1.1, which I’ve also seen as a common IP address for a default gateway or router, but my web browser wasn’t able to load anything. 

**Finding 5:**

Moving on to the register, I was able to find out that the POS is just an iPad kiosk that is run entirely by a single application, which after doing some research, is powered by Square.

[Square | Solutions For Your Small, Medium & Large Business](https://squareup.com/us/en)

Square seems to be a very common SAAS (software as a service) solution for small businesses, and they seem to be very well established as a business in the POS industry as well. I tried to look up information on if they had a data breach in the past, and according to an article from their support page, they mentioned the following:

> “Square has not had a data breach occur, but there have been several highly publicised data breaches from many companies in recent years, exposing data from millions of users”
> 

[Square's Password Policy | Square Support Center - US](http://squareup.com/help/us/en/article/6212-square-s-password-policy)

There was no date on the article, but another article from Forbes mentions that their parent company, Block (who owns CashApp as well), did have a data breach by a former employee in April 2022, and their CEO is being sued for negligence of data security.

The author of this article is quoted below:

> “A [lawsuit](https://www.documentcloud.org/documents/22187290-cash-app-investments-sued-over-2022-breach?responsive=1&title=1) was filed claiming that another business founded by billionaire Jack Dorsey was also “negligent” in protecting user data. Block, Inc., which owns Cash App and Square payments technologies, was sued in a class action on Tuesday related to a December 2021 breach of Cash App Investing, in which 8.2 million users’ data was stolen by an employee who still had access to company reports even after they departed.”
> 
> 
> [Jack Dorsey’s Payments Company Block Is Sued For ‘Negligent’ Security After Breach Of 8.2 Million Users’ Data](https://www.forbes.com/sites/thomasbrewster/2022/08/24/jack-dorsey-block-sued-for-negligent-cyber-security-after-cash-app-breach/?sh=42464b282d05)
> 

However, Square POS systems are still used by several local businesses around the area, making this a bigger security risk than I had originally anticipated. While the coffee shop wasn’t able to do a lot about this, it is important for them to be aware of.

**Finding 6:**

In good news, they do have a security camera above their register, which I wasn’t able to spot until now as a frequent customer of this business. They originally had a second camera in the back lounge as well, but that was stolen and unable to be retrieved. The owner was able to check the security footage if needed, but they were not sure if they had any backups of the footage if needed, which could indicate another security vulnerability. I was not able to investigate this further because of the time allotted to interview the owner and the potential breach of privacy.

However, from the perspective of a customer, I was unable to detect where they could view the CCTV footage or find the camera without close inspection, which is good physical security.

**Other Findings:**

From other observations, it appears that they only have a single power strip, and any other device is plugged in to the wall whenever applicable (including the router and the POS). The devices plugged into the power strip are just lights though, so I would believe they have good protection against a power surge if it ever happened. The power strip is on the older side however, with visible debris built up around it over time, but it is okay if no important devices are plugged into it.

Front and back doors are locked outside of business hours, which is a good minimum for physical security as well. Finally, the owner mentioned that they did not have any previous experiences where their data was breached, their router/POS went offline due to an attack, or any other related experiences where their internet security was at risk. I believe this is due to their current security practices combined with their unmentioned belief that their security is based on obscurity, which is not a good philosophy to believe in. I have also attached the answers provided during the interview below:

1. What is your (public) wi-fi password?
    1. wehavewifi
2. How often do you change the password for this?
    1. Every month
3. What kind of equipment do you use to connect to the network? Is it just a router or do you have any other network equipment that you use?
    1. 2 routers. One in the main lobby and another in the back lounge (It looks like this is actually a mesh wi-fi setup, with the main router in the front lobby and a child node of the parent router in the back)
4. Does your business take any other special precautions to make sure the router is secure?
    1. No
5. Do you store any data over time on your cash register (tablet)? If so, what?
    1. Not that she is aware of. (It looks like it’s a tablet kiosk, and everything is cloud/app based).
6. Is the cash register password-protected or locked in any way?
    1. No
7. Is there CCTV or cameras in/around the building? If so, do you have access to review the footage if needed?
    1. One camera by the register, and another used to be in the back but it got stolen.
8. With the data on your cash register/CCTV’s, are there back-up copies made in case any data goes missing? If so, do you test the backups on them from time to time?
    1. She is not entirely sure, and if they have backups, they haven’t tested them.
9. Are front/back doors locked outside of business hours?
    1. Yes
10. Are there surge protectors plugged into your devices? If so, do you know how old they might be?
    1. Yes (into the lights), but she does not know how old they would be. (They look like they have been used for over a year, and upon closer inspection, these are power strips and not surge protectors)
11. Have you had any previous experiences where your internet security was at risk or breached as a business?
    1. No
12. Finally, do I have permission to continue looking for vulnerabilities or weak spots in your network? 
    1. Yes

---

# What are your recommendations:

Regarding recommendations, there are actually few that I would recommend, and with what I found, here’s my list (based on the order they should be implemented in):

**Recommendation 1: Router Placement**

By far, I think the easiest thing they could do would be to change the placement of the main lobby router. With public access, a malicious entity could easily infect the router or even destroy it and affect all business operations, including damage to their POS, potentially CCTV, and all of the customer’s devices. Having wi-fi in a coffee business is very important to attract customers so they could stay for prolonged periods of time. I would suggest that they keep this main router behind their employee counter and simply get a longer ethernet/power cord to keep the device connected if needed. This would be my primary recommendation to them, because it would be one of the easiest solutions they could do while having the greatest impact on their business.

**Recommendation 2: Backups on camera footage**

My next recommendation would be to see if the employees are able to find backup footage. It might be as simple as plugging an external drive in and set that for backups or by looking/searching up at the manual for the system. This is another important one to have in case your primary systems go offline in an attack.

As a hypothetical situation, if a burglar broke into the coffee shop in the middle of the night and damaged the cameras as well as other equipment, they would still be able to have a backup to trace whoever committed the crime. Depending on how this is actually done, this could also be a very economically friendly and effective recommendation for the company.

**Recommendation 3: Replacing power strips**

My third recommendation would be to replace any power strips in the area with surge protectors (or even a UPS for the cameras or essential equipment, like routers). This one is more of a minor recommendation, but I put this one at the third slot in the timeline because of the minimal effort it would take to set this up. Although the tablet POS would still have a battery in case of a power outage, I think it would be ideal to have the router connected to a UPS in case of an outage, so they could continue their essential operations if needed. This business is also relatively small and minimal in terms of equipment used, so they don’t need several surge protectors or even multiple UPS’s in the business. The business could also easily pay off the UPS or surge protectors with the revenue they could earn during an outage, so this could be a good investment.

**Recommendation 4: Configuring common ports to stealth**

Another recommendation I would make for the business would be to either configure the router or speak with their internet service provider to set up all of the common ports to stealth instead of some being set as closed. Having closed ports would send a signal back to anyone who sends out ICMP or echo packets (like using ShieldsUp), which they could use to detect a computer or device that could be potentially hacked or breached in some way. One coffee chain here in the Amarillo/Canyon area, Palace Coffee, has already taken these security measures to change all of their common port responses to stealth (as known from a previous port scan I did there), so it will most likely be possible for this business to do the same. While this change may require more technical experience, time, and effort being used, it is still an important one, which is why I would still add this as one of the top 5 recommendations on this list.

**Recommendation 5: Replacing POS system or figuring out better security measures to protect transaction data.**

My final recommendation in this list would be to replace their POS infrastructure or at least take better security measures to guard the data on the POS. The tablet is an iPad, so a passcode could easily be set up on this device. While that may be an easy change to protect the data on-site, that still doesn’t protect against data breaches against the POS company as a whole. If there are options to limit what data is stored on the specific application for this coffee shop, they may be able to configure that in the application in order to protect their customer’s data, but ultimately, they may need to switch POS providers if needed. This would could also help potentially boost the reputation of the coffee lounge while keeping the accessible ways to make transactions for their business (such as NFC, Apple Pay, etc.). This is the 5th recommendation on my timeline because of the effort required to replace one of their essential parts in the coffee shop’s business, but it is still an important one to consider.

---

# What is their risk posture:

For their overall risk posture, I would say that this business is actually in a decent spot for maintaining internet security. With the minimal amount of equipment they have to work with, this makes their network and their infrastructure easier to maintain while minimizing their digital footprint. I was also relieved to see that they have done their due diligence to some degree with maintaining their internet security - with changing the passwords every month and upgrading their routers security type to WPA3 or a similar security setting. However, they are not perfect, and they have some very important vulnerabilities/risks to look into as well.

I spoke to the owner of the coffee shop, and I mentioned to her that one of the greatest vulnerabilities this business has is with the placement of the router. With the router being located in the main lobby, an agitated person or intrusive entity could easily walk up to the router and either infect the network by directly connecting to it via ethernet or they could easily destroy it, which is probably the company’s most significant risk they are taking. While the child node of the router is less accessible, it still could easily take out their entire network by destroying the parent router. While they have been previously accepting this risk, they will be taking my recommendation to move the router to a more secure location behind their main counter, so employees could keep a closer eye on the router.

Here how I would rank them overall on the CIA triangle:

Confidentiality: Medium

Integrity: Medium

Availability: High

I would say that their most important concern is their availability, since they will always be doing transactions as the main source of revenue as a business. While it’s important it to keep their customer’s data secure during a transaction, it is more important in their case to make sure the transactions are always available so they could keep gaining and retaining revenue as a business. 

Also, while obscurity does not equal security, their location and minimized digital footprint (combined with their current level of due process and due diligence) help this business stay decently secure while staying as accessible to their customers as possible.
