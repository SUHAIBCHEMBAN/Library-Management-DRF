from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Book,Author

@receiver(post_save, sender=Book)
@receiver(post_delete, sender=Book)
def clear_cache(sender, **kwargs):
    cache.delete('books_cache')
    print('Book`s Signel Is Worked')

@receiver(post_save, sender=Author)
@receiver(post_delete, sender=Author)
def clear_cache(sender,**kwargs):
    cache.delete('authors_cache')
    print('Author`s Signel Is Worked')