#!/usr/bin/env python3
"""Generates the case study pages in work/ from the PROJECTS data below.

Edit the text here, then run:  python3 build.py
Images live in assets/cs/<slug>/01.jpg, 02.jpg ... (01 is the cover).
"""
import html, os, pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "work"

def count_images(slug):
    return len([f for f in os.listdir(ROOT / "assets/cs" / slug) if f.endswith(".jpg")])

# Door number = order in this list (1..12)
PROJECTS = [
  dict(
    slug="homely", title="Homely", cat="Mobile app · UX case study",
    tagline="A seamless home shopping experience for furniture, décor, plants and candles — all in one place.",
    meta=[("Role","UX research & UI design"),("Team","Amal Ahmed, Jaklen Sobhy"),("Platform","iOS & Android"),("Year","2026"),("Tools","Figma, Photoshop")],
    overview=[
      "Homely is a mobile application designed to simplify home shopping by bringing furniture, home décor, candles, plants and kitchen essentials together in one convenient platform.",
      "The concept client wanted a modern, inspiring experience that helps people furnish and decorate with confidence — solving the pain of finding matching products, comparing options across many stores, and picturing how items will fit into a real living space.",
    ],
    problems=["Searching across multiple home stores","Difficulty matching furniture and décor","Lack of confidence before purchasing","A time-consuming shopping experience","Too many options causing decision fatigue"],
    solutions=["All home essentials in one place","Curated collections by style","Smart search and filtering","Detailed product information and reviews","A simple, intuitive shopping flow"],
    audience=[("Young professionals","22–35 · furnishing a first home or apartment with stylish, quality pieces."),
              ("Newly married couples","25–35 · decorating a new home, looking for matching collections and affordable options."),
              ("Homeowners","30–50 · refreshing living spaces with furniture, plants, candles and accessories."),
              ("Décor enthusiasts","People who love interior design and regularly update their homes.")],
    phases=[("Empathize",["Stakeholder interview","User interviews","Competitive analysis","Survey"]),
            ("Define",["Empathy map","Persona","Problem statements","HMW questions","Storyboard"]),
            ("Ideate",["Card sorting","Priority matrix","Information architecture","User flow"]),
            ("Prototype",["Design system","Sketches","Mid-fi wireframes","Hi-fi prototype"])],
    stats=[("40","survey participants answering 10 questions about home-shopping habits"),
           ("3","direct competitors analysed: IKEA, Amazon and Wayfair"),
           ("10","user problem statements that shaped the feature set")],
    quotes=[("Users look for style, quality, and inspiration. Curated collections and room ideas can help them make confident choices.","Interior designer"),
            ("Customers want convenience, trust, and variety. Product details, reviews and easy checkout make a big difference.","Home store owner"),
            ("I want a simple app that helps me find everything for my home in one place without spending hours searching.","Potential user · young professional")],
    insights=["Users value stylish, high-quality products","Trust, reviews and product details are essential","A simple, inspiring shopping experience matters most","Room inspiration and curated collections are highly desired"],
    persona=dict(name="Omar Nasser", meta=["33 · Cairo","Married","Software engineer"],
      bio="Omar recently moved into his own apartment and wants to furnish it in a simple, modern way. He has little interest in interior design and prefers quick, practical solutions — he relies on online shopping, but finds choosing matching furniture, décor and kitchen items confusing.",
      goals=["Furnish the apartment quickly with minimal effort","Find simple, practical furniture","Get everything in one place","Keep the space clean, modern and functional"],
      pains=["Doesn't know how to match colours or styles","Overwhelmed by too many options","Worried about buying things that don't fit together","Finds home shopping boring and time-consuming"]),
    statements=["As a user, I want to find all home products in one place because switching between multiple apps is time-consuming.",
                "As a user, I want to see how items look in my space because I'm not sure they will match my home.",
                "As a user, I want personalized recommendations because I get overwhelmed by too many options.",
                "As a user, I want a simple checkout because complicated steps make me abandon the purchase."],
    features=[("AR “View in your space”","Place a sofa or vase in the room through the camera, rotate and reset it before buying."),
              ("Interest-based onboarding","Pick 4+ categories — sofas, candles, plants, kitchen — so the home feed feels personal from day one."),
              ("Category stores","Dedicated shops for Furniture, Plants, Décor and Candles with filters by style, price and rating."),
              ("Customizable products","Choose colour, size, scent or add a personal touch on décor and candles."),
              ("Scheduled delivery","Pick a delivery date and time, pay by card or cash, then follow every order status.")],
    screens=[21,25,30,33,35,37], exclude_last=True),

  dict(
    slug="house-basket", folder="basket", title="House Basket", ar="سلة البيت", cat="Mobile app · Grocery",
    tagline="An online grocery app that makes buying the week's essentials simple, fast and organized.",
    meta=[("Role","UX research & UI design"),("Team","Amal Ahmed"),("Platform","Mobile · Arabic first"),("Year","2026"),("Tools","Figma, Photoshop")],
    overview=[
      "House Basket (سلة البيت) is a UX project for an online grocery application that simplifies and speeds up buying daily essentials — especially for families and individuals living in urban areas.",
      "As people rely more on online shopping, existing apps showed recurring problems: complex checkouts, products that are hard to find, and unclear prices. The goal was a simpler, faster and more organized shopping experience, delivered across 50+ screens.",
    ],
    problems=["Product search wastes time across many categories","Long, complicated ordering steps","Final price and delivery fees appear too late","No easy way to repeat weekly shopping lists","Offers and ads that distract from essentials"],
    solutions=["Smart search with auto-suggestions and filters","Fewer checkout fields and fast payments (Apple Pay, Mada)","Clear totals and delivery fees before payment","One-tap reorder and saved shopping lists","Organized offers that don't get in the way"],
    audience=[("Working mothers","Primary persona · limited time, want quick reordering and simple checkout."),
              ("Families in urban areas","Buy groceries weekly or in bulk and need an organized way to manage essentials."),
              ("Busy professionals","Tight schedules, prefer fast delivery and repeat purchases."),
              ("Young adults","Comfortable with digital payments and interested in discounts.")],
    phases=[("Empathize",["Stakeholder interview","User interviews","Competitive analysis","Survey"]),
            ("Define",["Empathy map","Personas","Problem statements","HMW questions","Storyboard"]),
            ("Ideate",["Card sorting","Priority matrix","Information architecture","User flow"]),
            ("Prototype",["Design system","Sketches","Mid-fi wireframes","Hi-fi prototype"])],
    stats=[("50+","screens designed for the full shopping journey"),("6","core problem statements turned into features"),("KSA","geographic focus: urban cities with fast delivery")],
    statements=["As a user, I want an easy and fast way to find the products I need, so I can buy necessities without searching through many categories.",
                "As a user, I want to see the final price and delivery fees before paying, so I can buy with confidence and no surprises.",
                "As a user, I want to save recurring shopping lists and reorder easily, so I save time on weekly or monthly purchases.",
                "As a user, I want offers to be clear and organized, so I can focus on my essential purchases."],
    features=[("Reorder in one tap","Previous orders and saved baskets come back with a single “Reorder” button."),
              ("Points & prizes","Earn points on every order and redeem them for rewards."),
              ("Barcode scan","Scan a product to find it instantly and add it to the cart."),
              ("Order tracking & chat","Follow the order live and chat with support when something is out of stock.")],
    screens=[15,19,20,21,22,24], exclude_last=True),

  dict(
    slug="flexora", title="Flexora", cat="Mobile app · AI fitness coach",
    tagline="Your smart coach — an AI-powered fitness app that adapts workouts and meals to your energy, goals and progress.",
    meta=[("Role","UX/UI designer"),("Team","UXAWY design team: Amal Ahmed, Gerges Khalaf, Jaklen Sobhy, Kenzi Ahmed"),("Platform","Mobile + responsive"),("Timeline","Oct – Nov 2025"),("Tools","Figma")],
    overview=[
      "Flexora was designed by the UX/UI design team at UXAWY. It delivers a seamless, intuitive fitness experience: a clean interface and smart features focused on usability, accessibility and real value in people's daily lives.",
      "We used a user-centred design thinking process to understand why people quit fitness apps, define the core problem, and create a simple, personalized experience powered by AI.",
    ],
    problems=["Workouts aren't personalized","Motivation fades quickly","No real follow-up or guidance","Unsure if exercises are done correctly","Nutrition plans are hard to stick to"],
    solutions=["AI-generated workout and nutrition plans","Daily check-ins on energy and mood to adjust intensity","Real-time guidance with a live workout player","Friendly, personal reminders and streaks","Rewards and achievements for every milestone"],
    phases=[("Empathize",["Stakeholder interview","Competitor analysis","Feature comparison","Survey","User interviews"]),
            ("Define",["Empathy map","Persona","Problem statements","HMW questions","Storyboard"]),
            ("Ideate",["Information architecture","Card sorting","User flow"]),
            ("Prototype",["Design system","Sketches","Hi-fi UI","Responsive layouts"])],
    quotes=[("I tried a workout plan before, but I stopped because no one followed up with me.","Interviewee · empathy map"),
            ("I'm not sure if I'm doing the exercises correctly.","Interviewee · empathy map"),
            ("I'd like a smart coach that adapts to my time, mood, and progress.","Interviewee · empathy map")],
    persona=dict(name="Omar Ahmed", meta=["21 · Cairo, Egypt","Single","University student"],
      bio="Omar wants to stay fit but often feels too busy with classes and assignments. He follows short, effective workouts on his phone between lectures or in the evening, and likes apps that are easy to navigate, show exercises clearly and offer plans that match his goals.",
      goals=["Short, effective workouts that fit his schedule","A personalized plan for his goals","Track progress and stay motivated"],
      pains=["Not enough time for long sessions","Too many options make it hard to start","Loses motivation without follow-up"]),
    statements=["Time management — I need short, flexible workouts that fit my schedule, because I don't always have time for long sessions.",
                "Overwhelm — I need simple guidance that tells me exactly what to do today, because too many options make me less likely to start.",
                "Emotional support — I need a coach that understands my ups and downs, because my mood affects my consistency.",
                "Reward — I need achievements for every milestone, because small wins keep me motivated."],
    hmw=["How might we create personalized workout plans that adjust after every session?","How might we keep users motivated and consistent with streaks, points and weekly challenges?"],
    features=[("Meet your AI coach","Choose a coach, ask anything about exercises, meals or progress, and get answers in chat."),
              ("Today's workout","A clear home screen with today's plan, programs by level and a live exercise player."),
              ("Meal planner","Daily and weekly meal plans with calories, carbs, protein and fats."),
              ("Progress tracking","Weight, weekly hours and program completion in one place.")],
    screens=[26,27,28,29,30,33], exclude_last=True),

  dict(
    slug="book-hub-landing", folder="bookhub-landing", title="Book Hub Landing", cat="Landing page · Web",
    tagline="The marketing website for the Book Hub reading app — browse categories, discover authors and download the app.",
    meta=[("Role","UI designer"),("Team","Amal Ahmed, Mohammed Mohab, Osama Ahmed, Jaklen Sobhy"),("Platform","Web · Desktop"),("Year","2025"),("Tools","Figma")],
    overview=[
      "The Book Hub landing page introduces the Book Hub app on the web. It welcomes readers with a featured author, a quote that sets the mood, browsable categories and a best-seller shelf — then invites them to download the app.",
    ],
    features=[("Featured author","A hero spotlight on a celebrated author with a direct link to their books."),
              ("Categories","Horror, Law, Adventure, Politics, Fantasy, History, Math, Food — one click away."),
              ("Best sellers","A shelf of top books with author and price."),
              ("App download","A clear call to download the app, with free shipping highlighted.")],
    screens=[2], screens_single=True, exclude_last=False),

  dict(
    slug="book-hub-app", folder="bookhub-app", title="Book Hub", cat="Mobile app · Team case study",
    tagline="A reading app with fast delivery, a rich Arabic library, flexible payments and book borrowing.",
    meta=[("Role","UX/UI designer"),("Team","Amal Ahmed, Mohammed Mohab, Osama Ahmed, Jaklen Sobhy"),("Platform","Mobile app"),("Year","2025"),("Tools","Figma")],
    overview=[
      "I was part of a team that worked on a book application. We set out to solve the challenges readers face: slow book delivery, limited Arabic content, high prices and few payment options — plus missing features like book borrowing and cross-device sync. Similar apps were often complicated and not user-friendly.",
      "Applying the stages of design thinking, we created a book app that is simple to use, suited to readers' real needs, and balanced between attractive design and practical function.",
    ],
    problems=["Slow delivery of physical books","Limited Arabic content","High prices and restricted payment options","No option to borrow books","Reading features missing: sync, offline, notes, night mode"],
    solutions=["Faster delivery through local partners and warehouses","A rich Arabic library via local publishers","Multiple payment options: card, wallets, cash","Borrow books by the day at a lower cost","Sync, offline reading, highlights, notes and night mode"],
    phases=[("Empathize",["User research","Survey","Stakeholder interview","Competitor analysis"]),
            ("Define",["User personas","Empathy map","Storyboarding","Problem statements"]),
            ("Ideate",["User flow","Card sorting","Priority matrix","Information architecture"]),
            ("Design & test",["Paper wireframes","Visual design","Prototype","Usability check"])],
    stats=[("22","survey responses about reading habits"),("3","competitors analysed, incl. Abjjad & Book Depository"),("4","designers on the team")],
    persona=dict(name="Omar Hassan", meta=["21 · Cairo","Single","University student"],
      bio="Omar relies heavily on e-books for his studies because he dislikes carrying heavy paper books. He reads on his phone during commutes and breaks, prefers fast, easy platforms in Arabic, and is influenced by recommendations from classmates and social media.",
      goals=["Fast access to study books","Arabic content that's easy to find","Affordable reading options"],
      pains=["Physical book delivery takes too long","Limited Arabic academic content","Apps that are slow or complicated"]),
    hmw=["How might we reduce delivery time for young readers and parents so they don't get frustrated waiting for their books?",
         "How might we expand Arabic content so readers find what they're looking for?"],
    features=[("Buy or borrow","Every book can be bought or borrowed per day, with the total shown before you pay."),
              ("My booklist","Track New, Reading and Finished books, and know when a borrowed book is ready for pickup."),
              ("Comfortable reader","Adjust font size, line spacing and margins, with bookmarks and search inside the book."),
              ("Reading plans","6- and 12-month subscriptions with unlimited downloads for offline reading.")],
    screens=[25,28,31,33,35,36], exclude_last=True),

  dict(
    slug="fashion-app", folder="fashion", title="Fashion App", cat="Mobile app · UX case study",
    tagline="Style inspiration, personalized recommendations and accurate size guidance for easier online fashion shopping.",
    meta=[("Role","UX research & UI design"),("Team","Amal Ahmed"),("Platform","Mobile app"),("Year","2025"),("Tools","Figma, Miro")],
    overview=[
      "This fashion app gives users a seamless shopping experience by combining style inspiration, personalized recommendations and accurate size guidance. The goal: make online fashion shopping easier, more enjoyable and tailored to individual preferences.",
      "Users who shop online often struggle to find clothes that truly fit their size and match their style — which leads to frustration, wasted time and reduced trust. A personalized Size Guide became the heart of the solution.",
    ],
    problems=["Sizes are inconsistent, especially for kids and activewear","Returns are difficult or unavailable","Product photos don't reflect reality","Confusing layouts and unorganized categories","Suggestions that don't match personal taste"],
    solutions=["A size chart that recommends a size from your weight and height","A clear returns flow with wallet refunds","Real photo reviews rewarded with points","Simple navigation, filters and sellers","Mix & Match: upload an item and get matching pieces"],
    phases=[("Empathize",["Stakeholder interview","User interviews","Competitive analysis (SHEIN, Zara, H&M)","Survey"]),
            ("Define",["Empathy map","Persona","Problem statements","HMW questions","Storyboard"]),
            ("Ideate",["Card sorting","Priority matrix","Information architecture","User flow"]),
            ("Prototype",["Design system","Sketches","Mid-fi wireframes","Prototype"])],
    stats=[("54.5%","of respondents prefer buying casual clothing online"),("3","leading apps compared feature by feature"),("1","signature feature: the Size Guide")],
    quotes=[("Kids' sizes are always tricky.","Mona, 31 · empathy map"),("I need quick suggestions for Eid or school event outfits.","Mona, 31 · empathy map")],
    hmw=["How might we improve size accuracy for busy mothers shopping for their children, so they order confidently without fear of returns?",
         "How might we display more realistic photos and reviews, so young users trust that what they see is what they'll receive?",
         "How might we simplify navigation and filtering for users overwhelmed by too many options?"],
    features=[("Size Guide","Enter weight and height to get a recommended size, plus a detailed chart in cm and inches."),
              ("Mix & Match","Photograph an item and the app suggests pieces that go with it."),
              ("Reviews that pay","Add a review with a photo and earn 100 discount points."),
              ("Sellers & chat","Follow local stores, browse their brands and message them directly.")],
    screens=[27,30,32,34,36,37], exclude_last=True),

  dict(
    slug="magnolia-market", folder="magnolia", title="Magnolia Market", cat="E-commerce · Concept app",
    tagline="A concept app for a modern home-goods store: unique pieces, reviews, order tracking and AR placement.",
    meta=[("Role","UX/UI designer"),("Team","Amal Ahmed"),("Platform","Mobile app"),("Year","2023"),("Tools","Figma")],
    overview=[
      "A concept shopping app for Magnolia Market, the home goods and lifestyle brand. The aim: your perfect choice for a modern home — a personalized experience, unique pieces you may not find in the local market, other shoppers' reviews and order tracking.",
    ],
    phases=[("Research",["Competitor analysis","User interviews"]),("UX design",["User journey","User flow","Wireframes"]),("UI design",["Moodboard","Style guide","Sketch & wireframe"]),("Test",["Prototype","Testing"])],
    features=[("Catalogue & collections","Browse collections and sort products to find the right piece fast."),
              ("Product detail","Sizes, price range and add to cart in one clean view."),
              ("AR placement","Coach marks guide you to detect a surface and place a vase in your room."),
              ("Cart & checkout","An order overview with PayPal checkout.")],
    design=dict(font="Poppins", colors=["#F8E3E0","#3F5E29","#202627","#666666","#878787"]),
    screens=[10,12,13,14,17,18], exclude_last=True),

  dict(
    slug="weather-app", folder="weather", title="Weather App", cat="Mobile app · UI design",
    tagline="A clean weather app UI with hourly and 7-day forecasts, air quality, UV index and sunrise times.",
    meta=[("Role","UI designer"),("Team","Amal Ahmed"),("Platform","iOS & Android"),("Year","2023"),("Tools","Figma")],
    overview=["A weather app UI focused on at-a-glance information: the current temperature with max and min, an hourly timeline, a 7-day forecast, and cards for air quality, sunrise/sunset and UV index."],
    features=[("Hourly timeline","Today's temperatures hour by hour."),("7-day forecast","The week ahead in one row."),("Air quality","Health-risk level with more detail on tap."),("Sun & UV","Sunrise, sunset and UV index cards.")],
    screens=[], exclude_last=False),

  dict(
    slug="power-energy", folder="electrical", title="Power Energy", cat="E-commerce · Website",
    tagline="An electronics e-commerce website — cameras, telephones and consoles with categories, filters and reviews.",
    meta=[("Role","UI designer"),("Team","Amal Ahmed"),("Platform","Web"),("Year","2023"),("Tools","Figma, Adobe XD")],
    overview=["Power Energy is an e-commerce website for electrical products. The design covers the home page, popular products, category listings with price and popularity filters, customer feedback and an About page."],
    features=[("Popular products","A home page that leads with best sellers and customer feedback."),("Category pages","Breadcrumbs plus price and popularity filters."),("Brand story","An About page that tells the brand's history.")],
    design=dict(font="DM Sans", colors=["#A93070","#852763","#000000","#FFFFFF"]),
    screens=[], exclude_last=True),

  dict(
    slug="coffee-app", folder="coffee", title="Coffee App", cat="Mobile app · Ordering",
    tagline="Order your favourite coffee, follow it on the map, and pay in a few taps.",
    meta=[("Role","UX/UI designer"),("Team","Amal Ahmed"),("Platform","Mobile app"),("Year","2023"),("Tools","Figma")],
    overview=["A coffee ordering app covering the whole journey: sign in, browse the hot and iced menu, customise size, add to cart, pay by card and track the delivery live."],
    phases=[("Research",["Competitor analysis","User interviews"]),("UX design",["User flow","User journey","Wireframes"]),("UI design",["Colour & style guide","Typography","Icons"]),("Deliver",["Hi-fi screens","Prototype"])],
    features=[("Menu & categories","Hot, iced and pastries with ratings and prices."),("Product details","Recipe, rating and size choice before adding to cart."),("Card checkout","A clear card form and success state."),("Live tracking","Follow the courier on the map with an ETA.")],
    design=dict(font="Poppins", colors=["#B46E41","#000000","#FFFFFF"]),
    screens=[11,12,13,14,15,16], exclude_last=True),

  dict(
    slug="dashboard", title="Dashboard", cat="Web · Dashboard",
    tagline="An analytics dashboard: views, visits, new users, operating status and traffic by device and location.",
    meta=[("Role","UI designer"),("Team","Amal Ahmed"),("Platform","Web"),("Year","2023"),("Tools","Figma")],
    overview=["A clean analytics dashboard with a sidebar for projects, profiles and pages, and a main view of KPIs — views, visits, new users and active users — plus operating status and traffic by device and location."],
    screens=[], exclude_last=True),

  dict(
    slug="shopping-app", folder="shopping", title="Shopping App", cat="Mobile app · E-commerce",
    tagline="A gift-shopping app for watches and accessories, from discovery to swipe-to-pay.",
    meta=[("Role","UI designer"),("Team","Amal Ahmed"),("Platform","Mobile app"),("Year","2023"),("Tools","Figma")],
    overview=["A shopping app for finding the best gifts for your loved ones: new arrivals, watches and wristbands, recommendations, and a bag that checks out with a single swipe."],
    screens=[], exclude_last=False),
]

