import glob

old_str = r"""        <div class="footer-brand">
          <div class="logo">
            <img src="img/LOGOMARCA RECORTADA (1).png" alt="Criativa Soluções Contábeis" class="site-logo">"""

new_str = r"""        <div class="footer-brand">
          <div class="logo">
            <img src="img/logo rodape.png" alt="Criativa Soluções Contábeis" class="site-logo">"""

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(old_str, new_str)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Footer logo replaced in all HTML files.")
