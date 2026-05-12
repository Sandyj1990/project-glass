# MDA-deep audit · 30 - Apr - 2026

Auditor · Salman Saudagar (with Claude Opus 4.7 · 1M context)
Method · read every page; ran full-corpus grep for em-dashes, AI-slop, "Fynd Platform", date-format violations, stale versions, broken anchors, DRI conflicts, eleven-vs-twelve count drift.

---

## P0 (must-fix before MDA review)

1. [index.html:842] Footer hero badge says `v0.6.4` but nav badge says `v0.6.6` and author block says `0.6.6`. Bump to `v0.6.7` and align with author block.
2. [index.html:840] Footer "Last verified · 29 - Apr - 2026" while author block says "Date: 30 - Apr - 2026". Bump to 30 - Apr - 2026.
3. [index.html:662] Stale comment `<!-- 11 TRACKS -->` on a section with twelve cards. Update to `<!-- 12 TRACKS -->`.
4. [index.html:801] "Cross-cutting capability layer Fynd has shipped on top of the **eleven** tracks." Should be "twelve tracks" (HireFirst is Track 12).
5. [index.html:807] "Frontier Pool · 2-3 pager due **May 4**." Not DD-MMM-YYYY. Use `04 - May - 2026`.
6. [index.html:790] "Locked by Farooq · **Apr 25**" not DD-MMM-YYYY. Use `25 - Apr - 2026`.
7. [index.html:809] "Claude Cowork session **Apr 7**" not DD-MMM-YYYY. Use `07 - Apr - 2026`.
8. [index.html:765] "POC approved by country head **Apr 28**" not DD-MMM-YYYY. Use `28 - Apr - 2026`.
9. [index.html:684] "Command Centre Beta live **Apr 15** · Yousta PLM live · 62K styles · 39.9% GM. Lead: Kushan Shah." Not DD-MMM-YYYY. Use `15 - Apr - 2026`. Also Kushan is now CTPO, not "Lead" only · keep "Lead" since it's a track lead label.
10. [index.html:696] "Cortex live **Nov 13**" not DD-MMM-YYYY. Use `13 - Nov - 2025`.
11. [index.html:700] Pill says "Live · **Apr 29**" not DD-MMM-YYYY. Use `Live · 29 - Apr - 2026` (or just `Live`).
12. [index.html:352] "Bluebank STB → Luxshare IDU MTK 6601 (Jio WiFi) **Apr 22** pivot · FATP push **Apr 27**" not DD-MMM-YYYY.
13. [index.html:389] "Saudi German Hospitals signed **Apr 14** · Lulu **Jan 9** · cross-brand" not DD-MMM-YYYY.
14. [index.html:432] "GlamAR 3D AR ad banner Westelm **Mar 30**" not DD-MMM-YYYY.
15. [index.html:426] "JCP migrated **Mar 2024**" — this is a year-month, leave as is (long-form is acceptable for whole-month pointers, no specific day available). Marked acceptable.
16. [index.html:224] HTML comment "MATRIX · Software IP × Value Chain × Retail Type · per Farooq **Apr 25** directive" — comment-only, but bring to standard for consistency: `25 - Apr - 2026`.
17. [organisation/index.html:19] Section label "Organisation · who runs the **eleven** tracks." → "twelve tracks".
18. [organisation/index.html:79] "02 · **Eleven** tracks · who runs each one" → "Twelve tracks".
19. [organisation/index.html:80] Same section H2 still implies eleven; table at 86-96 has 11 rows · MUST add Track 12 row for HireFirst (DRI Pritam Jamsandekar).
20. [organisation/index.html:215] Footer span `v0.6.4` and date `29 - Apr - 2026`. Bump to `v0.6.7` and `30 - Apr - 2026`.
21. [autonomous/index.html:22] "**Eleven** sub-tracks where Fynd is shipping AI-native autonomy". Autonomous track is Track 03 with sub-IPs (different from the 12-track count) · keep "Eleven" if Autonomous truly has 11 sub-IPs but cross-check the H2 too.
22. [autonomous/index.html:63] "**Eleven** IPs in the Autonomous layer." Same · this is a sub-IP count, not the org-wide track count. Cross-check sub-IPs section to confirm count is 11; if so, leave. NOTE: this is internal to the Autonomous track and disambiguated, leave as-is.
23. [autonomous/index.html:303] Footer `v0.6.4` and date `29 - Apr - 2026`. Bump.
24. [hirefirst/index.html:237] Footer span `v0.6.5`. Bump to `v0.6.7`.
25. [culture/index.html:239] Footer span `v0.6.4` and date `29 - Apr - 2026`. Bump.
26. [jcp/index.html:319-355] Anchor links to `#oms`, `#wms`, `#tms`, `#endless-aisle`, `#engage-loyalty`, `#mdh`, `#catalog-cloud`, `#ai-pim`, `#pixelbin`, `#boltic`, `#pricing-markdowns`, `#vista` — none of these IDs exist on /jcp page. Fix · either add IDs to corresponding sections, or convert hrefs to plain text, or point at #sub-ips. **Fix · add IDs to the matching detail sections; if a section doesn't exist for that anchor target, point to #sub-ips fallback.**
27. [index.html:66, :71, :81] Home links `/jcp#channels` and `/jcp#scale` don't exist on JCP page (only `#ucp` exists). Fix · add `id="channels"` to the channels section and `id="scale"` to the scale section on /jcp.
28. [Footer "Other tracks" lists across alp, autonomous, forge, granary, impetus, jcp, rbl, rcpl, retail-jarvis, retail-vista, samarth, catalog] · all are missing /hirefirst (Track 12) and most are missing /autonomous and /retail-jarvis. **Fix · add /hirefirst to every footer's "Other tracks" list; ensure all footers list 11 sibling tracks consistently.**
29. [All footers across track pages] · Date `29 - Apr - 2026` and `v0.6.4` (or v0.6.5 on hirefirst). Bump all to `30 - Apr - 2026` and `v0.6.7`.
30. [Author blocks across alp, autonomous, catalog, culture, forge, granary, impetus, jcp, organisation, rbl, rcpl, retail-jarvis, retail-vista, samarth] · all show `Date: 29 - Apr - 2026` and `Version: 0.6.6`. Bump to `30 - Apr - 2026` and `0.6.7`.
31. [Nav `v0.6.6` badge across all 18 pages] · Bump to `v0.6.7`.

