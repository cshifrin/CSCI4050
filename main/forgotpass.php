<?php 
    $email = $_POST['inputEmail'];

    if (isset($_POST['forgotPass'])) { //if the forgot password button is clicked
        if ($_POST['inputEmail'] != "user@email.com" && $_POST['inputEmail'] != "admin@email.com") { //CHECK DATABASE TO MAKE SURE EMAIL EXISTS
            $error = "That email is not linked to an existing account.";
        }
        else {

            //SEND USER EMAIL CONTAINING USER PASSWORD

            header("Location: signin.php"); //redirects to sign in page
        }
    }
?>


<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Forgot Password?</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<body>
    <div class="main-content" style="margin: 15%;">
        <h1>Forgot Password?</h1>
        <p>Enter your email to receive an email containing your password. Then, you will be redirected to the sign in
            page.</p>
        <p class="error"><?php echo $error; ?></p>
        <form method="POST">
            <div class="form-group">
                <label for="inputEmail">Email (required)</label>
                <input type="email" class="form-control" name="inputEmail" id="inputEmail" placeholder="example@email.com" required>
            </div>

            <button type="submit" name="forgotPass" class="btn btn-outline-dark">Send Email</button>
        
        </form>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>