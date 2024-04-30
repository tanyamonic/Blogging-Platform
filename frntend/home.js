//javascript for home.html
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for like buttons
    const likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Toggle like button state
            button.classList.toggle('liked');

            // Update like count (example)
            const likeCount = button.parentElement.querySelector('.like-count');
            if (button.classList.contains('liked')) {
                likeCount.textContent = parseInt(likeCount.textContent) + 1;
            } else {
                likeCount.textContent = parseInt(likeCount.textContent) - 1;
            }
        });
    });

    
    });