---

## P1 (should-fix)

1. [catalog/index.html:357] Footer "Tracks" list missing /autonomous, /retail-jarvis, /hirefirst. Add them.
2. [hirefirst/index.html:20] Author block date 30 - Apr - 2026 but Version 0.6.6 · footer says v0.6.5 · misaligned. Bump to v0.6.7 throughout.
3. [organisation/index.html:208] Source line: "Founder timeline · Farooq Adam (01 - May - 2013) · Sreeraman Mohan Girija (01 - Apr - 2013)." Conflicts: line 28 says `Farooq + Sreeraman · since 01 - May - 2013` (single date for both), but lines 41-42 give `01 - May - 2013` for Farooq and `01 - Apr - 2013` for Sreeraman. Reconcile · use 01 - Apr - 2013 (earlier) on stat tile to be conservative, or keep "since 01 - May - 2013" but qualify "co-founder duo Mar–May 2013".
4. [jcp/index.html:660] "UCP releases · #general · Apr 1, 2, 3, 21 (Amogh Dubey)" not DD-MMM-YYYY. Reformat: `01 · 02 · 03 · 21 - Apr - 2026`.
5. [jcp/index.html:661] "JIIA on Google Cloud Next '26 · Apr 29 keynote" → `29 - Apr - 2026`.
6. [jcp/index.html:659] "AJIO × JCP Status Report · Apr 3" → `03 - Apr - 2026`.
7. [jcp/index.html:128, :129, :134, :138, :144, :146, :147, :148, :149] Brand storefront tables list "Storefront · website **Mar 30**" / "**Mar 11**" / "**Mar 25 target**" / "**Apr 15**" / "**Mar 18**" — date format violations across the JCP brand table.
8. [jcp/index.html:629] "RRVL Apex committed **Mar 31** deadline" → `31 - Mar - 2026`.
9. [jcp/index.html:632-634] "**Apr 2** · cleared / **Apr 8** · cleared / **Mar 31** · met" → DD - MMM - YYYY.
10. [granary/index.html:184-187] Timeline cards use short dates: `Apr 27`, `Apr 29`, `Jan 28`, `Jan 14`. Reformat to DD - MMM - YYYY.
11. [granary/index.html:176] "Karan Muley · **Apr 29**" → `29 - Apr - 2026`.
12. [impetus/index.html:37] "Last Apex" card: "**Feb 11** · MDA chain" → `11 - Feb - 2026`.
13. [impetus/index.html:205-208] Timeline card spans use `Apr 16`, `Apr 17`, `Mar 18`, `Feb 11` · reformat.
14. [rcpl/index.html:215-218] Cards: "**Apr 20** · weekly manual cycle / Completed **Apr 24** / **Apr 22-23** / Picked up **Apr 9**" · reformat to DD - MMM - YYYY.
15. [rcpl/index.html:224] "Competitive landscape · **Apr 7**" → `07 - Apr - 2026`.
16. [rcpl/index.html:266-267] Timeline `Jan 29`, `Mar 10` · reformat.
17. [rcpl/index.html:299-301] Slack source lines `Jan 29`, `Mar 10`, `Nov 27` · reformat to DD - MMM - YYYY.
18. [rcpl/index.html:226] "Farooq's directive **Apr 7**" → `07 - Apr - 2026`.
19. [rbl/index.html:64-65, :68, :69] Table cells with `Mar 12`, `Apr 15`, `Mar 11`, `Mar 25`. Reformat.
20. [retail-jarvis/index.html:271] Slack `Jan 2 (Salman)` → `02 - Jan - 2026`.
21. [forge/index.html:62] "Seamless assembly" — banned word. Replace with "End-to-end assembly" or "Continuous assembly".
22. [culture/index.html: multiple] · references "leverage" and "across the value chain" / "comprehensive" / "holistic" — these are intentional inside a section that explicitly mentions banning them; the prose shows them in quotes as banned phrases. Verify they remain in quoted context, not in marketing copy.
23. [/asks · /gaps] Cross-link "see related" · /asks should top-link to /gaps and vice versa (already partially done in the body of /gaps via inline links and risk cards, but not as a top "see related" line as instructed).
24. [autonomous/index.html] · author date is 29 - Apr - 2026 but the page now serves as backbone for a track in the Twelve. Bump date.

