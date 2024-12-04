document.getElementById('date').value = new Date().toLocaleDateString("fr");
const value = document.querySelector("#ratingvalue");
const input = document.querySelector("#rating");
value.textContent = input.value;
input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});

document.addEventListener("DOMContentLoaded", function () {
  // Trouve tous les éléments avec la classe 'alert'
  const alerts = document.querySelectorAll(".alert");

  // Parcourt chaque alerte et la fait disparaître après 3 secondes
  alerts.forEach(alert => {
      setTimeout(() => {
          alert.classList.add("fade-out");
      }, 3000); // 3000 ms = 3 secondes
  });

  // Supprime complètement les éléments du DOM après l'animation
  setTimeout(() => {
      alerts.forEach(alert => alert.remove());
  }, 3500); // Attendre la fin de l'animation (500ms supplémentaires)
});