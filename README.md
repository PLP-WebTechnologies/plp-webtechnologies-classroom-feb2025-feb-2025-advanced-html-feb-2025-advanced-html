 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML5 Example Page</title>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Welcome to My  Page Peter obonyo</h1>
    </header>

    <!-- Ordered List with Roman Numerals -->
    <section>
        <h2>Ordered List with Roman Numerals</h2>
        <ol type="I">
            <li>First Item</li>
            <li>Second Item</li>
            <li>Third Item</li>
            <li>Fourth Item</li>
        </ol>
    </section>

    <!-- External Image from Pexels -->
    <section>
        <h2>External Image</h2>
        <img src="https://images.pexels.com/photos/15286/pexels-photo.jpg" alt="Nature Image" width="500">
        <p>Image sourced from <a href="https://pexels.com" target="_blank">Pexels</a>.</p>
    </section>

    <!-- Table of Contacts -->
    <section>
        <h2>Contact Table</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Address</th>
                    <th>Mobile</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>peter obonyo</td>
                    <td>the uon, City</td>
                    <td>123-456-7890</td>
                    <td>odiwourp7@gmail.com</td>
                </tr>
                <tr>
                    <td>Joy F</td>
                    <td>456 Elm St, Town</td>
                    <td>234-567-8901</td>
                    <td>obonyoadhala@gmail.com</td>
                </tr>
                <tr>
                    <td>stell </td>
                    <td>789 Oak St, Village</td>
                    <td>345-678-9012</td>
                    <td>stell@gmail.com</td>
                </tr>
                <tr>
                    <td>Bob brown</td>
                    <td>101 Pine St, Hamlet</td>
                    <td>456-789-0123</td>
                    <td>bob@gmail.com</td>
                </tr>
                <tr>
                    <td>Charlie Davis</td>
                    <td>202 Maple St, Borough</td>
                    <td>567-890-1234</td>
                    <td>charlie@gmail.com</td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- Registration Form -->
    <section>
        <h2>Registration Form</h2>
        <form action="#" method="post">
            <!-- Name Field -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" placeholder="Enter your name" required>
            <br><br>

            <!-- Email Field -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="Enter your email" required>
            <br><br>

            <!-- Password Field -->
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" placeholder="Enter your password" required minlength="8">
            <br><br>

            <!-- Date Field -->
            <label for="dob">Date of Birth:</label>
            <input type="date" id="dob" name="dob" required>
            <br><br>

            <!-- Dropdown Menu -->
            <label for="country">Country:</label>
            <select id="country" name="country" required>
                <option value="">Select your country</option>
                <option value="us">United States</option>
                <option value="ca">Canada</option>
                <option value="uk">United Kingdom</option>
                <option value="au">Australia</option>
            </select>
            <br><br>

            <!-- Radio Buttons -->
            <label>Gender:</label>
            <input type="radio" id="male" name="gender" value="male" required>
            <label for="male">Male</label>
            <input type="radio" id="female" name="gender" value="female" required>
            <label for="female">Female</label>
            <input type="radio" id="other" name="gender" value="other" required>
            <label for="other">Other</label>
            <br><br>

            <!-- Checkboxes -->
            <label>Interests:</label>
            <input type="checkbox" id="coding" name="interests" value="coding">
            <label for="coding">Coding</label>
            <input type="checkbox" id="reading" name="interests" value="reading">
            <label for="reading">Reading</label>
            <input type="checkbox" id="traveling" name="interests" value="traveling">
            <label for="traveling">Traveling</label>
            <br><br>

            <!-- Submit Button -->
            <input type="submit" value="Register">
        </form>
    </section>

    <!-- Multimedia Elements -->
    <section>
        <h2>Multimedia Elements</h2>
        <!-- Audio -->
        <h3>Audio Example</h3>
        <audio controls>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>

        <!-- Video -->
        <h3>Video Example</h3>
        <video controls width="500">
            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
            Your browser does not support the video element.
        </video>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 My HTML5 Page. All rights reserved.</p>
    </footer>
</body>
</html>
