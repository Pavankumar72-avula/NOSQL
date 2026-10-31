
document.addEventListener("DOMContentLoaded", function () {

    console.log("Library Auth.js loaded successfully");

    // =====================================
    // SHOW / HIDE PASSWORD
    // =====================================

    const toggleButtons = document.querySelectorAll(".toggle-password");

    toggleButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.preventDefault();

            const wrapper = button.closest(".password-wrapper");

            if (!wrapper) {
                console.error("Password wrapper not found");
                return;
            }

            const input = wrapper.querySelector("input");

            if (!input) {
                console.error("Password input not found");
                return;
            }

            const showPassword = input.type === "password";

            input.type = showPassword ? "text" : "password";

            button.textContent = showPassword ? "🙈" : "👁️";

            button.setAttribute(
                "aria-label",
                showPassword ? "Hide password" : "Show password"
            );

            button.setAttribute(
                "title",
                showPassword ? "Hide password" : "Show password"
            );

        });

    });


    // =====================================
    // REGISTRATION PASSWORD VALIDATION
    // =====================================

    const registerForm = document.querySelector("#registerForm");

    if (registerForm) {

        registerForm.addEventListener("submit", function (event) {

            const password = registerForm.querySelector(
                'input[name="password"]'
            );

            const confirmPassword = registerForm.querySelector(
                'input[name="confirm_password"]'
            );

            if (!password || !confirmPassword) return;

            if (password.value !== confirmPassword.value) {

                event.preventDefault();

                alert("Passwords do not match!");

                confirmPassword.focus();

            }

        });

    }

});
