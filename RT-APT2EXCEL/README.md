# RedTeam - APT Group JSON file to EXCEL
Script takes MITRE ATT&CK APT Group JSON file as input and generate Excel file with Tactic, Techniques, Procedure mappings

## Pre-requisite:
* pip install -r requirements.txt

## Execution:
* Navigate to any [APT Group Page](https://attack.mitre.org/groups/G0096/)
* Click on Att&ck Navigator Layer - [view](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0096%2FG0096-enterprise-layer.json)
* In Layer Control, click 'download layer as json'
* Pass that JSON file as input to the script
* python main.py -i APT38.json

## Output
* Excel File

![Excel Output](https://repository-images.githubusercontent.com/262632359/2c7d5a00-9246-11ea-8cd8-a1d21019d54f)