---

## P2 (nice-to-have)

1. [index.html:202] "Fynd Public Q2 (Nexus Seawoods 15 - Jul - 2026)" — line 121 in /asks says same. Consistent. OK.
2. [forge/index.html:62] Already addressed in P1 #21.
3. Catalog filter UI — manual eyeball needed; functional check via grep shows `data-vertical` and `data-status` attributes present (catalog/index.html:131, :236). Implementation looks intact.
4. [organisation/index.html:215] No author/date author-block at the top says `Date: 29 - Apr - 2026 · Version: 0.6.6` — same fix as P0 row 30.
5. [granary/index.html:34] "Platform leads · Aushin Ganguli · Advait Pandit" but home (index.html:696) says "Lead: Aushin Ganguli" only. Granary track DRI (org page row 3): "Aushin Ganguli · Advait Pandit". Reconcile · home should say "Lead: Aushin Ganguli · Advait Pandit" or accept the short form on home. **Keep short form on home, no fix needed.**
6. [autonomous/index.html:22, :63] `Eleven IPs` in Autonomous layer · cross-check sub-IPs section count to ensure it really is 11. (Inspection: id list shows 11 anchors · ai-design, ai-photoshoot, ai-search, conversational-studio, cs-agent, fynd-horizon, fynd-studios, mtailor, nps, silent-nps, smart-restaurant. Confirmed 11. Acceptable.)

---

## DRI conflicts found · zero

Cross-checked Aushin Ganguli (Granary), Mayank Jain (Granary cards), Nishant Amin (Samarth), Karan Muley (ALP + Vista), Ashish Chandorkar (RCPL + JCP Channels), Pritam Ghosh (RBL), Pritam Jamsandekar (HireFirst). No conflicts. Org chart and individual track pages line up.

---

## Audit grep results

- em-dashes (—): **0 found** in any HTML file. Clean.
- "across the value chain": **0 in marketing copy.** Only mentioned in `/culture/index.html:117, :213` as a banned-phrase reference within quotation marks — intentional, leave.
- "comprehensive": **0 in marketing copy.** Only mentioned in `/culture/index.html:117, :213` as a banned-phrase reference within quotes.
- "holistic": **0 in marketing copy.** Only mentioned in `/culture/index.html:213` in quotes.
- "robust": **0 found.** Clean.
- "leverage": appears in `/culture/index.html:85, :117, :166, :213, :217` · uses in `:85` ("Operators get more leverage") and `:217` ("Leverage is the metric") are positive-frame uses of the word but still risk MDA flagging it. **Recommendation: replace `:85` "Operators get more leverage" → "Operators get more output per head"; `:217` "Leverage is the metric" → "Output per head is the metric". Other occurrences inside quoted "banned-phrase" contexts at `:117`, `:166`, `:213` — keep in quotes.**
- "imagine" / "picture" / "walk you through" / "it's worth noting" / "deep dive": **0 found.** Clean.
- "not just X but Y": **1 found** at `/culture/index.html:85` ("Not 'replace the team.'") · this is in quoted negation pattern, contextually OK · leave.
- "seamless": **1 found** at `/forge/index.html:62` "Seamless assembly". Replace.
- "streamlined": **0 found.** Clean.
- "Fynd Platform": **0 found.** Clean. Site uses "Jio Commerce Platform (JCP)" everywhere.
- Em-dash check (`—` Unicode): **0 found.**

---

## Page-level inconsistencies summary

