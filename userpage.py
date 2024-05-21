#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.2.0/fonts/remixicon.css" rel="stylesheet" />
    <title>M500</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap");

        :root {
            --primary-color: #f1faff;
            --text-dark: #030712;
            --text-light: #6b7280;
            --extra-light: #fbfbfb;
            --white: #ffffff;
            --max-width: 1200px;
        }

        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }

        .section__container {
            max-width: var(--max-width);
            margin: auto;
            padding: 5rem 1rem;
        }



        .section__title {
            padding-bottom: 0.5rem;
            margin-bottom: 4rem;
            text-align: center;
            font-size: 2rem;
            font-weight: 600;
            color: var(--text-dark);
            position: relative;
        }

        .section__title::after {
            content: "";
            position: absolute;
            left: 50%;
            bottom: 0;
            transform: translateX(-50%);
            height: 3px;
            width: 75px;
            background-color: var(--text-dark);
        }

        .btn {
            padding: 0.75rem 2rem;
            font-size: 0.8rem;
            outline: none;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }

        a {
            text-decoration: none;
        }

        img {
            width: 100%;
            display: block;
        }

        body {
            font-family: "Montserrat", sans-serif;
        }

        .header__bar {
            padding: 0.5rem;
            font-size: 0.8rem;
            text-align: center;
            background-color: var(--text-dark);
            color: var(--white);
        }

        .nav__container {
            padding: 2rem 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .nav__logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-dark);
        }

        .nav__links {
            list-style: none;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .link a {
            padding: 0 0.5rem;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-light);
            transition: 0.3s;
        }

        .link a:hover {
            color: var(--text-dark);
        }

        .nav__icons {
            display: flex;
            gap: 1rem;
        }

        .nav__icons span {
            font-size: 1.25rem;
            cursor: pointer;
        }

        header {
            margin-top: 10rem;
            background-color: var(--primary-color);
        }

        .header__container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
        }

        .header__content p {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-light);
            margin-bottom: 0.5rem;
        }

        .header__content h1 {
            font-size: 3rem;
            font-weight: 400;
            margin-bottom: 2rem;
            color: var(--text-dark);
        }

        .header__content .btn {
            background-color: var(--text-dark);
            color: var(--white);
        }

        .header__image {
            position: relative;
        }

        .header__image img {
            max-width: 400px;
            position: absolute;
            bottom: -5rem;
        }

        .collection__container {
            position: relative;
        }

        .collection__container img {
            max-width: 400px;
            margin: auto;
        }

        .collection__content {
            position: absolute;
            top: 50%;
            left: 2rem;
            transform: translateY(-50%);
        }

        .collection__content .section__title {
            margin-bottom: 2rem;
        }

        .collection__content p {
            font-size: 0.9rem;
            color: var(--text-light);
            margin-bottom: 0.5rem;
        }

        .collection__content h4 {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .collection__content .btn {
            border: 1px solid var(--text-dark);
            color: var(--text-dark);
            background-color: var(--white);
        }

        .collection__content .btn:hover {
            background-color: var(--text-dark);
            color: var(--white);
        }

        .sale__grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }

        .sale__card {
            position: relative;
            overflow: hidden;
        }

        .sale__content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            color: var(--white);
            text-align: center;
        }

        .sale__title {
            font-size: 2rem;
            font-weight: 600;
        }

        .sale__title span {
            font-size: 2.5rem;
        }

        .sale__subtitle {
            font-size: 1rem;
        }

        .sale__btn {
            margin-top: 2rem;
            color: var(--white);
            background-color: var(--text-dark);
        }

        .sale__card::before {
            position: absolute;
            content: "";
            height: 100%;
            width: 100%;
            top: -100%;
            left: 0;
            background-color: rgba(0, 0, 0, 0.5);
            transition: 0.5s;
        }

        .sale__card:hover::before {
            top: 0;
        }

        .sale__card:hover .sale__btn {
            color: var(--text-dark);
            background-color: var(--white);
        }

        .musthave__nav {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }

        .musthave__nav a {
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-light);
            transition: 0.3s;
        }

        .musthave__nav a:hover {
            color: var(--text-dark);
        }

        .musthave__grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
        }

        .musthave__card {
            display: grid;
            gap: 0.5rem;
            color: var(--text-dark);
        }

        .musthave__card h4 {
            font-size: 1rem;
            font-weight: 600;
        }

        .musthave__card p {
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }

        .musthave__card p del {
            font-weight: 400;
            color: var(--text-light);
        }

        .news {
            background-color: var(--extra-light);
        }

        .news__grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }

        .news__details {
            padding: 1rem;
            display: grid;
            gap: 1rem;
            text-align: center;
        }

        .news__details p {
            font-size: 0.8rem;
            color: var(--text-light);
        }

        .news__details p i {
            font-size: 0.5rem;
            color: var(--text-light);
            padding: 0.5rem;
        }

        .news__details p span {
            font-weight: 600;
        }

        .news__details h4 {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-dark);
        }

        .news__details a i {
            font-size: 1.2rem;
            color: var(--text-light);
            transition: 0.3s;
        }

        .news__details a:hover i {
            color: var(--text-dark);
        }

        .brands__container {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 2rem;
        }

        .brand__image {
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.5;
            cursor: pointer;
            transition: 0.3s;
        }

        .brand__image img {
            max-width: 120px;
        }

        .brand__image:hover {
            opacity: 1;
        }

        .footer__container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
        }

        .footer__heading {
            color: var(--text-light);
            font-size: 1rem;
            font-weight: 600;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
            position: relative;
        }

        .footer__heading::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: 0;
            height: 2px;
            width: 50px;
            background-color: var(--text-light);
        }

        .footer__col p {
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 1rem;
            color: var(--text-light);
            cursor: pointer;
            transition: 0.3s;
        }

        .footer__col p:hover {
            color: var(--text-dark);
        }

        .footer__col p i {
            font-size: 1rem;
            margin-right: 0.5rem;
        }

        .instagram__grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
        }

        .footer__bar {
            padding: 2rem 1rem;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            align-items: center;
            gap: 2rem;
        }

        .copyright {
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--text-light);
        }

        .footer__form {
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }

        .footer__form form {
            width: 100%;
            max-width: 400px;
            display: flex;
            align-items: center;
        }

        .footer__form input {
            width: 100%;
            padding: 0.75rem 1rem;
            outline: none;
            border: none;
            border-bottom: 1px solid var(--text-dark);
            font-size: 0.8rem;
        }

        .footer__form .btn {
            background-color: var(--text-dark);
            color: var(--white);
        }

        @media (width < 900px) {
            header {
                margin-top: 5rem;
            }

            .sale__grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .musthave__grid {
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
            }

            .news__grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .brands__container {
                grid-template-columns: repeat(3, 1fr);
            }

            .instagram__grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .footer__bar {
                grid-template-columns: repeat(1, 1fr);
            }

            .copyright {
                text-align: center;
            }

            .footer__form {
                justify-content: center;
            }
        }

        @media (width < 600px) {
            .nav__links {
                display: none;
            }

            header {
                margin-top: 0;
            }

            .header__container {
                grid-template-columns: repeat(1, 1fr);
            }

            .header__image {
                display: none;
            }

            .sale__grid {
                grid-template-columns: repeat(1, 1fr);
            }

            .musthave__grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .news__grid {
                grid-template-columns: repeat(1, 1fr);
            }

            .brands__container {
                grid-template-columns: repeat(2, 1fr);
            }

            .footer__container {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>

<body>
    <div class="header__bar">Free Shipping on Orders Over Rs.1000</div>
    <nav class="section__container nav__container">
        <a href="#" class="nav__logo">ZUDIO</a>
        <ul class="nav__links">
            <li class="link"><a href="./userpage.py">HOME</a></li>
            <li class="link"><a href="./shop.py">SHOP</a></li>
            <!-- <li class="link"><a href="#">PAGES</a></li>
            <li class="link"><a href="#">BLOG</a></li>
            <li class="link"><a href="#">LOOKBOOK</a></li> -->
        </ul>
        <div class="nav__icons">
            <span><i class="ri-shield-user-line"></i></span>
            <span><i class="ri-search-line"></i></span>
            <span><i class="ri-shopping-bag-2-line"></i></span>
        </div>
    </nav>

    <header>
        <div class="section__container header__container">
            <div class="header__content">
                <p>EXTRA 55% OFF IN SPRING SALE</p>
                <h1>Discover & Shop<br />The Trend</h1>
                <button class="btn">SHOP NOW</button>
            </div>
            <div class="header__image">
                <img src="assets/header.png" alt="header" />
            </div>
        </div>
    </header>

    <section class="section__container collection__container">
        <img src="assets/collection.jpg" alt="collection" />
        <div class="collection__content">
            <h2 class="section__title">New Collection</h2>
            <p>#35 ITEMS</p>
            <h4>Available on Store</h4>
            <button class="btn"><a href="./shop.py">SHOP NOW</a></button>
        </div>
    </section>

    <section class="section__container sale__container">
        <h2 class="section__title">On Sale</h2>
        <div class="sale__grid">
            <div class="sale__card">
                <img src="assets/sale-1.jpg" alt="sale" />
                <div class="sale__content">
                    <p class="sale__subtitle">MAN OUTERWEAR</p>
                    <h4 class="sale__title">sale <span>40%</span> off</h4>
                    <p class="sale__subtitle">- DON'T MISS -</p>
                    <button class="btn sale__btn"><a href="./shop.py">SHOP NOW</a></button>
                </div>
            </div>
            <div class="sale__card">
                <img src="assets/sale-2.jpg" alt="sale" />
                <div class="sale__content">
                    <p class="sale__subtitle">WOMAN T-SHIRT</p>
                    <h4 class="sale__title">sale <span>25%</span> off</h4>
                    <p class="sale__subtitle">- DON'T MISS -</p>
                    <button class="btn sale__btn"><a href="./shop.py">SHOP NOW</a></button>
                </div>
            </div>
            <div class="sale__card">
                <img src="assets/sale-3.jpg" alt="sale" />
                <div class="sale__content">
                    <p class="sale__subtitle">JACKETS</p>
                    <h4 class="sale__title">sale <span>20%</span> off</h4>
                    <p class="sale__subtitle">- DON'T MISS -</p>
                    <button class="btn sale__btn"><a href="./shop.py">SHOP NOW</a></button>
                </div>
            </div>
        </div>
    </section>

    <section class="section__container musthave__container">
        <h2 class="section__title">Featured Collection</h2>
        <!-- <div class="musthave__nav">
            <a href="#">ALL</a>
            <a href="#">MAN</a>
            <a href="#">WOMEN</a>
            <a href="#">BAG</a>
            <a href="#">SHOES</a>
        </div> -->
        <div class="musthave__grid">
            <div class="musthave__card">
                <img src="assets/musthave-1.png" alt="must have" />
                <h4>Basic long sleeve T-shirt</h4>
                <p><del>Rs.1299</del> Rs.699</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-2.png" alt="must have" />
                <h4>Ribbed T-shirt with buttons</h4>
                <p><del>Rs.1199</del> Rs.699</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-3.png" alt="must have" />
                <h4>Jacket withside strips</h4>
                <p><del>Rs.1099</del> Rs.549</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-4.png" alt="must have" />
                <h4>High-heel tubular sandals</h4>
                <p><del>Rs.999</del> Rs.499</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-5.png" alt="must have" />
                <h4>Coral fabric belt bag</h4>
                <p><del>Rs.777</del> Rs.477</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-6.png" alt="must have" />
                <h4>Piggy skater slogan T-shirt</h4>
                <p><del>Rs.999</del> Rs.666</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-7.png" alt="must have" />
                <h4>White platform boots</h4>
                <p><del>Rs.777</del> Rs.555</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-8.png" alt="must have" />
                <h4>Sweater vest with sleeves</h4>
                <p><del>Rs.399</del> Rs.567</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-9.png" alt="must have" />
                <h4>Slim fit pants</h4>
                <p><del>Rs.899</del> Rs.519</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-10.png" alt="must have" />
                <h4>Gray backpack</h4>
                <p><del>Rs.666</del> Rs.599</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-11.png" alt="must have" />
                <h4>Neon sweatshirt</h4>
                <p><del>Rs.699</del> Rs.550</p>
            </div>
            <div class="musthave__card">
                <img src="assets/musthave-12.png" alt="must have" />
                <h4>Hooded nautical jacket</h4>
                <p><del>Rs.777</del> Rs.500</p>
            </div>
        </div>
    </section>

    <section class="news">
        <div class="section__container news__container">
            <h2 class="section__title">Latest News</h2>
            <div class="news__grid">
                <div class="news__card">
                    <img src="assets/news-1.jpg" alt="news" />
                    <div class="news__details">
                        <p>
                            FASHION <i class="ri-checkbox-blank-circle-fill"></i>
                            <span>JAMES SIMSON</span>
                            <i class="ri-checkbox-blank-circle-fill"></i> FEB 2, 2019
                        </p>
                        <h4>Seasonal Trends</h4>
                        <hr />
                        <p>
                            Discuss the latest fashion trends for the current season and
                            offer tips and ideas on how to incorporate these trends into
                            your wardrobe.
                        </p>
                        <a href="#"><i class="ri-arrow-right-line"></i></a>
                    </div>
                </div>
                <div class="news__card">
                    <img src="assets/news-2.jpg" alt="news" />
                    <div class="news__details">
                        <p>
                            TRENDS <i class="ri-checkbox-blank-circle-fill"></i>
                            <span>JAMES SIMSON</span>
                            <i class="ri-checkbox-blank-circle-fill"></i> APR 15, 2019
                        </p>
                        <h4>Fashion Tips and Advice</h4>
                        <hr />
                        <p>
                            Provide your readers with practical tips and advice on how to
                            dress for different occasions, body types, or style preferences.
                        </p>
                        <a href="#"><i class="ri-arrow-right-line"></i></a>
                    </div>
                </div>
                <div class="news__card">
                    <img src="assets/news-3.jpg" alt="news" />
                    <div class="news__details">
                        <p>
                            STYLE <i class="ri-checkbox-blank-circle-fill"></i>
                            <span>JAMES SIMSON</span>
                            <i class="ri-checkbox-blank-circle-fill"></i> JUL 22, 2019
                        </p>
                        <h4>Sustainable Fashion</h4>
                        <hr />
                        <p>
                            Cover the growing trend of eco-conscious fashion and explore the
                            various ways to be sustainable in your fashion choices.
                        </p>
                        <a href="#"><i class="ri-arrow-right-line"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section__container brands__container">
        <div class="brand__image">
            <img src="assets/brand-1.png" alt="brand" />
        </div>
        <div class="brand__image">
            <img src="assets/brand-2.png" alt="brand" />
        </div>
        <div class="brand__image">
            <img src="assets/brand-3.png" alt="brand" />
        </div>
        <div class="brand__image">
            <img src="assets/brand-4.png" alt="brand" />
        </div>
        <div class="brand__image">
            <img src="assets/brand-5.png" alt="brand" />
        </div>
        <div class="brand__image">
            <img src="assets/brand-6.png" alt="brand" />
        </div>
    </section>

    <hr />

    <footer class="section__container footer__container">
        <div class="footer__col">
            <h4 class="footer__heading">CONTACT INFO</h4>
            <p>
                <i class="ri-map-pin-2-fill"></i> Cross cut road,Gandhipuram,Coimbatore.
            </p>
            <p><i class="ri-mail-fill"></i> support@zudio.com</p>
            <p><i class="ri-phone-fill"></i> +91 8940208302</p>
        </div>
        <div class="footer__col">
            <h4 class="footer__heading">COMPANY</h4>
            <p>Home</p>
            <p>About Us</p>
            <p>Work With Us</p>
            <p>Our Blog</p>
            <p>Terms & Conditions</p>
        </div>
        <div class="footer__col">
            <h4 class="footer__heading">USEFUL LINK</h4>
            <p>Help</p>
            <p>Track My Order</p>
            <p>Men</p>
            <p>Women</p>
            <p>Shoes</p>
        </div>
        <div class="footer__col">
            <h4 class="footer__heading">INSTAGRAM</h4>
            <div class="instagram__grid">
                <img src="assets/instagram-1.jpg" alt="instagram" />
                <img src="assets/instagram-2.jpg" alt="instagram" />
                <img src="assets/instagram-3.jpg" alt="instagram" />
                <img src="assets/instagram-4.jpg" alt="instagram" />
                <img src="assets/instagram-5.jpg" alt="instagram" />
                <img src="assets/instagram-6.jpg" alt="instagram" />
            </div>
        </div>
    </footer>

    <hr />

    <div class="section__container footer__bar">
        <div class="copyright">
            Copyright © 2023 Web Design Mastery. All rights reserved.
        </div>
        <div class="footer__form">
            <form>
                <input type="text" placeholder="ENTER YOUR EMAIL" />
                <button class="btn" type="submit">SUBSCRIBE</button>
            </form>
        </div>
    </div>
</body>

</html>
""")