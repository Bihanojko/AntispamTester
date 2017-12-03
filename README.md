# AntispamTester
Python script for testing antispam functionality

Put AntispamTester.py to the same folder as antispam. E-mails, which are to be tested, should be put in a ./Tests subfolder like this:

- antispam
- AntispamTester
- ./Tests
    - ./[subfolder_name]
        - ./spam
            - spam e-mails
        - ./ham
            - ham e-mails
    - ./[subfolder2_name]
    ...


For running only selected subfolders, specify their names as AntispamTester.py arguments.

Large e-mail databases:
- https://labs-repos.iit.demokritos.gr/skel/i-config/downloads/enron-spam/preprocessed/
- http://spamassassin.apache.org/old/publiccorpus/
- http://artinvoice.hu/spams/
- http://untroubled.org/spam/
- https://www.kaggle.com/c/adcg-ss14-challenge-02-spam-mails-detection/data
- https://plg.uwaterloo.ca/~gvcormac/treccorpus07/
