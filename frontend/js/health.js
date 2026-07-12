async function loadConditions(){

    const container = document.getElementById("conditions");

    container.innerHTML = "Loading...";

    const res = await fetch(
        `${API_BASE}/api/health/conditions/grouped`
    );

    const groups = await res.json();

    container.innerHTML = "";

    Object.keys(groups).forEach(category=>{

        const details=document.createElement("details");

        details.open=false;

        details.innerHTML=`
            <summary>
                <strong>${category}</strong>
                (${groups[category].length})
            </summary>
        `;

        groups[category].forEach(c=>{

            const label=document.createElement("label");

            label.style.display="block";

            label.style.margin="8px 0";

            label.innerHTML=`
                <input
                    type="checkbox"
                    value="${c.name}"
                >

                <strong>${c.name}</strong>

                <br>

                <small>
                    Severity :
                    ${c.severity}
                </small>
            `;

            details.appendChild(label);

        });

        container.appendChild(details);

    });

}