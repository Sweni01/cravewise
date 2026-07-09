from health.schemas.condition_schema import Condition

ENDOCRINE = [

    Condition(

        id="type_2_diabetes",

        name="Type 2 Diabetes",

        category="Endocrine",

        severity="high",

        aliases=[
            "diabetes",
            "t2dm",
            "type 2 diabetes"
        ],

        avoid_foods=[
            "soft drinks",
            "white bread",
            "cakes",
            "candy",
            "refined sugar"
        ],

        recommended_foods=[
            "whole grains",
            "vegetables",
            "lentils",
            "beans",
            "oats"
        ],

        preferred_nutrients=[
            "fiber",
            "protein"
        ],

        avoid_nutrients=[
            "added sugar"
        ],

        diet_tags=[
            "diabetic_friendly",
            "low_gi"
        ],

        notes="Maintain stable blood glucose and avoid high glycemic foods."

    )

]