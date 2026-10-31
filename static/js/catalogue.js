document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.getElementById("catalogueToggle");
    const overlay = document.getElementById("catalogueOverlay");
    const closeButton = document.getElementById("closeCatalogue");
    const arrow = document.getElementById("catalogueArrow");

    const subjectButtons = document.querySelectorAll(".subject-item");
    const bookCards = document.querySelectorAll(".book-card");

    const title = document.getElementById("collectionTitle");
    const count = document.getElementById("bookCount");
    const noBooks = document.getElementById("noBooksMessage");

    // Open catalogue popup
    toggle?.addEventListener("click", function () {
        overlay.classList.add("show");
        arrow.textContent = "⌃";
    });

    // Close popup
    function closeCatalogue() {
        overlay.classList.remove("show");
        arrow.textContent = "⌄";
    }

    closeButton?.addEventListener("click", closeCatalogue);

    overlay?.addEventListener("click", function (event) {
        if (event.target === overlay) {
            closeCatalogue();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeCatalogue();
        }
    });

    // Filter books by selected category
    subjectButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const selectedCategory = button.dataset.category;

            let visibleCount = 0;

            subjectButtons.forEach(function (item) {
                item.classList.remove("active");
            });

            button.classList.add("active");

            bookCards.forEach(function (card) {

                const category = card.dataset.category;

                const showBook =
                    selectedCategory === "all" ||
                    category === selectedCategory;

                card.style.display = showBook ? "" : "none";

                if (showBook) {
                    visibleCount++;
                }
            });

            if (selectedCategory === "all") {
                title.textContent = "Explore the collection";
            } else {
                title.textContent = button.querySelector("span").textContent;
            }

            count.textContent = visibleCount + " books in your library";

            noBooks.hidden = visibleCount !== 0;

            closeCatalogue();
            document.getElementById("catalogue").scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        });

    });

});