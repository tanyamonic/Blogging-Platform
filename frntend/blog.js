// Function to handle form submission
function submitForm() {
    const form = document.querySelector("form");
    const titleInput = document.getElementById("title");
    const contentInput = document.getElementById("content");
    const mediaInput = document.getElementById("media");

    if (titleInput.value.trim() === "" || contentInput.value.trim() === "") {
        alert("Please fill in all required fields.");
        return;
    }
const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        
        const href = link.getAttribute('href');
        
        window.location.href = href;
    });
});

    const formData = new FormData();
    formData.append("title", titleInput.value.trim());
    formData.append("content", contentInput.value.trim());
    formData.append("media", mediaInput.files[0]);

    fetch("submit_post.php", {
        method: "POST",
        body: formData
    })
        .then(response => {
            if (response.ok) {
                form.reset();
                alert("Post submitted successfully!");
            } else {
                throw new Error("Failed to submit post.");
            }
        })
        .catch(error => {
            console.error(error);
            alert("An error occurred while submitting the post.");
        });
}

// Event listener for form submission
document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission
    submitForm(); // Call the submitForm function
});
