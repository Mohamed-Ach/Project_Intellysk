<script lang="ts">
	import Scroll from './Scroll.svelte';

	// ** Get the current year
	const currentYear: number = new Date().getFullYear();
</script>

<div class="footer-style-four theme-basic-footer">
	<div class="container">
		<div class="inner-wrapper">
			<!-- /.subscribe-area -->
			<div class="row">
				<div class="col-lg-4 footer-intro mb-40">
					<div class="logo">
						<a href="index.html"><img src="images/logo/logo_01_alt.png" alt="" width="130" /></a>
					</div>
					<p>
						Renforcer l'avenir grâce à l'analyse prédictive, Débloquer le potentiel avec des
						insights alimentés par l'IA, Guider vers le succès grâce aux prédictions de performance
						des étudiants basées sur les données.
					</p>
					<ul class="d-flex social-icon style-none">
						<li><a href={null}><i class="fab fa-facebook-f"></i></a></li>
						<li><a href={null}><i class="fab fa-twitter"></i></a></li>
						<li><a href={null}><i class="fab fa-linkedin-in"></i></a></li>
					</ul>
				</div>
				<div class="col-lg-2 col-sm-4 ms-auto mb-30">
					<h5 class="footer-title">Auths</h5>
					<ul class="footer-nav-link style-none">
						<li><a href={null}>Se connecter</a></li>
						<li><a href={null}>S'inscrire</a></li>
					</ul>
				</div>
				<div class="col-lg-3 col-sm-4 mb-30">
					<h5 class="footer-title">Nos services</h5>
					<ul class="footer-nav-link style-none">
						<li><a href={null}>Machine Learning</a></li>
						<li><a href={null}>Data Analytics</a></li>
						<li><a href={null}>Data Visualization</a></li>
						<li><a href={null}>Statistical Modeling</a></li>
					</ul>
				</div>
				<div class="col-xl-2 col-lg-3 col-sm-4 mb-30">
					<h5 class="footer-title">À propos</h5>
					<ul class="footer-nav-link style-none">
						<li><a href={null}>Notre équipe</a></li>
						<li><a href={null}>FAQs</a></li>
					</ul>
				</div>
			</div>

			<div class="bottom-footer">
				<div class="d-lg-flex justify-content-between align-items-center">
					<ul class="order-lg-1 pb-15 d-flex justify-content-center footer-nav style-none">
						<li>
							<p class="copyright text-center order-lg-0 pb-15">
								Made by <a href="https://github.com/Mohamed-Ach"><strong>Mohamed Ach.</strong></a>
							</p>
						</li>
					</ul>
					<p class="copyright text-center order-lg-0 pb-15">
						Copyright @{currentYear} <strong>Intellysk</strong>
					</p>
				</div>
			</div>
		</div>
		<!-- /.inner-wrapper -->
	</div>
</div>
<!-- /.footer-style-four -->

<!-- Scroll to the top -->
<Scroll />
<!-- Scroll to the top end -->