# ---- Full case-study content for the smaller projects (merged into PROJECTS by slug) ----
EXTRA = {
  "book-hub-landing": dict(
    overview=[
      "The Book Hub landing page is the web front door for the Book Hub reading app. It had one job: make a first-time visitor feel the joy of reading in a few seconds — then send them to browse books or download the app.",
      "It was designed alongside the Book Hub mobile app, so it shares the same brand, typography and book-first visuals, and speaks to the same readers: students and book lovers looking for affordable books and more Arabic content.",
    ],
    problems=["Visitors don't know what Book Hub offers at first glance","Long pages hide the books behind text","No clear path from the website to the app","Hard to browse by interest before signing up"],
    solutions=["A hero that leads with an author spotlight and a reading quote","Books and covers above the fold — not paragraphs","A clear “Download our app” section","Category chips and a best-seller shelf to explore instantly"],
    audience=[("Students","Looking for study books and summaries at a fair price."),("Book lovers","Discovering new authors and best sellers."),("Parents","Browsing categories for the family."),("App prospects","Visitors deciding whether to install Book Hub.")],
    goals=["Explain Book Hub in one scroll","Put books, not text, at the centre","Turn visitors into app downloads","Match the mobile app's look and feel"],
    phases=[("Understand",["Reused app research","Reader needs","Competitor sites"]),("Structure",["Page sections","Content hierarchy","Call-to-action plan"]),("Design",["Wireframe","Visual design","Book imagery"]),("Polish",["Typography","Spacing","Responsive check"])],
    flow=["Hero: author spotlight","Reading quote","Download the app","Browse categories","Best sellers","Shop / contact"],
    decisions=[("Author-first hero","Leading with a celebrated author makes the page feel like a bookstore, not a tech product."),
               ("One idea per section","Each block — quote, app, categories, best sellers — answers one question a visitor has."),
               ("Free shipping up front","A small badge in the hero removes a common reason people hesitate to buy books online.")],
    next_steps=["Add a search bar in the hero so readers can jump to a title","Show Arabic books and authors in the spotlight","A/B test the app download section placement"],
    screens=[2,3], screens_single=True),

  "magnolia-market": dict(
    overview=[
      "A concept shopping app for Magnolia Market, the home goods and lifestyle brand. The aim: your perfect choice for a modern home — a personalized experience, unique pieces you may not find in the local market, other shoppers' reviews and order tracking.",
      "The challenge was to carry the brand's warm, farmhouse-modern feeling into a mobile store that is still fast to browse and simple to buy from.",
    ],
    problems=["Unique pieces are hard to discover in a long catalogue","Hard to imagine how décor will look at home","Shoppers rely on reviews but can't find them","Checkout feels long on mobile"],
    solutions=["Curated collections with sort and filter","AR placement with coach marks to try a piece in your room","Ratings shown on every product card","A short cart → PayPal checkout"],
    audience=[("Home lovers","People decorating and refreshing their homes."),("Gift shoppers","Looking for a unique present."),("Brand fans","Already know Magnolia and want the store in their pocket.")],
    goals=["Feel like the brand: warm, calm, natural","Make discovery effortless","Help shoppers buy with confidence","Keep checkout short"],
    flow=["Onboarding","Home","Catalogue","Product","AR placement","Cart","Checkout"],
    decisions=[("Soft pink + olive palette","#F8E3E0 and #3F5E29 echo the brand's natural, homely mood."),
               ("Poppins for clarity","A friendly geometric typeface keeps prices and names easy to scan."),
               ("Coach marks for AR","Step-by-step hints (detect surface → tap to place) make a new feature easy to try.")],
    next_steps=["Usability test the AR flow with first-time users","Add a wishlist and back-in-stock alerts","Design the order tracking screens in more detail"]),

  "weather-app": dict(
    overview=[
      "A weather app UI focused on at-a-glance information. Most people open a weather app for a few seconds, so every screen answers one question fast: What's it like now? What about later today? And this week?",
      "The visual direction uses a deep purple night sky, soft 3D weather icons and glassy cards, so the information feels calm and easy to read.",
    ],
    problems=["Weather apps cram too much data on one screen","Hourly and weekly forecasts are hard to compare","Extra info (air quality, UV) is buried in menus"],
    solutions=["One focus per screen: now, today, this week","Swipeable hourly and 7-day rows","Air quality, sunrise and UV as clear cards"],
    audience=[("Commuters","Checking quickly before leaving home."),("Outdoor lovers","Planning around rain, sun and UV."),("Everyone","A quick daily glance.")],
    goals=["Readable in under 5 seconds","Clear hierarchy: temperature first","A friendly, calm visual style"],
    flow=["Splash: Weather ForeCasts","Today: temperature + hourly","Week: 7-day forecast + details"],
    features=[("Big current temperature","19° with precipitation, max and min — the first thing you see."),("Hourly timeline","Today's temperatures hour by hour in one row."),("7-day forecast","Swipe through the week ahead."),("Detail cards","Air quality, sunrise/sunset and UV index.")],
    decisions=[("3D icons","Soft, illustrated weather icons make conditions instantly recognizable."),
               ("Glass cards","Translucent cards keep the background mood while separating information."),
               ("Yellow call-to-action","A warm yellow “Get Start” button stands out against the purple sky.")],
    next_steps=["Add location search and saved cities","Severe-weather alerts","A light theme for daytime"],
    screens=["d1","d2","d3"]),

  "power-energy": dict(
    overview=[
      "Power Energy is an e-commerce website for electrical and electronic products — cameras, telephones and gaming consoles. The goal was a store that feels trustworthy and makes it easy to compare products and buy.",
      "I worked from wireframes to a full visual design, with a bold berry colour palette that gives the store a distinctive, premium look.",
    ],
    problems=["Electronics stores feel cluttered and hard to scan","Shoppers can't compare prices quickly","Little trust in unknown online stores"],
    solutions=["A clean home page that leads with popular products","Category pages with price and popularity filters","Customer feedback and an About page that tells the brand story"],
    audience=[("Tech shoppers","Comparing cameras, phones and consoles."),("Gift buyers","Looking for a reliable electronic gift."),("Retro fans","Collectors of classic consoles and cameras.")],
    goals=["Make products the hero","Fast comparison by price and popularity","Build trust with reviews and brand story"],
    phases=[("Research",["Competitor stores","Product structure"]),("Wireframes",["Home","Categories","About"]),("Visual design",["Colour & typography","Icons"]),("Pages",["Home","Categories","About us"])],
    flow=["Home","Popular products","Category page","Filter by price / popularity","Product","Cart"],
    decisions=[("Berry palette","#A93070 and #852763 give a confident, premium feel different from typical blue tech stores."),
               ("DM Sans + Monotype Corsiva","A clean sans for the interface, with a script accent for personality."),
               ("Breadcrumbs","Home / Category / Brand paths help shoppers know where they are.")],
    next_steps=["Design the product detail and checkout pages","Add product comparison side by side","Test the filters with real shoppers"]),

  "coffee-app": dict(
    overview=[
      "A coffee ordering app covering the whole journey: sign in, browse the hot and iced menu, customise size, add to cart, pay by card and track the delivery live.",
      "The design uses warm coffee browns and simple layouts so ordering a drink takes only a few taps.",
    ],
    problems=["Ordering coffee by phone or in a queue is slow","Menus don't show prices and sizes clearly","No way to know when the order will arrive"],
    solutions=["A visual menu with categories, prices and ratings","Size selection on the product page","Live tracking with courier name and ETA"],
    audience=[("Busy workers","Ordering coffee to the office."),("Students","Quick, affordable drinks."),("Coffee lovers","Trying new hot and iced drinks.")],
    goals=["Order a drink in under a minute","Clear prices and options","Reassure users while they wait"],
    flow=["Sign in / sign up","Home & categories","Product details","Cart","Card checkout","Tracking","Profile"],
    decisions=[("Coffee brown palette","#B46E41 sets a warm, café-like mood."),
               ("Two prices on cards","Showing the original and the deal price highlights offers at a glance."),
               ("Map tracking","Seeing the courier and the minutes left reduces “where is my order?” anxiety.")],
    next_steps=["Add favourites and reorder","Loyalty points for frequent orders","Pickup option for nearby cafés"]),

  "dashboard": dict(
    overview=[
      "An analytics dashboard UI for teams that need to see how their product is doing at a glance: views, visits, new users and active users, plus traffic sources, devices and locations.",
      "The layout uses a three-column structure — navigation, main analytics, and a live activity panel — with soft colours so the data stays the focus.",
    ],
    problems=["Dashboards overload users with charts","Key numbers are hard to find","Team activity lives in a different tool"],
    solutions=["Four KPI cards at the top with trend %","Grouped charts: users, website, device, location","A right panel for notifications, activity and contacts"],
    audience=[("Product managers","Tracking growth week to week."),("Marketing teams","Watching traffic sources and SEO."),("Founders","A quick health check of the product.")],
    goals=["Show the most important numbers first","Make comparisons easy (this week vs last week)","Keep everything on one screen"],
    flow=["Sidebar: dashboards & pages","KPI cards","Total users chart","Traffic by website / device / location","Notifications & activity"],
    features=[("KPI cards","Views, visits, new users and active users with growth trends."),("Weekly comparison","Current vs previous week on one line chart."),("Traffic breakdown","By website, device and location."),("Activity panel","Notifications, team activity and contacts.")],
    decisions=[("Muted blue-grey cards","Calm colours stop the KPIs from shouting over each other."),
               ("Right activity rail","Keeps team updates visible without leaving the analytics."),
               ("Responsive, reusable components","Built as components so the layout adapts and scales.")],
    next_steps=["Add date-range filters and export","A dark mode for long sessions","Design the eCommerce and Projects dashboards"],
    screens=["d1","d2","d3"]),

  "shopping-app": dict(
    overview=[
      "A shopping app for finding the best gifts for your loved ones — focused on watches and accessories. The idea: make gift shopping feel special, from browsing new arrivals to checking out with a single swipe.",
      "Clean outlined cards on a warm cream background let the product photography do the talking.",
    ],
    problems=["Gift shopping takes too long","Too many products, little guidance","Checkout feels like a chore"],
    solutions=["New arrivals and “We recommend” sections","Simple categories: watches, wrist bands, wonders","Swipe to pay — one gesture to finish"],
    audience=[("Gift givers","Buying for partners, family and friends."),("Watch lovers","Browsing new models."),("Last-minute shoppers","Need a good gift fast.")],
    goals=["Inspire with beautiful product photos","Guide choice with recommendations","Make paying effortless"],
    flow=["Welcome: Find the best gifts","Home: new arrivals & recommendations","Product","My bag","Swipe to pay"],
    features=[("Gift-first home","Search, new arrivals and recommendations on one screen."),("Categories","Watches, wrist bands and wonders."),("My bag","Edit quantities and see the total instantly."),("Swipe to pay","A playful, deliberate gesture to confirm.")],
    decisions=[("Outlined cards","Thin outlines keep the UI light so product photos stand out."),
               ("Deep green accent","Matches the luxury gift boxes in the photography."),
               ("Swipe instead of tap","Prevents accidental purchases and feels satisfying.")],
    next_steps=["Gift wrapping and message options","Wishlist sharing","Delivery date picker for occasions"],
    screens=["d1","d2","d3"]),
}


