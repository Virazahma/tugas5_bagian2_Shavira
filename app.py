from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)

# Simulasi data pengguna dan produk
USERS = {
    "admin": {"nama": "Administrator Toko", "role": "Admin", "status": "Aktif"},
    "pelanggan1": {"nama": "Budi Santoso", "role": "Member Gold", "status": "Aktif"},
    "pelanggan2": {"nama": "Siti Rahma", "role": "Member Silver", "status": "Non-Aktif"},
}

PRODUCTS = {
    1: {"nama": "Laptop Asus VivoBook", "harga": "Rp 8.500.000", "stok": 10},
    2: {"nama": "Mouse Wireless Logitech", "harga": "Rp 250.000", "stok": 25},
    3: {"nama": "Keyboard Mechanical RGB", "harga": "Rp 650.000", "stok": 5},
}


# ==========================================
# 1. MINIMAL 4 ROUTE STATIS
# ==========================================
@app.route("/")
def beranda():
    return """
    <h1>Selamat Datang di Portal Toko</h1>
    <p>Ini adalah halaman Beranda utama.</p>
    <ul>
        <li><a href="/tentang">Tentang Kami</a></li>
        <li><a href="/produk">Katalog Produk</a></li>
        <li><a href="/kontak">Kontak</a></li>
        <li><a href="/cek/admin">Cek User Admin</a></li>
    </ul>
    """

@app.route("/tentang")
def tentang():
    return "<h1>Tentang Kami</h1><p>Platform e-commerce dan manajemen pengguna berbasis Flask.</p><a href='/'>Kembali</a>"

@app.route("/produk")
def list_produk():
    items = "".join([f"<li>ID {pid}: {p['nama']} - {p['harga']} (<a href='/produk/{pid}'>Detail</a>)</li>" for pid, p in PRODUCTS.items()])
    return f"<h1>Daftar Produk</h1><ul>{items}</ul><a href='/'>Kembali</a>"

@app.route("/kontak")
def kontak():
    return "<h1>Hubungi Kami</h1><p>Email: support@tokoflask.com | WhatsApp: 08123456789</p><a href='/'>Kembali</a>"


# ==========================================
# 2 & 4. DYNAMIC ROUTE, VALIDASI, URL_FOR & REDIRECT
# ==========================================
@app.route("/cek/<username>")
def cek_username(username):
    # Validasi: Cek apakah username ada dalam daftar
    if username in USERS:
        # Jika terdaftar, redirect ke dynamic route /user/<username> menggunakan url_for
        return redirect(url_for("profil_user", username=username))
    else:
        # Jika tidak terdaftar, tampilkan pesan validasi gagal
        return f"<h3>Username <u>'{username}'</u> tidak ditemukan!</h3><p>Silakan periksa kembali nama pengguna.</p><a href='/'>Kembali</a>", 404

@app.route("/user/<username>")
def profil_user(username):
    user = USERS.get(username)
    if not user:
        abort(404)
    return f"""
    <h1>Profil Pengguna: {username}</h1>
    <p><b>Nama:</b> {user['nama']}</p>
    <p><b>Role:</b> {user['role']}</p>
    <p><b>Status:</b> {user['status']}</p>
    <a href='/'>Kembali ke Beranda</a>
    """


# ==========================================
# 3. ROUTE CONVERTER INT & ABORT(404)
# ==========================================
@app.route("/produk/<int:id>")
def detail_produk(id):
    # Validasi apakah id produk ada di dictionary
    if id not in PRODUCTS:
        # Jika tidak ada, panggil abort(404)
        abort(404)
    
    produk = PRODUCTS[id]
    return f"""
    <h1>Detail Produk (ID: {id})</h1>
    <p><b>Nama:</b> {produk['nama']}</p>
    <p><b>Harga:</b> {produk['harga']}</p>
    <p><b>Stok:</b> {produk['stok']} unit</p>
    <a href='/produk'>Kembali ke Daftar Produk</a>
    """


# ==========================================
# 5. CUSTOM HALAMAN ERROR 404
# ==========================================
@app.errorhandler(404)
def halaman_error_404(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)