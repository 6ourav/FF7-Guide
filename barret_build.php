<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="icon" href="favicon-32x32.png" type="image/png">
    <link rel="stylesheet" href="style.css">
    <title>FF7 Character Guide</title>
</head>

<body>
    <div class="navbar">
        <!-- Home button on the left -->
        <img src="images/aerithsq.png" alt="aerith">
        <a href="index.html">Home</a>
        <a href="compare.html">Compare Stats</a>
        <div class="dropdown">
            <button class="dropbtn">Characters</button>
            <div class="dropdown-content">
                <a href="cloud.html">Cloud</a>
                <a href="tifa.html">Tifa</a>
                <a href="barret.html">Barret</a>
                <a href="aerith.html">Aerith</a>
            </div>
        </div>
    </div>

    <div class="title">
        <h1>Your <span style="color:#8b4513">Barret</span> Build</h1>
    </div>

    <?php
        if ($_SERVER["REQUEST_METHOD"] == "GET") {
            // Retrieve form data
            $q1a = $_GET['q1a'] ?? '';
            $q2a = $_GET['q2a'] ?? '';
            $q3a = $_GET['q3a'] ?? '';
            $q4a = $_GET['q4a'] ?? '';
            $q5a = $_GET['q5a'] ?? '';
            $q6a = $_GET['q6a'] ?? '';
            $q7a = $_GET['q7a'] ?? '';
            $q8a = $_GET['q8a'] ?? '';


            echo "<div class='title'><h3>Weapon:</h3>";

            if ($q7a == 'n') {
                echo "<img src=images/bb.jpg alt=h height=80px>";
                echo "<p>Big Bertha</p>";
            } else if ($q2a == 'm') {
                if ($q3a == "y") {
                    echo "<img src=images/sp.jpg alt=ms height=80px>";
                    echo "<p>Steel Pincers</p>";
                } else {
                    echo "<img src=images/wb.jpg alt=ms height=80px>";
                    echo "<p>Wrecking Ball</p>";
                }
            } else if ($q8a == 'y') {
                echo "<img src=images/ekg.jpg alt=nb height=80px>";
                echo "<p>EKG Cannon</p>";
            } else if ($q1a == 'magic') {
                echo "<img src=images/lmg.jpg alt=bs height=80px>";
                echo "<p>Light Machine Gun</p>";
            } else {
                echo "<img src=images/twin_stinger.jpg alt=ts height=80px>";
                echo "<p>Twin Stinger</p>";
            }

            echo "<h3>Armor:</h3>";

            if ($q5a == 'hp') {
                if ($q6a == 'y') {
                    echo "<img src=images/iron.jpg alt=im height=80px>";
                    echo "<p>Iron Maiden</p>";
                } else {
                    echo "<img src=images/supr.jpg alt=su height=80px>";
                    echo "<p>Supreme Bracer</p>";
                }
            } else if ($q5a == 'mp') {
                if ($q6a == 'y') {
                    echo "<img src=images/astr.jpg alt=as height=80px>";
                    echo "<p>Astral Cuff</p>";
                } else {
                    echo "<img src=images/rune.jpg alt=ru height=80px>";
                    echo "<p>Rune Armlet</p>";
                }
            } else {
                echo "<img src=images/chain.jpg alt=ch height=80px>";
                echo "<p>Chain Bangle</p>";
            }


            echo "<h3>Accessory:</h3>";

            if ($q7a == 'n') {
                if ($q4a == 'rd') {
                    echo "<img src=images/cres.jpg alt=g height=80px>";
                    echo "<p>Crescent Moon Charm</p>";
                } else {
                    echo "<img src=images/salv.jpg alt=g height=80px>";
                    echo "<p>Salvation Badge</p>";
                }
            } else {
                echo "<img src=images/spwr.jpg alt=cb height=80px>";
                echo "<p>Supernatural Wristguards</p>";
            }

            echo "</div>";


        }
    ?>
    


</body>

</html>