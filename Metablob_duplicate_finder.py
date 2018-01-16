import json
import sys

from pprint import pprint

data = json.load(open('duplicates.json'))


def iterate(data):
    duplicates = []
    for index in range(len(data) - 1):
        val = data[index]
        for index2 in range(index + 1, len(data)):
            val2 = data[index2]
            if (val['Item']['RuleOptionCode'] == val2['Item']['RuleOptionCode']) and \
                    (val['Item']['VHCode'] == val2['Item']['VHCode']) and \
                    (val['Item']['RuleType'] == val2['Item']['RuleType']) and \
                    (val['Item']['MasterOptionCode'] == val2['Item']['MasterOptionCode']) and \
                    (val['Item']['PrimaryEnvCode'] == val2['Item']['PrimaryEnvCode']) and \
                    (val['Item']['MatchType'] == val2['Item']['MatchType']) and \
                    (val['Item']['Equator'] == val2['Item']['Equator']) and \
                    (val['Item']['SecondaryEnvCode'] == val2['Item']['SecondaryEnvCode']) and \
                    (val['Item']['AttributeValue'] == val2['Item']['AttributeValue']) and \
                    (val['Item']['Modifier'] == val2['Item']['Modifier']):
                duplicates.append(val)

    return duplicates


print('\n'.join(map(str, (iterate(data)))))
