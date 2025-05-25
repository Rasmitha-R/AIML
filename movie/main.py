import webbrowser
import os

# HTML content for the login page
login_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LET'S ENTER INTO THE WORLD OF ENTERTAINMENT !!</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: url("https://brobible.com/wp-content/uploads/2021/09/movie-theater.jpg") no-repeat center center fixed;
      background-size: cover;
    }

    h1 {
      text-align: center;
      background-color: red;
      color: white;
      padding: 20px;
      margin: 0;
      font-size: 28px;
      letter-spacing: 1px;
    }

    .container {
      width: 350px;
      margin: 100px auto;
      padding: 30px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 15px;
      backdrop-filter: blur(10px);
      box-shadow: 0 0 30px rgba(255,255,255,0.9);
      animation: slideIn 1s ease-out;
      color: white;
    }

    @keyframes slideIn {
      from { transform: translateY(100vh); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    input {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      border: none;
      border-radius: 8px;
      font-size: 14px;
    }

    button {
      width: 100%;
      padding: 12px;
      border: none;
      border-radius: 8px;
      background-color: crimson;
      color: white;
      font-size: 16px;
      cursor: pointer;
      margin-top: 10px;
    }

    .success {
      text-align: center;
      font-size: 14px;
      color: lime;
      margin-top: 10px;
      display: none;
    }
  </style>
</head>
<body>
  <h1>LET'S ENTER INTO THE WORLD OF ENTERTAINMENT !!</h1>

  <div class="container">
    <form onsubmit="login(event)">
      <input type="text" placeholder="Name" id="name" required>
      <input type="email" placeholder="Email" id="email" required>
      <button type="submit">Login</button>
    </form>
    <div id="successMsg" class="success">Successfully Logged In 🎉</div>
  </div>

  <script>
    function login(e) {
      e.preventDefault();
      const name = document.getElementById("name").value;
      document.getElementById("successMsg").style.display = "block";
      setTimeout(() => {
        window.location.href = "dashboard.html?user=" + encodeURIComponent(name);
      }, 1500);
    }
  </script>
</body>
</html>
'''

# Write the HTML content to a file
with open("login.html", "w", encoding="utf-8") as f:
    f.write(login_html)

# Open the login page in the default web browser
webbrowser.open("file://" + os.path.realpath("login.html"))
