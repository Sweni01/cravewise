async function loginUser(){

    const email =
        document.getElementById("loginEmail").value;

    const password =
        document.getElementById("loginPassword").value;

    const res = await fetch(
        `${API_BASE}/api/auth/login`,
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                email,
                password
            })
        }
    );

    const data = await res.json();

    if(data.success){

        localStorage.setItem(
            "user_id",
            data.user_id
        );

        localStorage.setItem(
            "token",
            data.access_token
        );

        document.getElementById(
            "loginModal"
        ).style.display="none";

        alert("Welcome!");

    }

    else{

        alert("Invalid Login");

    }

}

function logoutUser(){

    localStorage.clear();

    location.reload();

}