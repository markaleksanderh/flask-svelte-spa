<script>
    let random_number = -1;

	fetch('http://localhost:5000/randint')
		.then((response) => response.json())
		.then((random) => {
			console.log(random)
			random_number = random.integer;
	})
	
	
</script>

<main>
	<h1>{random_number}</h1>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>