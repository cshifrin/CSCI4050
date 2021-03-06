<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Home</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<body style="background-image: url('css/homebg.jpg');">
    <div class="home-main">
        <h1>Welcome to<br>Our Bookstore</h1>
        <p>Reading has never been so rewarding.</p>
        <button type="button" class="btn btn-light btn-lg" onclick="window.location.href = 'reg.php';">Register</button>
        <button type="button" class="btn btn-outline-light btn-lg" onclick="window.location.href = 'signin.php';">Sign
            in</button>
            <br>
        <button type="button" class="btn btn-outline-light btn-lg" id="home-search" onclick="window.location.href = 'unregsearch.php';">Search
            Books</button>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>