from app import create_app, db
from app.models import Category, Article

app = create_app()

with app.app_context():
    db.create_all()

    # Clear existing data
    Article.query.delete()
    Category.query.delete()

    # Categories
    food = Category(name='Food', icon='🍚',
        description='What humans actually need to eat — beyond diet trends and marketing myths.')
    body = Category(name='Body', icon='💪',
        description='Foundational strength, joint health, posture and movement — not bodybuilding.')
    environment = Category(name='Environment', icon='🌿',
        description='Air, water, sunlight and the environment your body was designed for.')
    clothing = Category(name='Clothing', icon='👕',
        description='What you wear affects your body more than you think.')
    shelter = Category(name='Shelter', icon='🏠',
        description='Ventilation, light and sleep environment — what makes a home healthy.')

    db.session.add_all([food, body, environment, clothing, shelter])
    db.session.commit()

    # Food articles
    a1 = Article(
        title='Why India Has the World\'s Highest Type 2 Diabetes Rate',
        myth='Traditional Indian food like rice and roti is healthy and balanced.',
        truth='Refined carbohydrates like white rice, maida, and sugar dominate the modern Indian diet and spike blood sugar repeatedly throughout the day — leading to insulin resistance over time.',
        content='India has over 100 million diabetics — more than any country on earth. The root cause is not genetics but a shift from traditional whole foods to refined carbohydrates and seed oils. Traditional Indian diets included millets, legumes, and ghee. Modern Indian diets are dominated by white rice, maida-based bread, biscuits, and ultra-processed snacks. Each of these causes rapid blood sugar spikes. Over years of repeated spikes, the body becomes insulin resistant — the foundation of Type 2 diabetes. The solution is not to avoid all carbs but to return to whole food sources: millets over maida, jaggery over sugar, ghee over refined oil.',
        sources='Lancet Diabetes Study 2023, ICMR National Diabetes Survey',
        category_id=food.id
    )

    a2 = Article(
        title='Traditional Indian Fats vs Seed Oils — What Changed',
        myth='Vegetable oils like sunflower and soybean oil are heart-healthy.',
        truth='Traditional Indian cooking fats — ghee, coconut oil, mustard oil — are more stable at high heat and better suited to the Indian digestive system than industrially processed seed oils.',
        content='For thousands of years, Indians cooked in ghee, coconut oil, and mustard oil. In the 1970s, the vegetable oil industry funded research promoting seed oils as heart-healthy alternatives. Today India is one of the largest consumers of refined sunflower and soybean oil. These oils are high in omega-6 fatty acids and oxidize rapidly at cooking temperatures, producing inflammatory compounds. Traditional fats are saturated or monounsaturated — stable at heat and used by the body efficiently. The shift to seed oils correlates with rising rates of heart disease and diabetes in India, not declining rates.',
        sources='Dr. Malhotra BMJ Review 2017, Weston A Price Foundation Research',
        category_id=food.id
    )

    # Body articles
    a3 = Article(
        title='Walking Is the Most Underrated Human Exercise',
        myth='You need a gym membership and structured workouts to be healthy.',
        truth='The human body evolved for walking 10-15km per day. Modern sedentary lifestyles have removed this baseline movement, and no amount of gym sessions fully compensates for 8 hours of sitting.',
        content='Hunter-gatherer studies show humans walked 10-15km daily as a baseline — not for exercise, but for survival. This sustained low-intensity movement regulates blood sugar, maintains joint health, supports lymphatic drainage, and maintains cardiovascular baseline. Modern humans sit for 8-12 hours and then do 1 hour of intense exercise, which does not replicate the benefits of distributed movement throughout the day. Walking after meals specifically reduces post-meal blood sugar spikes by up to 30%. The simplest health intervention available to any human is walking 30 minutes after each meal.',
        sources='Hadza Hunter-Gatherer Study 2012, Stanford Walking Research 2019',
        category_id=body.id
    )

    # Environment articles
    a4 = Article(
        title='Why Indians Are Vitamin D Deficient Despite Living in Sunshine',
        myth='Living in a sunny country means you get enough Vitamin D.',
        truth='Vitamin D is synthesized from UVB rays hitting bare skin between 10am-3pm. Most Indians avoid midday sun, cover skin fully, and work indoors — making deficiency extremely common despite abundant sunlight.',
        content='India receives intense sunlight year-round, yet studies show 70-90% of urban Indians are Vitamin D deficient. The reason is behavioral and cultural. UVB rays — the specific wavelength that triggers Vitamin D synthesis — are only present when the sun is high in the sky (10am-3pm). Most Indians avoid this time due to heat. Clothing that covers arms and legs blocks UVB entirely. Glass windows block UVB completely — so working near a sunny window provides no Vitamin D. Vitamin D deficiency leads to weakened bones, impaired immunity, depression, and insulin resistance. 20 minutes of midday sun on bare arms and legs produces adequate Vitamin D for the day.',
        sources='AIIMS Vitamin D Study 2021, WHO South Asia Nutrition Report',
        category_id=environment.id
    )

    # Clothing articles
    a5 = Article(
        title='Why Cotton Beats Polyester for the Indian Climate',
        myth='Synthetic fabrics like polyester are fine to wear in any climate.',
        truth='Polyester traps heat and moisture against the skin, raises body temperature, and creates an environment for bacterial growth. Cotton breathes, wicks moisture, and has been worn in tropical climates for thousands of years for good reason.',
        content='Traditional Indian clothing — cotton kurtas, dhotis, sarees — was engineered for the climate over centuries. Cotton allows airflow, absorbs sweat, and releases heat. Polyester, introduced in the 20th century, is a petroleum product that traps heat and moisture. In a country where average temperatures exceed 30 degrees for 6-8 months, wearing polyester raises core body temperature and increases sweating without relief. Studies on textile and skin health show synthetic fabrics increase skin infections, heat rash, and discomfort in tropical climates. The traditional choice was not aesthetic — it was functional.',
        sources='Journal of Textile Science 2020, NIFT Climate-Textile Study',
        category_id=clothing.id
    )

    # Shelter articles
    a6 = Article(
        title='What Modern Apartments Do to Your Sleep',
        myth='Any bedroom is fine for sleep as long as you are tired enough.',
        truth='Light pollution, poor ventilation, noise, and unnatural temperatures in modern urban apartments chronically disrupt sleep quality even when total sleep hours appear adequate.',
        content='Traditional Indian homes were designed with cross-ventilation, thick walls for thermal mass, and courtyards that regulated temperature naturally. Modern apartments seal occupants in concrete boxes with artificial air conditioning, light from screens and street lights, and noise from urban environments. The human body requires darkness below 10 lux to produce melatonin. A typical urban bedroom has 50-200 lux from streetlights alone. Body temperature must drop 1-2 degrees to initiate deep sleep — air conditioning set too cold or too warm disrupts this. The result is sleep that is technically 7-8 hours but lacks sufficient deep and REM phases, leaving people chronically fatigued despite adequate time in bed.',
        sources='Matthew Walker Why We Sleep 2017, IIT Delhi Urban Noise Study',
        category_id=shelter.id
    )

    db.session.add_all([a1, a2, a3, a4, a5, a6])
    db.session.commit()
    print("Database seeded successfully.")
