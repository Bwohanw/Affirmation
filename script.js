
const afflist = [
  love,
  health,
  beauty,
  gratitude,
  spiritual,
  happiness,
  money,
  blessing,
  sleep
]

affliststr = [
  "love",
  "health",
  "beauty",
  "gratitude",
  "spiritual",
  "happiness",
  "money",
  "blessing",
  "sleep"
]

for (let i = 0; i < afflist.length; i++) {
  document.getElementById(`${affliststr[i]}btn`).addEventListener('click',() => {
    let idx = Math.floor(Math.random() * afflist[i].length);
    localStorage.setItem('affirmation', afflist[i][idx]);
  })
}