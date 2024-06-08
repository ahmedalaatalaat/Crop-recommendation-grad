function validateForm() {
    var fullname = document.getElementById("fullname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
    var errorMessage = "";

    // Validate Full Name
    if (fullname.trim() === "") {
        errorMessage += "Please enter your full name.\n";
    }

    // Validate Email
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errorMessage += "Please enter a valid email address.\n";
    }

    // Validate Password
    if (password.trim() === "") {
        errorMessage += "Please enter a password.\n";
    } else if (password.length < 6) {
        errorMessage += "Password must be at least 6 characters long.\n";
    }

    // Validate Confirm Password
    if (confirmPassword.trim() === "") {
        errorMessage += "Please confirm your password.\n";
    } else if (password !== confirmPassword) {
        errorMessage += "Passwords do not match.\n";
    }

    // Display Error Message if any
    if (errorMessage !== "") {
        document.getElementById("error-message").innerText = errorMessage;
        return false;
    }

    return true;
}
