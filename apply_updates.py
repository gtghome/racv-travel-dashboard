#!/usr/bin/env python3
"""Apply all 4 Monday Update section replacements to index.html"""

import re

def replace_section(content, start_marker, end_marker, new_section):
    """Replace content between start_marker and end_marker (inclusive)"""
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"ERROR: start_marker not found: {start_marker[:60]}")
        return content
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        print(f"ERROR: end_marker not found: {end_marker[:60]}")
        return content
    end_idx += len(end_marker)
    print(f"  Found section from char {start_idx} to {end_idx}")
    return content[:start_idx] + new_section + content[end_idx:]

with open('/home/user/workspace/racv-dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file: {len(content)} chars")

# ============================================================
# SECTION 1: page-r-update
# ============================================================
print("\n[1] Replacing page-r-update...")

r_update_new = '''<section class="page" id="page-r-update">
  <div class="page-header">
    <h1>Resorts Monday Update</h1>
    <p>Current edition: Issue 5 &middot; 13 April 2026 &middot; Editor: GTG Travel Intelligence Team</p>
  </div>

  <!-- Edition header card -->
  <div class="card section-gap" style="background:linear-gradient(135deg, var(--color-primary-highlight) 0%, var(--color-surface) 100%); border-color: var(--color-primary);">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:var(--space-3)">
      <div>
        <div style="font-size:var(--text-xs);font-weight:700;color:var(--color-primary);text-transform:uppercase;letter-spacing:0.08em">Issue 5 &middot; 13 April 2026</div>
        <div style="font-size:var(--text-lg);font-weight:700;color:var(--color-text);margin-top:var(--space-1)">Resorts: Fuel Stabilising, Easter Mixed &amp; Pricing Power Rising</div>
        <div style="font-size:var(--text-xs);color:var(--color-text-muted);margin-top:4px">7&#8211;12 Apr 2026 &middot; 4 stories &middot; Updated weekly</div>
      </div>
      <div style="display:flex;gap:var(--space-2)">
        <span class="tag red">Fuel Crisis</span>
        <span class="tag amber">Easter Mixed</span>
        <span class="tag green">Free Transport</span>
        <span class="tag green">Pricing Power</span>
      </div>
    </div>
  </div>

  <!-- 4 update stories -->
  <div class="grid-2 section-gap">

    <div class="card">
      <div class="card-header">
        <span class="card-title">Story 1 &#8212; Fuel Crisis: Stabilising But No Relief Yet</span>
        <span class="card-badge red">Ongoing</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.abc.net.au/news/2026-04-10/fuel-prices-australia-excise-cut/" target="_blank">ABC News</a>, <a href="https://www.globalpetrolprices.com/Australia/" target="_blank">GlobalPetrolPrices</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#9981;</span>
        <span class="insight-text"><strong>Current prices:</strong> Petrol at $2.25/L (post-excise cut, down from $2.58 high). Diesel at $3.08/L and still rising. 312+ stations ran dry this week, mostly rural VIC. No significant price relief expected until mid-May at earliest.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128202;</span>
        <span class="insight-text"><strong>Resort portfolio pressure:</strong> Regional properties dependent on long drive distances remain under cost pressure. Cobram and Healesville are most exposed as fuel cost remains a booking deterrent for budget-conscious families.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#127919;</span>
        <span class="insight-text"><strong>Recommended action:</strong> Maintain fuel-conscious messaging for Cobram and Healesville &#8212; bundle fuel rebates or complimentary EV charging credits into packages. Activate proximity-based marketing for properties within the 90-minute corridor.</span>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Resorts Marketing Lead</span>
        <span>Deadline: 16 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Story 2 &#8212; Easter 2026 Results: Proximity Wins Again</span>
        <span class="card-badge amber">Mixed</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.abc.net.au/news/2026-04-09/victoria-easter-tourism-results/" target="_blank">ABC News</a>, <a href="https://7news.com.au/news/vic" target="_blank">7NEWS Melbourne</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#127958;</span>
        <span class="insight-text"><strong>Mornington Peninsula:</strong> Results described as &ldquo;pretty solid&rdquo; though spending patterns remain uncertain. Remote VIC destinations (e.g. Dargo) reported occupancy down 20%. 7NEWS VIC confirmed strong visitor numbers but operators worried about the next 3 months.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128205;</span>
        <span class="insight-text"><strong>Portfolio read-out:</strong> Cape Schanck and Torquay, both within the 90-minute drive corridor, likely outperformed the portfolio. Properties further afield faced headwinds from high fuel costs. Proximity to Melbourne was the decisive performance factor.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128161;</span>
        <span class="insight-text"><strong>Forward signal:</strong> Operator confidence for May&#8211;Jun is fragile. Recommend proactive May school holiday packages targeting 90-minute corridor properties &#8212; urgency messaging before bookings fall away.</span>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Resorts Revenue Team</span>
        <span>Deadline: 17 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Story 3 &#8212; VIC Free Transport: Resort Opportunity Window</span>
        <span class="card-badge green">Opportunity</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://thetraveler.org/victoria-free-public-transport-april-2026/" target="_blank">The Traveler</a>, <a href="https://www.ptv.vic.gov.au/tickets/free-travel/" target="_blank">VIC Govt / PTV</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128646;</span>
        <span class="insight-text"><strong>All VIC public transport free through April 2026</strong> &#8212; trains, trams, buses &#8212; as a crisis response to fuel prices. Additionally: under-18s free travel permanent from Jan 2026; seniors free weekends ongoing. V/Line to Geelong, Ballarat and Bendigo is free.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#127919;</span>
        <span class="insight-text"><strong>&ldquo;Train &amp; Stay&rdquo; packaging window:</strong> V/Line connects to resort-corridor feeder towns. Healesville (Lilydale line) and Goldfields properties (Ballarat/Bendigo trains) can be reached car-free. Package &ldquo;take the free train, stay the weekend&rdquo; to fuel-fatigued Melbourne members.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128176;</span>
        <span class="insight-text"><strong>Campaign economics:</strong> Member saves $40&#8211;80 on fuel costs. Resort fills rooms with no discount required. Brief the marketing team to launch this package by 16 April before the free-transport window closes end of month.</span>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Resorts Marketing + Revenue</span>
        <span>Deadline: 16 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Story 4 &#8212; Hotel Market: RACV Resorts Pricing Power</span>
        <span class="card-badge green">Strong</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.cbre.com.au/research-and-reports/australia-hotel-market-outlook-2025" target="_blank">CBRE Hotel Outlook</a>, <a href="https://www.revpargenius.com/blog/australia-hotel-revpar-2025/" target="_blank">RevPARGenius</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#127976;</span>
        <span class="insight-text"><strong>Record AU hotel market:</strong> Australian hotel transactions hit AUD $2.7B in 2025 (record, +80% YoY). RevPAR grew 8%+ nationally; Melbourne specifically up +18.2%. Only 7,300 rooms under construction nationally &#8212; structural supply constraint.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128201;</span>
        <span class="insight-text"><strong>Supply pipeline stark:</strong> Future new supply is 41% below historic averages and 35% below demand growth pace. Construction cost inflation is structurally preventing new rooms coming to market. This is not a short-term dynamic.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128185;</span>
        <span class="insight-text"><strong>RACV Resorts positioned to lift ADR:</strong> With supply constrained and demand solid, this is the strongest pricing environment in a decade. Revenue team should review ADR floor prices across all properties for May&#8211;Sep 2026 and stress-test upward scenarios.</span>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Resorts Revenue Director</span>
        <span>Deadline: 18 Apr 2026</span>
      </div>
    </div>

  </div>

  <!-- Monday Priority Actions -->
  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">Monday Priority Actions &#8212; RACV Resorts</span>
      <span class="card-badge gold">7&#8211;12 Apr 2026</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Priority</th><th>Action</th><th>Channel</th><th>Owner</th><th>Deadline</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Launch &ldquo;Train &amp; Stay&rdquo; package for Healesville and Goldfields &#8212; free V/Line window closes end of April</td>
            <td>Email / Website</td>
            <td>Resorts Marketing</td>
            <td>16 Apr</td>
            <td><span class="tag amber">Brief Needed</span></td>
          </tr>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Review ADR floor pricing across portfolio &#8212; market supports uplift given 41% below-trend supply</td>
            <td>Revenue System</td>
            <td>Revenue Director</td>
            <td>18 Apr</td>
            <td><span class="tag amber">In Review</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Activate fuel-rebate or EV credit bundle for Cobram and Healesville May&#8211;Jun packages</td>
            <td>Email + App</td>
            <td>Resorts Marketing</td>
            <td>16 Apr</td>
            <td><span class="tag amber">Draft Ready</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Brief May school holiday urgency campaign for 90-minute corridor properties (Cape Schanck, Torquay)</td>
            <td>CRM Email</td>
            <td>Resorts Marketing</td>
            <td>17 Apr</td>
            <td><span class="tag amber">Pending</span></td>
          </tr>
          <tr>
            <td><span class="tag blue">P3</span></td>
            <td style="font-size:11px;">Monitor diesel price impact on Cobram forward bookings &#8212; alert if May&#8211;Jun tracking &gt;10% below budget</td>
            <td>Ops Dashboard</td>
            <td>GM Resorts</td>
            <td>Ongoing</td>
            <td><span class="tag blue">Monitoring</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</section>'''

content = replace_section(
    content,
    '<section class="page" id="page-r-update">',
    '</section>\n<section class="page" id="page-c-brand">',
    r_update_new + '\n<section class="page" id="page-c-brand">'
)

# ============================================================
# SECTION 2: page-c-update
# ============================================================
print("\n[2] Replacing page-c-update...")

c_update_new = '''<section class="page" id="page-c-update">

  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">RACV Club &#8212; Monday Intelligence Update</span>
      <span class="card-badge gold">7&#8211;12 Apr 2026</span>
    </div>
    <p class="insight-text" style="margin-bottom:0;">Priority intelligence for RACV Club operations, sales and marketing. Covers fuel savings milestones, Total Care policy changes, dining demand signals and cost-of-living context from the past 72 hours.</p>
  </div>

  <!-- Priority Updates -->
  <div class="grid-2 section-gap">

    <div class="card">
      <div class="card-header">
        <span class="card-title">Fuel Crisis Membership Value</span>
        <span class="card-badge green">Peak Relevance</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.racv.com.au/membership/member-benefits/fuel-savings.html" target="_blank">RACV Membership Benefits</a>, <a href="https://www.abc.net.au/news/2026-04-10/fuel-prices-australia-excise-cut/" target="_blank">ABC News</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#9981;</span>
        <div class="insight-text"><strong>$3.8M saved since Sep 2025:</strong> RACV fuel discount at EG Ampol has now saved 318,000 members $3.8M in total &#8212; up from $1.8M at the last milestone. With petrol at $2.25/L and diesel at $3.08/L, this is RACV&rsquo;s strongest-ever member value proof point.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128227;</span>
        <div class="insight-text"><strong>Deploy in all Club member comms immediately:</strong> During the fuel crisis, the fuel discount benefit is the single most resonant message RACV can send. Feature prominently in renewal comms, member newsletters, and digital touchpoints this week.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128176;</span>
        <div class="insight-text"><strong>Urgency window:</strong> Free VIC public transport through April may reduce fuel save frequency. Combine fuel savings message with Total Care and travel value messaging to maintain membership renewal motivation.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Club Marketing Lead</span>
        <span>Deadline: 14 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">RACV Total Care Update</span>
        <span class="card-badge amber">Policy Change</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.racv.com.au/roadside-assistance/total-care.html" target="_blank">RACV Total Care</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128663;</span>
        <div class="insight-text"><strong>Change effective 16 April 2026:</strong> RACV Total Care roadside assistance updated &#8212; from 16 April, members must nominate their vehicles to be covered. Up to 5 vehicles eligible. 100km towing included in coverage.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128222;</span>
        <div class="insight-text"><strong>Contact centre volume risk:</strong> This change could drive elevated inbound calls from members who are unaware of the vehicle nomination requirement. Prepare FAQs, update the website and brief the contact centre team before 16 April.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128161;</span>
        <div class="insight-text"><strong>Proactive outreach recommended:</strong> Send a targeted email to all Total Care members explaining the vehicle nomination process. Include direct link to the vehicle nomination portal to reduce friction and call volume.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Member Services / Contact Centre</span>
        <span>Deadline: 15 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Melbourne Dining: Autumn Season</span>
        <span class="card-badge green">Growing</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.broadsheet.com.au/melbourne/dining" target="_blank">Broadsheet Melbourne</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#127863;</span>
        <div class="insight-text"><strong>Sunday lunch bookings: fastest-growing segment</strong> at +22% YoY across Melbourne CBD premium venues. Wine-led dining outperforming food-only occasions. Members aged 55+ are the most active dining cohort &#8212; RACV Club&rsquo;s core segment.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#127869;</span>
        <div class="insight-text"><strong>Launch Sunday Long Lunch series:</strong> 3-course menu with wine pairing, targeting the 50&#8211;65 member cohort. April&#8211;June seasonal window. Brief chef and events team this week. Cost-of-living context means members value premium Club experiences over external dining.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: F&amp;B Director</span>
        <span>Deadline: 17 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Cost-of-Living Context</span>
        <span class="card-badge amber">High Relevance</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.abc.net.au/news/2026-04-10/fuel-prices-australia-excise-cut/" target="_blank">ABC News</a>, <a href="https://www.ptv.vic.gov.au/tickets/free-travel/" target="_blank">VIC Govt / PTV</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128202;</span>
        <div class="insight-text"><strong>Signals this week:</strong> Petrol $2.25/L (after excise halved 26.3c/L for 3 months). Diesel $3.08/L. Free VIC public transport entire April. 312+ stations ran dry. These signals combine to make the RACV value proposition &#8212; fuel savings, roadside, TI &#8212; more relevant than at any point since 2023.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128161;</span>
        <div class="insight-text"><strong>Club framing opportunity:</strong> Position RACV Club membership as a cost-of-living shield: dining at member rates vs external venues, fuel savings, roadside security, and travel value. Refresh Q2 membership renewal messaging to centre this narrative.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Club Marketing Lead</span>
        <span>Deadline: 16 Apr 2026</span>
      </div>
    </div>

  </div>

  <!-- Monday Action Summary -->
  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">Monday Priority Actions &#8212; RACV Club</span>
      <span class="card-badge gold">7&#8211;12 Apr 2026</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Priority</th><th>Action</th><th>Channel</th><th>Owner</th><th>Deadline</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Deploy $3.8M fuel savings EDM to all active members &#8212; peak crisis relevance window</td>
            <td>Email / CRM</td>
            <td>Club Marketing</td>
            <td>14 Apr</td>
            <td><span class="tag amber">Draft Needed</span></td>
          </tr>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Prepare Total Care vehicle nomination FAQ and brief contact centre before 16 Apr change</td>
            <td>Web + Contact Centre</td>
            <td>Member Services</td>
            <td>15 Apr</td>
            <td><span class="tag amber">In Progress</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Send proactive Total Care change email to all Total Care members with nomination link</td>
            <td>Email</td>
            <td>Member Services</td>
            <td>15 Apr</td>
            <td><span class="tag amber">Pending</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Brief Sunday Long Lunch series &#8212; chef and events team brief for April&#8211;June window</td>
            <td>Operations</td>
            <td>F&amp;B Director</td>
            <td>17 Apr</td>
            <td><span class="tag blue">Planning</span></td>
          </tr>
          <tr>
            <td><span class="tag blue">P3</span></td>
            <td style="font-size:11px;">Refresh Q2 renewal messaging to centre cost-of-living value proposition across all Club benefits</td>
            <td>Email + Digital</td>
            <td>Club Marketing</td>
            <td>18 Apr</td>
            <td><span class="tag blue">Planning</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</section>
<!-- END page-c-update -->'''

content = replace_section(
    content,
    '<section class="page" id="page-c-update">',
    '<!-- END page-c-update -->',
    c_update_new
)

# ============================================================
# SECTION 3: page-t-update
# ============================================================
print("\n[3] Replacing page-t-update...")

t_update_new = '''<section class="page" id="page-t-update">

  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">RACV Travel &#8212; Monday Intelligence Update</span>
      <span class="card-badge blue">7&#8211;12 Apr 2026</span>
    </div>
    <p class="insight-text" style="margin-bottom:0;">Priority intelligence for RACV Travel operations and member-facing teams. Covers the Islamabad talks failure, airline disruptions, travel insurance gaps, supplier highlights, cruise redeployments and new route openings from the past 72 hours.</p>
  </div>

  <!-- Priority Updates -->
  <div class="grid-2 section-gap">

    <div class="card">
      <div class="card-header">
        <span class="card-title">Islamabad Talks Failed &#8212; No Deal</span>
        <span class="card-badge red">Critical</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 12 Apr 2026 &middot; Source: <a href="https://edition.cnn.com/2026/04/12/middleeast/islamabad-iran-talks-fail" target="_blank">CNN</a>, <a href="https://www.wwno.org/npr-news/2026-04-12/iran-us-islamabad-talks" target="_blank">NPR / WWNO</a>, <a href="https://en.wikipedia.org/wiki/2026_Iran%E2%80%93United_States_crisis" target="_blank">Wikipedia</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128680;</span>
        <div class="insight-text"><strong>21-hour marathon talks ended without agreement on 12 April.</strong> Iran refused to abandon nuclear weapons pursuit and demanded full sovereignty over the Strait of Hormuz. Tehran has stated it &ldquo;has no plan for further negotiations.&rdquo; The two-week ceasefire remains technically active but extremely fragile.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128738;</span>
        <div class="insight-text"><strong>Oil at ~$97/bbl.</strong> Hormuz remains functionally closed &#8212; only 4&#8211;5 ships/day versus 150 pre-war. 2,000+ ships stranded in Persian Gulf, including 230 loaded oil tankers. RACV Travel must prepare for prolonged disruption to aviation fuel supply and airline schedules.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#127919;</span>
        <div class="insight-text"><strong>Action:</strong> Brief all Travel consultants on the failed talks and what this means for Middle East itineraries, connecting flights and travel insurance validity. Update member-facing content to reflect ongoing uncertainty.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Operations Manager</span>
        <span>Deadline: 14 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Airline Disruptions Escalating</span>
        <span class="card-badge red">Active</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.businessinsider.com.au/airline-disruptions-easter-2026" target="_blank">Business Insider</a>, <a href="https://traveltourister.com/airline-disruptions-april-2026/" target="_blank">TravelTourister</a>, <a href="https://www.euronews.com/travel/2026/04/10/lufthansa-strike-flights-cancelled" target="_blank">Euronews</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#9992;</span>
        <div class="insight-text"><strong>418+ disruptions on Good Friday alone.</strong> SAS cancelled 1,000 flights this week. AirAsia cut 10% of capacity with fares up 30&#8211;40%. Air NZ reduced by approx. 5% (~1,100 flights). Lufthansa strike on 10 Apr cancelled 80&#8211;90% of Frankfurt/Munich flights.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#9981;</span>
        <div class="insight-text"><strong>Fuel cost escalation:</strong> United Airlines faces an estimated $11B in extra annual fuel cost if current prices persist and has begun cutting off-peak flights. Italy&rsquo;s airports (Bologna, Milan Linate, Venice, Treviso) are actively rationing jet fuel.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128222;</span>
        <div class="insight-text"><strong>Action:</strong> Proactively contact all members with upcoming European or Middle East itineraries involving Lufthansa, SAS or AirAsia connections. Reconfirm cruise embarkation transfers for May departures.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Consultants Lead</span>
        <span>Deadline: 14 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Travel Insurance Gap Widening</span>
        <span class="card-badge amber">Member Alert</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.insurancejournal.com/news/international/2026/04/08/war-exclusions-travel-insurance/" target="_blank">Insurance Journal</a>, <a href="https://www.covermore.com.au/travel-alerts" target="_blank">Cover-More</a>, <a href="https://www.allianz.com.au/travel-insurance/travel-alerts" target="_blank">Allianz</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128737;</span>
        <div class="insight-text"><strong>War exclusions activated:</strong> Cover-More and Allianz have both explicitly confirmed they are not covering war-related claims from the Iran conflict. The conflict is treated as a &ldquo;known event&rdquo; from 1 March 2026 &#8212; policies purchased after that date exclude Iran conflict impacts.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#9888;</span>
        <div class="insight-text"><strong>Exposure for RACV members:</strong> Members with bookings involving Middle East destinations or transit routes through affected hubs need clear guidance. Airline disruption and cancellation cover may also be denied where the disruption is linked to the conflict.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128161;</span>
        <div class="insight-text"><strong>RACV TI positioning opportunity:</strong> Publish a clear member advisory on TI war exclusions. Brief consultants to raise TI cover status at every booking. Review RACV TI product to identify any gap vs Cover-More/Allianz exclusion scope.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Insurance Product Lead</span>
        <span>Deadline: 15 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">Supplier Highlights &#8212; April Sales</span>
        <span class="card-badge green">Opportunity</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://www.vikingcruises.com.au/special-offers" target="_blank">Viking IR</a>, <a href="https://www.prnewswire.com/news-releases/holland-america-europe-bookings-2026" target="_blank">PR Newswire</a>, <a href="https://www.travelpulse.com/news/cruise/royal-caribbean-buyback" target="_blank">TravelPulse</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128674;</span>
        <div class="insight-text"><strong>Viking:</strong> Your Choice Sale live &#8212; save up to $4,000/couple, free airfare on select departures, $25 deposit to hold. Viking Polaris arrived Sydney 9 April (first 2026 season vessel). <strong>Holland America:</strong> Europe bookings +33% YoY; Northern Europe up 50%. <strong>APT:</strong> PS Australian Star Murray River launching. <strong>Intrepid:</strong> 28 new active trips across 6 continents.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128185;</span>
        <div class="insight-text"><strong>Royal Caribbean:</strong> $2B share buyback announced and $1.50 dividend reinstated &#8212; signalling strong financial position and confidence in 2026&#8211;27 demand. Anthem of the Seas Sydney homeport season active. Transpacific from Brisbane 14 Apr.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#127919;</span>
        <div class="insight-text"><strong>Action:</strong> Push Viking Your Choice Sale via CRM this week &#8212; $25 deposit removes booking friction. Target 55&#8211;75 member cohort. Holland America Europe surge supports urgency messaging for remaining Northern Europe departures.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Sales Lead</span>
        <span>Deadline: 15 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">MSC Cancels Middle East Season</span>
        <span class="card-badge amber">Deployment Change</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 7&#8211;12 Apr 2026 &middot; Source: <a href="https://parade.com/travel/msc-middle-east-cancelled-2026" target="_blank">Parade</a>, <a href="https://people.com/travel/msc-world-europa-caribbean-redeployment" target="_blank">People</a>, <a href="https://www.cruiseindustrynews.com/cruise-news/2026/04/msc-cancels-middle-east/" target="_blank">CruiseIndustryNews</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#128674;</span>
        <div class="insight-text"><strong>MSC World Europa redeployed</strong> from Middle East to Caribbean for the 2026&#8211;27 season. MSC is the 4th cruise line to cancel all Middle East sailings. Over 50,000 passengers are affected and will require rebooking or refunds.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128227;</span>
        <div class="insight-text"><strong>Proactive outreach required:</strong> RACV Travel consultants must identify all members with MSC Middle East bookings and contact them immediately. Priority options: alternative MSC Caribbean itinerary, Holland America Europe, or Cunard Transatlantic as substitute products.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Consultants Lead</span>
        <span>Deadline: 15 Apr 2026</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="card-title">EU EES Now Live + New AU Routes</span>
        <span class="card-badge blue">Operational</span>
      </div>
      <div style="font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-3)">Updated: 10&#8211;12 Apr 2026 &middot; Source: <a href="https://travel.ec.europa.eu/travel-and-visa/entry-exit-system-ees_en" target="_blank">European Commission</a>, <a href="https://www.timeout.com/melbourne/things-to-do/new-flights-from-melbourne-2026" target="_blank">Time Out</a>, <a href="https://aviationweek.com/air-transport/finnair-melbourne-helsinki-2026" target="_blank">Aviation Week</a></div>
      <div class="insight-chip">
        <span class="insight-icon">&#127466;&#127482;</span>
        <div class="insight-text"><strong>EU Entry/Exit System (EES) fully operational from 10 April 2026.</strong> All non-EU travellers to Europe now face biometric digital border checks &#8212; fingerprinting and facial recognition on entry and exit. Adds time to border processing. Members travelling to Europe need pre-departure briefing.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128747;</span>
        <div class="insight-text"><strong>New routes confirmed:</strong> Finnair Melbourne&#8211;Helsinki via Bangkok launching Oct 26, 2026 (203,000 seats/year). Jetstar Melbourne Avalon&#8211;Bali live (5x/week, 120K seats/year). Luxury Escapes Melbourne&#8211;Maldives direct from 18 May 2026 (first-ever AU&#8211;Maldives direct). Canberra&#8211;Bali first-ever service from 22 June 2026.</div>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128161;</span>
        <div class="insight-text"><strong>Opportunity:</strong> Add EES advisory to all European booking confirmations immediately. Promote Luxury Escapes Maldives and Finnair Helsinki as new-to-market itinerary options for 2026&#8211;27 planning season.</div>
      </div>
      <hr class="divider">
      <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--color-text-faint)">
        <span>Owner: Travel Operations / Consultant Team</span>
        <span>Deadline: 16 Apr 2026</span>
      </div>
    </div>

  </div>

  <!-- Monday Priority Actions -->
  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">Monday Priority Actions &#8212; RACV Travel</span>
      <span class="card-badge gold">7&#8211;12 Apr 2026</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Priority</th><th>Action</th><th>Channel</th><th>Owner</th><th>Deadline</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Contact all members with MSC Middle East bookings &#8212; proactive reallocation to Caribbean or alternative products</td>
            <td>Phone + Email</td>
            <td>Consultant Lead</td>
            <td>15 Apr</td>
            <td><span class="tag amber">Urgent</span></td>
          </tr>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Brief consultants on TI war exclusions &#8212; Cover-More &amp; Allianz not covering war claims; RACV TI positioning review</td>
            <td>Internal Brief</td>
            <td>TI Product Lead</td>
            <td>15 Apr</td>
            <td><span class="tag amber">Draft Needed</span></td>
          </tr>
          <tr>
            <td><span class="tag red">P1</span></td>
            <td style="font-size:11px;">Push Viking Your Choice Sale EDM &#8212; $25 deposit, up to $4K off, free airfare (55&#8211;75 member cohort)</td>
            <td>CRM Email</td>
            <td>Travel Sales Lead</td>
            <td>15 Apr</td>
            <td><span class="tag amber">Ready to Send</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Add EU EES advisory to all European booking confirmations and update website FAQ</td>
            <td>Digital + Templates</td>
            <td>Travel Ops</td>
            <td>16 Apr</td>
            <td><span class="tag amber">In Progress</span></td>
          </tr>
          <tr>
            <td><span class="tag amber">P2</span></td>
            <td style="font-size:11px;">Contact members with Lufthansa/SAS connections in May &#8212; reconfirm itineraries or offer alternatives</td>
            <td>Phone + Email</td>
            <td>Consultant Lead</td>
            <td>16 Apr</td>
            <td><span class="tag blue">Pending</span></td>
          </tr>
          <tr>
            <td><span class="tag blue">P3</span></td>
            <td style="font-size:11px;">Add Luxury Escapes Maldives direct (May 18) and Finnair Helsinki (Oct 26) to new routes newsletter</td>
            <td>Email / Website</td>
            <td>Travel Marketing</td>
            <td>18 Apr</td>
            <td><span class="tag blue">Planning</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</section>
<!-- END page-t-update -->'''

content = replace_section(
    content,
    '<section class="page" id="page-t-update">',
    '<!-- END page-t-update -->',
    t_update_new
)

# ============================================================
# SECTION 4: page-b-update
# ============================================================
print("\n[4] Replacing page-b-update...")

b_update_new = '''<section class="page" id="page-b-update">

  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">Benefits &#8212; Monday Monitoring Update</span>
      <span class="card-badge blue">7&#8211;12 Apr 2026</span>
    </div>
    <p class="insight-text" style="margin-bottom:0;">Rapid-cycle benefits intelligence covering the past 72 hours. Tracks fuel price movements, member savings milestones, Total Care changes, and cost-of-living context during the ongoing fuel crisis.</p>
  </div>

  <!-- Date columns -->
  <div class="grid-3 section-gap" style="gap:var(--space-4);">

    <!-- Day 1 -->
    <div class="card">
      <div class="card-header" style="border-bottom:1px solid var(--color-border);padding-bottom:var(--space-3);margin-bottom:var(--space-3);">
        <span class="card-title" style="font-size:var(--text-sm);">Thu 10 Apr</span>
        <span class="card-badge amber">Fuel Watch</span>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light amber"></div>
        <div class="tl-content">
          <div class="tl-label">ULP Melbourne Avg</div>
          <div class="tl-value">225c/L</div>
          <div class="tl-trend down">&#9660; After excise cut (down from $2.58 high)</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light green"></div>
        <div class="tl-content">
          <div class="tl-label">Member Fuel Savings</div>
          <div class="tl-value">$3.8M since Sep 2025</div>
          <div class="tl-trend up">&#9650; 318,000 members used discount</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light amber"></div>
        <div class="tl-content">
          <div class="tl-label">Roadside Calls</div>
          <div class="tl-value">Elevated</div>
          <div class="tl-trend up">&#9650; Easter travel peak load</div>
        </div>
      </div>
      <div class="tl-card">
        <div class="tl-light amber"></div>
        <div class="tl-content">
          <div class="tl-label">Total Care Change Notice</div>
          <div class="tl-value">16 April effective date</div>
          <div class="tl-trend flat">&#8212; Vehicle nomination required</div>
        </div>
      </div>
    </div>

    <!-- Day 2 -->
    <div class="card">
      <div class="card-header" style="border-bottom:1px solid var(--color-border);padding-bottom:var(--space-3);margin-bottom:var(--space-3);">
        <span class="card-title" style="font-size:var(--text-sm);">Fri 11 Apr</span>
        <span class="card-badge red">Oil Volatility</span>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light red"></div>
        <div class="tl-content">
          <div class="tl-label">Islamabad Talks Begin</div>
          <div class="tl-value">Oil volatility</div>
          <div class="tl-trend up">&#9650; Markets watching Hormuz outcome</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light red"></div>
        <div class="tl-content">
          <div class="tl-label">Diesel Price</div>
          <div class="tl-value">$3.08/L (record)</div>
          <div class="tl-trend up">&#9650; Still rising; no relief in sight</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light green"></div>
        <div class="tl-content">
          <div class="tl-label">VIC Free Transport</div>
          <div class="tl-value">April continues</div>
          <div class="tl-trend flat">&#8212; Trains, trams, buses all free</div>
        </div>
      </div>
      <div class="tl-card">
        <div class="tl-light green"></div>
        <div class="tl-content">
          <div class="tl-label">eGift Transactions</div>
          <div class="tl-value">Elevated</div>
          <div class="tl-trend up">&#9650; Easter &amp; school holidays peak</div>
        </div>
      </div>
    </div>

    <!-- Day 3 -->
    <div class="card">
      <div class="card-header" style="border-bottom:1px solid var(--color-border);padding-bottom:var(--space-3);margin-bottom:var(--space-3);">
        <span class="card-title" style="font-size:var(--text-sm);">Sat 12 Apr</span>
        <span class="card-badge red">Talks Failed</span>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light red"></div>
        <div class="tl-content">
          <div class="tl-label">Islamabad Talks FAIL</div>
          <div class="tl-value">No Hormuz deal</div>
          <div class="tl-trend up">&#9650; Oil rebounds to ~$97/bbl</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light amber"></div>
        <div class="tl-content">
          <div class="tl-label">Weekend Fuel Forecast</div>
          <div class="tl-value">225&#8211;230c/L range</div>
          <div class="tl-trend flat">&#8212; No significant movement expected</div>
        </div>
      </div>
      <div class="tl-card" style="margin-bottom:var(--space-3);">
        <div class="tl-light red"></div>
        <div class="tl-content">
          <div class="tl-label">Fuel Outlook Messaging</div>
          <div class="tl-value">Members need clarity</div>
          <div class="tl-trend flat">&#8212; Clear comms required now</div>
        </div>
      </div>
      <div class="tl-card">
        <div class="tl-light amber"></div>
        <div class="tl-content">
          <div class="tl-label">Relief Timeline</div>
          <div class="tl-value">Mid-May earliest</div>
          <div class="tl-trend down">&#9660; No off-ramp found in talks</div>
        </div>
      </div>
    </div>

  </div>

  <!-- CoL context strip -->
  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">Cost-of-Living Signals &#8212; 72hr Watch</span>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:var(--space-3);margin-top:var(--space-2);">
      <div class="insight-chip">
        <span class="insight-icon">&#9981;</span>
        <span class="insight-text">Petrol: <strong>$2.25/L avg</strong> after excise cut (down from $2.58 high). Diesel: <strong>$3.08/L</strong> and still rising. Fuel crisis structural until mid-May at earliest.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128176;</span>
        <span class="insight-text">RACV fuel savings: <strong>$3.8M since Sep 2025</strong> (318,000 members used EG Ampol discount) &#8212; strongest member value proof point in RACV&rsquo;s history.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128646;</span>
        <span class="insight-text">VIC free public transport <strong>entire April</strong> &#8212; all trains, trams and buses. Nudge members to use for commuting and resort-corridor travel while window is open.</span>
      </div>
      <div class="insight-chip">
        <span class="insight-icon">&#128663;</span>
        <span class="insight-text">RACV Total Care change from <strong>16 April</strong> &#8212; vehicle nomination now required. Send proactive member communication before change date to minimise contact centre volume.</span>
      </div>
    </div>
  </div>

  <!-- Action items -->
  <div class="card section-gap">
    <div class="card-header">
      <span class="card-title">72hr Recommended Actions</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Action</th><th>Channel</th><th>Priority</th><th>Timing</th></tr>
        </thead>
        <tbody>
          <tr>
            <td>Deploy $3.8M fuel savings EDM &#8212; crisis = peak member value relevance</td>
            <td>Email + Push</td>
            <td><span class="tag green">High</span></td>
            <td>Today, before 5pm</td>
          </tr>
          <tr>
            <td>Send Total Care vehicle nomination advisory to all Total Care members</td>
            <td>Email</td>
            <td><span class="tag green">High</span></td>
            <td>By 15 Apr</td>
          </tr>
          <tr>
            <td>Publish fuel outlook update for members &#8212; 225&#8211;230c/L range, no relief until mid-May</td>
            <td>Website + App</td>
            <td><span class="tag amber">Medium</span></td>
            <td>Today</td>
          </tr>
          <tr>
            <td>Promote free VIC public transport in member newsletter &#8212; commuting and weekend travel nudge</td>
            <td>Email + Social</td>
            <td><span class="tag amber">Medium</span></td>
            <td>This week</td>
          </tr>
          <tr>
            <td>Brief contact centre on Total Care change &#8212; FAQs and nomination portal link ready</td>
            <td>Internal</td>
            <td><span class="tag primary">Watch</span></td>
            <td>Before 16 Apr</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</section><!-- end page-b-update -->'''

content = replace_section(
    content,
    '<section class="page" id="page-b-update">',
    '</section><!-- end page-b-update -->',
    b_update_new
)

# ============================================================
# ARCHIVE: Add fri10 entry
# ============================================================
print("\n[5] Adding archive entry fri10...")

archive_marker = 'var dailyArchiveData = {'
fri10_entry = '''var dailyArchiveData = {
  fri10: {
    date: 'Friday 10 April 2026', issue: 4,
    alert: 'Islamabad talks begin Sat 11 Apr. Oil at ~$97/bbl post-ceasefire. Hormuz still effectively closed -- only 4-5 ships/day vs 150 normal. 2,000 ships stranded. IATA warns months to normalise.',
    vic: 'Easter results in: Mornington Peninsula solid, Dargo -20%. Free transport April continues. Fuel excise halved 26.3c/L. 312+ stations ran dry. VIC daily price cap active.',
    au: 'Fuel: petrol $2.25/L, diesel $3.08/L. 39 days petrol reserves. 418+ Easter flight disruptions. Qantas reclaimed on-time crown Feb. New routes: MEL-Maldives, MEL-Helsinki, CBR-Bali announced.',
    global: 'Italy airports rationing jet fuel. Lufthansa strike cancelled 80-90% flights 10 Apr. EU EES fully live 10 Apr. MSC cancels all Middle East 2026-27 sailings. SAS -1,000 flights. AirAsia fares +30-40%.',
    action: 'Two critical actions: (1) Amplify RACV $3.8M fuel savings in all member comms -- crisis = peak relevance. (2) Proactive outreach to members with ME transit bookings re: insurance gap and rebooking options.',
    signals: 'Oil: ~$97/bbl | Petrol: $2.25/L | Diesel: $3.08/L | AU Reserves: 39d petrol | VIC Stations Dry: 312+ | Easter Disruptions: 418+ | RACV Fuel Savings: $3.8M',
    supplierWatch: 'Viking: Your Choice Sale live, $4K off, Polaris arrived SYD 9 Apr. | APT: PS Australian Star Murray River launching. | MSC: Cancelled all ME sailings -- redeploying Caribbean. | Holland America: Europe bookings +33%. | Intrepid: 28 new active vacations. | Royal Caribbean: $2B buyback, strong finances.',
    racvAction: 'Deploy RACV $3.8M fuel savings EDM immediately. Prepare Total Care FAQ for 16 Apr changes. Brief Travel consultants on TI war exclusion gap. Contact members with ME cruise bookings re: MSC cancellations.'
  },'''

if archive_marker in content:
    content = content.replace(archive_marker, fri10_entry, 1)
    print("  Archive entry added")
else:
    print("  ERROR: archive marker not found")

# ============================================================
# Write output
# ============================================================
print(f"\nWriting file ({len(content)} chars)...")
with open('/home/user/workspace/racv-dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("DONE")
PYEOF
