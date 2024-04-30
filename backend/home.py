from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from database import database # type: ignore

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html lang="en">

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Blog - Home</title>
<style>
    

html {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    
}
.open-button {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 20px; 
  cursor:grabbing;
  padding-bottom: 40px;
}


header {
    background-color: #4CAF50;
    color: #fff;
    padding: 20px 0;
    text-align: center;
    border-bottom: 4px solid #388E3C;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

header h1 {
    font-size: 36px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.main-nav {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.main-nav a {
    font-size: 18px;
    font-weight: 500;
    text-decoration: none;
    color: #fff;
    padding: 10px 20px;
    margin: 0 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.main-nav a:hover {
    background-color: #388E3C;
}

.main-nav a.active {
    background-color: #388E3C;
}

.main-nav a:not(:last-child) {
    border-right: 1px solid #fff;
}

.overlay {
    height: 0%;
    width: 100%;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.9);
    overflow-y: hidden;
    transition: 0.5s;
}

.overlay-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.overlay a {
    font-size: 24px;
    color: #fff;
    display: block;
    margin-bottom: 20px;
    text-decoration: none;
    transition: color 0.3s ease;
}

.overlay a:hover {
    color: #4CAF50;
}

.overlay .closebtn {
    position: absolute;
    top: 20px;
    right: 45px;
    font-size: 40px;
    color: #fff;
    text-decoration: none;
    transition: color 0.3s ease;
}

.overlay .closebtn:hover {
    color: #4CAF50;
}

.filter-options {
    margin-bottom: 20px;
}

.filter-options label {
    font-size: 20px;
    font-weight: 500;
    margin-right: 10px;
}

.filter-options select {
    font-size: 18px;
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
    transition: border-color 0.3s ease;
}

.filter-options select:focus {
    border-color: #4CAF50;
}

.post {
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease;
}

.post:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.post h3 {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 10px;
}

.post p {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 20px;
}

.post a {
    font-size: 18px;
    text-decoration: none;
    color: #4CAF50;
    transition: color 0.3s ease;
}

.post a:hover {
    color: #388E3C;
}

.post img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 20px;
}

.post-actions {
    text-align: right;
}

.post-actions button {
    font-size: 16px;
    font-weight: 500;
    background-color: transparent;
    color: #4CAF50;
    border: 2px solid #4CAF50;
    border-radius: 5px;
    padding: 8px 16px;
    margin-left: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.post-actions button:hover {
    background-color: #4CAF50;
    color: #fff;
}

.post-actions button.active {
    background-color: #388E3C;
    border-color: #388E3C;
    color: #fff;
}

footer {
    background-color: #4CAF50;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

footer p {
    font-size: 16px;
    font-weight: 500;
}



@media screen and (max-width: 768px) {
    header h1 {
        font-size: 30px;
    }

    .main-nav {
        flex-wrap: wrap;
    }

    .main-nav a {
        font-size: 16px;
        padding: 8px 16px;
        margin: 5px 0;
        border-right: none;
    }

    .filter-options label {
        font-size: 18px;
    }

    .filter-options select {
        font-size: 16px;
    }

    .post h3 {
        font-size: 20px;
    }

    .post p {
        font-size: 16px;
    }

    .post a {
        font-size: 16px;
    }

    .post-actions button {
        font-size: 14px;
        padding: 6px 12px;
    }
}

</style>

</head>

  <span class="open-button" id="open" style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776;OPEN</span>
  <header>
    <div class="container">
      <h1>My Blog</h1>
    </div>
  </header>
  <div id="myNav" class="overlay">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
    <div class="overlay-content">
      <a href="home.html">Home</a>
      <a href="blog.html">Create a Blog</a>
      <a href="editor.html">Edit a Blog</a>
      <a href="profile.html">View Profile</a>
    </div>
  </div>

  <main>
    <section class="container">
      <h2>Filter Posts</h2>
      <div class="filter-options">
        <label for="tag-filter">Filter by Tag:</label>
        <select id="tag-filter">
          <option value="">All</option>
          <option value="tag1">Tag 1</option>
          <option value="tag2">Tag 2</option>
          <!-- Add more tag options as needed -->
        </select>
      </div>
    </section>

    <section class="container">
      <h2>Latest Posts</h2>
      <div class="post">
        <h3><a href="#">Post Title 1</a></h3>
        <img src="img1.png" alt="Post 1 Image" style="width: 800px; height: 600px; ">
        <!-- Add image here -->
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis velit eget justo ullamcorper finibus.</p>
        <a href="#">Read more</a>
        <div class="post-actions">
          <button class="like-btn">Like</button>
          <button class="comment-btn">Comment</button>
        </div>
      </div>
      <div class="post">
        <h3><a href="#">Post Title 2</a></h3>
        <img src="img2.png" alt="Post 2 Image" style="width: 800px; height: 600px; ">
      
        <!-- Add image here -->
        <p>Nullam dignissim velit et nunc lobortis, at elementum metus tincidunt. Cras nec tempor nulla, non malesuada metus.</p>
        <a href="#">Read more</a>
        <div class="post-actions">
          <button class="like-btn">Like</button>
          <button class="comment-btn">Comment</button>
        </div>
      </div>
      <!-- Add more posts here -->
    </section>
  </main>

  <footer>
    <div class="container">
      <p>&copy; 2024 My Blog. All rights reserved.</p>
    </div>
  </footer>

  <script>
   // JavaScript code to open and close the sidebar
function openNav() {
  document.getElementById("myNav").style.height = "100%";
}

function closeNav() {
  document.getElementById("myNav").style.height = "0%";
}

    // JavaScript code to add toggle and hover effects
    const likeButtons = document.querySelectorAll('.like-btn');
    const commentButtons = document.querySelectorAll('.comment-btn');

    // Toggle active class on like button click
    likeButtons.forEach(button => {
      button.addEventListener('click', () => {
        button.classList.toggle('active');
      });
    });

    // Add hover effect to comment buttons
    commentButtons.forEach(button => {
      button.addEventListener('mouseover', () => {
        button.style.backgroundColor = '#ff6600';
      });
      button.addEventListener('mouseout', () => {
        button.style.backgroundColor = '#333';
      });
    });
  </script>
</body>

</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_home_page():
    return html_content

