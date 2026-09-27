"""Screenshot live URLs + local Django/Next.js projects for Projek.in portfolio."""
import sys, os, time, subprocess

OUT = "C:/Users/cubeb/OneDrive/Documents/coding/projects/projekin-landing/assets/projects"

from playwright.sync_api import sync_playwright

def screenshot_url(pw, url, filename, wait_ms=4000, viewport=(1440, 900)):
    browser = pw.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": viewport[0], "height": viewport[1]}, device_scale_factor=2)
    page = ctx.new_page()
    try:
        page.goto(url, timeout=25000, wait_until="networkidle")
    except Exception:
        try:
            page.goto(url, timeout=15000, wait_until="load")
        except Exception as e:
            print(f"FAIL {filename}: {e}")
            browser.close()
            return False
    page.wait_for_timeout(wait_ms)
    path = os.path.join(OUT, filename)
    page.screenshot(path=path, full_page=False)
    print(f"OK: {path}")
    browser.close()
    return True

with sync_playwright() as pw:
    # 1. sim-akreditasi-django (live Railway)
    screenshot_url(pw, "https://sim-akreditasi-web-production.up.railway.app/", "sim-akreditasi.png", wait_ms=5000)

    # 2. Web-Weave (live Vercel staging)
    screenshot_url(pw, "https://web-weave-lake.vercel.app/", "web-weave.png", wait_ms=5000)

print("Done with live URLs.")
