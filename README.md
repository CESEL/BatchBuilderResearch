# Travis CI build batching

This repository contains the replication package for this paper: 

__Batching Builds and Modeling Change Risk during Testing on Travis Projects__

Mohammad Javad Beheshtian, Peter C. Rigby

<s_ehesht@encs.concordia.ca>, <peter.rigby@concordia.ca>

# Installation

## Requirements

* Python 3.5+


Install required modules using `pip`...

```
pip install -r requiremnts.txt
```

# Quick Start

```
python run.py
```


![Snapshot](https://github.com/CESEL/BatchBuilderResearch/raw/master/snapshot.png "Command line snapshot")

# Data

There is no need to download any additional data as it is included in this repository.

Build information are extracted from [TravisTorrent](https://travistorrent.testroots.org/) dataset for these projects:
* ruby/ruby
* rapid7/metasploit-framework
* Graylog2/graylog2-server
* owncloud/android
* mitchellh/vagrant
* gradle/gradle
* puppetlabs/puppet
* opal/opal
* rspec/rspec-core
