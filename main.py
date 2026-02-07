<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>Play AI Store</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #f5f5f5;
    }

    header {
      background: #111;
      color: white;
      padding: 15px;
      text-align: center;
    }

    nav {
      display: flex;
      justify-content: space-around;
      background: #222;
      padding: 10px;
    }

    nav a {
      color: white;
      text-decoration: none;
      font-weight: bold;
    }

    nav a:hover {
      color: #00e0ff;
    }

    .container {
      padding: 20px;
    }

    .hero {
      background: linear-gradient(to left, #000, #333);
      color: white;
      padding: 40px;
      border-radius: 10px;
      text-align: center;
    }

    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
      margin-top: 30px;
    }

    .product {
      background: white;
      padding: 15px;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .product button {
      margin-top: 10px;
      padding: 8px 15px;
      border: none;
      background: #00bcd4;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }

    .support {
      margin-top: 40px;
      background: white;
      padding: 20px;
      border-radius: 10px;
    }

    footer {
      margin-top: 40px;
      background: #111;
      color: white;
      text-align: center;
      padding: 15px;
    }

    .whatsapp {
      position: fixed;
      bottom: 20px;
      left: 20px;
      background: #25D366;
      color: white;
      padding: 12px 16px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: bold;
    }
  </style>
</head>

<body>

<header>
  <h1>Play AI Store</h1>
  <p>منصة منتجات رقمية وخدمة عملاء ذكية</p>
</header>

<nav>
  <a href="#">الرئيسية</a>
  <a href="#products">المنتجات</a>
  <a href="#support">خدمة العملاء</a>
</nav>

<div class="container">

  <div class="hero">
    <h2>أهلاً بك 👋</h2>
    <p>أفضل المنتجات الرقمية + دعم سريع عبر Play AI</p>
  </div>

  <section id="products">
    <h2>🛒 المنتجات</h2>

    <div class="products">
      <div class="product">
        <h3>اشتراك Play AI</h3>
        <p>دعم ذكي 24/7</p>
        <button onclick="alert('تم الطلب بنجاح')">شراء</button>
      </div>

      <div class="product">
        <h3>تصميم موقع</h3>
        <p>موقع احترافي سريع</p>
        <button>شراء</button>
      </div>

      <div class="product">
        <h3>بوت خدمة عملاء</h3>
        <p>رد تلقائي ذكي</p>
        <button>شراء</button>
      </div>
    </div>
  </section>

  <section id="support" class="support">
    <h2>🎧 خدمة العملاء</h2>
    <p>تواصل معنا في أي وقت، فريق Play AI جاهز لخدمتك</p>
    <button onclick="openChat()">بدء محادثة</button>
    <p id="chatBox"></p>
  </section>

</div>

<footer>
  © 2026 Play AI - جميع الحقوق محفوظة
</footer>

<a class="whatsapp" href="https://wa.me/97300000000" target="_blank">
  واتساب 💬
</a>

<script>
  function openChat() {
    document.getElementById("chatBox").innerHTML =
      "🤖 مرحباً! أنا Play AI، كيف أقدر أساعدك؟";
  }
</script>

</body>
</html>