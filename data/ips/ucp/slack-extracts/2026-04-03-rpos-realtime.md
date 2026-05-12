# UCP × RPOS · real-time integration
Source · Slack #general · 03 - Apr - 2026 · Amogh Dubey
Tag · :ucp:

---

## Release · Real-Time RPOS Integration · NEW FEATURE

### TL;DR

UCP now ingests real-time offline transaction events from Reliance Retail POS (RPOS) across **75+ formats and 15,000+ stores**, powering near real-time audience segments, targeted campaigns, and time-sensitive use cases like NPS surveys.

Approximately 1.5 million orders flow through Reliance Retail stores every single day. Until now, that data lived in batch pipelines, arriving hours (sometimes a full day) after a customer walked out of the store. That meant audience segments were always stale, campaign triggers were always late, and time-sensitive moments like post-purchase NPS surveys were more "post" than anyone wanted. Not anymore.

### What shipped

UCP has gone live with a deep integration into the Reliance Retail POS (RPOS) system. Every in-store transaction now streams into UCP within minutes of checkout, covering 80+ retail formats across 15,000+ stores under both Reliance Retail Limited (RRL) and Reliance Brands Limited (RBL).

This is the foundation for building audience segments off real offline purchase behaviour, not yesterday's data dump.

### How it works

- When a customer completes an in-store purchase, RPOS sends the transaction event to UCP in near real-time
- UCP captures key data points: customer mobile number, store code, city, state, pincode, payment time, POS ID, item count, and more
- This data feeds directly into UCP's segmentation and campaign engines, so teams can build audiences, trigger campaigns (SMS, RCS, CleverTap, Google and Meta Custom Audiences), and launch post-purchase flows within minutes of a transaction
- Currently processing approx. 1.5 million orders per day across the network
- It is also powering near real time NPS for 75+ formats

### What this means

Your offline customers are no longer invisible until the next morning. Segments refresh based on what is actually happening in stores right now, campaigns land while the shopping bag is still warm, and NPS surveys hit inboxes while the experience is still fresh. This turns every Reliance Retail store into a live signal for personalisation and outreach.

### Where to find it

UCP > Audience > Create New Audience · choose the "Order Completed" event and add filters like Order Total · create one-time or recurring audience for near real-time use cases.

### What's next

Deeper transactional data capture is on the way, including line-item level details and payment mode breakdowns, giving teams even richer signals to segment and personalize with.

### Built by

- UCP Devs · Divya Birla · Gurveer Singh
- Engineering · Vaibhav Kulkarni
- Product · Prem Nathwani · Binit Jain
- Program · Atri Ashwin Trivedi
- Mentors · Saumil Dalal
- UCP TOPs and SRE · Srinivasa RDS · Bhushan Barhate and team

Special thanks to Farooq Adam, Advait Pandit, and Kushan Shah for clearing the path.
