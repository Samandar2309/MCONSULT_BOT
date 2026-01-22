import os
from dotenv import load_dotenv

# =====================================================
# 🔐 .env YUKLASH
# =====================================================
load_dotenv()


# =====================================================
# 🤖 BOT SOZLAMALARI
# =====================================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN topilmadi (.env faylni tekshiring)")


# =====================================================
# 👑 ADMIN / OPERATOR SOZLAMALARI
# =====================================================
ADMIN_ID = int(os.getenv("ADMIN_ID", "5784897634"))
OPERATOR_GROUP_ID = int(os.getenv("OPERATOR_GROUP_ID", "-1003633229619"))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:12345678@localhost:5432/mc_mchj")
# =====================================================
# 📞 KONTAKT MA’LUMOTLAR
# =====================================================
PHONE = os.getenv("PHONE", "+998947077178")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "@MC_MCHJ")

INSTAGRAM = os.getenv(
    "INSTAGRAM",
    "https://www.instagram.com/jumabayev_samandar"
)
WEBSITE = os.getenv(
    "WEBSITE",
    "https://www.instagram.com/jumabayev_samandar"
)


# =====================================================
# 📍 GEOLOKATSIYA
# =====================================================
LOCATION_LAT = float(os.getenv("LOCATION_LAT", "41.203921"))
LOCATION_LON = float(os.getenv("LOCATION_LON", "69.236953"))
