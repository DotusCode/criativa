import re

with open("blog.html", "r", encoding="utf-8") as f:
    content = f.read()

new_content = r"""  <!-- Hero -->
  <section class="hero">
    <div class="hero-bg">
      <img src="img/8J1A3188.jpg" alt="Blog">
    </div>
    <div class="hero-content">
      <h1>Dicas dos Especialistas em Contabilidade</h1>
    </div>
  </section>

  <!-- Blog Content -->
  <section class="section">
    <div class="container" style="display: flex; gap: 40px; align-items: flex-start; flex-wrap: wrap;">
      
      <!-- Main Content -->
      <div style="flex: 1; min-width: 60%;">
        <h2 style="font-family: 'Poppins', sans-serif; font-size: 32px; font-weight: 700; color: var(--navy); margin-bottom: 30px;">Posts Recentes</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px;">
          <!-- Post 1 -->
          <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 200px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/IMG_3989 (1).jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 24px;">
              <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--red); margin-bottom: 12px; font-weight: 600;">
                <span><i class="far fa-user"></i> Criativa</span>
                <span><i class="far fa-calendar"></i> Janeiro 16, 2025</span>
              </div>
              <h3 style="font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">Expanda seu negócio com confiança!</h3>
              <p style="font-size: 14px; color: var(--gray-600); line-height: 1.6;">A contabilidade empresarial é mais do que cumprir obrigações fiscais, é estratégica para avaliar a saúde financeira, identificar oportunidades...</p>
            </div>
          </div>

          <!-- Post 2 -->
          <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 200px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/IMG_4043 (1).jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 24px;">
              <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--red); margin-bottom: 12px; font-weight: 600;">
                <span><i class="far fa-user"></i> Criativa</span>
                <span><i class="far fa-calendar"></i> Janeiro 15, 2025</span>
              </div>
              <h3 style="font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">MEI, a contribuição mensal foi ajustada. Saiba mais!</h3>
              <p style="font-size: 14px; color: var(--gray-600); line-height: 1.6;">E agora, o que mudou? Com o novo salário mínimo de R$ 1.518, o valor do DAS-MEI foi reajustado. Agora você vai pagar de R$ 76,60 a R$ 81,60...</p>
            </div>
          </div>
          
          <!-- Post 3 -->
          <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 200px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/IMG_4121 (1).jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 24px;">
              <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--red); margin-bottom: 12px; font-weight: 600;">
                <span><i class="far fa-user"></i> Criativa</span>
                <span><i class="far fa-calendar"></i> Agosto 15, 2024</span>
              </div>
              <h3 style="font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">Abra seu CNPJ conosco sem burocracia!</h3>
              <p style="font-size: 14px; color: var(--gray-600); line-height: 1.6;">Conheça a Contabilidade Online da Criativa Soluções Contábeis. Uma contabilidade PRÁTICA, ÁGIL e que CABE NO SEU BOLSO!...</p>
            </div>
          </div>
          
          <!-- Post 4 -->
          <div style="background: var(--white); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 200px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/8J1A3188.jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 24px;">
              <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--red); margin-bottom: 12px; font-weight: 600;">
                <span><i class="far fa-user"></i> Criativa</span>
                <span><i class="far fa-calendar"></i> Agosto 15, 2024</span>
              </div>
              <h3 style="font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">Você pode estar pagando mais impostos que deveria!</h3>
              <p style="font-size: 14px; color: var(--gray-600); line-height: 1.6;">Você é Profissional Liberal? VEJA ESTE VÍDEO! Você sabia que pode estar pagando mais impostos que deveria? A Contabilidade Criativa pode te ajudar...</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Sidebar -->
      <aside style="width: 320px; flex-shrink: 0;">
        <div style="display: flex; margin-bottom: 40px;">
          <input type="text" placeholder="Search..." style="flex: 1; padding: 12px 16px; border: 1px solid var(--gray-300); border-radius: 4px 0 0 4px; font-family: 'Inter', sans-serif; outline: none;">
          <button style="background: var(--red); color: white; border: none; padding: 0 20px; border-radius: 0 4px 4px 0; cursor: pointer;"><i class="fas fa-search"></i></button>
        </div>

        <h3 style="font-family: 'Poppins', sans-serif; font-size: 20px; font-weight: 700; color: var(--navy); margin-bottom: 20px;">Confira Nossos Outros Conteúdos</h3>
        
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <!-- Small Post 1 -->
          <div style="background: var(--white); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 120px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/IMG_4121 (1).jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 16px;">
              <div style="font-size: 11px; color: var(--red); margin-bottom: 8px; font-weight: 600;">
                <i class="far fa-calendar"></i> Agosto 15, 2024
              </div>
              <h4 style="font-size: 16px; font-weight: 700; color: var(--navy);">Você pode estar pagando mais impostos que deveria!</h4>
            </div>
          </div>
          
          <!-- Small Post 2 -->
          <div style="background: var(--white); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--gray-200);">
            <div style="height: 120px; background: #f3f4f6; display: flex; align-items: center; justify-content: center; overflow: hidden;">
              <img src="img/IMG_3989 (1).jpg" style="width: 100%; height: 100%; object-fit: cover;" alt="Post">
            </div>
            <div style="padding: 16px;">
              <div style="font-size: 11px; color: var(--red); margin-bottom: 8px; font-weight: 600;">
                <i class="far fa-calendar"></i> Agosto 15, 2024
              </div>
              <h4 style="font-size: 16px; font-weight: 700; color: var(--navy);">Você recebe vendas por meio de</h4>
            </div>
          </div>
        </div>
      </aside>

    </div>
  </section>"""

# Replace content between <!-- Hero --> and <!-- Footer -->
pattern = re.compile(r'<!-- Hero -->.*?<!-- Footer -->', re.DOTALL)
content = pattern.sub(new_content + "\n\n  <!-- Footer -->", content)

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(content)

print("blog.html updated.")
