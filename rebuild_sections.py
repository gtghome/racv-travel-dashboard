#!/usr/bin/env python3
"""
Replace page-hotels and page-packages sections in index.html
with new rebuilt versions.
"""

import re

# Read the source files
with open('/home/user/workspace/racv-dashboard/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('/home/user/workspace/racv-dashboard/hotels-section.html', 'r', encoding='utf-8') as f:
    hotels_html = f.read().strip()

with open('/home/user/workspace/racv-dashboard/packages-section.html', 'r', encoding='utf-8') as f:
    packages_html = f.read().strip()

print(f"Original file length: {len(content)} chars")

# Find the exact positions of each section
hotels_start_tag = '<section class="page" id="page-hotels">'
packages_start_tag = '<section class="page" id="page-packages">'
tbrand_start_tag = '<section class="page" id="page-t-brand">'

hotels_start = content.find(hotels_start_tag)
packages_start = content.find(packages_start_tag)
tbrand_start = content.find(tbrand_start_tag)

print(f"page-hotels starts at char: {hotels_start}")
print(f"page-packages starts at char: {packages_start}")
print(f"page-t-brand starts at char: {tbrand_start}")

if hotels_start == -1 or packages_start == -1 or tbrand_start == -1:
    print("ERROR: Could not find one or more section markers!")
    exit(1)

# Extract segments:
# before_hotels: everything before page-hotels
# between: the gap between end of packages and start of t-brand (whitespace/newlines)
# after_tbrand: page-t-brand onwards

before_hotels = content[:hotels_start]
after_packages_before_tbrand = content[packages_start:tbrand_start]

# Find end of packages section - it's </section> before page-t-brand
# We need to find the closing </section> of page-packages
# The packages section ends just before page-t-brand
packages_section_end = content.rfind('</section>', packages_start, tbrand_start)
print(f"packages </section> closes at char: {packages_section_end}")

# Everything between end of packages section and page-t-brand (whitespace)
gap_between = content[packages_section_end + len('</section>'):tbrand_start]
after_tbrand = content[tbrand_start:]

print(f"Gap between packages and t-brand: {repr(gap_between[:100])}")

# Build the new content
new_content = (
    before_hotels +
    '\n' + hotels_html + '\n\n\n' +
    '\n' + packages_html + '\n\n\n' +
    gap_between +
    after_tbrand
)

print(f"New file length: {len(new_content)} chars")

# Verify the new sections exist
assert '<section class="page" id="page-hotels">' in new_content, "page-hotels missing!"
assert '<section class="page" id="page-packages">' in new_content, "page-packages missing!"
assert '<section class="page" id="page-t-brand">' in new_content, "page-t-brand missing!"

# Write backup
with open('/home/user/workspace/racv-dashboard/index.html.bak', 'w', encoding='utf-8') as f:
    f.write(content)
print("Backup written to index.html.bak")

# Write new file
with open('/home/user/workspace/racv-dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("New index.html written successfully!")

# Verify the order of sections
new_hotels_pos = new_content.find('<section class="page" id="page-hotels">')
new_packages_pos = new_content.find('<section class="page" id="page-packages">')
new_tbrand_pos = new_content.find('<section class="page" id="page-t-brand">')

print(f"\nVerification:")
print(f"  page-hotels at: {new_hotels_pos}")
print(f"  page-packages at: {new_packages_pos}")
print(f"  page-t-brand at: {new_tbrand_pos}")
print(f"  Order correct: {new_hotels_pos < new_packages_pos < new_tbrand_pos}")

# Check no RACV Resort or RACV Club names in the new sections
hotels_section_new = new_content[new_hotels_pos:new_packages_pos]
packages_end = new_content.find('</section>', new_packages_pos)
# Find the last </section> before t-brand
packages_section_new_end = new_content.rfind('</section>', new_packages_pos, new_tbrand_pos)
packages_section_new = new_content[new_packages_pos:packages_section_new_end + len('</section>')]

forbidden = ['RACV Resort', 'RACV Club', 'Cape Schanck', 'Torquay Resort', 'Healesville Resort',
             'Royal Pines', 'Cobram', 'Inverloch Resort']

print(f"\nChecking for forbidden RACV property names in new sections:")
for name in forbidden:
    in_hotels = name.lower() in hotels_section_new.lower()
    in_packages = name.lower() in packages_section_new.lower()
    if in_hotels or in_packages:
        print(f"  WARNING: Found '{name}' - hotels: {in_hotels}, packages: {in_packages}")
    else:
        print(f"  OK: '{name}' not found")

print("\nDone!")
