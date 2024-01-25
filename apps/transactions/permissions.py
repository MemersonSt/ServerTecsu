from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Transaction

def create_transaction_permission():
    content_type = ContentType.objects.get_for_model(Transaction)

    if not Permission.objects.filter(codename='add_transaction').exists():
        Permission.objects.create(
            codename='add_transaction',
            name='Can add transaction',
            content_type=content_type,
        )

    if not Permission.objects.filter(codename='delete_transaction').exists():
        Permission.objects.create(
            codename='delete_transaction',
            name='Can delete transaction',
            content_type=content_type,
        )

    if not Permission.objects.filter(codename='view_transaction').exists():
        Permission.objects.create(
            codename='view_transaction',
            name='Can view transaction',
            content_type=content_type,
        )

    if not Permission.objects.filter(codename='list_transaction').exists():
        Permission.objects.create(
            codename='list_transaction',
            name='Can list transaction',
            content_type=content_type,
        )

create_transaction_permission()





