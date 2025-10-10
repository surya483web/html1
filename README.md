 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Store</title>
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
            color: white;
        }
    </style>
</head>
<body>
    <nav>
        <h1>Mobile Store</h1>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#products">Products</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <section class="hero" id="home">
        <h1>Welcome to Mobile Store</h1>
        <p>Find the best smartphones at unbeatable prices!</p>
        <a href="#products">Shop Now</a>
    </section>

    <section class="products" id="products">
        <h2>Our Latest Mobiles</h2>
        <div class="product-grid">

            <!-- Existing products -->
            <div class="product">
                <img src="https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg" alt="iPhone 13">
                <h3>iPhone 13</h3>
                <p>Powerful A15 Bionic chip with stunning camera performance.</p>
                <h4>Price: ₹65,000</h4>
                <a href="#" class="buy-button">Buy Now</a>
            </div>

            <!-- New Redmi Note 11T product -->
            <div class="product">
                <img src="https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-11t-5g-1.jpg" alt="Redmi Note 11T">
                <h3>Redmi Note 11T 5G</h3>
                <p>Powerful Dimensity processor, 5G connectivity, 6.6" FHD+ display, and 5000mAh battery.</p>
                <h4>Price: ₹13,000</h4>
                <a href="#" class="buy-button">Buy Now</a>
            </div>

        </div>
    </section>

    <section class="contact" id="contact">
        <h2>Contact Us</h2>
        <form>
            <input type="text" placeholder="Your Name" required>
            <input type="email" placeholder="Your Email" required>
            <textarea rows="4" placeholder="Your Message"></textarea>
            <button type="submit">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2025 Mobile Store. All rights reserved.</p>
    </footer>
</body>
</html>
