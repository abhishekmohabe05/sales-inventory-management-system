// main.js

document.addEventListener("DOMContentLoaded", function() {
    let lowStockElements = document.querySelectorAll(".low-stock");

    lowStockElements.forEach(function(el) {
        // Highlight the element
        el.style.backgroundColor = "#ffe6e6"; // light red background
        el.style.fontWeight = "bold";

        // Show alert in the page (not just console)
        let warning = document.createElement("p");
        warning.textContent = "⚠️ Low stock alert: " + el.textContent;
        warning.style.color = "red";
        el.parentNode.appendChild(warning);

        console.log("Low stock alert for: " + el.textContent);
    });
});
