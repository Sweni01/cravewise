async function saveFavorite(recipe){

    const userId = localStorage.getItem("user_id");

    if(!userId){

        alert("Please login first.");

        return;

    }

    const response = await fetch(`${API_BASE}/api/favorites/add`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            user_id:Number(userId),

            recipe_name:recipe.name,

            recipe_image:recipe.image,

            youtube:recipe.youtube

        })

    });

    const data = await response.json();

    if(data.success){

        alert("❤️ Recipe saved!");

    }else{

        alert("Couldn't save recipe.");

    }
    }
async function loadFavorites(){

    const userId = localStorage.getItem("user_id");

    if(!userId){

        alert("Please login first.");

        return;

    }

    const res = await fetch(
        `${API_BASE}/api/favorites/${userId}`
    );

    const favorites = await res.json();

    const container =
        document.getElementById("favoriteList");

    document.getElementById(
        "favoritesContainer"
    ).style.display="block";

    if(favorites.length===0){

        container.innerHTML="<p>No saved recipes.</p>";

        return;

    }

    container.innerHTML="";

    favorites.forEach(f=>{

        container.innerHTML += `
        <div style="
        display:flex;
        gap:20px;
        margin-bottom:20px;
        align-items:center;
        ">

            <img
            src="${f.recipe_image}"
            width="120"
            style="border-radius:12px;">

            <div>

                <h3>${f.recipe_name}</h3>

                <a
                href="${f.youtube}"
                target="_blank">
                ▶ Watch Recipe
                </a>

                <br><br>

                <button
                onclick="deleteFavorite(${f.id})">
                ❌ Remove
                </button>

            </div>

        </div>
        `;

    });

}
async function deleteFavorite(id){

    await fetch(

        `${API_BASE}/api/favorites/${id}`,

        {
            method:"DELETE"
        }

    );

    loadFavorites();

}

if(localStorage.getItem("token")){

    document.getElementById(
        "loginModal"
    ).style.display="none";

}    