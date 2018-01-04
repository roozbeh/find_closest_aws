import commands
import json
import operator
import pprint

print "Fetching regions"
out = commands.getstatusoutput("aws ec2 describe-regions")
regions = json.loads(out[1])
round_trips = {}
for r in regions['Regions']:
    print "Calculating round trip for %s" % r['Endpoint']
    out = commands.getstatusoutput("ping -c10 %s" % r['Endpoint'])
    round_trip = float(out[1].split('\n')[-1].split('/')[4])
    round_trips[r['RegionName']] = round_trip

sorted_times = sorted(round_trips.items(), key=operator.itemgetter(1))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sorted_times)
    