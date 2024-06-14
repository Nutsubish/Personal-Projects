document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".addbtn");
    const itemCount = document.getElementById("items");
    let count = 0;

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            count++;
            itemCount.textContent = count;
            itemCount.classList.remove("hidden");
            itemCount.style.backgroundColor = "red";
            itemCount.style.padding = "3px"
            itemCount.style.borderRadius = "50%"
        });
    });
});
