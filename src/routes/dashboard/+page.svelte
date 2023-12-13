<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import Header from '$lib/components/Header.svelte';

	export let data;
</script>

<div class="main-page-wrapper">
	<!-- Header -->
	<Header {data} />
	<!-- end Header -->

	=
	<div class="theme-inner-banner">
		<div class="container">
			<h2 class="intro-title text-center">Nos Services</h2>
			<ul class="page-breadcrumb style-none d-flex justify-content-center">
				<li><a href="index.html">Home</a></li>
				<li class="current-page">Dashboard</li>
			</ul>
		</div>
		<img src="images/shape/shape_38.svg" alt="" class="shapes shape-one" />
		<img src="images/shape/shape_39.svg" alt="" class="shapes shape-two" />
	</div>
	<!-- /.theme-inner-banner -->

	<div class="fancy-feature-twentyFour">
		<div class="container">
			<div class="row">
				<div class="col-xl-9 col-lg-8 order-lg-1 mt-100 mb-20">
					<div class="service-details-meta ps-lg-5 ms-xxl-4">
						<h2 class="main-title">3lax lharrachy jab Ratt 3and C++</h2>
						<p>
							Khawa 7naya drari d 9ahwa dl 7afa, costa dl 7afa nosotros hermanitos y nada problema,
							Daba nta kat5dem walakin moxkila dyalek nhar d mti7an makatrekzxi, Xoflek xi 7al, dir
							xi haja tfrega3 dir xi 7aja
						</p>
					</div>
					<!-- /.service-details-meta -->
				</div>
			</div>
		</div>
	</div>
	<!-- Footer -->
	<Footer />
	<!-- End Footer -->
</div>
