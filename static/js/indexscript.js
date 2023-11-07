var signupButton = document.getElementById("SignUpButton");
var signinButton = document.getElementById("SignInButton");
var signoutButton = document.getElementById("SignOutButton");

document.getElementById("SignUpButton").addEventListener("click", function() {
    console.log('sd');
    window.location.href = "../../templates/authentication/signup.html";
});