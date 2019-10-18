monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "Jun":"June",
    "May":"May",
    "Jul":"July",
    "Aug":"August",
    "Oct":"October",
    "Sep":"September",
    "Nov":"November",
    "Dec":"December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("sds","Not vailed Key"))