<script lang="ts">
	import type { ActionData } from './$types';
	import { applyAction, enhance } from '$app/forms';
	export let form: ActionData;
	const currentYear: number = new Date().getFullYear();

	// ** The EyeSlash component:
	let isEyeSlash: boolean = false;
	let inputType: string = 'password';

	const toggleEyeSlash = () => {
		isEyeSlash = !isEyeSlash;
		inputType = isEyeSlash ? 'text' : 'password';
	};
</script>

<form
	action="?/login"
	use:enhance={() => {
		return async ({ result }) => {
			await applyAction(result);
		};
	}}
	method="POST"
	class="user-data-form mt-60 lg-mt-40"
>
	<h2>
		Hi, bienvenue
		<br /> Dos!
	</h2>
	<p class="header-info pt-20 pb-20 lg-pt-10 lg-pb-10">
		Vous n'avez toujours pas de compte ? <a href="/register">s'inscrire</a>
	</p>

	<div class="row">
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="email">Email*</label>
				<input
					type="email"
					name="email"
					class={form?.errors?.email ? 'border-error' : ''}
					value={form?.data?.email ?? ''}
					placeholder="email@gmail.com"
					required
				/>
				{#if form?.errors?.email}
					<span class="label-text-alt text-error">{form?.errors?.email[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="password">Mot de passe*</label>
				<input
					type={inputType}
					name="password"
					placeholder="Enter Password"
					class="pass_log_id {form?.errors?.email ? 'border-error' : ''}"
					value=""
					required
				/>
				<span class="placeholder_icon">
					<span class="passVicon {isEyeSlash ? 'eye-slash' : ''}" on:click={toggleEyeSlash}
						><img src="images/icon/icon_40.svg" alt="" /></span
					></span
				>
			</div>
		</div>
		<div class="col-12">
			<div class="agreement-checkbox d-flex justify-content-between align-items-center">
				<div>
					<input type="checkbox" id="remember" name="rememberMe" />
					<label for="remember">Se souvenir de moi</label>
				</div>
				<a href={null}>Mot de passe oublié?</a>
			</div>
		</div>
		<div class="col-12">
			<button type="submit" class="btn-eight w-100 mt-50 mb-40 lg-mt-30 lg-mb-30"
				>Se connecter</button
			>
			<!-- Alerts Messages -->
			{#if form?.error}
				<div class="alert alert-danger alert-dismissible fade show" role="alert">
					<strong>Avertissement!</strong>
					{form.error}
					<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"
					></button>
				</div>
			{/if}
		</div>
		<div class="col-12">
			<p class="text-center copyright-text m0">Copyright @{currentYear} Intellysk.</p>
		</div>
	</div>
</form>
