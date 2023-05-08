def counter_for_sites(lst):
    site_dict = {}
    site = ""
    for i in lst:
        site = i[-2:]
        print(site)
        if site in site_dict:
            site_dict[site] = site_dict[site] + 1 
        else: 
            site_dict[site] = 1
    return site_dict

print(counter_for_sites(["cdfg-IN", "sedfkhjoi-ID", "skfjhs-PL", "skfjhs-PL"]))
