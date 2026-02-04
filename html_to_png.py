#!/usr/bin/env python3
"""
Convert HTML infographic to PNG using Playwright
"""

from playwright.sync_api import sync_playwright
import os
import shutil
from pathlib import Path

def html_to_png(html_file, output_file, copy_to_downloads=True):
    """Convert HTML file to PNG screenshot"""

    # Get absolute paths
    html_path = os.path.abspath(html_file)
    output_path = os.path.abspath(output_file)

    print(f"Converting {html_path} to PNG...")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # Set viewport size for proper rendering
        page.set_viewport_size({"width": 1400, "height": 2400})

        # Navigate to the HTML file
        page.goto(f'file:///{html_path}')

        # Wait for the page to fully load
        page.wait_for_load_state('networkidle')

        # Take screenshot of the full page
        page.screenshot(path=output_path, full_page=True)

        browser.close()

    print(f"[SUCCESS] PNG created successfully: {output_path}")

    # Copy to Downloads folder
    if copy_to_downloads:
        downloads_path = Path.home() / "Downloads" / os.path.basename(output_file)
        shutil.copy2(output_path, downloads_path)
        print(f"[SUCCESS] Copy saved to Downloads: {downloads_path}")
        return output_path, downloads_path

    return output_path

if __name__ == "__main__":
    html_file = "architecture-infographic.html"
    output_file = "D365-Contact-Center-Architecture-Infographic.png"

    try:
        html_to_png(html_file, output_file, copy_to_downloads=True)
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
