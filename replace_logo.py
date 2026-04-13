import os
import glob
import re

old_logo_html = r"""        <div>
          <div class="logo-text"><span>&</span>Criativa</div>
          <span class="logo-sub">Soluções Contábeis</span>
        </div>"""

old_logo_html_footer = r"""            <div>
              <div class="logo-text"><span>&</span>Criativa</div>
              <span class="logo-sub">Soluções Contábeis</span>
            </div>"""

new_logo_html = r"""        <img src="img/LOGOMARCA RECORTADA (1).png" alt="Criativa Soluções Contábeis" class="site-logo">"""
new_logo_html_footer = r"""            <img src="img/LOGOMARCA RECORTADA (1).png" alt="Criativa Soluções Contábeis" class="site-logo">"""

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(old_logo_html, new_logo_html)
    content = content.replace(old_logo_html_footer, new_logo_html_footer)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Logo replaced in all HTML files.")
