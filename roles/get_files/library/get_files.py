#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
from glob import glob


def get_conf_files(path, mask):
    result = glob(path + mask)
    return '\n'.join(result)


def main():
    fields = {
        "path": {
            "required": True,
            "type": "str"
        },
        "mask": {
            "required": True,
            "type": "str"
        }
    }
    module = AnsibleModule(argument_spec=fields)

    try:
        module.exit_json(changed=False,
                         files=get_conf_files(module.params["path"],
                                              module.params["mask"]))
    except Exception as e:
        module.fail_json(msg=e)


if __name__ == "__main__":
    main()
