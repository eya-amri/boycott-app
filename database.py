import sqlite3

DB = "database.db"


def get_db():
    return sqlite3.connect(DB)


def init_db():
    db = get_db()
    c = db.cursor()

    # ------------------ USERS ------------------
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """
    )

    # ------------------ LOCATIONS ------------------
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        alt_name TEXT
    )
    """
    )

    # ------------------ PRODUCTS ------------------
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        boycotted INTEGER,
        alternative TEXT
    )
    """
    )

    # ------------------ ADMIN ACCOUNT ------------------
    c.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin', 'admin')")

    # ------------------ 20 LIEUX ------------------
    lieux = [
        ("Carrefour", "Aziza"),
        ("KFC", "Quick"),
        ("Monoprix", "Leader Price"),
        ("Magasin Local", "Superette"),
        ("Géant", "Casino"),
        ("Auchan", "Carrefour"),
        ("Lidl", "Leader Price"),
        ("Marjane", "Aswak"),
        ("Hyper U", "Carrefour"),
        ("McDonald’s", "Burger King"),
        ("Pizza Hut", "Domino's"),
        ("Quick", "KFC"),
        ("Bazar", "Magasin Local"),
        ("Market", "Superette"),
        ("Supermarché", "Carrefour"),
        ("Foodland", "Superette"),
        ("Shop&Go", "Magasin Local"),
        ("E.Leclerc", "Auchan"),
        ("Alimentation", "Marché Local"),
        ("Grocery Store", "Superette"),
    ]

    for name, alt in lieux:
        c.execute(
            "INSERT OR IGNORE INTO locations (name, alt_name) VALUES (?, ?)",
            (name, alt),
        )

    # ------------------ 100 PRODUITS ------------------
    boycotted_products = [
        # Alimentation et boissons
        ("Coca Cola", "Boga"),
        ("Pepsi", "Fanta"),
        ("Fanta", "Sprite"),
        ("Schweppes", "Pepsi"),
        ("Red Bull", "Monster"),
        ("Lipton Ice Tea", "Nestea"),
        ("Nestea", "Arizona"),
        ("Arizona Tea", "Lipton Ice Tea"),
        ("Snapple", "Lipton Ice Tea"),
        # Produits laitiers
        ("Strauss Milk", "Delice"),
        ("Tnuva Cheese", "Kiri"),
        ("Sabra Hummus", "Haig's Hummus"),
        ("Tribe Hummus", "Local hummus"),
        ("Osem Yogurt", "Danone"),
        ("Carmel Cheese", "Delice"),
        ("Jaffa Oranges", "Local oranges"),
        ("King Solomon Dates", "Medjool Dates"),
        # Snacks et biscuits
        ("Oreo", "LU"),
        ("Nutella", "Chocapic Spread"),
        ("Kiri Cheese", "President"),
        ("Picon Drink", "Boga"),
        ("Kinder Chocolate", "Milka"),
        ("M&M's", "Smarties"),
        ("Lay's Chips", "Pringles"),
        ("Pringles", "Lay's"),
        ("Chipsy", "Lay's"),
        ("Bambino Juice", "Local juice"),
        # Produits de boulangerie
        ("Monoprix Bread", "Local bakery bread"),
        ("Carrefour Pastry", "Local bakery pastry"),
        ("Marjane Cake", "Local bakery cake"),
        ("Auchan Muffins", "Local muffins"),
        ("Lidl Croissant", "Local croissant"),
        # Cosmétiques
        ("Estée Lauder", "The Body Shop"),
        ("Clinique", "Bioderma"),
        ("MAC Cosmetics", "NYX"),
        ("Bobbi Brown", "NARS"),
        ("Aveda Shampoo", "Davines"),
        ("Origins Skincare", "L'Occitane"),
        ("Jo Malone", "Diptyque"),
        ("La Mer", "Sisley"),
        ("M∙A∙C Lipstick", "Makeup Forever"),
        ("Matrix Haircare", "Redken"),
        # Mode et vêtements
        ("Puma Shoes", "Adidas"),
        ("Ahava Lotion", "L'Occitane"),
        ("Delta Galil Underwear", "Local brands"),
        ("Moda Operandi Dress", "Local boutiques"),
        ("Golf & Co. Sportswear", "Local sportswear"),
        ("Renuar Shirt", "Zara"),
        ("Fox Jeans", "Local fashion"),
        ("Castro Jacket", "H&M"),
        ("Bagir Suit", "Local tailor"),
        ("Gottex Swimsuit", "Local swimwear"),
        # Supermarchés et restauration
        ("Carrefour", "Aziza"),
        ("KFC", "Quick"),
        ("Monoprix", "Leader Price"),
        ("Magasin Local", "Superette"),
        ("Géant", "Casino"),
        ("Auchan", "Carrefour"),
        ("Lidl", "Leader Price"),
        ("Marjane", "Aswak"),
        ("Hyper U", "Carrefour"),
        ("McDonald’s", "Burger King"),
    ]
    for product, alternative in boycotted_products:
        c.execute(
            "INSERT OR IGNORE INTO products (name, boycotted, alternative) VALUES (?, ?, ?)",
            (product, 1, alternative),
        )

    non_boycotted_brands = [
        # 🇹🇳 Marques tunisiennes
        "Boga (boisson non alcoolisée)",  # marque de soda tunisien :contentReference[oaicite:1]{index=1}
        "Delice (produits laitiers et confiseries)",
        "Poulina Group Holding (agroalimentaire)",
        "Terra d’Elyssa (huile d'olive tunisienne)",
        "Evertek (smartphones & accessoires)",  # marque tech tunisienne :contentReference[oaicite:2]{index=2}
        "Wallyscar (constructeur automobile tunisien)",  # marque auto 🇹🇳 :contentReference[oaicite:3]{index=3}
        "Hamadi Abid (mode tunisienne)",
        "Fouta Harissa (textiles & foulards) :contentReference[oaicite:4]{index=4}",
        "Chez Nous (mode et lifestyle) :contentReference[oaicite:5]{index=5}",
        "BOLD DENIM (streetwear tunisien) :contentReference[oaicite:6]{index=6}",
        "BARRA.GARA (mode textile) :contentReference[oaicite:7]{index=7}",
        "Ben Yaghlane Shops (retail tunisien)",
        "Manel Yousef Beauté (cosmétiques) :contentReference[oaicite:8]{index=8}",
        "Azar Shop (mode & accessoires) :contentReference[oaicite:9]{index=9}",
        "KaheNako Collection (mode & accessoires) :contentReference[oaicite:10]{index=10}",
        # 🌍 Marques internationales (généralement populaires et non ciblées par boycott fort)
        "Samsung (électronique) ",
        "Apple (technologie grand public)",
        "Microsoft (logiciels et cloud)",
        "Toyota (automobile)",
        "Honda (automobile & moto)",
        "Nike (vêtements & chaussures)",
        "Adidas (sport & sneakers)",
        "Puma (équipements sportifs)",
        "Lego (jouets)",
        "IKEA (ameublement)",
        "Unilever (produits d’hygiène et alimentaires)",
        "Procter & Gamble (PG – soins & hygiène)",
        "L’Oréal (cosmétiques)",
        "Estée Lauder (cosmétiques)",
        "Maybelline (cosmétiques)",
        "Sephora (magasin de beauté)",
        "Nestlé (certains produits – attention aux controverses globales)",
        "Danone (produits laitiers)",
        "Heinz (condiments)",
        "Kellogg’s (céréales)",
        "Reckitt (produits de nettoyage)",
        "Colgate‑Palmolive (hygiène bucco‑dentaire)",
        "Canon (photo & impression)",
        "Sony (électronique grand public)",
        "Panasonic (électronique)",
        "LG (électronique & électroménager)",
        "Bosch (outillage et électroménager)",
        "Philips (électronique)",
        "HP (ordinateurs & imprimantes)",
        "Dell (ordinateurs)**",
        "Lenovo (ordinateurs)",
        "Nike (sport)",
        "New Balance (chaussures)",
        "Converse (chaussures)",
        "Vans (chaussures & vêtements)",
        "Levi’s (jeans & vêtements)",
        "Hugo Boss (mode)",
        "Ralph Lauren (mode)",
        "Gap (mode)",
        "Old Navy (mode)",
        "Zara (parent Inditex – note : controverses locales variables)",
        "H&M (mode)",
        "Bershka (Inditex)",
        "Pull & Bear (Inditex)",
        "Forever 21 (mode)",
        "Timberland (chaussures)",
        "The North Face (outdoor)",
        "Columbia (outdoor)",
        "New Era (casquettes)",
        "Casio (montres & instruments)",
        "Fender (guitares)",
        "Gibson (guitares)",
        "Bose (audio)",
        "JBL (audio)",
        "Spotify (streaming musical)",
        "Netflix (streaming vidéo)",
        "Disney+ (streaming vidéo)",
        "YouTube (plateforme vidéo)",
        "Amazon (e‑commerce)",
        "Netflix (entertainment)",
        "Adobe (logiciels créatifs)",
        "Autodesk (logiciels créatifs)",
        "Intel (semiconducteurs)",
        "NVIDIA (processeurs graphiques)",
        "AMD (processeurs)",
        "Toyota (auto)",
        "Honda (auto/moto)",
        "Ferrari (luxe auto)",
        "BMW (automobile)",
        "Mercedes‑Benz (automobile)",
        "Audi (automobile)",
        "Volkswagen (automobile)",
        "Porsche (automobile)",
        "Tesla (voitures électriques)",
        "Rolex (montres de luxe)",
        "Gucci (luxe)",
        "Prada (luxe)",
        "Hermès (luxe)",
        "Louis Vuitton (luxe)",
        "Chanel (luxe)",
        "Burberry (luxe)",
        "Cartier (bijoux)",
        "Tiffany & Co (bijoux)",
        "Rolex (montres)",
        "TAG Heuer (montres)",
        "Ray‑Ban (lunettes)",
        "Oakley (lunettes)",
    ]
    for product in non_boycotted_brands:
        c.execute(
            "INSERT OR IGNORE INTO products (name, boycotted, alternative) VALUES (?, ?, ?)",
            (product, 0, ""),
        )
    db.commit()
    db.close()
    print("Database initialized.")
