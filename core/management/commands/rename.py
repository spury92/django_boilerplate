from django.core.management.base import BaseCommand

import os

class Command(BaseCommand):
    help = 'Command to rename a project'

    def add_arguments(self, parser):
        parser.add_argument(
            'new_name',
            type=str,
            help='new name for a project'
            )
    
    def handle(self, *args, **kwargs):
        new_name = kwargs['new_name']

        files_to_open = [
            'demo/settings/base.py',
            'demo/wsgi.py',
            'manage.py'
        ]
        folder_name = 'demo'
        for f in files_to_open:
            with open (f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('demo', new_name)

            with open (f, 'w') as file:
                file.write(filedata)

        os.rename(folder_name, new_name)

        self.stdout.write(
            self.style.SUCCESS('Project successfully renamed to {}'.format(new_name)))
