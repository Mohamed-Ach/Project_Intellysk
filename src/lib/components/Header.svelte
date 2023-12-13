<script lang="ts">
	import { page } from '$app/stores';
	import { onMount, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';

	export let data;
	const { user } = data;

	// ** The Sticky Menu Effect :
	const scrollPosition = writable(0);
	const handleScroll = () => {
		scrollPosition.set(window.scrollY || document.documentElement.scrollTop);
	};
	onMount(() => {
		window.addEventListener('scroll', handleScroll);
		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});
	let isFixed = false;
	const unsubscribe = scrollPosition.subscribe((scrollY) => {
		isFixed = scrollY >= 100;
	});

	onDestroy(() => {
		unsubscribe();
	});

	// ** The Active Anchor Tag :

	const isActive = (url: string) => $page.url.toString() === url;
	console.log($page.url.toString());
</script>

<header class="theme-main-menu sticky-menu theme-menu-four {isFixed ? 'fixed' : ''}">
	<div class="inner-content">
		<div class="d-flex align-items-center">
			<div class="logo order-lg-0">
				<a href="/" class="d-block"><img src="images/logo/logo_03_alt.png" alt="" width="150" /></a>
			</div>
			{#if !user}
				<div class="right-widget d-flex align-items-center ms-auto order-lg-3">
					<a href="/login" class="send-msg-btn tran3s d-none d-lg-block">Se connecter</a>
				</div>
			{:else}
				<div class="right-widget d-flex align-items-center ms-auto order-lg-3">
					<a href="/logout" class="send-msg-btn tran3s d-none d-lg-block">Se déconnecter</a>
				</div>
			{/if}

			<!-- /.right-widget -->

			<nav class="navbar navbar-expand-lg order-lg-2">
				<button
					class="navbar-toggler d-block d-lg-none"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarNav"
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNav">
					<ul class="navbar-nav">
						<li class="d-block d-lg-none">
							<div class="logo">
								<a href="/"><img src="images/logo/logo_01_alt.png" alt="" width="130" /></a>
							</div>
						</li>
						<li class="nav-item {isActive('/') ? 'active' : ''} dropdown">
							<a class="nav-link" href="/" role="button">Home</a>
						</li>
						<li class="nav-item dropdown">
							<a
								class="nav-link {isActive('/dashboard') ? 'active' : ''} dropdown"
								href="/dashboard"
								role="button">Dashboard</a
							>
						</li>
						<!-- 
						<li class="nav-item dropdown">
							<a
								class="nav-link dropdown-toggle"
								href={null}
								role="button"
								data-bs-toggle="dropdown"
								data-bs-auto-close="outside"
								aria-expanded="false">Portfolio</a
							>
							<ul class="dropdown-menu">
								<li>
									<a href="portfolio-V1.html" class="dropdown-item"
										><span>Portfolio 3 Column</span></a
									>
								</li>
								<li>
									<a href="portfolio-V2.html" class="dropdown-item"
										><span>Portfolio 2 Column</span></a
									>
								</li>
								<li>
									<a href="portfolio-V3.html" class="dropdown-item"
										><span>Portfolio Masonry</span></a
									>
								</li>
								<li>
									<a href="portfolio-details-V1.html" class="dropdown-item"
										><span>Single Portfolio</span></a
									>
								</li>
							</ul>
						</li>
						<li class="nav-item dropdown">
							<a
								class="nav-link dropdown-toggle"
								href={null}
								role="button"
								data-bs-toggle="dropdown"
								data-bs-auto-close="outside"
								aria-expanded="false">Blog</a
							>
							<ul class="dropdown-menu">
								<li>
									<a href="blog-V1.html" class="dropdown-item"><span>Grid Layout</span></a>
								</li>
								<li>
									<a href="blog-V2.html" class="dropdown-item"><span>Grid With Sidebar</span></a>
								</li>
								<li>
									<a href="blog-V3.html" class="dropdown-item"><span>Blog Masonary</span></a>
								</li>
								<li>
									<a href="blog-V4.html" class="dropdown-item"><span>Blog Standard</span></a>
								</li>
								<li>
									<a href="blog-details.html" class="dropdown-item"><span>Blog Details</span></a>
								</li>
							</ul>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="contact-us.html" role="button">Contact</a>
						</li> -->
					</ul>
					<!-- Mobile Content -->
					<div class="mobile-content d-block d-lg-none">
						{#if !user}
							<div class="d-flex flex-column align-items-center justify-content-center mt-70">
								<a href="/login" class="send-msg-btn tran3s mb-10">Se connecter</a>
							</div>
						{:else}
							<div class="d-flex flex-column align-items-center justify-content-center mt-70">
								<a href="/login" class="send-msg-btn tran3s mb-10">Se connecter</a>
							</div>
						{/if}
					</div>
					<!-- /.mobile-content -->
				</div>
			</nav>
		</div>
	</div>
	<!-- /.inner-content -->
</header>
