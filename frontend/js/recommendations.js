async function getRecommendations(){
  const statusEl = document.getElementById("status");
  const resultsEl = document.getElementById("results");
  statusEl.innerHTML = `
<div class="ai-loading">

<div class="spinner"></div>

<h3>🧠 CraveWise AI is analyzing your request...</h3>

<p id="loadingText">
Checking health conditions...
</p>

</div>
`;
const loadingMessages = [

"Checking health conditions...",

"Analyzing your cravings...",

"Matching pantry ingredients...",

"Finding recipes...",

"Ranking recommendations...",

"Almost done..."

];

let i = 0;

const loadingInterval = setInterval(() => {

const el = document.getElementById("loadingText");

if(el){

el.innerText = loadingMessages[i];

}

i = (i + 1) % loadingMessages.length;

},700);
  resultsEl.innerHTML = "";

  const conditions =
      [...document.querySelectorAll(
          '#conditions input:checked'
      )
  ].map(x=>x.value);
  const pantry = document.getElementById("pantry").value.split(",").map(s => s.trim()).filter(Boolean);

  const payload = {
    profile: {
      goal: document.getElementById("goal").value,
      health_conditions: conditions
    },
    craving: document.getElementById("craving").value,
    pantry: pantry,
    budget: Number(document.getElementById("budget").value) || null,
    time_limit_minutes: Number(document.getElementById("time").value) || null
  };

  try{
    const res = await fetch(`${API_BASE}/api/recommend`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    if(!res.ok) throw new Error(`Server returned ${res.status}`);
    const data = await res.json();
    clearInterval(loadingInterval);
    statusEl.textContent = `${data.count} option(s) found.`;
    renderResults(data.recommendations);
  }catch(err){
    statusEl.textContent = "Couldn't reach the backend. Is it running at " + API_BASE + "? (" + err.message + ")";
  }
}

function bar(pct, color){
  return `<div class="bar"><div style="width:${pct}%; background:${color || ''}"></div></div>`;
}

function renderResults(list){
  const resultsEl = document.getElementById("results");
  if(!list.length){

    document.getElementById("dashboard").style.display = "none";

    resultsEl.innerHTML = `
<div class="card" style="text-align:center;padding:40px;">

<h2>😔 No recipes found</h2>

<p>

Try one of these:

</p>

<ul style="display:inline-block;text-align:left;">

<li>Increase your budget</li>

<li>Increase cooking time</li>

<li>Remove one health filter</li>

<li>Try a different craving</li>

</ul>

</div>
`;

    return;

}
  // ---------- Dashboard ----------

const dashboard = document.getElementById("dashboard");

dashboard.style.display = "grid";

document.getElementById("totalRecipes").innerText = list.length;

const avgCalories = Math.round(
    list.reduce((sum,r)=>sum+r.calories,0)/list.length
);

const avgProtein = Math.round(
    list.reduce((sum,r)=>sum+r.protein,0)/list.length
);

const avgMatch = Math.round(
    list.reduce((sum,r)=>sum+r.ai_match,0)/list.length
);

document.getElementById("avgCalories").innerText =
avgCalories + " kcal";

document.getElementById("avgProtein").innerText =
avgProtein + " g";

document.getElementById("avgMatch").innerText =
avgMatch + "%";
  let html = "";
  list.forEach(r => {
    const missing = r.missing_ingredients.length
      ? `<div class="missing"><b>Missing from pantry:</b> ${r.missing_ingredients.join(", ")}</div>`
      : `<div class="missing" style="color:var(--sage-deep)">You have everything you need.</div>`;

    const swaps = Object.keys(r.healthy_swaps).length
      ? `<div class="missing" style="color:var(--butter-deep)"><b>Healthy swap:</b> ${Object.entries(r.healthy_swaps).map(([a,b]) => `${a} → ${b}`).join(", ")}</div>`
      : "";

    html += `
            <div style="display:flex;gap:20px;">
            
      <div>
      
      <img
      src="${r.image || 'https://placehold.co/300x300?text=Recipe'}"
      style="
      width:170px;
      height:170px;
      object-fit:cover;
      border-radius:15px;
      ">
      
      </div>
      
      <div style="flex:1;">
      
      <h3>${r.name}</h3> 
      <div class="match-score">
        ⭐ ${r.ai_match}% AI Match
      </div> 
                <div class="explain">${r.explanation}</div>
          <div class="stats">
            <span><b>${r.calories}</b> kcal</span>
            <span><b>${r.protein}g</b> protein</span>
            <span><b>${r.carbs}g</b> carbs</span>
            <span><b>₹${r.cost}</b></span>
            <span><b>${r.time_minutes} min</b></span>
            <span><b>${r.difficulty}</b></span>
          </div>
          <div class="tags">
          ${r.tags.map(tag => `
          <span class="tag">${tag}</span>
          `).join("")}
          </div>
          ${missing}
          ${swaps}
          <div style="margin-top:15px;">

      <a
                
      href="${r.youtube}"
                
      target="_blank"
                
      style="
                
      background:#E53935;
                
      color:white;
                
      padding:10px 18px;
                
      border-radius:10px;
                
      text-decoration:none;
                
      font-weight:bold;
                
      ">
                
      ▶ Watch Recipe
                
      </a>
      <button
onclick='saveFavorite(${JSON.stringify(r)})'
class="favorite-btn">
❤️ Save Recipe
</button>
      </div>
        </div>
        <div class="scores">
          <div class="score-row">Health score: ${r.health_score}${bar(r.health_score, "#A7C4A0")}</div>
          <div class="score-row">Craving match: ${r.craving_score}${bar(r.craving_score, "#F5DFA0")}</div>
          <div class="score-row">Pantry match: ${r.pantry_match_pct}%${bar(r.pantry_match_pct, "#E38CA0")}</div>
          <div class="score-row"><b>Total score: ${r.total_score}</b></div>
        </div>
      </div>`
      ;
  });

  html += buildComparisonTable(list);
  resultsEl.innerHTML = html;
}

function buildComparisonTable(list){
  let rows = list.map(r => `
    <tr>
      <td>${r.name}</td>
      <td>${r.health_score}</td>
      <td>${r.craving_score}</td>
      <td>₹${r.cost}</td>
      <td>${r.time_minutes} min</td>
      <td>${r.total_score}</td>
    </tr>`).join("");

  return `
    <div class="card">
      <h2>Decision comparison</h2>
      <table class="compare">
        <tr><th>Option</th><th>Health</th><th>Craving</th><th>Cost</th><th>Time</th><th>Total</th></tr>
        ${rows}
      </table>
    </div>`;
}

document
    .getElementById("conditionSearch")
    .addEventListener("input", function(){

        const text = this.value.toLowerCase();

        document
            .querySelectorAll("#conditions label")
            .forEach(label => {

                label.style.display =
                    label.textContent
                        .toLowerCase()
                        .includes(text)
                        ? "block"
                        : "none";

            });

    }); 