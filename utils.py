START = "11/26/2018" # Start of 2019 candidate filing period
END = "12/31/2019" # End of 2019 election cycle

CAND_FILES = [
    "contributions/chico-clean.json",
    "contributions/daley-clean.json",
    "contributions/enyia-clean.json",
    "contributions/joyce-clean.json",
    "contributions/lightfoot-clean.json",
    "contributions/mendoza-clean.json",
    "contributions/preckwinkle-clean.json",
    "contributions/vallas-clean.json",
    "contributions/wilson-clean.json",
]

ZIP_INTS = [60647, 60622, 60642, 60611, 60610, 60654, 60614, 60615, 60653,
    60616, 60609, 60605, 60604, 60649, 60619, 60637, 60621, 60620,
    60617, 60628, 60827, 60643, 60633, 60608, 60632, 60629, 60638,
    60636, 60652, 60655, 60623, 60644, 60624, 60612, 60607, 60639,
    60651, 60661, 60634, 60707, 60618, 60641, 60657, 60625, 60630,
    60606, 60602, 60603, 60601, 60656, 60646, 60659, 60645, 60626,
    60660, 60640, 60631, 60706, 60613]

ZIP_STRS = ['60647','60622','60642', '60611', '60610', '60654', '60614', '60615', '60653',
    '60616', '60609', '60605', '60604', '60649', '60619', '60637', '60621', '60620',
    '60617', '60628', '60827', '60643', '60633', '60608', '60632', '60629', '60638',
    '60636', '60652', '60655', '60623', '60644', '60624', '60612', '60607', '60639',
    '60651', '60661', '60634', '60707', '60618', '60641', '60657', '60625', '60630',
    '60606', '60602', '60603', '60601', '60656', '60646', '60659', '60645', '60626',
    '60660', '60640', '60631', '60706', '60613']


# References (relevant dates):
# Illinois State Board of Elections 2019 Election and Campaign Finance Calendar
# available at https://www.elections.il.gov/Main/Publications.aspx
# 10 ILCS 5/9-1.9 available at https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=001000050K9-1.9