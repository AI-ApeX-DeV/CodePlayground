<!DOCTYPE html>
<html>
<head>
	<title>Random Quote Generator</title>
</head>
<body>
	<h1>Random Quote Generator</h1>

	<?php
		// Define an array of quotes
		$quotes = array(
			"Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
			"Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
			"Believe you can and you're halfway there. - Theodore Roosevelt",
			"Strive not to be a success, but rather to be of value. - Albert Einstein",
			"I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",
			"The only way to do great work is to love what you do. - Steve Jobs"
		);

		// Get a random quote from the array
		$random_quote = $quotes[array_rand($quotes)];

		// Print the random quote
		echo "<p>" . $random_quote . "</p>";
	?>
</body>
</html>