# ---------------------------------------------------------------- rendering
from content_ar import AR, AR_META

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Instrument+Serif:ital@1&family=Unbounded:wght@600;800&family=Space+Mono:wght@400;700&family=Cairo:wght@400;600;800&family=IBM+Plex+Sans+Arabic:wght@400;500;600&display=swap" rel="stylesheet">'
SITE = "https://alaashaheen93.github.io/Amal-s-portoflio-/"  # live address, used for link previews
LINKS = [("LinkedIn","https://www.linkedin.com/in/amal-shaheen-33ba88283/"),("Behance","https://www.behance.net/amalahmed30")]
e = html.escape

UI = {
 "en": dict(back='← <span class="long">Back to the</span> calendar', talk="Let's talk ↗", door="Door {n} of 12", overview="Overview",
   challenge="Challenge &amp; solution", problem="The problem", solution="Our solution", audience="Who it's for", goals="Design goals",
   process="Process", research="Research", persona="Persona", p_goals="Goals", p_pains="Frustrations", defining="Defining the problem",
   flow="User flow", features="Key features", decisions="Design decisions", ds="Design system", typeface="Typeface",
   screens="Final screens", nexts="What I'd do next", full="The full case study", see="See every board of the original {t} case study",
   boards="{k} boards · research, flows, design system and all screens", open="Open all boards ↓", close="Close boards ↑",
   nextdoor="Next door", arrow="→", foot="© 2026 Amal Ahmed · UI/UX designer · Cairo", switch="العربية", screen="screen", board="board"),
 "ar": dict(back='→ <span class="long">العودة إلى</span> التقويم', talk="تواصلي معي ↗", door="الباب {n} من 12", overview="نظرة عامة",
   challenge="التحدي والحل", problem="المشكلة", solution="الحل", audience="لمن هذا التصميم", goals="أهداف التصميم",
   process="مراحل العمل", research="البحث", persona="الشخصية", p_goals="الأهداف", p_pains="الإحباطات", defining="تحديد المشكلة",
   flow="رحلة المستخدم", features="أهم المميزات", decisions="قرارات التصميم", ds="نظام التصميم", typeface="الخط",
   screens="الشاشات النهائية", nexts="الخطوات القادمة", full="دراسة الحالة كاملة", see="شاهد كل لوحات دراسة حالة {t} الأصلية",
   boards="{k} لوحة · البحث ورحلات المستخدم ونظام التصميم وكل الشاشات", open="افتح كل اللوحات ↓", close="أغلق اللوحات ↑",
   nextdoor="الباب التالي", arrow="←", foot="© 2026 أمل أحمد · مصممة UI/UX · القاهرة", switch="English", screen="شاشة", board="لوحة"),
}

