"""Master spec for every IP that powers the Reliance Retail × Fynd register.

Edit this file to update an IP's canonical data. Run `python3 tools/build_data/build.py`
to regenerate the `data/ips/<slug>/` folders.

Sources used to populate this spec:
- JCP Migration Tracker (Salman Saudagar)
- Impetus Sell Track IPs · Sheet 2 (Devam Gosalia · 29 - Apr - 2026)
- UCP Release Notes Timeline (Amogh Dubey · 29 - Apr - 2026)
- Slack channels of record per IP
- Website itself · v0.8.1
"""

# Each IP follows the schema in data/SCHEMA.md.
# Tracks (the 12) are also IPs in this list, marked role="track-headline".
IPS = [
    # =========================================================================
    # TRACK 01 · JCP · Jio Commerce Platform
    # =========================================================================
    {
        "slug": "jcp",
        "name": "Jio Commerce Platform",
        "tagline": "The single Sell + Support layer underneath every B2C and B2B Reliance Retail brand. 79 channels.",
        "track": "jcp",
        "track_role": "track-headline",
        "status": "Live",
        "since": "2023-07-31",
        "last_release": "2026-04-21",
        "verticals": ["fashion", "grocery", "electronics", "beauty", "pharma", "home", "jewellery"],
        "value_chain": ["plan", "buy-make", "move", "sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp",
        "external_url": "https://www.jiomart.com",
        "tags": ["platform", "commerce", "microservices"],
        "narrative": """JCP is the single commerce stack that runs every Reliance retail business · online and offline. 78 distinct channels migrated, 68 live in production today, across 10 retail verticals. The microservice architecture handles 350K peak orders/hour, scales to JioMart's 1.6M daily orders, and onboards new sellers from 2 weeks down to 48 hours.

Fynd built JCP. Reliance owns and runs it. Every brand site, every storefront, every B2B distribution flow runs through it.""",
        "why_this_matters": "JCP is the moat. No retailer in India runs ten verticals on one stack. Every new Reliance brand launches in days, not quarters. Every cross-vertical insight (UCP identity, JIIA agentic shopping, Konnect orchestration) is unlocked because there's one platform underneath.",
        "metrics": [
            ("channels_total", "Channels on JCP", "78", "B2C and B2B channels migrated or migrating", "JCP Migration Tracker · 21 - Feb - 2026", "audited"),
            ("channels_live", "Channels Live", "68", "Customer using it today", "JCP Migration Tracker", "audited"),
            ("channels_pilot", "Channels Pilot", "5", "UAT or single-store live", "JCP Migration Tracker", "audited"),
            ("channels_build", "Channels Build", "5", "In active engineering", "JCP Migration Tracker", "audited"),
            ("peak_orders_per_hour", "Peak orders / hour", "350K", "Architecture-tested through flash sale, IPL, EOSS", "JCP load testing", "tested"),
            ("orders_per_min_peak", "Orders / min · peak", "50K+", "Sustained peak", "JCP ops", "audited"),
            ("customers_served", "Customers served", "300M+", "Active customers on JCP-routed flows", "UCP analytics", "live"),
            ("uptime_fy26", "Uptime FY26", "99.9%", "JioMart at 1.6M daily orders", "JCP SRE", "audited"),
        ],
        "team": {
            "cpo": ["Ashish Chandorkar"],
            "cpo_jcp": ["Arunoday Ray"],
            "engineering": ["Pratikkumar Patel · Director Engineering", "Kapil Kapri · Staff EM", "Imran Khan · EM", "Avinash Ajith Kumar · EM"],
            "ril_counterpart": ["Jeyandran", "Vineeth Nair"],
            "mentors": ["Jigarkumar Dafda · CTPO Fynd Central", "Farooq Adam"],
        },
        "links": {
            "production_urls": [
                ("https://www.jiomart.com", "JioMart"),
                ("https://www.ajio.com", "AJIO"),
                ("https://www.tirabeauty.com", "Tira"),
                ("https://www.netmeds.com", "Netmeds"),
            ],
        },
    },

    # ----- UCP -----
    {
        "slug": "ucp",
        "name": "Unified Customer Platform",
        "tagline": "One identity across every Reliance retail business.",
        "track": "jcp",
        "track_role": "headline",
        "status": "Live",
        "since": "2024-01-11",
        "last_release": "2026-04-21",
        "verticals": ["fashion", "grocery", "electronics", "beauty", "pharma"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#ucp",
        "tags": ["customer-data", "identity", "cdp", "audience"],
        "narrative": """UCP is the customer data platform underneath every Reliance retail surface. 400M+ profile records unified across online and offline, eliminating third-party CDPs. Powers OTP, in-house messaging (JioCX), personalisation, NPS, audience segmentation, and near-real-time campaign activation.

API latency ~19ms. Event processing ~300ms end-to-end. 500 events/sec sustained. TOPs-managed in production. Vetted by Jio InfoSec.""",
        "why_this_matters": "Every other Sell-side IP (loyalty, NPS, campaigns, recommendations) sits on UCP. Without UCP unified across formats, every channel runs its own customer file and the cross-format value of Reliance's customer base is uncapturable.",
        "metrics": [
            ("identities_unified", "Identities unified", "400M+", "UCP profile records across RR online + offline · multi-device", "UCP production", "live"),
            ("rpos_daily_orders", "RPOS daily orders streaming", "1.5M", "Every in-store transaction streams into UCP within minutes", "UCP analytics", "audited"),
            ("rpos_stores", "Stores streaming RPOS", "15,000+", "Across 75+ formats · RRL + RBL", "UCP × RPOS integration", "audited"),
            ("nps_formats", "NPS coverage · formats", "79", "SMS-based NPS triggered 1-2 hours after POS purchase", "UCP NPS", "live"),
            ("nps_orders_processed", "NPS orders processed", "7.2M", "Cumulative since rollout 01 - Apr - 2026", "UCP NPS", "live"),
            ("api_latency_ms", "API latency p50", "~19 ms", "UCP API", "UCP SRE", "live"),
            ("event_processing_ms", "Event processing end-to-end", "~300 ms", "Stream-to-segment", "UCP SRE", "live"),
            ("throughput_events_per_sec", "Throughput sustained", "500/sec", "Production load", "UCP SRE", "live"),
        ],
        "team": {
            "dri": ["Amogh Dubey · Product"],
            "em": ["Saumil Dalal"],
            "product": ["Prem Nathwani", "Amogh Dubey", "Binit Jain"],
            "engineering_lead": ["Vaibhav Kulkarni"],
            "engineering": [
                "Aniket Aggarwal", "Gurveer Singh", "Nirmal", "Divya Birla",
                "Ratnakirti", "Priyank Suthar", "Krupali Mehta", "Jatin Hazrati",
            ],
            "qa": ["Priyanjali Manore"],
            "program": ["Atri Ashwin Trivedi"],
            "devops": ["Amboj Goyal", "Manish Singh", "Ayushi", "Tejas F"],
            "tops_sre": ["Srinivasa RDS · UCP TOPs", "Bhushan Barhate"],
            "mentors": ["Farooq Adam", "Advait Pandit", "Kushan Shah"],
        },
        "releases": [
            ("2026-04-21", "Campaign Coupon Codes", "Shared and personalised coupons in Campaign Manager. CSV / ZIP customer-to-coupon mapping at delivery time.", "JCP Coupons + Central Promotion Engine integration"),
            ("2026-04-03", "RPOS Real-Time · 15K+ stores", "Every in-store transaction streams into UCP within minutes. 1.5M orders/day · 75+ formats · RRL + RBL. Replaces day-old batch data.", None),
            ("2026-04-02", "Fayda Meter on JioMart", "Lifetime savings + neighbourhood savings (pincode aggregation on Databricks). Featured in JioMart's IPL season ads.", None),
            ("2026-04-01", "NPS at scale · 79 formats", "SMS triggered 1-2 hours after every in-store POS purchase. 7.2M orders processed · 500K daily surveys · ~7K daily responses.", None),
            ("2026-03-24", "API-First Retail Account + Unified Address Book", "Native login/signup UI without SDKs or redirections. Cross-platform address reuse for frictionless checkout.", None),
            ("2026-01-30", "Multi-feature rollout · RPOS, RCS, Analytics", "RPOS bringing ~2L daily transaction events · NPS expansion · native RCS campaigns · device fingerprinting · audiences pushed to Meta and Google Ads. 46 campaigns run · 7 format adoptions.", None),
            ("2025-12-15", "AI-Powered UCP Documentation", "Step-by-step business-user guide built with Cursor + Docusaurus + Scribe. Live at docs.sit.ccpz0.de.", None),
            ("2025-09-19", "SizeSense · live in AJIO", "Reads brand, fit type, size to suggest the right option on AJIO product pages. Reduces returns.", None),
            ("2025-05-02", "More For Me · personalised recommendations on JioMart", "Homepage product suggestions powered by order history and localised preferences. Backend · RRA → Kafka → MongoDB → real-time API.", None),
            ("2025-04-10", "Reliance Retail Account v2 · the unified login", "Eleven months in development. DPDP-compliant consent, centralised account management, Retail SSO, JioSwift email integration, JCP Beta whitelisting.", None),
            ("2025-02-03", "Platform Foundation + Personalisation", "360° Single Customer View · Audience Builder v2 · Complete Your Basket AI/ML widget on JioMart · RBAC · OTP service rehauled.", None),
            ("2024-02-23", "Reliance Retail Authentication + Address Optimisation", "In-house OTP for JioMart. Address Optimisation pilot · 69,318 addresses optimised across 76 pincodes via Jio ACL. MilkBasket integration goes live.", None),
            ("2024-01-11", "First UCP launch · Reliance Retail Identity", "310M customers unified across online + offline RR. Live with JioMart, AJIO, Netmeds, Tira, FreshPik. TOPs-managed. InfoSec vetted.", None),
        ],
        "links": {
            "demos": [("https://youtu.be/9KCFnV6kXEU", "AI Native UCP · full demo")],
            "case_studies": [("https://reliance-retail-fynd.vercel.app/jcp#ucp", "Reliance Digital · Digital Discount Days · ₹20.39 Cr · 1.25M recipients")],
        },
        "case_study": {
            "name": "Reliance Digital · Digital Discount Days",
            "window": "2026-04-11 to 2026-04-19",
            "campaigns": 10,
            "headline_metrics": {
                "recipients": "1.25M",
                "product_revenue_inr": "₹20.39 Cr",
                "transacting_buyers": 5660,
                "open_rate": "30.68%",
                "avg_ticket_value_inr": "₹34,145",
            },
            "transactor_segment_lift": {
                "open_rate": "+25%",
                "click_rate": "+314%",
                "ctor": "+234%",
            },
            "category_mix": {
                "large_appliances_inr_cr": 8.11,
                "telecom_inr_cr": 6.90,
                "entertainment_inr_cr": 1.91,
                "it_inr_cr": 1.81,
                "small_appliances_inr_cr": 1.37,
            },
            "saturday_19_apr_revenue_inr_cr": 4.08,
        },
    },

    # ----- Companion App -----
    {
        "slug": "companion-app",
        "name": "Trends Companion App",
        "tagline": "The biggest Sell milestone · 117 → 3,000+ stores · ₹7.83 Cr platform fees.",
        "track": "samarth",
        "track_role": "headline",
        "status": "Live",
        "since": "2024-09-01",
        "last_release": "2026-04-15",
        "verticals": ["fashion", "grocery", "electronics"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/#companion-app",
        "tags": ["mobile-app", "in-store", "loyalty", "scan-and-go"],
        "narrative": """One mobile app for every in-store moment across Trends, Reliance Digital, and Smart Bazaar. Started at 117 Trends stores. Live across 3,000+ stores combined in under 12 months.

12 P0 features in production · Store Detection, Scan & Go, Endless Aisle, Gamified Look Builder, Wishlist Transfer, Trends Tube creator feed, Post-Visit Engagement, R-One Loyalty wallet, Lookbook, Wardrobe, Missions, Coupon engine.

Single Cart vs Dual Cart architecture · won at Apex review.""",
        "why_this_matters": "Companion App is the only surface that bridges in-store and digital for Reliance fashion. ₹7.83 Cr in Platform Fees is recurring SaaS-style revenue · grows linearly with store count, not project count. Architecture decision (Single Cart) sets the template for every future companion-app surface across Reliance.",
        "metrics": [
            ("stores_live", "Stores live", "3,000+", "Combined Trends + RD + Smart Bazaar · 25× growth from 117 baseline", "Companion App ops · 29 - Apr - 2026", "live"),
            ("platform_fees_inr_cr", "Platform fees booked YTD", "₹7.83 Cr", "Cumulative platform fees FY26 · run-rate scaling", "Fynd finance · 29 - Apr - 2026", "audited"),
            ("p0_features", "P0 features shipped", "12", "Store Detection · Scan & Go · Endless Aisle · Look Builder · Wishlist Transfer · Trends Tube · Post-Visit · Wallet · Lookbook · Wardrobe · Missions · Coupons", "Product roadmap", "live"),
            ("trends_stores", "Trends stores · primary footprint", "2,171", "Reliance Trends format only", "Reliance Retail FY26", "audited"),
            ("rd_stores", "Reliance Digital stores · Companion rolling", "650+", "RD format", "Reliance Retail", "audited"),
            ("smart_bazaar_stores", "Smart Bazaar stores · Companion + JioGames", "1,200+", "Smart Bazaar format", "Reliance Retail", "audited"),
            ("yousta_scans", "Yousta · scans on Companion", "92.4K+", "Across 87 stores", "Yousta ops", "live"),
        ],
        "team": {
            "dri": ["Brijkishor Singh"],
            "engineering": ["Store OS Eng team", "POS team"],
            "mentors": ["Shyam Dixit", "Devam Gosalia"],
        },
        "releases": [
            ("2026-04-15", "Single Cart architecture · Apex sign-off", "Single Cart won over Dual Cart at Apex review. Sets template for every future companion-app surface.", None),
            ("2025-12-01", "3,000+ store milestone reached", "From 117 stores at start. 25× scale.", None),
            ("2025-09-01", "P0 feature freeze · 12 features in production", "Store Detection, Scan & Go, Endless Aisle, Look Builder, Wishlist Transfer, Trends Tube, Post-Visit, Wallet, Lookbook, Wardrobe, Missions, Coupons.", None),
        ],
    },

    # ----- Konnect -----
    {
        "slug": "konnect",
        "name": "Fynd Konnect",
        "tagline": "Marketplace orchestration OS for Reliance brand sites.",
        "track": "jcp",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2023-08-01",
        "verticals": ["fashion", "grocery", "electronics"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#konnect",
        "tags": ["marketplace", "orchestration", "b2b"],
        "narrative": """Konnect is the marketplace OS layer of JCP · routes orders, inventory, catalog, and pricing across 50+ external marketplaces (Amazon, Flipkart, Myntra, Tata CLiQ) and Reliance brand storefronts.""",
        "metrics": [
            ("channels", "Marketplace channels", "50+", "Amazon · Flipkart · Myntra · Tata CLiQ · etc.", "Konnect ops", "live"),
        ],
        "team": {
            "dri": ["Farhan Khan · Director Growth and Product"],
            "mentors": ["Jigarkumar Dafda"],
        },
    },

    # ----- ZIP -----
    {
        "slug": "zip",
        "name": "ZIP · AJIO Commerce Agent",
        "tagline": "Natural-language shopping agent on AJIO.com.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-09-15",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#zip",
        "external_url": "https://www.ajio.com",
        "tags": ["ai-agent", "conversational", "search"],
        "narrative": """ZIP is the AI shopping agent on AJIO.com · natural-language search and recommendation via chat and voice. Replaces menu-driven navigation for vague-intent shoppers.""",
        "metrics": [
            ("positive_engagement", "Positive engagement", "88%", "User feedback on ZIP responses", "AJIO product analytics", "live"),
            ("catalog_coverage", "Catalog coverage", "86%", "% of catalog ZIP can answer for", "AJIO product analytics", "live"),
            ("chats_total", "Chats driven through ZIP", "2M+", "Cumulative", "AJIO product analytics", "live"),
        ],
        "team": {"dri": ["AJIO + Fynd AI team"]},
    },

    # ----- JIIA -----
    {
        "slug": "jiia",
        "name": "JIIA · Jio Intelligent Agentic shopping",
        "tagline": "Agentic shopping on JioMart · Google Cloud Next '26 keynote.",
        "track": "jcp",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-09-01",
        "verticals": ["grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#jiia",
        "tags": ["ai-agent", "agentic", "google-cloud"],
        "narrative": """JIIA is the agentic shopping layer on JioMart · powers natural-language queries, multi-turn dialogues, image search, and complex shopping intents. Featured in Google Cloud Next '26 keynote with Gemini integration.""",
        "metrics": [
            ("images_indexed", "Images indexed", "40M+", "Multimodal index across catalog", "JIIA system", "live"),
        ],
        "team": {"mentors": ["Jigarkumar Dafda"]},
    },

    # =========================================================================
    # TRACK 02 · IMPETUS · F&L AI Platform
    # =========================================================================
    {
        "slug": "impetus",
        "name": "Impetus",
        "tagline": "Reliance's AI-first platform for Fashion and Lifestyle retail.",
        "track": "impetus",
        "track_role": "track-headline",
        "status": "Live",
        "since": "2024-11-13",
        "last_release": "2026-04-25",
        "verticals": ["fashion"],
        "value_chain": ["plan", "buy-make", "move", "sell"],
        "ownership": "reliance",
        "web_anchor": "/impetus",
        "tags": ["ai-platform", "fashion", "fl"],
        "narrative": """Impetus is the AI platform powering Plan, Buy/Make, Move, Sell across Reliance Fashion and Lifestyle. 14 IPs in production today. Took a 9-month design-to-shelf cycle and rebuilt it as a 3.6-day vendor-to-store loop.

Trend research, 3D design, manufacturing, store delivery, in-store sell, customer listening, and real-time decisioning · all running on one stack with daily prod deploys.""",
        "why_this_matters": "Fashion is Reliance's most complex retail vertical. Impetus standardised the AI brain across every brand · Trends, Azorte, Yousta, Fashion Factory, AJIO, RBL · so a Trend-to-Design improvement at AJIO automatically helps Trends, and a Cortex planning win at Trends helps Azorte.",
        "metrics": [
            ("ips_in_production", "IPs in production", "14", "Live IP register", "Impetus product team", "live"),
            ("vendor_to_store_days", "Vendor-to-store cycle", "3.6 days", "Down from 9-month design-to-shelf baseline", "Impetus ops", "live"),
            ("active_manufacturers", "Active manufacturers", "930", "Vendor Scan & Pack network", "Impetus ops", "live"),
            ("options_per_year", "Options designed per year", "39.2K", "Through AI Cataloging + AI Photoshoot pipeline", "Impetus catalog", "live"),
        ],
        "team": {
            "dri": ["Kushan Shah · CTPO Impetus"],
            "engineering": ["Kingshuk Bhattacharya · EM-2", "Arvind Mishra · EM-2", "Arjunsingh Yadav · EM-2", "Purav Shah · EM-2"],
        },
    },

    # ----- Trend-to-Design -----
    {
        "slug": "trend-to-design",
        "name": "Trend-to-Design Agent",
        "tagline": "Trend → moodboard → linesheet → tech-pack · Claude Code skill.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-10-01",
        "verticals": ["fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/impetus#trend-to-design",
        "external_url": "https://www.ajio.com/superdry-sdx-keys-t-shirt",
        "tags": ["ai-agent", "design", "claude-code"],
        "narrative": """Converts trend + brand context into manufacturable design options and auto-generates complete tech packs (specs, BOM, trims, artwork) for vendor-ready handoff. Re-runnable Claude Code skill per category × season × geography.

Proven at Superdry SDX · 120 designs in 5 days with 2 designers. 90% reduction in design time. Live on AJIO.""",
        "metrics": [
            ("designs_per_run", "Designs · Superdry SDX", "120", "In 5 days", "AJIO product launch", "live"),
            ("time_reduction", "Time reduction vs manual", "90%", "Design cycle", "Superdry SDX case", "live"),
        ],
        "team": {
            "dri": ["Kushan Shah"],
            "team": ["Chestha", "Harsh Kumar"],
        },
    },

    # ----- AI Cataloging -----
    {
        "slug": "ai-cataloging",
        "name": "AI Cataloging",
        "tagline": "Auto-generated catalog imagery, attributes, copy across brands.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2024-08-01",
        "verticals": ["fashion"],
        "value_chain": ["buy-make", "sell"],
        "ownership": "reliance",
        "web_anchor": "/impetus#ai-cataloging",
        "tags": ["catalog", "ai-pim"],
        "narrative": """AI-powered catalog suite · Mannequin Image generation, AI-generated models library (ethnicity / age / size / gender), AI Photoshoot Studio, AI Enriched Catalog, AI Generated Video. Live for Trends. Expanding to Azorte, Yousta, Fashion Factory through FY26-27.""",
        "team": {"dri": ["Rajnandini Sharma"]},
    },

    # ----- Print Designer + Garment Designer -----
    {
        "slug": "print-designer",
        "name": "Print Designer",
        "tagline": "15-day turnaround compressed to 3 minutes.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-06-01",
        "verticals": ["fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/impetus#print-designer",
        "tags": ["design", "ai-generation"],
        "metrics": [
            ("cycle_time_before", "Cycle time before", "15 days", "Manual print designer turnaround", "Impetus baseline", "audited"),
            ("cycle_time_after", "Cycle time after", "3 min", "AI-assisted with human review", "Impetus production", "live"),
        ],
    },

    {
        "slug": "garment-designer",
        "name": "Garment Designer",
        "tagline": "24-day cycle compressed to 30 minutes.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-09-01",
        "verticals": ["fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/impetus#garment-designer",
        "tags": ["design", "ai-generation"],
        "metrics": [
            ("cycle_time_before", "Cycle time before", "24 days", "Manual garment designer turnaround", "Impetus baseline", "audited"),
            ("cycle_time_after", "Cycle time after", "30 min", "AI-assisted", "Impetus production", "live"),
        ],
    },

    # ----- Cortex Planning -----
    {
        "slug": "cortex",
        "name": "Cortex · Planning Agent",
        "tagline": "Store-realistic POR · fixture-level VM · daily prod deploys.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-09-15",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["plan"],
        "ownership": "reliance",
        "web_anchor": "/impetus#cortex",
        "tags": ["planning", "ai-agent"],
        "narrative": """Cortex generates a store-realistic Plan of Record (POR) and converts it into fixture and slot-level Visual Merchandising layouts. Detects exceptions in execution and triggers replans automatically. The planning brain inside Impetus Fashion · also seeded into Granary for grocery.""",
    },

    # ----- Fynd Create -----
    {
        "slug": "fynd-create",
        "name": "Fynd Create",
        "tagline": "Vendor-to-store loop · 600+ vendors · 10M+ pieces/month capacity.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-04-01",
        "verticals": ["fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/impetus#fynd-create",
        "tags": ["sourcing", "vendor"],
        "narrative": """Fynd Create runs the vendor management loop for Azorte, Superdry, and the broader Reliance fashion portfolio. 600+ vendors active. 10M+ pieces/month manufacturing capacity orchestrated.""",
        "metrics": [
            ("active_vendors", "Active vendors", "600+", "Through Fynd Create", "Fynd Create ops", "live"),
            ("monthly_capacity_pieces", "Monthly capacity", "10M+", "Pieces/month", "Fynd Create ops", "live"),
        ],
    },

    # ----- AutRi -----
    {
        "slug": "autri",
        "name": "AutRi · Autonomous Robotics",
        "tagline": "95%+ shelf compliance · 98% SKU recognition · 20-30K sq.ft per run.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Pilot",
        "since": "2025-11-01",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["move"],
        "ownership": "reliance",
        "web_anchor": "/impetus#autri",
        "tags": ["robotics", "shelf", "computer-vision"],
        "narrative": """Autonomous shelf-compliance robots + AI delivering real-time shelf intelligence. Detects out-of-stock, pricing errors, planogram non-compliance.""",
        "metrics": [
            ("shelf_compliance_accuracy", "Shelf compliance accuracy", "95%+", "vs 60% industry average for manual audits", "AutRi pilot", "live"),
            ("sku_recognition", "SKU recognition · real-time", "98%+", "Across pilot deployments", "AutRi pilot", "live"),
            ("coverage_per_run_sqft", "Coverage per robot run", "20-30K sq.ft", "Single deployment", "AutRi pilot", "live"),
        ],
    },

    # ----- Vendor Scan & Pack -----
    {
        "slug": "vendor-scan-pack",
        "name": "Vendor Scan & Pack",
        "tagline": "3.6 days vendor-to-store · 930 active manufacturers · 39.2K options/year.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2024-06-01",
        "verticals": ["fashion"],
        "value_chain": ["move"],
        "ownership": "reliance",
        "web_anchor": "/impetus#vendor-scan-pack",
        "tags": ["logistics", "vendor"],
    },

    # ----- Digital Twin -----
    {
        "slug": "digital-twin",
        "name": "Digital Twin",
        "tagline": "Fabric · garment · supply · store · 4 layers digitally mirrored.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-08-01",
        "verticals": ["fashion"],
        "value_chain": ["plan", "move"],
        "ownership": "reliance",
        "web_anchor": "/impetus#digital-twin",
        "tags": ["3d", "supply-chain", "simulation"],
        "narrative": """From fabric to store, digitally mirrored. Fabric (3D drape simulation), Garment (fit visualization), Garment Supply Chain (capacity tracking), Store (planogram + shelf layouts). Eliminates physical swatches, reduces sampling cycles, improves space utilization.""",
    },

    # ----- Ask Impetus -----
    {
        "slug": "ask-impetus",
        "name": "Ask Impetus · AI Business Analyst",
        "tagline": "CXO + brand-head facing · NL Q&A across all retail systems.",
        "track": "impetus",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-12-01",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/impetus#ask-impetus",
        "tags": ["ai-agent", "analyst", "natural-language"],
        "narrative": """Natural-language Q&A across all retail systems. Explains the why, quantifies impact, recommends the next-best fix. Removes the analyst-as-bottleneck for store, brand, and category decisions.""",
    },

    # =========================================================================
    # TRACK 03 · GRANARY · Grocery AI
    # =========================================================================
    {
        "slug": "granary",
        "name": "Granary",
        "tagline": "Grocery AI Platform · Phase 1 live across Smart Bazaar + Smart Point · 11-store Mumbai pilot.",
        "track": "granary",
        "track_role": "track-headline",
        "status": "Live",
        "since": "2025-11-13",
        "verticals": ["grocery"],
        "value_chain": ["plan", "buy-make", "move", "sell"],
        "ownership": "reliance",
        "web_anchor": "/granary",
        "tags": ["grocery-ai", "forecasting", "assortment"],
        "narrative": """Granary is the agentic planning and assortment platform for grocery retail. Smart replenishment, perishable inventory management, category optimisation. The grocery counterpart to Impetus Fashion.

Fynd built the brain (Cortex), the data spine (Databricks), the shelf-truth layer (AutRi), and the ordering rails (Quick · WMS · DMS) that turn 12K SKUs across 4K stores into a single autonomous operating loop.""",
        "metrics": [
            ("skus_modeled", "SKUs modeled", "12K", "Per ML forecasting cycle", "Granary ops", "live"),
            ("stores_modeled", "Stores modeled", "4K", "Per ML forecasting cycle", "Granary ops", "live"),
            ("rows_processed", "Rows processed per cycle", "48M", "Per LightGBM run", "Granary data spine", "live"),
            ("mape", "MAPE", "41%", "16-loc validation · down from 55%+ baseline · L4 target ~25-30%", "Granary ML team", "live"),
            ("autonomous_decisions", "Autonomous decisions", "70-80%", "Replenishment + assortment", "Granary ops", "live"),
            ("shelving_events_reduction", "Shelving events reduction", "−28%", "Phase 1 · 10 Mumbai stores", "Assortment Intelligence", "live"),
        ],
        "team": {
            "platform_leads": ["Aushin Ganguli", "Advait Pandit"],
            "ml": ["Shahid Kazi · DRI ML Forecasting"],
        },
        "releases": [
            ("2025-11-13", "Granary Cortex · live on Maharashtra rollout", "150+ users trained", None),
            ("2025-12-01", "Assortment Intelligence · 10 Mumbai stores phase 1", "−28% shelving events", None),
        ],
    },

    # =========================================================================
    # TRACK 04 · SAMARTH · Workforce
    # =========================================================================
    {
        "slug": "samarth",
        "name": "Samarth",
        "tagline": "Workforce + in-store ops · Store OS · POS · Companion App.",
        "track": "samarth",
        "track_role": "track-headline",
        "status": "Live",
        "since": "2024-04-01",
        "last_release": "2026-04-29",
        "verticals": ["fashion", "grocery", "electronics", "beauty"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth",
        "tags": ["workforce", "store-os", "pos"],
        "narrative": """Samarth runs the daily operating beat of every Reliance Retail format. Store OS, POS, Companion App, Scan & Go, R-One Loyalty, Coupons, AI Cataloging in-store, Workforce Intelligence dashboards.""",
        "team": {
            "dri": ["Nishant Amin · Product / Program lead"],
            "team": ["Sai Jaswanth Marlapalli", "Manasa Kandukuri", "Karan Muley"],
        },
    },

    # ----- Scan & Go -----
    {
        "slug": "scan-and-go",
        "name": "Scan & Go",
        "tagline": "8 RIL brands live · ₹2.5 Cr/year invoice savings · 5 min/customer saved.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2023-08-09",
        "verticals": ["fashion", "grocery", "beauty"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#scan-and-go",
        "tags": ["self-checkout", "qr"],
        "narrative": """Mobile self-checkout via QR · customer scans, pays digitally, walks out with e-invoice. Saves ₹2.5 Cr/year in invoice costs and 5 minutes per customer per visit.

Live across Reliance Trends, Yousta, Azorte, GAP, FreshPik, RIL Jewels, JioGames, Fashion Factory.""",
        "metrics": [
            ("brands_live", "Brands live", "8", "Trends, Yousta, Azorte, GAP, FreshPik, RIL Jewels, JioGames, Fashion Factory", "Scan & Go ops", "live"),
            ("invoice_savings_inr_cr", "Invoice savings · annual", "₹2.5 Cr", "Across rolled-out brands", "Finance", "audited"),
            ("time_saved_per_customer_min", "Time saved per customer per visit", "5 min", "vs traditional checkout", "Scan & Go ops", "live"),
        ],
        "team": {
            "dri": ["Shyam Dixit"],
            "engineering": ["Kedar Kulkarni", "Chalapathi Rao", "Muralidhar Edam"],
            "mentors": ["Farooq Adam"],
        },
    },

    # ----- PulsePoint -----
    {
        "slug": "pulsepoint",
        "name": "Retail PulsePoint",
        "tagline": "Sales-force optimisation · pilot at 17 stores since 07 - Nov - 2025.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Pilot",
        "since": "2025-11-07",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#pulsepoint",
        "tags": ["store-ops", "kpi"],
        "narrative": """One-stop Store Operations Solution. 3 pillars · Business Enablement (AOP vs Actuals KPIs), Inventory Insights (scan-stock, sales velocity, weeks-of-cover), Operational Efficiency (Task Mgmt, Ticket Mgmt, Staff Rostering, Planograms). Pilot store · Kammanahalli (36 employees).""",
        "metrics": [
            ("stores_live", "Stores live", "17", "Pilot footprint since 07 - Nov - 2025", "PulsePoint ops", "live"),
            ("users_active", "Active users", "33", "Across pilot stores", "PulsePoint ops", "live"),
            ("tasks_logged", "Tasks logged", "2,948", "Cumulative since launch", "PulsePoint", "live"),
            ("task_completion_rate", "Task completion rate", "77.42%", "Pilot performance", "PulsePoint", "live"),
        ],
        "team": {"dri": ["Devam Gosalia · Saaket Chawali"]},
    },

    # ----- Store Command Center -----
    {
        "slug": "store-command-center",
        "name": "Store Command Center",
        "tagline": "Unified ops cockpit · 3 modules · Impetus stack.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#store-command-center",
        "narrative": """Unified ops cockpit · monitor + plan + act across the entire retail ecosystem. 3 modules · Command Center (unified view), Agentic Control Tower (real-time exception resolution), Store Intelligence (AI-powered demand/competition decoding). Adjacent to Store Kundli (store 360 dossier) and Store Adoption & Visits.""",
        "team": {"dri": ["Om · Pritam"]},
    },

    # ----- R-One Loyalty -----
    {
        "slug": "r-one-loyalty",
        "name": "Club R-One Loyalty",
        "tagline": "Tiered loyalty · standardised across Sephora, Hamleys, Kiko, Trends, Azorte, Yousta.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion", "beauty"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#r-one-loyalty",
        "narrative": """Reliance-One loyalty integration across the RBL and JCP brand portfolio. Tier system (Red/Blue/Black), points earn/burn/expiry, cash vouchers + product rewards, missions, daily/weekly check-ins, dormancy & lapser journeys, cart abandonment triggers, personalised recommendation engine.""",
        "team": {"dri": ["Brijkishor Singh"]},
    },

    # ----- Digital Coupons -----
    {
        "slug": "digital-coupons",
        "name": "Digital Coupons",
        "tagline": "Brand-level, segment-targeted · 1.3L+ wedding-card coupons issued.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#digital-coupons",
        "narrative": """Coupon issuance, validation, and redemption infrastructure on Trends Companion App + Scan & Go storefronts. Brand-level, time-bound, customer-segment-targeted coupons. Wedding-cards motion alone issued 1.3L+ coupons. Powers EOSS, Black Friday, V-Day campaigns.""",
        "metrics": [
            ("wedding_cards_issued", "Wedding-cards motion · coupons issued", "1.3L+", "Single campaign", "Coupons ops", "live"),
        ],
        "team": {"dri": ["Pritam · Megatron service team"]},
    },

    # ----- AI-Led Digital Campaigns -----
    {
        "slug": "ai-campaigns",
        "name": "AI-Led Digital Campaigns",
        "tagline": "Agentic marketing · ~2 campaigns/month for Trends + Reliance brands.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#ai-campaigns",
        "external_url": "https://trends.shop/tunewithtrends",
        "narrative": """Agentic Marketing · autonomously builds and optimises commerce campaigns (audiences, creatives, timing, measurement). ~2 campaigns/month for Trends + Reliance brands. Generative media stack · PixelBin (5K+ images), Fynd Studios (50+ AI Ads), Fynd Snap (25K photoshoots), GlamAR (200+ AR/VR).""",
        "team": {"dri": ["Farhan Mirza"]},
    },

    # =========================================================================
    # TRACK 05 · ALP · Real-Estate Platform
    # =========================================================================
    {
        "slug": "alp",
        "name": "ALP · Adaptive Land Platform",
        "tagline": "Real-estate platform for new-store decisions · grounded in revenue forecasts.",
        "track": "alp",
        "track_role": "track-headline",
        "status": "Build",
        "since": "2025-08-01",
        "verticals": ["fashion", "grocery", "electronics"],
        "value_chain": ["plan"],
        "ownership": "reliance",
        "web_anchor": "/alp",
        "tags": ["real-estate", "geospatial", "agentic"],
        "narrative": """ALP folds Vista's geospatial signals, RIL's transaction data, and an agentic feasibility engine into one ALP record per site, so every Reliance new-store decision is auditable, format-aware, and grounded in revenue forecasts rather than tribal knowledge.""",
        "team": {"dri": ["Karan Muley"]},
    },

    # =========================================================================
    # TRACK 06 · RCPL · FMCG B2B
    # =========================================================================
    {
        "slug": "rcpl",
        "name": "RCPL · FMCG B2B platform",
        "tagline": "Cross-brand FMCG · DMS · 1.3 Cr outlet ambition by 2028.",
        "track": "rcpl",
        "track_role": "track-headline",
        "status": "Build",
        "since": "2024-06-01",
        "verticals": ["grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/rcpl",
        "stake_inr_cr": 4500.0,
        "tags": ["b2b", "fmcg", "dms"],
        "narrative": """Cross-brand FMCG B2B distribution · DMS, supplier portal, DSR app, beat planning AI, B2B credit rails. Currently serves Campa and Independence with an 8-10 engineer pod. 30-dev sign-off (see /asks) unblocks the path to 1.3 Cr outlet ambition by 2028.""",
        "team": {
            "dri": ["Ashish Chandorkar · CPO"],
            "em": ["Abhishek Shinde"],
        },
    },

    # =========================================================================
    # TRACK 07 · RETAIL VISTA · Geospatial
    # =========================================================================
    {
        "slug": "retail-vista",
        "name": "Retail Vista",
        "tagline": "Geospatial intelligence · H3 hex · 22 data categories · 21,911 retail stores.",
        "track": "retail-vista",
        "track_role": "track-headline",
        "status": "Pilot",
        "since": "2025-11-19",
        "verticals": ["fashion", "grocery", "electronics"],
        "value_chain": ["plan", "move"],
        "ownership": "reliance",
        "web_anchor": "/retail-vista",
        "tags": ["geospatial", "h3", "google-cloud"],
        "narrative": """Reliance Retail's enterprise Geospatial Intelligence Platform built on H3 hexagonal spatial index. Integrates 22 data categories · UCP, POS, Telco, Government, 3rd-party POI · across 36 states, 10.5Cr buildings, 21,911 retail stores. Powers 3 priority use cases · Store Catchment (Huff Gravity), Dark Store Drive Time, New Store Planning.""",
        "metrics": [
            ("data_categories", "Data categories integrated", "22", "UCP · POS · Telco · Government · 3rd-party POI", "Vista platform", "live"),
            ("buildings_indexed", "Buildings indexed", "10.5 Cr", "Across 36 states", "Vista platform", "live"),
            ("stores_indexed", "Retail stores indexed", "21,911", "Reliance footprint", "Vista platform", "live"),
        ],
        "team": {
            "dri": ["Karan Muley"],
            "ril_counterpart": ["Sh. Biswaketan Kundu · RIL GIS"],
        },
    },

    # =========================================================================
    # TRACK 10 · RETAIL JARVIS · CX Sensing
    # =========================================================================
    {
        "slug": "retail-jarvis",
        "name": "Retail Jarvis",
        "tagline": "Real-time store intelligence · Sense → Analyze → Act → Verify loop.",
        "track": "retail-jarvis",
        "track_role": "track-headline",
        "status": "Build",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/retail-jarvis",
        "tags": ["cx", "sensing", "ai"],
        "narrative": """Real-time store intelligence platform fusing CCTV, wearable audio, POS, NPS, and inventory signals via a continuous Sense → Analyze → Act → Verify loop. Multi-sensor fusion · automated escalations · privacy-first & DPDP-compliant.""",
        "team": {"dri": ["Devam Gosalia · Saaket Chawali"]},
    },

    # =========================================================================
    # NPS Intelligence (Jarvis sub-IP)
    # =========================================================================
    {
        "slug": "nps-intelligence",
        "name": "NPS Intelligence Dashboard",
        "tagline": "3-layer NPS quality stack · live · 7-Eleven wedge.",
        "track": "retail-jarvis",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/retail-jarvis#nps-intelligence",
        "external_url": "https://nps.jioimpetus.com/",
        "narrative": """3-layer NPS quality stack · NPS Fraud Engine (anomaly-based manipulation detection, Streamlit), Silent NPS (inferred CSAT from behavioural signals), Anomaly Detection (real-time ops alerts). Layered into Retail Jarvis as a key signal source.""",
        "team": {"dri": ["Devam Gosalia · Saaket Chawali"]},
    },

    # =========================================================================
    # TRACK 09 · FORGE MES · Manufacturing
    # =========================================================================
    {
        "slug": "forge",
        "name": "Forge MES",
        "tagline": "AI-native Manufacturing Execution System · electronics + hardware factories.",
        "track": "forge",
        "track_role": "track-headline",
        "status": "Pilot",
        "since": "2025-09-01",
        "verticals": ["electronics"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/forge",
        "tags": ["manufacturing", "mes", "p2p"],
        "narrative": """Unified AI-native Manufacturing Execution System for electronics + hardware factories. Replaces fragmented ERP / MES / WMS silos. Modules · P2P, Warehousing, MES + Production, BOM/Version Control, People & Labour, Client Mgmt, AI Orchestration. Pilot at NeoLync Tirupati · pivoted 22 - Apr - 2026 from Bluebank STB to Luxshare IDU on MTK 6601 (Jio WiFi).""",
        "metrics": [
            ("plan_cycle_reduction", "Plan cycle time reduction", "90%", "vs traditional MES baseline at NeoLync pilot", "Forge pilot", "live"),
            ("throughput_increase", "Throughput increase", "5-10%", "Pilot baseline", "Forge pilot", "live"),
            ("stockout_reduction", "Stockout reduction · target", "50%", "Pilot target", "Forge pilot", "estimate"),
        ],
        "team": {
            "dri": ["Sameer Dev · Principal Engineer"],
            "mentors": ["Salman Saudagar"],
        },
        "releases": [
            ("2026-04-27", "FATP push · Luxshare IDU", "Final Assembly Test Pack push following pivot.", None),
            ("2026-04-22", "Pivot · Bluebank STB → Luxshare IDU on MTK 6601", "We slipped, then re-aimed. Bluebank STB demand softened. Pivoted to Luxshare IDU MTK 6601 (Jio WiFi). MES, BOM, production tooling carried over.", None),
        ],
    },

    # =========================================================================
    # TRACK 11 · AUTONOMOUS · Capability Layer
    # =========================================================================
    {
        "slug": "autonomous",
        "name": "Autonomous",
        "tagline": "Capability layer · 11 sub-IPs shipping AI-native autonomy into Reliance Retail.",
        "track": "autonomous",
        "track_role": "track-headline",
        "status": "Live",
        "verticals": ["fashion", "grocery", "electronics", "beauty"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous",
        "tags": ["capability-layer", "ai"],
        "narrative": """Eleven sub-tracks where Fynd is shipping AI-native autonomy into Reliance Retail customer-facing surfaces · design, photography, video, in-store immersion, conversational commerce, customer experience sensing.""",
        "metrics": [
            ("sub_tracks", "Sub-tracks", "11", "Total in Autonomous capability layer", "Autonomous canvas", "live"),
            ("live_production", "Live · production", "7", "Out of 11", "Autonomous canvas", "live"),
            ("pilot", "Pilot", "2", "Out of 11", "Autonomous canvas", "live"),
            ("in_development", "In development", "2", "Out of 11", "Autonomous canvas", "live"),
        ],
    },

    # ----- AI Photoshoot -----
    {
        "slug": "ai-photoshoot",
        "name": "AI Photoshoot",
        "tagline": "25K+ photoshoots shipped on Tira · 90% cost reduction · enterprise-grade platform.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2024-09-01",
        "verticals": ["beauty", "fashion"],
        "value_chain": ["buy-make", "sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#ai-photoshoot",
        "tags": ["ai", "photography", "catalog"],
        "narrative": """AI photo generation replacing physical shoots · model gen (ethnicity / age / size / gender) · annotation · catalog enrichment · cuts photoshoot cycle from weeks to hours.

25K+ photoshoots shipped on Tira via the Fynd Snap pipeline. 90% cost reduction vs physical photoshoots. Same pipeline that runs Tira is paid-customer-ready outside Reliance · proof of enterprise-grade platform.""",
        "metrics": [
            ("photoshoots_shipped", "Photoshoots shipped on Tira", "25K+", "Cumulative since live", "Fynd Snap ops", "live"),
            ("cost_reduction", "Cost reduction vs physical", "90%", "Tira baseline", "Fynd Snap economics", "live"),
            ("external_contract_inr_lakh", "Saudi German Hospitals contract", "₹30L", "Signed 14 - Apr - 2026", "Commerce Global", "audited"),
        ],
        "team": {
            "dri": ["Rajnandini Sharma"],
        },
        "external_validation": [
            "Saudi German Hospitals · ₹30L contract signed 14 - Apr - 2026",
            "Lulu · in test 09 - Jan - 2026",
        ],
    },

    # ----- AI Design -----
    {
        "slug": "ai-design",
        "name": "AI Design",
        "tagline": "Trend → moodboard → linesheet → tech-pack · same Claude Code skill as Trend-to-Design.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#ai-design",
        "tags": ["ai", "design", "claude-code"],
    },

    # ----- Fynd Studios -----
    {
        "slug": "fynd-studios",
        "name": "Fynd Studio",
        "tagline": "Gen-Media studio · 50+ AI ads · 4K films · cinematics.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2025-08-01",
        "last_release": "2026-04-25",
        "verticals": ["fashion", "beauty"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#fynd-studios",
        "stake_inr_cr": 100.0,
        "tags": ["gen-media", "video"],
        "narrative": """Built as a Claude Code skill on Remotion + Seedance 2.0 + Pixelbin. AI-generated 4K shorts, brand films, music videos, full storyboards · for Reliance brands and external global names.""",
        "metrics": [
            ("q1_target_inr_cr", "Q1 ambition", "₹10 Cr", "Locked 25 - Apr - 2026", "Farooq directive", "live"),
            ("fy_target_inr_cr", "FY ambition", "₹100 Cr", "Locked 25 - Apr - 2026", "Farooq directive", "live"),
            ("ai_ads_shipped", "AI ads shipped", "50+", "Cumulative", "Studio ops", "live"),
        ],
        "team": {
            "dri": ["Debajit Sardar"],
            "team": ["Rhea Bordoloi"],
        },
        "releases": [
            ("2026-04-28", "Lacoste / Aldo / Footlocker / Guess Malaysia · POC approved", "External global brand POCs greenlit", None),
            ("2026-04-25", "Fynd Studio Q1 ₹10 Cr · FY ₹100 Cr · targets locked", "By Farooq", None),
        ],
    },

    # ----- mTailor / MAGA -----
    {
        "slug": "mtailor",
        "name": "mTailor (MAGA)",
        "tagline": "Body-scan-driven made-to-measure for Reliance fashion portfolio.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Pilot",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#mtailor",
        "narrative": """Custom tailoring + size/fit visualisation. "Make Apparel Great Again". Body-scan-driven made-to-measure for the Reliance fashion portfolio.""",
        "team": {"dri": ["Yash Singh", "Shyam Dixit", "Salman Saudagar"]},
    },

    # ----- Fynd Horizon -----
    {
        "slug": "fynd-horizon",
        "name": "Fynd Horizon",
        "tagline": "Immersive in-store 3D body scan + virtual try-on · MDA + MM Sir unveil 14 - Apr - 2026.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "since": "2026-04-14",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#fynd-horizon",
        "stake_inr_cr": 1000.0,
        "tags": ["immersive", "3d", "body-scan"],
        "narrative": """In-store immersive experience · large interactive screen turns any physical store into a window onto endless digital inventory. 3D Body Measurement >98% accuracy via Intel RealSense, Gemini cloud rendering <2s, infinite aisle (2K → 50K+ SKUs).

Reliance Live. Fynd Public Q2 launch on Nexus Seawoods · 15 - Jul - 2026.""",
        "metrics": [
            ("body_measurement_accuracy", "3D body measurement accuracy", ">98%", "Intel RealSense pipeline", "Horizon test results", "tested"),
            ("cloud_render_latency_s", "Gemini cloud render latency", "<2 s", "Per body model", "Horizon production", "live"),
            ("skus_at_launch", "Initial SKU coverage", "2K", "Pilot launch", "Horizon catalog", "live"),
            ("skus_target", "Target SKU coverage", "50K+", "Full rollout", "Horizon catalog", "estimate"),
            ("reliance_mandate_inr_cr", "Reliance mandate · aspirational", "₹1,000 Cr", "Trigger conditions on /asks", "Apex review", "estimate"),
            ("fynd_public_book_inr_cr", "Fynd Public commercial book", "₹60 Cr", "External commercial book", "Fynd Public", "live"),
        ],
        "team": {
            "dri": ["Shyam Dixit · architecture"],
            "commercial": ["Yash Singh · Farhan Mirza"],
            "team": ["Salman Saudagar", "Gaurav", "Shubham Salunkhe", "Rajesh Bagul", "Sanket Pisat", "Rachit Shah"],
        },
        "releases": [
            ("2026-04-29", "Bodygram pivot to in-house pipeline · 27-29 Apr 2026", "In-house pipeline cutover begins to remove third-party licence dependency.", "Q2 FY27 cutover target"),
            ("2026-04-27", "AP Sir + Vineeth follow-up", "Detailed engagement after MDA unveil", None),
            ("2026-04-14", "MDA + MM Sir unveil at RCP", "Mirror failed evening before. Team rebuilt overnight at venue. MDA spent 30 minutes in detailed engagement.", "Q2 public launch on Nexus Seawoods 15 - Jul - 2026"),
        ],
    },

    # ----- NPS -----
    {
        "slug": "nps",
        "name": "NPS",
        "tagline": "3-layer NPS quality stack · live · 7-Eleven wedge.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#nps",
        "external_url": "https://nps.jioimpetus.com/",
        "team": {"dri": ["Devam Gosalia", "Saaket Chawali"]},
    },

    # ----- Silent NPS -----
    {
        "slug": "silent-nps",
        "name": "Silent NPS (SNPS)",
        "tagline": "Inferred customer satisfaction from behavioural signals · without explicit survey.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Build",
        "verticals": ["fashion", "grocery"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#silent-nps",
        "narrative": """Inferred customer satisfaction from behavioural signals · without explicit survey. Cross-channel signal fusion → CX score.""",
        "team": {"dri": ["Devam Gosalia"]},
    },

    # =========================================================================
    # TRACK 12 · HIREFIRST (ORION) · HR Tech
    # =========================================================================
    {
        "slug": "hirefirst",
        "name": "HireFirst (Orion)",
        "tagline": "Reliance HR Tech · hiring on rails · SAP OM RFC daily sync.",
        "track": "hirefirst",
        "track_role": "track-headline",
        "status": "Pilot",
        "since": "2026-04-07",
        "verticals": [],
        "value_chain": [],
        "ownership": "reliance",
        "web_anchor": "/hirefirst",
        "external_url": "https://hiring.ril.com",
        "tags": ["hr-tech", "ai-scoring", "sap-om"],
        "narrative": """Codename Orion. RIL-facing brand HireFirst at hiring.ril.com. Replaces a manual recruiter workflow with an AI-scored hiring pipeline that pulls from SAP OM in real time and pushes back vacancy-to-job creation in one click.

8 modules live on SIT · SAP OM RFC sync, AI score calibration, Email templates, Candidate Portal, Apollo.io Auto Enrich, Instant Interview, Candidate Blocklist, GCP infra. 6 modules in development · Ideal Candidate Profile, Interview Chatbot, AI-prompt autofill, native SAP OM, LinkedIn Chrome extension, hirefirst/careersfirst domain split.""",
        "metrics": [
            ("modules_live_sit", "Modules Live on SIT", "8", "Per release timeline", "Orion-squad", "live"),
            ("modules_in_dev", "Modules in development", "6", "Per Slack todos", "Orion-squad", "live"),
            ("apollo_db_size", "Apollo.io contact database", "275M+", "Auto-enrich corpus", "Apollo.io", "live"),
        ],
        "team": {
            "dri": ["Pritam Jamsandekar"],
            "principal_engineer": ["Sameer Dev"],
            "engineering": ["Paul Lobo", "Manish"],
            "devops": ["Vijay", "Amboj Goyal"],
            "mentors": ["Jigarkumar Dafda · CTPO"],
            "ril_counterpart": ["Naren · Bond team · RIL HR Tech", "Mythili · Hypercare lead for New Energy"],
        },
        "releases": [
            ("2026-04-09", "Weekly Farooq update · BRD execution + team expansion", "Two devs + Paul Lobo added internally. Major SIT updates · AI Score Calibration, Email Templates, Candidate Portal, SAP OM Integration.", None),
            ("2026-04-07", "SIT deploy · 3 majors", "Negative Feedback Loop AI Score Calibration · Customisable Email Templates · SAP OM RFC daily sync.", None),
            ("2026-04-03", "Candidate Blocklist · GCP infra production-ready", "Block list at platform scope. GCP project, billing, network with IDC, Cloud Run, Bastion, Postgres, Artifact Registry.", None),
            ("2026-04-02", "Apollo.io Auto Enrich · Instant Interview Quick Job · RIL portal branding to HireFirst", "Three production releases", None),
            ("2026-04-01", "Daily todos · GCP setup, RFC integration, Apollo, branding, IRM approval, domain split", None, None),
        ],
        "links": {
            "production_urls": [
                ("https://hiring.ril.com", "RIL HireFirst Production · sign-off pending"),
            ],
            "sit_urls": [
                ("https://ril.sit.fyndx1.de", "SIT environment"),
                ("https://hiring-ril.sit.fyndx1.de", "Hiring SIT"),
            ],
        },
    },

    # =========================================================================
    # ADJACENT IPS · referenced across the register
    # =========================================================================
    {
        "slug": "fynd-quick",
        "name": "Fynd Quick · Q-commerce OS",
        "tagline": "700+ orders/min · 90% on-time · sub-30-min from dark stores.",
        "track": "granary",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["grocery"],
        "value_chain": ["move", "sell"],
        "ownership": "reliance",
        "web_anchor": "/granary#fynd-quick",
        "metrics": [
            ("orders_per_min", "Orders per minute", "700+", "Sustained peak", "Quick ops", "live"),
            ("on_time_rate", "On-time rate", "90%", "Sub-30-min delivery target", "Quick ops", "live"),
        ],
    },

    {
        "slug": "fynd-snap",
        "name": "Fynd Snap",
        "tagline": "AI photoshoot pipeline · 25K+ shoots · 90% cost saving.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["beauty", "fashion"],
        "value_chain": ["buy-make"],
        "ownership": "reliance",
        "web_anchor": "/autonomous#ai-photoshoot",
        "team": {"dri": ["Rajnandini Sharma"]},
    },

    {
        "slug": "pixelbin",
        "name": "PixelBin",
        "tagline": "DAM + transformations · cross-team · 5K+ images for Tira alone.",
        "track": "autonomous",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["fashion", "beauty"],
        "value_chain": ["buy-make", "sell"],
        "ownership": "fynd",
        "web_anchor": "/jcp#pixelbin",
    },

    {
        "slug": "boltic",
        "name": "Boltic",
        "tagline": "Workflow automation · vibe-to-production · Clickstream SDK.",
        "track": "jcp",
        "track_role": "sub-ip",
        "status": "Live",
        "ownership": "fynd",
        "web_anchor": "/jcp#boltic",
        "external_url": "https://www.boltic.io",
    },

    {
        "slug": "ratl-ai",
        "name": "ratl.ai",
        "tagline": "AI-first testing · 1,300 test cases on AJIO × JCP.",
        "track": "jcp",
        "track_role": "sub-ip",
        "status": "Live",
        "ownership": "fynd",
        "web_anchor": "/jcp#ratl",
        "team": {"dri": ["Nagabhushan C R · Head of Reliability"]},
    },

    {
        "slug": "fynd-kio",
        "name": "Fynd Kio",
        "tagline": "Self-checkout kiosk · 168 units locked for Fashion Factory · ~₹18 Cr FY26-27.",
        "track": "samarth",
        "track_role": "sub-ip",
        "status": "Pilot",
        "since": "2025-12-01",
        "verticals": ["fashion"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/samarth#fynd-kio",
        "stake_inr_cr": 18.0,
        "tags": ["self-checkout", "hardware"],
        "narrative": """Self-checkout kiosk · 3-step Scan → Pay → Go flow. 21.5" Full HD touchscreen, modular for clothing/footwear/beauty/grocery. 3X faster checkout vs traditional POS. ~₹18 Cr Fashion Factory hardware line FY26-27.""",
        "team": {
            "dri": ["Salman Saudagar"],
            "finance": ["Naveen"],
        },
    },

    {
        "slug": "glamar",
        "name": "GlamAR",
        "tagline": "VTO · 3D · AR · VR · Sephora · Vision Express · LensCrafters · WestElm.",
        "track": "rbl",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["beauty", "fashion"],
        "value_chain": ["sell"],
        "ownership": "fynd",
        "web_anchor": "/jcp#glamar",
        "metrics": [
            ("returns_reduction", "Returns reduction", "−40%", "Across deployed brands", "GlamAR product analytics", "live"),
            ("revenue_per_visit_lift", "Revenue per visit lift", "+106%", "GlamAR sessions vs control", "GlamAR analytics", "live"),
            ("engagement_lift", "Engagement lift", "+90%", "GlamAR sessions", "GlamAR analytics", "live"),
        ],
    },

    {
        "slug": "swap-easy",
        "name": "SwapEasy",
        "tagline": "Reliance Digital trade-in · 625 stores live · ₹1.5 Cr Month-1 · ~₹14K AOV.",
        "track": "jcp",
        "track_role": "sub-ip",
        "status": "Live",
        "verticals": ["electronics"],
        "value_chain": ["sell"],
        "ownership": "reliance",
        "web_anchor": "/jcp#swap-easy",
        "metrics": [
            ("stores_live", "Stores live", "625", "Reliance Digital footprint", "RD ops", "live"),
            ("month_1_revenue_inr_cr", "Month-1 revenue", "₹1.5 Cr", "Live launch month", "RD finance", "audited"),
            ("aov_inr", "AOV", "~₹14,000", "Per swap transaction", "SwapEasy ops", "live"),
        ],
    },
]
