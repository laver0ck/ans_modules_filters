#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule


def test_func(var):
    return f"this is {var}"


def main():
    fields = {
        "test": {
            "required": False,
            "type": "str",
            "default": "testtest"
        }
    }
    module = AnsibleModule(argument_spec=fields)

    try:
        module.exit_json(changed=False,
                         homelist=parse_profiles(module.params["test"]))
    except Exception as e:
        module.fail_json(msg=e)


if __name__ == "__main__":
    main()
