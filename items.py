
files = {}

for interface, config in node.metadata.get('interfaces', {}).items():
    mac = config.get('mac', None)
    if mac is not None:
        content = [
            '[Match]',
            'MACAddress={}'.format(mac),
            '[Link]',
            'Name={}'.format(interface),
        ]
        files['/etc/systemd/network/10-interface_{}.link'.format(mac.replace(':', '_'))] = {
            'content': '\n'.join(content) + '\n',
            'content_type': 'text',
            'owner': "root",
            'group': "root",
            'mode': "0644",
            'triggers': ["action:interfaces_update_initramfs"],
        }

actions = {
    'interfaces_update_initramfs': {
        'command': "update-initramfs -u",
        'triggered': True,
    }
}
