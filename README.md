<style>
    /* Navbar */
    nav {
        background: rgba(0, 0, 0, 0.8);
        padding: 15px 20px;
        position: sticky;
        top: 0;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    nav h1 {
        font-size: 24px;
        background: linear-gradient(to right, red, purple);
        -webkit-background-clip: text;
        color: transparent;
    }

    .nav-links {
        display: flex;
        gap: 15px;
    }

    .nav-links a {
        color: white;
        text-decoration: none;
        padding: 10px 15px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 5px;
        transition: 0.3s;
    }

    .nav-links a:hover {
        background: rgba(255, 255, 255, 0.5);
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 50px 20px;
    }

    .hero h1 {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 20px;
        opacity: 0.8;
    }

    .hero a {
        display: inline-block;
        margin-top: 20px;
        padding: 10px 20px;
        background: purple;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: 0.3s;
    }

    .hero a:hover {
        background: darkviolet;
    }

    /* Products */
    .products {
        padding: 50px 20px;
        text-align: center;
    }

    .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
    }

    .product {
        background: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }

    .product img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }

    .product h3 {
        margin-top: 10px;
    }

    .buy-button {
        display: inline-block;
        margin-top: 10px;
        padding: 10px 15px;
        background: green;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: 0.3s;
    }

    .buy-button:hover {
        background: darkgreen;
    }

    /* Contact Form */
    .contact {
        text-align: center;
        padding: 50px 20px;
    }

    .contact form {
        max-width: 400px;
        margin: auto;
    }

    .contact input,
    .contact textarea {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: none;
    }

    .contact button {
        background: purple;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        transition: 0.3s;
        cursor: pointer;
    }

    .contact button:hover {
        background: darkviolet;
    }

    /* Footer */
    footer {
        text-align: center;
        background: rgba(0, 0, 0, 0.8);
        padding: 20px;
        margin-top: 20px;
    }
</style>

<!-- ✅ Redmi Note 11T added below -->
<div class="product-grid">
    <div class="product">
        <img src="https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-11t-5g-1.jpg" alt="Redmi Note 11T">
        <h3>Redmi Note 11T 5G</h3>
        <p>Powerful Dimensity processor, 5G connectivity, 6.6&quot; FHD+ display, and 5000mAh battery.</p>
        <h4>Price: ₹13,000</h4>
        <a href="#" class="buy-button">Buy Now</a>
    </div>
</div>
