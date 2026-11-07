document.addEventListener("DOMContentLoaded", () => {
  const pageWrapper = document.getElementById("pageWrapper");

  // 1. Animasi Masuk Saat Halaman Dibuka
  if (pageWrapper) {
    requestAnimationFrame(() => {
      pageWrapper.classList.add("page-loaded");
    });
  }

  // 2. Tandai Menu Navbar yang Sedang Aktif
  const currentPath = window.location.pathname;
  document.querySelectorAll(".navbar-nav .nav-link").forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active-link");
    }
  });

  // 3. Efek Transisi Halus Saat Klik Menu Pindah Halaman
  document.querySelectorAll("a").forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetUrl = this.getAttribute("href");

      // Pastikan link internal dan bukan tab baru
      if (
        targetUrl &&
        targetUrl.startsWith("/") &&
        !targetUrl.startsWith("//") &&
        !this.hasAttribute("target") &&
        !e.ctrlKey &&
        !e.metaKey
      ) {
        e.preventDefault();
        if (pageWrapper) {
          pageWrapper.classList.remove("page-loaded");
          pageWrapper.classList.add("page-exit");
        }
        setTimeout(() => {
          window.location.href = targetUrl;
        }, 280);
      }
    });
  });

  // 4. Validasi Live Interaktif pada Input Username
  const usernameInput = document.getElementById("usernameInput");
  const liveFeedback = document.getElementById("liveFeedback");

  if (usernameInput && liveFeedback) {
    usernameInput.addEventListener("input", (e) => {
      const val = e.target.value.trim();

      if (val.length === 0) {
        liveFeedback.innerHTML = "";
        return;
      }

      if (val.length < 4) {
        liveFeedback.innerHTML = `
          <div class="d-inline-flex align-items-center gap-2 px-3 py-2 mt-2 rounded-3 bg-warning-subtle text-warning-emphasis border border-warning-subtle small fw-medium animate-item">
            <span>⚠️ Minimal 4 karakter (Saat ini: ${val.length} karakter)</span>
          </div>`;
      } else {
        liveFeedback.innerHTML = `
          <div class="d-inline-flex align-items-center gap-2 px-3 py-2 mt-2 rounded-3 bg-teal-subtle text-success border border-success-subtle small fw-medium animate-item">
            <span>✨ Format jumlah karakter valid (${val.length} karakter) — Klik tombol Periksa!</span>
          </div>`;
      }
    });
  }
});