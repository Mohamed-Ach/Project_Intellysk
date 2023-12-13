<div class="main-page-wrapper">
	<!-- 
	=============================================
		Sign In
	============================================== 
	-->
	<div class="user-data-page clearfix d-md-flex">
		<div class="illustration-wrapper d-none d-md-flex align-items-center">
			<h3>
				Vous voulez des prévisions <br /> de performances de niveau supérieur ? Essayez
				<a href="/">Intellysk.</a>
			</h3>
			<div class="illustration-holder">
				<img src="images/assets/ils_22.svg" alt="" class="illustration m-auto" />
			</div>
		</div>
		<!-- /.illustration-wrapper -->

		<div class="form-wrapper">
			<div class="d-flex justify-content-between align-items-center">
				<div class="logo">
					<a href="/" class="d-block"
						><img src="images/logo/logo_01_alt.png" alt="" width="131" /></a
					>
				</div>
				<a href="/" class="go-back-button tran3s">Go to home</a>
			</div>
			<slot />
		</div>
		<!-- /.form-wrapper -->
	</div>
	<!-- /.user-data-page -->

	<button class="scroll-top">
		<i class="bi bi-arrow-up-short"></i>
	</button>
</div>
