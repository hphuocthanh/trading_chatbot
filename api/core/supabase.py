from .settings import settings
from supabase import Client, create_client


supabase: Client = create_client(settings.SUPABSASE_URL, settings.SUPABSASE_KEY)


def get_supabase():
    return supabase
