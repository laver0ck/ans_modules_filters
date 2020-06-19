#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
from glob import glob
import re


def parse_profiles(path):
    profiles = glob(path + '/.profile*')
    oracle_homes = set()
    for profile in profiles:
        with open(profile, 'r') as profile_contents:
            contents = profile_contents.read()
            target = re.search("ORACLE_HOME=.*\\d", contents)
            if target:
                oracle_homes.add(target.group().lstrip('ORACLE_HOME='))

    return list(oracle_homes)


def main():
    fields = {
        "home_path": {
            "required": False,
            "type": "str",
            "default": "/home/oracle"
        }
    }
    module = AnsibleModule(argument_spec=fields)
    try:
        module.exit_json(changed=False,
                         homelist=parse_profiles(module.params["home_path"]))
    except Exception as e:
        module.fail_json(msg=e)


if __name__ == "__main__":
    main()
