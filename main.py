from fastapi import FastAPI
from supabase import create_client, Client

url: str = "https://stflqvzixivnkqiwcojd.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN0ZmxxdnppeGl2bmtxaXdjb2pkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMjU3NTUyOCwiZXhwIjoyMDE4MTUxNTI4fQ.9JKGGJd98NExPc8sqmrdMgObkRbCz09CQP_zJTjdvW0"
supabase: Client = create_client(url, key)
print(supabase)

app = FastAPI()


@app.get("/")
async def root():
    resp = supabase.table('users').select("*").execute()
    data = resp.data[0]
    return data

