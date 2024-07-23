import openpyexcel
from openpyexcel.styles import Font, Alignment

# Create a new workbook and select the active sheet
wb = openpyexcel.Workbook()
sheet = wb.active
sheet.title = "DC Metro VC Firms"

# Define the headers
headers = ["Firm Name", "Location", "Website", "Background", "Deal Interests", "Investment Stage", "Notable Investments"]

# Add headers to the first row
for col, header in enumerate(headers, start=1):
    cell = sheet.cell(row=1, column=col)
    cell.value = header
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

# Define the data
data = [
    ["New Enterprise Associates (NEA)", "Chevy Chase MD", "www.nea.com", "One of the world's largest and most active venture capital firms", "Technology, healthcare, energy, enterprise software", "Seed to Growth", "Coursera, Duolingo, Cloudflare"],
    ["Revolution Ventures", "Washington DC", "www.revolution.com", "Founded by Steve Case (AOL co-founder) focuses on transformative companies", "Consumer technology, enterprise software, healthcare IT", "Early to Growth", "DraftKings, Sweetgreen, Framebridge"],
    ["Motley Fool Ventures", "Alexandria VA", "www.foolventures.com", "Venture arm of the financial services company The Motley Fool", "Technology-enabled businesses, consumer products, health tech", "Early Stage", "Embark, Wunder Capital, Trove"],
    ["Lavrock Ventures", "McLean VA", "www.lavrockvc.com", "Focuses on enterprise software and frontier tech companies", "Cybersecurity, AI/ML, data analytics, enterprise SaaS", "Seed to Series B", "NS8, Sayari Labs, Stardog"],
    ["QED Investors", "Alexandria VA", "www.qedinvestors.com", "Specializes in fintech investments globally", "Fintech, insurtech, proptech, healthcare IT", "Seed to Growth", "Credit Karma, SoFi, Klarna"],
    ["Resolute Ventures", "Washington DC", "www.resolute.vc", "Early-stage fund focusing on ambitious founders", "Enterprise SaaS, consumer tech, marketplaces", "Seed", "Openpath, Bark, Superhuman"],
    ["Aldrich Capital Partners", "Vienna VA", "www.aldrichcap.com", "Growth equity firm focusing on technology companies", "Healthcare IT, fintech, IoT, cybersecurity", "Growth", "Limeade, Woundtech, Zipari"],
    ["Blu Venture Investors", "Vienna VA", "www.bluventureinvestors.com", "Angel investment group turned VC firm", "Cybersecurity, big data, IoT, AI/ML", "Seed to Series A", "Cybrary, Ostendio, Huntress Labs"],
    ["Enlightenment Capital", "Chevy Chase MD", "www.enlightenment-cap.com", "Focuses on aerospace defense and government services", "Defense tech, cybersecurity, intelligence solutions", "Growth", "ByteCubed, Telos, Diplomatic Language Services"],
    ["Sands Capital Ventures", "Arlington VA", "www.sandscapital.com/ventures", "Venture arm of Sands Capital Management", "Life sciences, technology, consumer, business services", "Early to Growth", "DocuSign, Didi Chuxing, Sweetgreen"],
    ["Accel Partners", "Washington DC", "www.accel.com", "Global venture capital firm with a long history of backing successful startups", "Enterprise software, consumer tech, infrastructure", "Early to Growth", "Facebook, Spotify, Slack"],
    ["Bessemer Venture Partners", "Washington DC", "www.bvp.com", "One of the oldest venture capital firms in the U.S.", "Cloud computing, cybersecurity, healthcare IT", "Early to Growth", "LinkedIn, Pinterest, Twilio"],
    ["Columbia Capital", "Alexandria VA", "www.colcap.com", "Focuses on enterprise IT infrastructure and services", "Enterprise IT, communications, data centers", "Early to Growth", "Zayo Group, Presidio, euNetworks"],
    ["Grotech Ventures", "Vienna VA", "www.grotech.com", "Invests in high-potential technology companies", "Enterprise software, cybersecurity, healthcare IT", "Early Stage", "HelloWallet, Contactually, Optoro"],
    ["In-Q-Tel", "Arlington VA", "www.iqt.org", "Strategic investor for U.S. intelligence and defense communities", "AI/ML, data analytics, cybersecurity, biotechnology", "Early Stage", "Confidential due to nature of investments"],
    ["NextGen Venture Partners", "Washington DC", "www.nextgenvp.com", "Network-driven venture capital firm", "Enterprise software, consumer tech, marketplaces", "Seed to Series A", "Hurdlr, Ceros, Spotluck"],
    ["Pillar VC", "Washington DC", "www.pillar.vc", "Founder-friendly firm focused on breakthrough technologies", "Deep tech, AI/ML, robotics, life sciences", "Seed to Series A", "Desktop Metal, PillPack, Jellyfish"],
    ["Route 66 Ventures", "Alexandria VA", "www.route66ventures.com", "Provides venture capital and credit solutions to emerging financial services companies", "Fintech, insurtech, real estate tech", "Early to Growth", "Kabbage, Remitly, Bluevine"],
    ["SWaN & Legend Venture Partners", "Vienna VA", "www.swanandlegend.com", "Invests in technology-enabled consumer and enterprise companies", "Consumer brands, enterprise tech, media", "Early to Growth", "CustomInk, DreamBox Learning, Quad Learning"],
    ["The Carlyle Group", "Washington DC", "www.carlyle.com", "Global investment firm with a venture and growth equity arm", "Technology, healthcare, consumer", "Growth to Late Stage", "Beats Electronics, Avigilon, Ortho Clinical Diagnostics"]
]

# Add data to the sheet
for row, firm_data in enumerate(data, start=2):
    for col, value in enumerate(firm_data, start=1):
        cell = sheet.cell(row=row, column=col)
        cell.value = value
        cell.alignment = Alignment(wrap_text=True)

# Adjust column widths

# Save the workbook
wb.save("DC_Metro_VC_Firms.xlsx")

print("Excel file 'DC_Metro_VC_Firms.xlsx' has been created successfully.")