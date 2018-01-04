# Find Closest AWS Region
---

This repository is created to find the closest AWS region to the current environment. I notices that most of the time the closest geographic location might not be the fastest region. 

# Requirements
```pip install awscli --upgrade --user```

# How to
```python find_servers.py```

# Sample output
The following output shows the best region for the current location is `EU Central` and `EU-West-1` while the closest geographic location to here is `Asia Pacific (Mumbai)`

```
Fetching regions
Calculating round trip for ec2.ap-south-1.amazonaws.com
Calculating round trip for ec2.eu-west-3.amazonaws.com
Calculating round trip for ec2.eu-west-2.amazonaws.com
Calculating round trip for ec2.eu-west-1.amazonaws.com
Calculating round trip for ec2.ap-northeast-2.amazonaws.com
Calculating round trip for ec2.ap-northeast-1.amazonaws.com
Calculating round trip for ec2.sa-east-1.amazonaws.com
Calculating round trip for ec2.ca-central-1.amazonaws.com
Calculating round trip for ec2.ap-southeast-1.amazonaws.com
Calculating round trip for ec2.ap-southeast-2.amazonaws.com
Calculating round trip for ec2.eu-central-1.amazonaws.com
Calculating round trip for ec2.us-east-1.amazonaws.com
Calculating round trip for ec2.us-east-2.amazonaws.com
Calculating round trip for ec2.us-west-1.amazonaws.com
Calculating round trip for ec2.us-west-2.amazonaws.com
[   (u'eu-central-1', 100.532),
    (u'eu-west-1', 113.736),
    (u'eu-west-2', 165.367),
    (u'eu-west-3', 167.845),
    (u'ca-central-1', 193.861),
    (u'us-east-2', 249.249),
    (u'us-east-1', 304.829),
    (u'us-west-1', 321.09),
    (u'us-west-2', 326.586),
    (u'ap-south-1', 327.82),
    (u'ap-southeast-1', 349.339),
    (u'ap-northeast-2', 404.092),
    (u'ap-southeast-2', 465.684),
    (u'ap-northeast-1', 470.601),
    (u'sa-east-1', 501.489)]
```

# Geographic map of AWS servers

![alt text](https://d1.awsstatic.com/global-infrastructure/maps/Global_Infrastructure_about-aws_12.6.17.8047dae94d37855413251eafdf0809cf78ea65a6.png)
