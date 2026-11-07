from flask import Flask, render_template, abort, redirect, url_for, request

app = Flask(__name__)

# Data simulasi akun pengguna
USERS = {
    "admin": {"nama": "Shavira Zakiya", "role": "Founder & Perfumer", "status": "Aktif"},
    "member01": {"nama": "Nadia Putri", "role": "VIP Collector", "status": "Aktif"},
    "member02": {"nama": "Rizky Pratama", "role": "Regular Member", "status": "Aktif"},
}

# Data katalog 8 produk parfum (Shopee Style)
PRODUCTS = {
    1: {
        "nama": "bohe sage green tea edp 35ml",
        "kategori": "Fresh & Green",
        "harga": "Rp 145.000",
        "harga_asli": "Rp 185.000",
        "diskon": "22%",
        "stok": 24,
        "rating": 4.9,
        "terjual": "1,2rb",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Perpaduan segar daun teh hijau pilihan, clary sage, dan sentuhan citrus lembut yang memberikan kesan bersih dan menenangkan sepanjang hari di kampus."
    },
    2: {
        "nama": "bohe faye floral musk edp 35ml",
        "kategori": "Soft Floral",
        "harga": "Rp 149.000",
        "harga_asli": "Rp 190.000",
        "diskon": "21%",
        "stok": 15,
        "rating": 4.8,
        "terjual": "850",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Aroma buket bunga putih elegan yang berpadu dengan powdery musk lembut, menciptakan aura feminin dan anggun."
    },
    3: {
        "nama": "saff & co. s.o.t.b extrait de parfum",
        "kategori": "Tropical Sweet",
        "harga": "Rp 199.000",
        "harga_asli": "Rp 249.000",
        "diskon": "20%",
        "stok": 32,
        "rating": 4.9,
        "terjual": "4,5rb",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Wangi eksotis mandarin orange, sweet floral, dan vanilla musk dengan projection kuat yang tahan hingga 8 jam."
    },
    4: {
        "nama": "saff & co. loui fresh fruity 30ml",
        "kategori": "Fresh Fruity",
        "harga": "Rp 185.000",
        "harga_asli": "Rp 225.000",
        "diskon": "18%",
        "stok": 19,
        "rating": 4.9,
        "terjual": "3,1rb",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Kombinasi verbena, green, dan aldehydic yang sangat segar seperti habis mandi, cocok untuk cuaca tropis yang terik."
    },
    5: {
        "nama": "kyoto uji matcha zen mist 50ml",
        "kategori": "Artisan Matcha",
        "harga": "Rp 210.000",
        "harga_asli": "Rp 260.000",
        "diskon": "19%",
        "stok": 9,
        "rating": 5.0,
        "terjual": "620",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Ekstrak teh hijau Uji Kyoto berpadu dengan white chocolate tipis dan cedarwood, menghadirkan ketenangan khas ruang teh Jepang."
    },
    6: {
        "nama": "octarine citrus bergamot breeze 50ml",
        "kategori": "Citrus Woody",
        "harga": "Rp 125.000",
        "harga_asli": "Rp 165.000",
        "diskon": "24%",
        "stok": 28,
        "rating": 4.7,
        "terjual": "1,8rb",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Semprotan pertama langsung memancarkan kesegaran jeruk bergamot Italia dan lemon zest yang membangkitkan semangat pagi."
    },
    7: {
        "nama": "velvet white jasmine & pear edp",
        "kategori": "Fruity Floral",
        "harga": "Rp 175.000",
        "harga_asli": "Rp 215.000",
        "diskon": "19%",
        "stok": 12,
        "rating": 4.8,
        "terjual": "940",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1563170351-be82bc888aa4?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Kesegaran buah pir matang yang manis segar dibalut kelopak bunga melati putih dan amber yang hangat."
    },
    8: {
        "nama": "white tea & ginger calming extrait",
        "kategori": "Aromatic Tea",
        "harga": "Rp 230.000",
        "harga_asli": "Rp 280.000",
        "diskon": "18%",
        "stok": 7,
        "rating": 4.9,
        "terjual": "510",
        "lokasi": "Kota Surabaya",
        "gambar": "https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=600&q=80",
        "deskripsi": "Aroma teh putih bersih dengan sentuhan rempah jahe hangat dan kardamom untuk kesan dewasa yang berkelas."
    }
}


# ==========================================
# 1. ROUTE STATIS
# ==========================================
@app.route("/")
def beranda():
    return render_template("beranda.html")

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


# ==========================================
# 2. LIST DATA & DETAIL PRODUK
# ==========================================
@app.route("/produk")
def list_produk():
    return render_template("produk.html", produk_list=PRODUCTS)

@app.route("/produk/<int:id>")
def detail_produk(id):
    if id not in PRODUCTS:
        abort(404)
    return render_template("detail_produk.html", id=id, produk=PRODUCTS[id])


# ==========================================
# 3. CEK USERNAME (3 KONDISI JINJA2)
# ==========================================
@app.route("/cek", methods=["GET"])
def form_cek():
    username = request.args.get("username", "").strip().lower()
    if not username:
        return render_template("cek.html", username="", valid=False, tersedia=False)
    
    valid = len(username) >= 4
    tersedia = valid and (username not in USERS)
    return render_template("cek.html", username=username, valid=valid, tersedia=tersedia)

@app.route("/cek/<username>")
def cek_langsung(username):
    username = username.strip().lower()
    valid = len(username) >= 4
    tersedia = valid and (username not in USERS)
    return render_template("cek.html", username=username, valid=valid, tersedia=tersedia)

@app.route("/user/<username>")
def profil_user(username):
    user = USERS.get(username.lower())
    if not user:
        abort(404)
    return render_template("profil.html", username=username, user=user)


# ==========================================
# 4. CUSTOM ERROR HANDLER 404
# ==========================================
@app.errorhandler(404)
def halaman_error_404(e):
    return render_template("404.html"), 404


# ==========================================
# MENJALANKAN SERVER (PORT 5001)
# ==========================================
if __name__ == "__main__":
    app.run(debug=True, port=5001)