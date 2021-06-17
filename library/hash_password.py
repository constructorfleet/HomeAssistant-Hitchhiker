#!/usr/bin/python
from ansible.module_utils._text import to_native

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: hash_password

short_description: Salt and hash password using bcrypt

version_added: "2.9"

description:
    - Thie module accepts a password argument and hashes with with a generated salt.

options:
    password:
        description:
            - The raw password to be salted/hased
        required: true

author:
    - Teagan Glenn (@Teagn42)
'''

EXAMPLES = '''
- name: Salt and Hash Password
  hash_password:
    password: my_password
  register: password_hash
'''

RETURN = '''
hashed_password:
    description: The salt and hashed password
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import base64
import bcrypt


def run_module():
    module_args = dict(
        password=dict(
            type='str',
            required=True,
            no_log=True
        ),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    password = module.params['password']
    if not password:
        module.fail_json(
            msg=to_native("You must provide a valid, non-empty value for password")
        )

    encoded_password = None
    hashed_password = None
    try:
        encoded_password = password.encode()
    except UnicodeEncodeError:
        module.fail_json(
            msg=to_native("The provided password must not contain unicode characters")
        )

    try:
        hashed_password = bcrypt.hashpw(
            encoded_password,
            bcrypt.gensalt(rounds=12)
        )
    except TypeError or ValueError:
        module.fail_json(
            msg=to_native("There was an error salting and hashing the password")
        )

    module.exit_json(**dict(
        changed=True,
        hashed_pw=base64.b64encode(hashed_password)
    ))


def main():
    run_module()


if __name__ == '__main__':
    main()