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
async function signupUser() {

    const name = document.getElementById("signupName").value;
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    const response = await fetch(`${API_BASE}/api/auth/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            email: email,
            password: password
        })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Account created successfully!");

        document.getElementById("signupModal").style.display = "none";

        document.getElementById("loginModal").style.display = "flex";
    } else {
        alert(data.detail || "Signup failed.");
    }
}
function logoutUser(){

    localStorage.clear();

    location.reload();

}