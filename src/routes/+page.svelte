<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import Header from '$lib/components/Header.svelte';
	export let data;
</script>

<div class="main-page-wrapper">
	<!-- ===================================================
				Loading Transition
			==================================================== -->
	<!-- <section>
		<div id="preloader">
			<div id="ctn-preloader" class="ctn-preloader">
				<div class="animation-preloader">
					<div class="icon">
						<img src="images/logo/logo_01.svg" alt="" class="m-auto d-block" width="38" />
					</div>
					<div class="txt-loading mt-2">
						<span data-text-preloader="S" class="letters-loading"> S </span>
						<span data-text-preloader="I" class="letters-loading"> I </span>
						<span data-text-preloader="N" class="letters-loading"> N </span>
						<span data-text-preloader="C" class="letters-loading"> C </span>
						<span data-text-preloader="O" class="letters-loading"> O </span>
					</div>
				</div>
			</div>
		</div>
	</section> -->
	<!-- 
			=============================================
				Theme Main Menu
			============================================== 
			-->
	<Header {data} />
	<!-- /.theme-main-menu -->

	<!-- 
			=============================================
				Theme Hero Banner
			============================================== 
			-->
	<div class="hero-banner-five">
		<div class="container">
			<div class="row">
				<div class="col-xxl-6 col-md-7">
					<h1 class="hero-heading">
						Charting the ENSAT's success with <span>AI/ML.</span>
					</h1>
					<p class="text-lg mb-50 pt-40 pe-xl-5 md-pt-30 md-mb-40">
						Intellysk fournit des prédictions précises et perspicaces des performances des étudiants
						de l'ENSA Tanger.
					</p>
					<ul class="style-none button-group d-flex align-items-center">
						<li class="me-4">
							<a href="/register" class="demo-btn ripple-btn tran3s">Rejoignez-nous</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<!-- /.container -->
		<div class="illustration-holder">
			<img src="images/assets/ils_13.svg" alt="" class="main-illustration ms-auto" />
			<img src="images/assets/ils_13_1.svg" alt="" class="shapes shape-one" />
			<img src="images/assets/ils_13_2.svg" alt="" class="shapes shape-two" data-aos="fade-down" />
			<img
				src="images/assets/ils_13_2.svg"
				alt=""
				class="shapes shape-three"
				data-aos="fade-down"
			/>
		</div>
		<!-- /.illustration-holder -->
		<div class="shapes oval-one"></div>
	</div>
	<!-- /.hero-banner-five -->

	<!-- Footer -->
	<Footer />
	<!-- End Footer -->
</div>
<!-- /.main-page-wrapper -->