- **Author blocks:** 14 of 18 pages have `Date: 29 - Apr - 2026 · Version: 0.6.6`; 4 have `Date: 30 - Apr - 2026 · Version: 0.6.6` (home, asks, gaps, hirefirst). Goal v0.6.7: all 18 pages → `Date: 30 - Apr - 2026 · Version: 0.6.7`.
- **Footers (mono span):** 15 of 18 pages have `v0.6.4`; 1 has `v0.6.5` (hirefirst); 2 have `v0.6.6` (asks, gaps). Goal: all 18 → `v0.6.7`.
- **Footer "Last verified" dates:** 13 of 18 say `29 - Apr - 2026`. Goal: all → `30 - Apr - 2026`.
- **Nav badge `v0.6.6`:** All 18 pages. Goal: all → `v0.6.7`.

---

## Things MDA would specifically ask · status

- "How many tracks?" → **Twelve.** Home, /catalog, /organisation must all say twelve consistently. Currently /organisation, /index.html line 801, autonomous (sub-IP page) carry "eleven" residue.
- "Who owns Track 12 (HireFirst)?" → Pritam Jamsandekar (HR Tech). Must be added to /organisation track-owner table.
- "When does Frontier Pool decision land?" → 04 - May - 2026 (5 days). Must be DD-MMM-YYYY in every reference (not "May 4").
- "What does Fynd Studio earn?" → Q1 ₹10 Cr · FY ₹100 Cr. Confirmed and consistent across home, /autonomous, /asks.
- "What's not done?" → /gaps exists, lists 5 slipped commitments + 8 maturity gaps + 4 vacant DRIs + 6 risks. Adequate.

---

## Final state · post-fix verification (after v0.6.7)

Run after all P0/P1 fixes applied.

- em-dashes (`—`): **0 matches** across all 18 HTML files.
- "across the value chain": **0** in marketing copy (only inside quoted banned-phrase reference on /culture).
- "comprehensive": **0** in marketing copy (only inside quoted banned-phrase reference on /culture).
- "holistic": **0** in marketing copy (only inside quoted banned-phrase reference on /culture).
- "robust" / "streamlined" / "deep dive" / "imagine" / "picture" / "walk you through" / "it's worth noting": **0 matches.**
- "seamless": **0 matches** (was 1 in /forge, replaced with "End-to-end").
- "Fynd Platform": **0 matches.** Site uses "Jio Commerce Platform (JCP)" exclusively.
- "leverage" outside of quoted-banned context: **0 matches** (replaced two on /culture).
- Stale versions (`v0.6.0`-`v0.6.6`): **0 matches.** All 18 pages → `v0.6.7` in nav badge and footer.
- "Eleven tracks" / "eleven tracks" in track-count context: **0 matches.** /index.html, /organisation, /catalog all read "twelve tracks".
- "/hirefirst" present in every track-page footer "Other tracks" list: **18 of 18 pages.**
- "Last verified 29 - Apr - 2026" in section labels: **0 matches** (bumped to 30 - Apr - 2026 where applicable).
- Author block `Date: 30 - Apr - 2026 · Version: 0.6.7`: **18 of 18 pages.**
- Footer mono-span `v0.6.7`: **18 of 18 pages.**
- Auth.js src tag `<script src="/auth.js">`: **18 of 18 pages.**
- Cross-link /asks ↔ /gaps: **added** as "See related" line on both pages, top of section.

Page-specific:
- /jcp · added `id="channels"` and `id="scale"` anchors so home stats links resolve. Re-pointed 11 broken `#oms`, `#wms`, `#tms`, `#endless-aisle`, `#engage-loyalty`, `#mdh`, `#catalog-cloud`, `#ai-pim`, `#pixelbin`, `#boltic`, `#pricing-markdowns` hrefs to `#sub-ips`. Re-pointed `#vista` to `/retail-vista`.
- /organisation · added Track 12 (HireFirst, DRI Pritam Jamsandekar) row to track-owner table.
- /forge · replaced "Seamless assembly" → "End-to-end assembly".
- /culture · replaced two non-quoted "leverage" uses with "output per head".
- /jcp · brand storefront table dates Mar 11/12/18/25/30 and Apr 15 reformatted to DD - MMM - YYYY.
- /granary · timeline cards Apr 27, Apr 29, Jan 28, Jan 14 reformatted.
- /rcpl · timeline + competitive-landscape cards reformatted (Apr 7, Apr 9, Apr 20, Apr 22-23, Apr 24, Jan 29, Mar 10, Nov 27).
- /impetus · timeline cards Apr 16/17, Mar 18, Feb 11 reformatted.
- /rbl · brand table cells with Mar 11/12/25 and Apr 15 reformatted.
- /retail-jarvis · Slack Jan 2 reformatted.

