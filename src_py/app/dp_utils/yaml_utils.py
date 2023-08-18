import yaml


def load_config(config):
    return yaml.safe_load(open(config))


if __name__ == '__main__':
    to_yaml = {
        'path': ['switchport mode access',
                 'switchport access vlan',
                 'switchport nonegotiate',
                 'spanning-tree portfast',
                 'spanning-tree bpduguard enable'],
        'trunk': ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan'],
    }

    with open('sw_templates.yaml', 'w') as f:
        yaml.dump(to_yaml, f)

    with open('sw_templates.yaml') as f:
        print(f.read())

    from pprint import pprint

    with open('info.yaml') as f:
        templates = yaml.safe_load(f)

    pprint(templates)
