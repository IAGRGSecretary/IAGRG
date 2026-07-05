import os
import re
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

# ==================================================
# CONFIG
# ==================================================

SPREADSHEET_NAME = "Responses"
WORKSHEET_NAME = "Form Responses 1"
POSTS_DIR = "_posts"

os.makedirs(POSTS_DIR, exist_ok=True)

# ==================================================
# AUTH
# ==================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES,
)

client = gspread.authorize(creds)

sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)

# Read every row as a list (avoids duplicate-header problems)
rows = sheet.get_all_values()

# ==================================================
# COLUMN INDICES
# ==================================================

TIMESTAMP = 0

CATEGORY = 3

JOB_TITLE = 4
JOB_PLACE = 5
JOB_DEADLINE = 6
JOB_DESCRIPTION = 7
JOB_URL = 8
JOB_CONTACT = 9

CONF_TITLE = 10
CONF_PLACE = 11
CONF_START = 12
CONF_END = 13
CONF_REG = 14
CONF_ABS = 15
CONF_DESCRIPTION = 16
CONF_URL = 17
CONF_CONTACT = 18

NEWS_TITLE = 19
NEWS_DESCRIPTION = 20
NEWS_URL = 21
NEWS_CONTACT = 22

STATUS = 23

# ==================================================
# HELPERS
# ==================================================

def clean(x):
    return str(x).strip()

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

# ==================================================
# PROCESS
# ==================================================

created = 0

# Skip header row
for sheet_row_number, row in enumerate(rows[1:], start=2):

    # Pad short rows if necessary
    while len(row) <= STATUS:
        row.append("")

    status = clean(row[STATUS]).lower()

    if status != "approved":
        continue

    category = clean(row[CATEGORY]).lower()

    title = ""
    body = ""

    # ==================================================
    # JOB
    # ==================================================

    if category == "job":

        title = clean(row[JOB_TITLE])

        body = f"""
**Location:** {clean(row[JOB_PLACE])}

**Deadline:** {clean(row[JOB_DEADLINE])}

{clean(row[JOB_DESCRIPTION])}

**Website:** <{clean(row[JOB_URL])}>

**Contact:** {clean(row[JOB_CONTACT])}
"""

    # ==================================================
    # CONFERENCE
    # ==================================================

    elif category == "conference":

        title = clean(row[CONF_TITLE])

        body = f"""
**Venue:** {clean(row[CONF_PLACE])}

**Dates:** {clean(row[CONF_START])} to {clean(row[CONF_END])}

**Registration Deadline:** {clean(row[CONF_REG])}

**Abstract Deadline:** {clean(row[CONF_ABS])}

{clean(row[CONF_DESCRIPTION])}

**Website:** <{clean(row[CONF_URL])}>

**Contact:** {clean(row[CONF_CONTACT])}
"""

    # ==================================================
    # NEWS
    # ==================================================

    elif category == "news":

        title = clean(row[NEWS_TITLE])

        body = f"""
{clean(row[NEWS_DESCRIPTION])}

**Website:** <{clean(row[NEWS_URL])}>

**Contact:** {clean(row[NEWS_CONTACT])}
"""

    else:
        continue

    if not title:
        continue

    # ==================================================
    # DATE
    # ==================================================

    try:
        dt = datetime.strptime(clean(row[TIMESTAMP]), "%m/%d/%Y %H:%M:%S")
    except Exception:
        dt = datetime.now()

    date_prefix = dt.strftime("%Y-%m-%d")
    post_datetime = dt.strftime("%Y-%m-%d %H:%M:%S +0530")

    slug = slugify(title)

    filename = f"{date_prefix}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    counter = 2

    while os.path.exists(filepath):
        filename = f"{date_prefix}-{slug}-{counter}.md"
        filepath = os.path.join(POSTS_DIR, filename)
        counter += 1

    md = f"""---
layout: post
title: "{title}"
date: {post_datetime}
category: {category}
---

{body}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Created: {filename}")

    # Update status to Published
    sheet.update_cell(sheet_row_number, STATUS + 1, "Published")

    created += 1

print(f"\nDone. {created} new posts created.")