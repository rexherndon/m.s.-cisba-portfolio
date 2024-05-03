# Networking and Cybersecurity Overview

This folder contains my written appraisal for the Networking and Cybersecurity curriculum area in the Master of Computer Information Systems and Business Analytics (MS CISBA) degree program. It goes through the classes I have taken within the curriculum, what they have taught me, the strengths and weaknesses I have regarding this knowledge area, samples of the work I have done within these classes, and any future developments I wish to make related to this knowledge area.

In the Networking and Cybersecurity curriculum area, I have taken two courses:

- CIDM 6341 - Cybersecurity
- CIDM 6340 - Networking Management and Information Security

During that time, I produced different artifacts of work showcasing the knowledge and skills developed in this curriculum area. These artifacts can be found in three different repositories, but I have also taken the time to copy the contents from those repositories into sub-folders within this repository as well (to keep everything consolidated).

- [https://github.com/rexherndon/cidm-6340-artifact](https://github.com/rexherndon/cidm-6340-artifact)
- [https://github.com/rexherndon/cidm-6341-artifact](https://github.com/rexherndon/cidm-6341-artifact)

The CIDM-6340 artifact is a ransomware recovery plan I created for a local business, where I performed an audit of network and cybersecurity posture and identified mission critical assets and preventative measures they could take to help the recovery process.

The CIDM-6341 artifact is similar, but it is an assignment where I performed a security audit on a local business to find any vulnerabilities in their network and provide recommendations for remediating them.

Regarding the implementation of the Cybersecurity and Networking portion of the curriculum, there are two areas I knew I needed to focus on after speaking with Dr. Jennex - security through documentation (ie. - legal security) and application hardening. As the owner of Chordity, I could be held liable for any misuse of the platform if a user faces legal trouble using my website. Because of this, I created a terms of service document that users have to agree to before they finish registering an account to ensure I had security through my documentation. Additionally, I implemented more security features through application hardening. I ensured that all forms on the website included a CSRF token to prevent CSRF/MITM attacks, disabled debug features, restricted API access to certain URLs, and imported my secret variables, such as security/access keys, to Render so they could be encrypted and unable to be accessed when viewing the source code in an HTTP request.