def img(folder, i):
    # i is a board number (1 = cover) or a file name like "d1" for a close-up crop
    return f"../assets/cs/{folder}/{i:02d}.jpg" if isinstance(i, int) else f"../assets/cs/{folder}/{i}.jpg"

def section(idx, label, body):
    return f'''<section class="sec wrap"><div class="sec-grid"><div class="sec-label rv"><span class="idx">{idx:02d}</span><h2>{label}</h2></div><div class="rv">{body}</div></div></section>'''

def href(slug, lang):
    return f"{slug}.html" if lang == "en" else f"{slug}-ar.html"

def localize(p, lang):
    if lang == "en":
        return p
    q = dict(p)
    ar = AR[p["slug"]]
    q.update(ar)
    if "meta" not in ar:  # fall back to translating just the labels
        q["meta"] = [(AR_META.get(a, a), b) for a, b in q["meta"]]
    return q

def page(n, base, nxt_base, nn, lang):
    T = UI[lang]
    p = localize(base, lang); nxt = localize(nxt_base, lang)
    folder = p.get("folder", p["slug"])
    total = count_images(folder)
    s, k = [], 0
    def add(label, body):
        nonlocal k; k += 1; s.append(section(k, label, body))
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)

    add(T["overview"], '<div class="prose">' + "".join(f'<p class="{"lead" if i==0 else ""}">{e(t)}</p>' for i,t in enumerate(p["overview"])) + "</div>")
    if p.get("problems"):
        add(T["challenge"], f'<div class="duo"><div class="box"><h3>{T["problem"]}</h3><ul>{li(p["problems"])}</ul></div><div class="box dark"><h3>{T["solution"]}</h3><ul>{li(p["solutions"])}</ul></div></div>')
    if p.get("audience"):
        add(T["audience"], '<div class="cards">' + "".join(f'<div class="card"><b>{e(a)}</b><span>{e(b)}</span></div>' for a,b in p["audience"]) + "</div>")
    if p.get("goals"):
        add(T["goals"], '<div class="cards">' + "".join(f'<div class="card"><b>{i+1:02d}</b><span class="g">{e(g)}</span></div>' for i,g in enumerate(p["goals"])) + "</div>")
    if p.get("phases"):
        add(T["process"], '<div class="phases">' + "".join(
            f'<div class="phase"><span class="pn">{i+1:02d}</span><h4>{e(t)}</h4><ul>{li(ms)}</ul></div>' for i,(t,ms) in enumerate(p["phases"])) + "</div>")
    if p.get("stats") or p.get("quotes"):
        body = ""
        if p.get("stats"):
            body += '<div class="stats">' + "".join(f'<div class="stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v,l in p["stats"]) + "</div>"
        if p.get("quotes"):
            body += '<div class="quotes">' + "".join(f'<blockquote class="quote"><p>“{e(q)}”</p><cite>{e(w)}</cite></blockquote>' for q,w in p["quotes"]) + "</div>"
        if p.get("insights"):
            body += '<ul class="insights">' + "".join(f"<li><span>{i+1:02d}</span>{e(x)}</li>" for i,x in enumerate(p["insights"])) + "</ul>"
        add(T["research"], body)
    if p.get("persona"):
        pe = p["persona"]; ini = pe.get("initials") or "".join(w[0] for w in pe["name"].split()[:2])
        add(T["persona"], f'''<div class="persona"><div class="who"><div><div class="avatar">{e(ini)}</div><h4>{e(pe["name"])}</h4></div><div>{"".join(f"<small>{e(m)}</small>" for m in pe["meta"])}</div></div>
<div class="body"><p class="bio">{e(pe["bio"])}</p><div class="cols"><div><h5>{T["p_goals"]}</h5><ul>{li(pe["goals"])}</ul></div><div><h5>{T["p_pains"]}</h5><ul>{li(pe["pains"])}</ul></div></div></div></div>''')
    if p.get("statements") or p.get("hmw"):
        body = '<div class="statements">' + "".join(f'<div class="statement"><i>{i+1:02d}</i><span>{e(t)}</span></div>' for i,t in enumerate(p.get("statements",[])))
        body += "".join(f'<div class="statement hmw"><i>HMW</i><span>{e(t)}</span></div>' for t in p.get("hmw",[])) + "</div>"
        add(T["defining"], body)
    if p.get("flow"):
        add(T["flow"], '<div class="flow">' + "".join(f'<span><i>{i+1:02d}</i>{e(st)}</span>' for i,st in enumerate(p["flow"])) + "</div>")
    if p.get("features"):
        add(T["features"], '<div class="features">' + "".join(f'<div class="feature"><b>{e(a)}</b><p>{e(b)}</p></div>' for a,b in p["features"]) + "</div>")
    if p.get("decisions"):
        add(T["decisions"], '<div class="statements">' + "".join(f'<div class="statement"><i>{i+1:02d}</i><span><b>{e(a)}.</b> {e(b)}</span></div>' for i,(a,b) in enumerate(p["decisions"])) + "</div>")
    if p.get("design"):
        d = p["design"]
        add(T["ds"], '<div class="ds">' + f'<div class="font-card"><span class="eyebrow">{T["typeface"]}</span><b style="font-family:{e(d["font"])},sans-serif" dir="ltr">Aa</b><span dir="ltr">{e(d["font"])}</span></div>' +
            "".join(f'<div class="swatch"><i style="background:{c}"></i><span dir="ltr">{c}</span></div>' for c in d["colors"]) + "</div>")

    screens = p.get("screens") or []
    if screens:
        k += 1
        cls = "screens single" if p.get("screens_single") else ("screens three" if len(screens) == 3 and isinstance(screens[0], str) else "screens")
        s.append(f'<section class="sec wrap"><div class="sec-label rv" style="position:static;margin-bottom:24px"><span class="idx">{k:02d}</span><h2>{T["screens"]}</h2></div><div class="{cls}">' +
                 "".join(f'<figure class="rv"><img src="{img(folder,i)}" alt="{e(p["title"])} {T["screen"]}" loading="lazy"></figure>' for i in screens) + "</div></section>")
    if p.get("next_steps"):
        add(T["nexts"], '<ul class="insights" style="margin-top:0">' + "".join(f"<li><span>{i+1:02d}</span>{e(x)}</li>" for i,x in enumerate(p["next_steps"])) + "</ul>")

    last = total - (1 if p.get("exclude_last") else 0)
    boards = list(range(2, last + 1))
    boards_html = ""
    if len(boards) > 1:
        boards_html = f'''<section class="wrap"><div class="boards-toggle rv"><div><span class="eyebrow">{T["full"]}</span><h3>{T["see"].format(t=e(p["title"]))}</h3><p>{T["boards"].format(k=len(boards))}</p></div>
<button class="pill" id="bt" aria-expanded="false" data-open="{T["open"]}" data-close="{T["close"]}">{T["open"]}</button></div>
<div class="boards" id="boards">{"".join(f'<figure><img src="{img(folder,i)}" alt="{e(p["title"])} {T["board"]} {i}" loading="lazy"><figcaption dir="ltr">{i:02d} / {last:02d}</figcaption></figure>' for i in boards)}</div></section>'''

    nfolder = nxt.get("folder", nxt["slug"])
    meta = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a,b in p["meta"])
    extra_title = p.get("ar") if lang == "en" else None
    title_extra = f' <em class="sub">{e(extra_title)}</em>' if extra_title else ""
    other = "ar" if lang == "en" else "en"
    return f'''<!doctype html>
<html lang="{lang}" dir="{"rtl" if lang=="ar" else "ltr"}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])} — {"أمل أحمد" if lang=="ar" else "Amal Ahmed"}</title>
<meta name="description" content="{e(p["tagline"])}">
<meta property="og:title" content="{e(p["title"])} — {"أمل أحمد" if lang=="ar" else "Amal Ahmed"}">
<meta property="og:description" content="{e(p["tagline"])}">
<meta property="og:image" content="{SITE}assets/cs/{folder}/01.jpg">
<meta property="og:url" content="{SITE}work/{href(p["slug"], lang)}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="{other}" href="{href(p["slug"], other)}">
<link rel="icon" href="../assets/avatar.jpg">
{FONTS}
<link rel="stylesheet" href="../assets/case.css">
</head>
<body class="{lang}">
<div class="progress-bar" id="pb"></div>
<nav><div class="wrap"><a href="../index.html#calendar" class="back">{T["back"]}</a><a href="../index.html" class="logo">{"أمل" if lang=="ar" else "amal"}</a>
<div class="nav-r"><a class="lang" href="{href(p["slug"], other)}" data-lang="{other}" lang="{other}">{T["switch"]}</a><a href="../index.html#contact" class="pill solid">{T["talk"]}</a></div></div></nav>

<header class="cs-hero wrap">
  <div class="door-badge rv"><span class="num">{n}</span><span class="eyebrow">{T["door"].format(n=n)} · {e(p["cat"])}</span></div>
  <h1 class="rv">{e(p["title"])}{title_extra}</h1>
  <p class="tagline rv">{e(p["tagline"])}</p>
  <dl class="meta rv">{meta}</dl>
</header>
<div class="cover rv"><img src="{img(folder,1)}" alt="{e(p["title"])}"></div>

{"".join(s)}
{boards_html}

<div class="wrap next"><a href="{href(nxt["slug"], lang)}"><div><span class="eyebrow">{T["nextdoor"]} · {nn:02d}</span><h3>{e(nxt["title"])} {T["arrow"]}</h3></div><div class="thumb"><img src="{img(nfolder,1)}" alt="" loading="lazy"></div></a></div>
<footer><div class="wrap"><span>{T["foot"]}</span><div class="soc">{"".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t,u in LINKS)}</div></div></footer>

<div class="lb" id="lb" role="dialog" aria-label="Image preview"><button aria-label="Close">×</button><img alt=""></div>
<script src="../assets/case.js"></script>
</body>
</html>
'''

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for p in PROJECTS:
        p.update(EXTRA.get(p["slug"], {}))
    missing = [p["slug"] for p in PROJECTS if p["slug"] not in AR]
    if missing:
        raise SystemExit(f"Missing Arabic content for: {missing}")
    for i, p in enumerate(PROJECTS):
        j = (i + 1) % len(PROJECTS)
        for lang in ("en", "ar"):
            (OUT / href(p["slug"], lang)).write_text(page(i + 1, p, PROJECTS[j], j + 1, lang), encoding="utf-8")
    print(f"wrote {len(PROJECTS)*2} pages to work/")
