# UCP · Fayda Meter for JioMart
Source · Slack · 02 - Apr - 2026 · Amogh Dubey
Tag · :ucp:

---

## Release · Fayda Meter (powered by UCP) for JioMart

Ever wondered how much you've actually saved shopping on JioMart? Now you don't have to guess. The new Fayda Meter shows you your lifetime savings · and even what your entire neighbourhood has saved together.

Because saving alone is good. But saving together? That hits different.

## How it works

Every time an order is completed on JioMart, UCP captures the event and stacks the discount from that order onto the customer's running total, building their lifetime savings over time.

In parallel, we run a pincode-level aggregation on Databricks, grouping discounts by location to compute the neighbourhood savings number.

Both streams · individual and pincode-level · feed into JioMart to power the Fayda Meter in near real time.

## Why this matters

JioMart customers get a real-time view of their savings alongside what others in their pincode are saving · creating a natural nudge: if your neighbours are grabbing deals, why aren't you?

And with the Fayda Meter front and centre in JioMart's IPL season ads, that nudge reaches millions. Catch it during the matches and see it in action. Promo Video link · https://youtu.be/z1r24TH2VBM

## Built by

- UCP Devs · Ratnakirti · Priyank Suthar
- EM · Saumil Dalal
- Product · Amogh Dubey
- Program · Atri Ashwin Trivedi
- UCP TOPs and SRE · Srinivasa RDS · Bhushan Barhate and team

Fayda Meter is currently visible only on Android Devices, with iOS rollout planned in the next few days.
